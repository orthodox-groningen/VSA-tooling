from pathlib import Path


WORKFLOW = Path(".github/workflows/pages-preview.yml")


def test_pages_preview_workflow_exists():
    assert WORKFLOW.exists()


def test_pages_preview_runs_on_push():
    text = WORKFLOW.read_text(encoding="utf-8")

    assert "on:" in text
    assert "push:" in text


def test_pages_preview_builds_with_preview_baseurl():
    text = WORKFLOW.read_text(encoding="utf-8")

    assert '--baseURL "https://orthodox-groningen.github.io/preview/"' in text


def test_pages_preview_deploys_only_preview_directory_to_gh_pages():
    text = WORKFLOW.read_text(encoding="utf-8")

    assert "gh-pages" in text
    assert "rm -rf .pages/preview" in text
    assert "cp -a generated/preview/site/. .pages/preview/" in text
    assert "git -C .pages add -A .nojekyll preview" in text


def test_pages_preview_does_not_modify_manual_production_workflow():
    production = Path(".github/workflows/pages-demo.yml").read_text(encoding="utf-8")

    assert "workflow_dispatch" in production
    assert "actions/deploy-pages" in production
