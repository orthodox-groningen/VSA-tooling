"""Docs-build workflow: TEv2 + MkDocs smoke."""

from pathlib import Path


DOCS_BUILD = Path(".github/workflows/docs-build.yml")
DOCS_PAGES = Path(".github/workflows/docs-pages.yml")


def test_docs_build_workflow_exists():
    assert DOCS_BUILD.exists()


def test_docs_build_runs_on_push_and_pr():
    text = DOCS_BUILD.read_text(encoding="utf-8")
    assert "push:" in text
    assert "pull_request:" in text
    assert "mkdocs build --strict" in text


def test_docs_build_runs_tev2_before_mkdocs():
    text = DOCS_BUILD.read_text(encoding="utf-8")
    assert "prepare-tev2-docs.py" in text
    assert "mrg-import" in text
    assert "mrgt" in text
    assert "hrgt" in text
    assert "trrt" in text
    assert "check-tev2-termrefs.py" in text
    assert text.index("prepare-tev2-docs.py") < text.index("mkdocs build")
    assert text.index("trrt") < text.index("mkdocs build")


def test_docs_build_has_no_hugo_pipeline():
    text = DOCS_BUILD.read_text(encoding="utf-8").lower()
    assert "mkdocs build" in text
    assert "hugo --" not in text
    assert "examples/hugo-demo" not in text


def test_docs_pages_runs_tev2_and_commits_mrgs():
    text = DOCS_PAGES.read_text(encoding="utf-8")
    assert "prepare-tev2-docs.py" in text
    assert "mrg-import" in text
    assert "mrg.vsa-tooling" in text
    assert "git-auto-commit-action" in text
    assert text.index("trrt") < text.index("mkdocs build")
