import argparse
import json
from pathlib import Path

from .parser import Parser
from .block_parser import parse_markdown_blocks


def main():
    argparser = argparse.ArgumentParser(description="VSA CLI")

    subparsers = argparser.add_subparsers(dest="command")

    parse_cmd = subparsers.add_parser("parse", help="Parse één VSA-bestand")
    parse_cmd.add_argument("input")
    parse_cmd.add_argument("--ast", action="store_true")

    blocks_cmd = subparsers.add_parser("blocks", help="Toon VSA-blokken in Markdown")
    blocks_cmd.add_argument("input")
    blocks_cmd.add_argument("--json", action="store_true")

    # Backwards compatible: vsa input.vsa --ast
    argparser.add_argument("legacy_input", nargs="?")
    argparser.add_argument("--ast", action="store_true")

    args = argparser.parse_args()

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
