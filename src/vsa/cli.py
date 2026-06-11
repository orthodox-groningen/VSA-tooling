from __future__ import annotations

import argparse
import json
import sys
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

from .block_parser import parse_markdown_blocks
from .config import load_config
from .markdown_builder import build_markdown_site
from .markdown_processor import ProcessValidationError, process_path
from .parser import Parser
from .svg_renderer import SVGRenderer
from .validation_runner import validate_path


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

    parse = subparsers.add_parser("parse")
    parse.add_argument("path")
    parse.add_argument("--ast", action="store_true")

    blocks = subparsers.add_parser("blocks")
    blocks.add_argument("path")
    blocks.add_argument("--json", action="store_true")

    svg = subparsers.add_parser("svg")
    svg.add_argument("input")
    svg.add_argument("output")
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
        _print_validation_messages(result.messages)

    if result.ok:
        if not result.messages:
            print("OK")
        return 0

    return 1


def _cmd_parse(args):
    text = Path(args.path).read_text(encoding="utf-8")
    document = Parser(text).parse()

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
    text = Path(args.input).read_text(encoding="utf-8")
    document = Parser(text).parse()

    renderer = SVGRenderer()
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


def _print_validation_messages(messages):
    for message in messages:
        severity = getattr(message, "severity", "error").upper()

        print(
            f"{message.source}:{message.line}:{message.column}: "
            f"{severity}: {message.code}: {message.message_nl}"
        )


if __name__ == "__main__":
    raise SystemExit(main())
