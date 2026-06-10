import argparse
import json
import sys
from pathlib import Path

from .parser import Parser
from .block_parser import parse_markdown_blocks
from .validation_runner import validate_path
from .svg_export import export_svg
from .markdown_processor import process_path, ProcessValidationError
from .markdown_builder import build_markdown_site
from .config import load_config


def _print_validation_messages(messages):
    for message in messages:
        print(
            f"{message.source}:{message.line}:{message.column}: "
            f"{message.code}: {message.message_nl}"
        )


def _resolve_max_line_width(cli_value, config):
    if cli_value is not None:
        return cli_value

    return config.rendering.max_line_width


def _resolve_output_mode(cli_value, config):
    if cli_value is not None:
        return cli_value

    return config.hugo.output_mode


def main():
    argparser = argparse.ArgumentParser(description="VSA CLI")
    argparser.add_argument("--config", default=None)

    subparsers = argparser.add_subparsers(dest="command")

    parse_cmd = subparsers.add_parser("parse")
    parse_cmd.add_argument("input")
    parse_cmd.add_argument("--ast", action="store_true")

    blocks_cmd = subparsers.add_parser("blocks")
    blocks_cmd.add_argument("input")
    blocks_cmd.add_argument("--json", action="store_true")

    validate_cmd = subparsers.add_parser("validate")
    validate_cmd.add_argument("input")

    svg_cmd = subparsers.add_parser("svg")
    svg_cmd.add_argument("input")
    svg_cmd.add_argument("output")
    svg_cmd.add_argument("--max-line-width", type=float, default=None)

    process_cmd = subparsers.add_parser("process")
    process_cmd.add_argument("input")
    process_cmd.add_argument("output_dir")
    process_cmd.add_argument("--no-validate", action="store_true")
    process_cmd.add_argument("--max-line-width", type=float, default=None)

    build_cmd = subparsers.add_parser("build-markdown")
    build_cmd.add_argument("input_dir")
    build_cmd.add_argument("output_dir")
    build_cmd.add_argument("assets_dir")
    build_cmd.add_argument("--assets-url-prefix", default=None)
    build_cmd.add_argument("--max-line-width", type=float, default=None)
    build_cmd.add_argument(
        "--output-mode",
        choices=["img", "shortcode"],
        default=None,
    )

    argparser.add_argument("legacy_input", nargs="?")
    argparser.add_argument("--ast", action="store_true")

    args = argparser.parse_args()
    config = load_config(args.config)

    if args.command == "build-markdown":
        try:
            result = build_markdown_site(
                input_dir=args.input_dir,
                output_dir=args.output_dir,
                assets_dir=args.assets_dir,
                assets_url_prefix=args.assets_url_prefix or config.hugo.assets_url_prefix,
                max_line_width=_resolve_max_line_width(args.max_line_width, config),
                output_mode=_resolve_output_mode(args.output_mode, config),
            )
        except ProcessValidationError as exc:
            _print_validation_messages(exc.messages)
            sys.exit(1)

        print(f"{len(result.markdown_files)} Markdownbestand(en) geschreven")
        print(f"{len(result.svg_files)} SVG-bestand(en) geschreven")
        return

    if args.command == "process":
        try:
            result = process_path(
                args.input,
                args.output_dir,
                validate=not args.no_validate,
                max_line_width=_resolve_max_line_width(args.max_line_width, config),
            )
        except ProcessValidationError as exc:
            _print_validation_messages(exc.messages)
            sys.exit(1)

        print(f"{len(result.blocks)} SVG-bestand(en) gegenereerd")

        for block in result.blocks:
            print(f"- {block.output_file}")

        return

    if args.command == "svg":
        export_svg(
            args.input,
            args.output,
            max_line_width=_resolve_max_line_width(args.max_line_width, config),
        )
        print(f"SVG geschreven naar: {args.output}")
        return

    if args.command == "validate":
        result = validate_path(args.input)

        if result.ok:
            print("OK")
            sys.exit(0)

        _print_validation_messages(result.messages)
        sys.exit(1)

    if args.command == "blocks":
        markdown = Path(args.input).read_text(encoding="utf-8")
        blocks = parse_markdown_blocks(markdown)

        if args.json:
            payload = [
                {
                    "start_line": block.start_line,
                    "end_line": block.end_line,
                    "metadata": block.effective_metadata(),
                    "body": block.body,
                    "ast": block.parse_body().to_dict(),
                }
                for block in blocks
            ]
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(f"{len(blocks)} VSA-blok(ken) gevonden")

        return

    if args.command == "parse":
        input_path = args.input
        show_ast = args.ast
    else:
        input_path = args.legacy_input
        show_ast = args.ast

    if not input_path:
        argparser.print_help()
        return

    text = Path(input_path).read_text(encoding="utf-8")
    document = Parser(text).parse()

    if show_ast:
        print(json.dumps(document.to_dict(), ensure_ascii=False, indent=2))
    else:
        print("OK")


if __name__ == "__main__":
    main()
