import argparse
import json
import sys
from pathlib import Path

from .parser import Parser
from .block_parser import parse_markdown_blocks
from .validation_runner import validate_file
from .svg_export import export_svg


def main():
    argparser = argparse.ArgumentParser(description="VSA CLI")

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

    argparser.add_argument("legacy_input", nargs="?")
    argparser.add_argument("--ast", action="store_true")

    args = argparser.parse_args()

    if args.command == "svg":
        export_svg(args.input, args.output)
        print(f"SVG geschreven naar: {args.output}")
        return

    if args.command == "validate":
        result = validate_file(args.input)

        if result.ok:
            print("OK")
            sys.exit(0)

        for message in result.messages:
            print(
                f"{message.source}:{message.line}:{message.column}: "
                f"{message.code}: {message.message_nl}"
            )

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
