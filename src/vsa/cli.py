from __future__ import annotations

from .markdown_newline_policy import preserve_vsa_source_newlines
from .include_vsa import IncludeVsaError, prepare_markdown_block_body, prepare_vsa_body
import argparse
import json
import sys
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

from .block_parser import DEFAULT_METADATA, parse_markdown_blocks
from .config import load_config
from .markdown_builder import build_markdown_site
from .markdown_processor import ProcessValidationError, process_path
from .musicxml_package import (
    _MUSICXML_SUFFIX,
    _MXL_SUFFIX,
    _KNOWN_SUFFIXES,
    musicxml_output_suffix,
    write_musicxml_output,
)
from .musicxml_renderer import MusicXMLExportError, MusicXMLRenderer
from .parser import Parser
from .svg_renderer import SVGRenderer
from .validation_display import format_validation_message
from .validation_runner import validate_path
from .yaml_frontmatter import frontmatter_to_block_metadata, parse_vsa_frontmatter


def main(argv=None):
    parser = _build_parser()
    args = parser.parse_args(argv)

    try:
        return _run(args)
    except ProcessValidationError as exc:
        _print_validation_messages(exc.messages)
        return 1
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1


def _build_parser():
    parser = argparse.ArgumentParser(prog="vsa")
    parser.add_argument("--config", help="Pad naar vsa.toml", default=None)
    parser.add_argument("--version", action="store_true", help="Toon versie")

    subparsers = parser.add_subparsers(dest="command")

    validate = subparsers.add_parser("validate")
    validate.add_argument("path")
    validate.add_argument("--config", default=None)
    validate.add_argument(
        "--summary",
        action="store_true",
        help="Compacte eenregelige foutmeldingen (zonder broncontext).",
    )

    parse = subparsers.add_parser("parse")
    parse.add_argument("path")
    parse.add_argument("--ast", action="store_true")

    blocks = subparsers.add_parser("blocks")
    blocks.add_argument("path")
    blocks.add_argument("--json", action="store_true")

    svg = subparsers.add_parser("svg")
    svg.add_argument("input")
    svg.add_argument("output")
    svg.add_argument("--config", default=None)
    svg.add_argument("--max-line-width", type=float, default=None)

    process = subparsers.add_parser("process")
    process.add_argument("input")
    process.add_argument("output_dir")
    process.add_argument("--config", default=None)
    process.add_argument("--no-validate", action="store_true")
    process.add_argument("--max-line-width", type=float, default=None)

    build_markdown = subparsers.add_parser("build-markdown")
    build_markdown.add_argument("input_dir")
    build_markdown.add_argument("output_dir")
    build_markdown.add_argument("assets_dir")
    build_markdown.add_argument("--config", default=None)
    build_markdown.add_argument("--assets-url-prefix", default=None)
    build_markdown.add_argument("--max-line-width", type=float, default=None)
    build_markdown.add_argument(
        "--output-mode",
        choices=["img", "shortcode"],
        default=None,
    )

    musicxml = subparsers.add_parser("musicxml")
    musicxml.add_argument(
        "input",
        help="VSA-bestand (.vsa), Markdown-bestand (.md) of map.",
    )
    musicxml.add_argument(
        "output",
        help=(
            "Uitvoerbestand (.mxl standaard, of .musicxml) voor een enkel "
            "invoerbestand, of uitvoermap voor meerdere bestanden."
        ),
    )
    musicxml.add_argument("--config", default=None)
    musicxml.add_argument(
        "--format",
        choices=["musicxml", "mxl"],
        default=None,
        help=(
            "Uitvoerformaat: .mxl (default) of .musicxml. "
            "Bij een enkel bestand overschrijft een expliciete extensie dit."
        ),
    )
    musicxml.add_argument(
        "--do",
        default=None,
        help="Grondtoon, bijv. F4 (overschrijft bestand-metadata).",
    )
    musicxml.add_argument(
        "--mode",
        default=None,
        help="Modus, bijv. major of minor (overschrijft bestand-metadata).",
    )
    musicxml.add_argument(
        "--tempo",
        default=None,
        help="Tempo in BPM (overschrijft bestand-metadata).",
    )
    musicxml.add_argument(
        "--musicxml-profile",
        choices=["playback", "engraving"],
        default=None,
        help=(
            "MusicXML-exportprofiel: playback (default, Coria/MuseScore) "
            "of engraving (expliciete maatstrepen, typografie)."
        ),
    )

    return parser


def _run(args):
    if args.version:
        print(f"vsa {_version()}")
        return 0

    if args.command is None:
        print("Geen commando opgegeven.", file=sys.stderr)
        return 1

    config = load_config(getattr(args, "config", None))

    if args.command == "validate":
        return _cmd_validate(args, config)

    if args.command == "parse":
        return _cmd_parse(args)

    if args.command == "blocks":
        return _cmd_blocks(args)

    if args.command == "svg":
        return _cmd_svg(args, config)

    if args.command == "process":
        return _cmd_process(args, config)

    if args.command == "build-markdown":
        return _cmd_build_markdown(args, config)

    if args.command == "musicxml":
        return _cmd_musicxml(args, config)

    print(f"Onbekend commando: {args.command}", file=sys.stderr)
    return 1


