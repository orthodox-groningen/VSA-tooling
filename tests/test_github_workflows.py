from pathlib import Path


def test_vsa_ci_workflow_exists():
    assert Path(".github/workflows/vsa-ci.yml").exists()


def test_hugo_demo_workflow_exists():
    assert Path(".github/workflows/hugo-demo.yml").exists()


def test_legacy_hugo_workflow_is_dispatch_only():
    path = Path(".github/workflows/hugo.yml")

    assert path.exists()

    text = path.read_text(encoding="utf-8")

    assert "workflow_dispatch" in text
