from pathlib import Path

from docs_contracts import doc, read_doc, assert_terms


def test_config_severity_user_doc_exists():
    assert doc("config_reference").exists()


def test_config_severity_user_doc_mentions_commands():
    text = read_doc("config_reference")

    assert_terms(text, ("vsa validate", "vsa process", "vsa build-markdown", "vsa.toml"))


def test_config_severity_user_doc_explains_error_and_warning():
    text = read_doc("config_reference")

    assert_terms(text, ("`error`", "`warning`", "Syntax-errors blijven altijd `error`"))


def test_cli_config_demo_page_exists_and_is_linked():
    page = Path("examples/hugo-demo/content-source/voorbeelden/cli/config.md")
    index = Path("examples/hugo-demo/content-source/voorbeelden/cli.md")

    assert page.exists()
    assert "(config/)" in index.read_text(encoding="utf-8")


def test_cli_config_demo_mentions_supported_commands():
    text = Path("examples/hugo-demo/content-source/voorbeelden/cli/config.md").read_text(encoding="utf-8")

    assert_terms(
        text,
        ("`vsa validate`", "`vsa process`", "`vsa build-markdown`", "severity-overrides"),
    )
