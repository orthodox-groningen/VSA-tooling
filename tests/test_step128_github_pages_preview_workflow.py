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


def test_pages_preview_deploys_preview_directory_to_gh_pages():
    text = WORKFLOW.read_text(encoding="utf-8")

    assert "peaceiris/actions-gh-pages@v3" in text
    assert "publish_branch: gh-pages" in text
    assert "destination_dir: preview" in text
    assert "keep_files: true" in text


def test_pages_preview_keeps_manual_production_workflow_separate():
    production = Path(".github/workflows/pages-demo.yml").read_text(encoding="utf-8")

    assert "workflow_dispatch" in production
    assert "push:" not in production
    assert "destination_dir: preview" not in production