def _version():
    for package_name in ["vsa-tool", "vsa"]:
        try:
            return version(package_name)
        except PackageNotFoundError:
            continue

    return "0.1.0"


def _cmd_validate(args, config):
    result = validate_path(args.path, config=config)

    if result.messages:
        _print_validation_messages(result.messages, summary=args.summary)

    if result.ok:
        if not result.messages:
            print("OK")
        return 0

    return 1


def _cmd_parse(args):
    path = Path(args.path)
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".vsa":
        try:
            text, _ = prepare_vsa_body(text, path)
        except IncludeVsaError as exc:
            print(f"{path}: {exc.message_nl}", file=sys.stderr)
            return 1
    document = Parser(preserve_vsa_source_newlines(text)).parse()

    if args.ast:
        print(json.dumps(document.to_dict(), ensure_ascii=False, indent=2))
    else:
        print("OK")

    return 0


def _cmd_blocks(args):
    text = Path(args.path).read_text(encoding="utf-8")
    blocks = parse_markdown_blocks(text)

    if args.json:
        data = []

        for block in blocks:
            item = {
                "start_line": block.start_line,
                "end_line": block.end_line,
                "metadata": block.effective_metadata(),
                "body": block.body,
                "ast": block.parse_body().to_dict(),
            }
            data.append(item)

        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(f"{len(blocks)} VSA-blok(ken) gevonden")

    return 0


def _cmd_svg(args, config):
    input_path = Path(args.input)
    text = input_path.read_text(encoding="utf-8")
    try:
        body, _ = prepare_vsa_body(text, input_path)
    except IncludeVsaError as exc:
        print(f"{input_path}: {exc.message_nl}", file=sys.stderr)
        return 1
    document = Parser(preserve_vsa_source_newlines(body)).parse()

    renderer = SVGRenderer(svg_config=config.rendering.svg)
    renderer.max_line_width = (
        args.max_line_width
        if args.max_line_width is not None
        else config.rendering.max_line_width
    )

    svg = renderer.render_document(document)
    Path(args.output).write_text(svg, encoding="utf-8")

    print(f"SVG geschreven naar: {args.output}")
    return 0


def _cmd_process(args, config):
    max_line_width = (
        args.max_line_width
        if args.max_line_width is not None
        else config.rendering.max_line_width
    )

    result = process_path(
        args.input,
        args.output_dir,
        validate=not args.no_validate,
        max_line_width=max_line_width,
        config=config,
    )

    print(f"{len(result.blocks)} SVG-bestand(en) gegenereerd")

    for block in result.blocks:
        print(f"- {block.output_file}")

    return 0


def _cmd_build_markdown(args, config):
    assets_url_prefix = (
        args.assets_url_prefix
        if args.assets_url_prefix is not None
        else config.hugo.assets_url_prefix
    )
    max_line_width = (
        args.max_line_width
        if args.max_line_width is not None
        else config.rendering.max_line_width
    )
    output_mode = (
        args.output_mode
        if args.output_mode is not None
        else config.hugo.output_mode
    )

    result = build_markdown_site(
        args.input_dir,
        args.output_dir,
        args.assets_dir,
        assets_url_prefix=assets_url_prefix,
        max_line_width=max_line_width,
        output_mode=output_mode,
        config=config,
    )

    print(f"{len(result.markdown_files)} Markdownbestand(en) geschreven")
    print(f"{len(result.svg_files)} SVG-bestand(en) geschreven")
    return 0


def _cmd_musicxml(args, config):
    input_path = Path(args.input)

    cli_overrides: dict[str, str] = {}
    if args.do:
        cli_overrides["do"] = args.do
    if args.mode:
        cli_overrides["mode"] = args.mode
    if args.tempo:
        cli_overrides["tempo"] = args.tempo
    if args.musicxml_profile:
        cli_overrides["musicxml-profile"] = args.musicxml_profile

    output_suffix = _musicxml_batch_suffix(args)

    if input_path.is_dir():
        output_dir = Path(args.output)
        output_dir.mkdir(parents=True, exist_ok=True)
        written = 0
        for vsa_file in sorted(input_path.rglob("*.vsa")):
            rel = vsa_file.relative_to(input_path)
            out_file = output_dir / rel.with_suffix(output_suffix)
            out_file.parent.mkdir(parents=True, exist_ok=True)
            rc = _export_vsa_to_musicxml(vsa_file, out_file, cli_overrides)
            if rc != 0:
                return rc
            written += 1
        for md_file in sorted(input_path.rglob("*.md")):
            rel = md_file.relative_to(input_path)
            out_subdir = output_dir / rel.with_suffix("")
            rc, block_count = _export_md_to_musicxml(
                md_file, out_subdir, cli_overrides, output_suffix=output_suffix
            )
            if rc != 0:
                return rc
            written += block_count
        label = "MXL" if output_suffix == _MXL_SUFFIX else "MusicXML"
        print(f"{written} {label}-bestand(en) geschreven")
        return 0

    output_path = Path(args.output)

    if input_path.suffix.lower() == ".vsa":
        out_path = _resolve_musicxml_output_path(output_path, args)
        rc = _export_vsa_to_musicxml(input_path, out_path, cli_overrides)
        if rc == 0:
            print(f"MusicXML geschreven naar: {out_path}")
        return rc

    if input_path.suffix.lower() in {".md", ".markdown"}:
        output_path.mkdir(parents=True, exist_ok=True)
        rc, written = _export_md_to_musicxml(
            input_path, output_path, cli_overrides, output_suffix=output_suffix
        )
        if rc == 0 and written:
            label = "MXL" if output_suffix == _MXL_SUFFIX else "MusicXML"
            print(f"{written} {label}-bestand(en) geschreven")
        return rc

    print(
        f"Onbekend bestandstype: '{input_path.suffix}'. "
        "Gebruik .vsa, .md of een map.",
        file=sys.stderr,
    )
    return 1


