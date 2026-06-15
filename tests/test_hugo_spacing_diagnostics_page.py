from pathlib import Path


PAGE = Path("examples/hugo-demo/content-source/voorbeelden/rendering/spacing-diagnostiek.md")


def test_spacing_diagnostics_page_exists():
    assert PAGE.exists()


def test_spacing_diagnostics_contains_known_problem_cases():
    text = PAGE.read_text(encoding="utf-8")

    assert r"me{\\de}{/eeu_}wi{\ge}" in text
    assert r"eerstge{/bo_}re{\ne_}" in text
    assert r"{/ge}{/&/o}pen{baard_}" in text
    assert r"ge{\ble_}{\ven_}" in text


def test_spacing_diagnostics_mentions_markdown_hardbreaks():
    text = PAGE.read_text(encoding="utf-8")

    assert "Markdown hardbreak" in text
    assert "Bronregels blijven regels" in text
