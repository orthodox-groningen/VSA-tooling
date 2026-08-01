"""Docs-build workflow (MkDocs smoke; vervangt Hugo site-build)."""

from pathlib import Path


def test_docs_build_workflow_exists():
    assert Path(".github/workflows/docs-build.yml").exists()


def test_docs_build_runs_on_push_and_pr():
    text = Path(".github/workflows/docs-build.yml").read_text(encoding="utf-8")
    assert "push:" in text
    assert "pull_request:" in text
    assert "mkdocs build --strict" in text


def test_docs_build_has_no_hugo_pipeline():
    text = Path(".github/workflows/docs-build.yml").read_text(encoding="utf-8").lower()
    assert "mkdocs build" in text
    assert "hugo --" not in text
    assert "examples/hugo-demo" not in text
