from pathlib import Path


CONFIGURE = Path(".github/workflows/pages-configure-legacy.yml")


def test_pages_configure_legacy_workflow_exists():
    assert CONFIGURE.exists()


def test_pages_configure_legacy_is_workflow_dispatch():
    text = CONFIGURE.read_text(encoding="utf-8")

    assert "workflow_dispatch:" in text
    assert "pages: write" in text
    assert "administration: write" in text


def test_pages_configure_legacy_sets_gh_pages_branch():
    text = CONFIGURE.read_text(encoding="utf-8")

    assert "build_type\":\"legacy\"" in text
    assert '"branch":"gh-pages"' in text
    assert '"path":"/"' in text
