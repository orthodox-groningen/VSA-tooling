from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "examples" / "hugo-demo" / "content-source"
STABILIZE = ROOT / "scripts" / "stabilize-hugo-navigation.py"


def test_step81_scripts_exist():
    assert (ROOT / "scripts" / "update-nav-placeholders.py").exists()
    assert STABILIZE.exists()
    assert (ROOT / "scripts" / "repo_root.py").exists()


def test_stabilize_hugo_navigation_runs_from_repo_root():
    result = subprocess.run(
        [sys.executable, str(STABILIZE)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "navigatie gestabiliseerd" in result.stdout


def test_stabilize_hugo_navigation_runs_from_subdirectory():
    subdir = ROOT / "xxx"
    subdir.mkdir(exist_ok=True)

    result = subprocess.run(
        [sys.executable, str(STABILIZE)],
        cwd=subdir,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "navigatie gestabiliseerd" in result.stdout


def test_no_old_navigation_artifacts_remain_after_stabilize():
    offenders = []
    for path in CONTENT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        forbidden = [
            "Gegenereerd door scripts/apply-step71",
            "Gegenereerd door scripts/apply-step75",
            "VSA-INDEX-NAV-START",
            "VSA-SITE-NAV-START",
            "VSA-NAV-START",
        ]
        if any(item in text for item in forbidden):
            offenders.append(str(path))
    assert offenders == []


def test_index_pages_have_placeholders_after_stabilize():
    indexes = list(CONTENT.rglob("_index.md"))
    assert indexes

    offenders = []
    for index in indexes:
        text = index.read_text(encoding="utf-8")
        if "<!-- VSA-NAV:" not in text:
            offenders.append(str(index))
    assert offenders == []


def test_obsolete_examples_examples_directory_removed_or_absent():
    assert not (ROOT / "examples" / "examples").exists()
