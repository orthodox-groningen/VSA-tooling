from pathlib import Path


def test_cli_demo_pages_include_config_page_in_index():
    text = Path("examples/hugo-demo/content-source/voorbeelden/cli.md").read_text(encoding="utf-8")

    assert "[`--config`](config/)" in text


def test_cli_config_page_has_expected_sections():
    text = Path("examples/hugo-demo/content-source/voorbeelden/cli/config.md").read_text(encoding="utf-8")

    assert "## Voorbeeldconfig" in text
    assert "## Voorbeeld: validate" in text
    assert "## Voorbeeld: process" in text
    assert "## Voorbeeld: build-markdown" in text
    assert "## Wat blijft altijd hard?" in text
