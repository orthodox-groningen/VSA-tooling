from pathlib import Path


def test_config_severity_user_doc_exists():
    path = Path("docs/reference/config.md")

    assert path.exists()


def test_config_severity_user_doc_mentions_commands():
    text = Path("docs/reference/config.md").read_text(encoding="utf-8")

    assert "vsa validate" in text
    assert "vsa process" in text
    assert "vsa build-markdown" in text
    assert "vsa.toml" in text


def test_config_severity_user_doc_explains_error_and_warning():
    text = Path("docs/reference/config.md").read_text(encoding="utf-8")

    assert "`error`" in text
    assert "`warning`" in text
    assert "Syntax-errors blijven altijd `error`" in text


def test_cli_config_demo_page_exists_and_is_linked():
    page = Path("examples/hugo-demo/content-source/voorbeelden/cli/config.md")
    index = Path("examples/hugo-demo/content-source/voorbeelden/cli.md")

    assert page.exists()
    assert "(config/)" in index.read_text(encoding="utf-8")


def test_cli_config_demo_mentions_supported_commands():
    text = Path("examples/hugo-demo/content-source/voorbeelden/cli/config.md").read_text(encoding="utf-8")

    assert "`vsa validate`" in text
    assert "`vsa process`" in text
    assert "`vsa build-markdown`" in text
    assert "severity-overrides" in text
