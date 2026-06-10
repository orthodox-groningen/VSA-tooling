from pathlib import Path


def test_build_target_workflow_exists():
    assert Path(".github/workflows/build-target.yml").exists()


def test_build_target_workflow_has_preview_and_production():
    text = Path(".github/workflows/build-target.yml").read_text(encoding="utf-8")

    assert "preview" in text
    assert "production" in text
    assert "workflow_dispatch" in text


def test_preview_and_production_scripts_exist():
    assert Path("scripts/build-preview.cmd").exists()
    assert Path("scripts/build-production.cmd").exists()
