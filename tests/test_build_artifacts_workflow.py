from pathlib import Path


def test_build_artifacts_workflow_exists():
    assert Path(".github/workflows/build-artifacts.yml").exists()


def test_build_artifacts_script_exists():
    assert Path("scripts/build-artifacts.cmd").exists()


def test_build_artifacts_workflow_uploads_expected_artifacts():
    text = Path(".github/workflows/build-artifacts.yml").read_text(encoding="utf-8")

    assert "generated-markdown" in text
    assert "generated-svg" in text
    assert "generated-site" in text
