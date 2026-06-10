from pathlib import Path


def test_release_artifacts_workflow_exists():
    assert Path(".github/workflows/release-artifacts.yml").exists()


def test_changelog_exists():
    assert Path("CHANGELOG.md").exists()


def test_release_workflow_builds_python_package():
    text = Path(".github/workflows/release-artifacts.yml").read_text(encoding="utf-8")

    assert "python -m build" in text
    assert "dist/*" in text
