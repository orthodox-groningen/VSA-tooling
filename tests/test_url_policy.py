from pathlib import Path


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def test_no_github_server_url_in_docs_pages_workflow():
    text = read(".github/workflows/docs-pages.yml")
    assert "github.server_url" not in text
    assert "github.repository }}" not in text


def test_docs_pages_production_url():
    text = read(".github/workflows/docs-pages.yml")

    assert "https://orthodox-groningen.github.io/VSA-tooling/" in text
    assert "https://orthodox-groningen.github.io/VSA-tooling/docs/" not in text


def test_docs_pages_preview_url():
    text = read(".github/workflows/docs-pages.yml")

    assert "https://orthodox-groningen.github.io/VSA-tooling/preview/" in text
    assert "docs-preview" not in text


def test_docs_pages_uses_github_pages_host():
    text = read(".github/workflows/docs-pages.yml")

    assert "https://orthodox-groningen.github.io/VSA-tooling/" in text
    assert "https://orthodox-groningen.github.io/VSA-tooling/preview/" in text
