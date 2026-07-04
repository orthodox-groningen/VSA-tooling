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

    assert '--baseURL "https://orthodox-groningen.github.io/VSA-tooling/preview/"' in text


def test_pages_preview_deploys_preview_directory_to_gh_pages():
    text = WORKFLOW.read_text(encoding="utf-8")
    reusable = Path(".github/workflows/pages-deploy-reusable.yml").read_text(
        encoding="utf-8"
    )

    assert "pages-deploy-reusable.yml" in text
    assert "destination_dir: preview" in text
    assert "peaceiris/actions-gh-pages@v3" in reusable
    assert "keep_files:" in reusable


def test_pages_preview_skips_redundant_pytest():
    text = WORKFLOW.read_text(encoding="utf-8")

    assert "pytest" not in text


def test_pages_preview_keeps_manual_production_workflow_separate():
    production = Path(".github/workflows/pages-demo.yml").read_text(encoding="utf-8")

    assert "workflow_dispatch" in production
    assert "push:" not in production
    assert "destination_dir: preview" not in production
