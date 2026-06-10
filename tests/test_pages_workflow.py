from pathlib import Path


def test_pages_workflow_exists():
    assert Path(".github/workflows/pages-demo.yml").exists()


def test_pages_workflow_is_manual_only():
    text = Path(".github/workflows/pages-demo.yml").read_text(encoding="utf-8")

    assert "workflow_dispatch" in text
    assert "push:" not in text


def test_pages_workflow_uses_pages_actions():
    text = Path(".github/workflows/pages-demo.yml").read_text(encoding="utf-8")

    assert "actions/configure-pages" in text
    assert "actions/upload-pages-artifact" in text
    assert "actions/deploy-pages" in text
