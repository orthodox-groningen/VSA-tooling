from pathlib import Path


CLI_PAGES = [
    "validate",
    "svg",
    "blocks",
    "parse",
    "process",
    "build-markdown",
    "version",
]


def test_cli_demo_pages_exist():
    for page in CLI_PAGES:
        assert Path(f"examples/hugo-demo/content-source/voorbeelden/cli/{page}.md").exists()


def test_cli_index_links_to_all_command_pages():
    text = Path("examples/hugo-demo/content-source/voorbeelden/cli.md").read_text(encoding="utf-8")

    for page in CLI_PAGES:
        assert f"]({page}/)" in text


def test_each_cli_page_contains_command_input_and_output_sections():
    for page in CLI_PAGES:
        text = Path(f"examples/hugo-demo/content-source/voorbeelden/cli/{page}.md").read_text(encoding="utf-8")

        assert "## Waarvoor gebruik je dit?" in text
        assert "## Commando" in text
        assert "Verwachte output" in text or "verwachte output" in text


def test_validate_page_contains_good_and_bad_example():
    text = Path("examples/hugo-demo/content-source/voorbeelden/cli/validate.md").read_text(encoding="utf-8")

    assert "Goed voorbeeld" in text
    assert "Fout voorbeeld" in text
    assert "VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH" in text


def test_build_markdown_page_explains_three_paths():
    text = Path("examples/hugo-demo/content-source/voorbeelden/cli/build-markdown.md").read_text(encoding="utf-8")

    assert "<input-dir>" in text
    assert "<output-dir>" in text
    assert "<assets-dir>" in text
