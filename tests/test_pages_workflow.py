from pathlib import Path


WORKFLOW = Path(".github/workflows/pages-demo.yml")


def test_pages_workflow_exists():
    assert WORKFLOW.exists()


def test_pages_workflow_is_manual_only():
    text = WORKFLOW.read_text(encoding="utf-8")

    assert "workflow_dispatch:" in text
    assert "push:" not in text


def test_pages_workflow_deploys_production_root_via_deploy_pages():
    text = WORKFLOW.read_text(encoding="utf-8")

    assert "actions/upload-pages-artifact@v3" in text
    assert "actions/deploy-pages@v4" in text
    assert "generated/site/" in text
    assert "pages-site/preview/" not in text


def test_pages_workflow_preserves_existing_site_state():
    text = WORKFLOW.read_text(encoding="utf-8")

    assert "actions/cache/restore@v4" in text
    assert "actions/cache/save@v4" in text
