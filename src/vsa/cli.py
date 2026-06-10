import argparse
import json
from pathlib import Path

from .parser import Parser


def main():
    argparser = argparse.ArgumentParser(description="VSA CLI")
    argparser.add_argument("input", help="VSA inputbestand")
    argparser.add_argument("--ast", action="store_true", help="Print AST als JSON")

    args = argparser.parse_args()

    text = Path(args.input).read_text(encoding="utf-8")
    document = Parser(text).parse()

    if args.ast:
        print(json.dumps(document.to_dict(), ensure_ascii=False, indent=2))
    else:
        print("OK")


if __name__ == "__main__":
    main()
