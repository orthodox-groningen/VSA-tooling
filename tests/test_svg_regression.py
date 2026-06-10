from pathlib import Path
import json

from vsa.parser import Parser
from vsa.svg_renderer import SVGRenderer


def test_svg_regression_cases():
    base = Path("examples/regression")

    cases = [
        path
        for path in base.iterdir()
        if path.is_dir() and (path / ".svg-regression").exists()
    ]

    assert cases, "Geen SVG-regressietests gevonden."

    for case in cases:
        input_file = case / "input.vsa"
        expected_meta_file = case / "expected-svg-meta.json"

        assert input_file.exists(), f"Ontbreekt: {input_file}"
        assert expected_meta_file.exists(), f"Ontbreekt: {expected_meta_file}"

        source = input_file.read_text(encoding="utf-8")
        expected = json.loads(expected_meta_file.read_text(encoding="utf-8"))

        document = Parser(source).parse()
        actual = SVGRenderer().render_document(document)

        assert actual.startswith("<svg"), f"Geen SVG-start in {case}"
        assert "</svg>" in actual, f"Geen SVG-einde in {case}"

        for text in expected.get("contains_text", []):
            assert text in actual, f"Ontbrekende tekst '{text}' in {case}"

        if "min_lines" in expected:
            assert actual.count("<line") >= expected["min_lines"], f"Te weinig lijnen in {case}"

        if "min_circles" in expected:
            assert actual.count("<circle") >= expected["min_circles"], f"Te weinig punten in {case}"