def _musicxml_batch_suffix(args) -> str:
    return musicxml_output_suffix(format_name=args.format)


def _resolve_musicxml_output_path(output_path: Path, args) -> Path:
    if output_path.suffix.lower() in _KNOWN_SUFFIXES:
        return output_path
    return output_path.with_suffix(_musicxml_batch_suffix(args))


def _export_vsa_to_musicxml(
    input_path: Path,
    output_path: Path,
    cli_overrides: dict[str, str],
) -> int:
    text = input_path.read_text(encoding="utf-8")
    frontmatter, vsa_body = parse_vsa_frontmatter(text)
    try:
        vsa_body, _ = prepare_vsa_body(text, input_path)
    except IncludeVsaError as exc:
        print(f"{input_path}: {exc.message_nl}", file=sys.stderr)
        return 1
    fm_meta = frontmatter_to_block_metadata(frontmatter)

    metadata = dict(DEFAULT_METADATA)
    metadata.update(fm_meta)
    metadata.update(cli_overrides)

    explicit_keys = set(fm_meta.keys()) | set(cli_overrides.keys())

    document = Parser(preserve_vsa_source_newlines(vsa_body)).parse()

    try:
        renderer = MusicXMLRenderer(metadata=metadata, explicit_keys=explicit_keys)
        xml_str = renderer.render(document)
    except MusicXMLExportError as exc:
        print(f"{input_path}: fout bij MusicXML-export: {exc}", file=sys.stderr)
        return 1

    write_musicxml_output(output_path, xml_str)
    return 0


def _export_md_to_musicxml(
    input_path: Path,
    output_dir: Path,
    cli_overrides: dict[str, str],
    *,
    output_suffix: str = _MUSICXML_SUFFIX,
) -> tuple[int, int]:
    text = input_path.read_text(encoding="utf-8")
    blocks = parse_markdown_blocks(text)

    if not blocks:
        return 0, 0

    output_dir.mkdir(parents=True, exist_ok=True)
    stem = input_path.stem
    written = 0

    for i, block in enumerate(blocks):
        metadata = block.effective_metadata()
        metadata.update(cli_overrides)
        try:
            expanded_body, _ = prepare_markdown_block_body(
                block.body,
                markdown_path=input_path,
                markdown_text=text,
            )
        except IncludeVsaError as exc:
            print(f"{input_path} (blok {i + 1}): {exc.message_nl}", file=sys.stderr)
            return 1, written
        document = block.parse_body(expanded_body)

        explicit_keys = set(block.metadata.keys()) | set(cli_overrides.keys())

        try:
            renderer = MusicXMLRenderer(metadata=metadata, explicit_keys=explicit_keys)
            xml_str = renderer.render(document)
        except MusicXMLExportError as exc:
            print(
                f"{input_path} (blok {i + 1}): fout bij MusicXML-export: {exc}",
                file=sys.stderr,
            )
            return 1, written

        suffix = f"-{i + 1}" if len(blocks) > 1 else ""
        out_file = output_dir / f"{stem}{suffix}{output_suffix}"
        write_musicxml_output(out_file, xml_str)
        written += 1

    return 0, written


def _print_validation_messages(messages, *, summary=False):
    source_lines: dict[str, list[str]] = {}

    for message in messages:
        source_line = None
        if not summary:
            source_line = _validation_context_line(message.source, message.line, source_lines)

        for line in format_validation_message(
            message,
            summary=summary,
            source_line=source_line,
        ):
            print(line)


def _validation_context_line(source: str, line_number: int, cache: dict[str, list[str]]) -> str | None:
    if source not in cache:
        path = Path(source)
        if not path.is_file():
            return None
        cache[source] = path.read_text(encoding="utf-8").splitlines()

    lines = cache[source]
    if line_number < 1 or line_number > len(lines):
        return None

    return lines[line_number - 1]


if __name__ == "__main__":
    raise SystemExit(main())
