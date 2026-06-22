from pathlib import Path


WORKFLOW = Path(".github/workflows/pages-demo.yml")


def test_pages_workflow_exists():
    assert WORKFLOW.exists()


def test_pages_workflow_is_manual_only():
    text = WORKFLOW.read_text(encoding="utf-8")

    assert "workflow_dispatch:" in text
    assert "push:" not in text


def test_pages_workflow_deploys_production_root_to_gh_pages():
    text = WORKFLOW.read_text(encoding="utf-8")

    assert "peaceiris/actions-gh-pages@v3" in text
    assert "publish_branch: gh-pages" in text
    assert "publish_dir: generated/site" in text
    assert "destination_dir: preview" not in text


def test_pages_workflow_preserves_existing_gh_pages_files():
    text = WORKFLOW.read_text(encoding="utf-8")

    assert "keep_files: true" in text
