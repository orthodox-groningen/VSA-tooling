from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore").replace("\r\n", "\n")


def test_gitignore_marks_generated_as_build_output():
    text = read(ROOT / ".gitignore")
    assert "generated/" in text


def test_ci_uses_consumer_minimal_not_mutating_source():
    text = read(SCRIPTS / "ci.cmd")
    assert r"examples\consumer-minimal\content-source" in text
    assert "build-markdown" in text
    assert "sync-bron-zondagen" not in text
    assert "sync_bron_zondagen" not in text


def test_retry_cmd_is_obsolete_and_points_to_test_cmd():
    retry = SCRIPTS / "retry.cmd"
    if not retry.exists():
        return

    text = read(retry).lower()
    assert "verouderd" in text or "obsolete" in text
    assert r"scripts\test.cmd" in text


def test_scripts_readme_warns_against_rewriting_content_source():
    text = read(SCRIPTS / "README.md")
    assert "niet redactioneel herschrijven" in text.lower() or "content-source" in text


def test_repo_root_detection_uses_package_markers():
    import sys

    sys.path.insert(0, str(SCRIPTS))
    from repo_root import find_repo_root

    root = find_repo_root(SCRIPTS)
    assert (root / "pyproject.toml").is_file()
    assert (root / "src" / "vsa").is_dir()
