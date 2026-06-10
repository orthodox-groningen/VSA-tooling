import json
from pathlib import Path

from vsa.parser import Parser


def test_parser_regression_expected_ast_files():
    base = Path("examples/regression")

    for directory in base.iterdir():
        if not directory.is_dir():
            continue

        marker_file = directory / ".parser-step1"

        if not marker_file.exists():
            continue

        input_file = directory / "input.vsa"
        expected_file = directory / "expected-ast.json"

        assert input_file.exists(), f"Ontbreekt: {input_file}"
        assert expected_file.exists(), f"Ontbreekt: {expected_file}"

        source = input_file.read_text(encoding="utf-8")
        expected = json.loads(expected_file.read_text(encoding="utf-8"))

        actual = Parser(source).parse().to_dict()

        assert actual == expected, f"AST mismatch in {directory}"
