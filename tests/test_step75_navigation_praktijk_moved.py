from pathlib import Path
import subprocess
import sys


APPLY = Path("scripts/apply-step75-navigation-praktijk-moved.py")
CHECK = Path("scripts/check-hugo-links-and-assets.py")
CONTENT = Path("examples/hugo-demo/content-source")


def test_step75_scripts_exist():
    assert APPLY.exists()
    assert CHECK.exists()


def test_step75_apply_runs():
    result = subprocess.run(
        [sys.executable, str(APPLY)],
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Stap 75" in result.stdout


def test_home_links_to_moved_praktijk_if_present():
    home = CONTENT / "_index.md"
    if not (CONTENT / "praktijk").exists():
        return

    text = home.read_text(encoding="utf-8")
    assert "./praktijk/" in text
    assert "./voorbeelden/praktijk/" not in text


def test_praktijk_index_exists_if_praktijk_dir_exists():
    if not (CONTENT / "praktijk").exists():
        return

    assert (CONTENT / "praktijk" / "_index.md").exists()


def test_link_checker_script_mentions_vsa_assets():
    text = CHECK.read_text(encoding="utf-8")
    assert "img=" in text
    assert "href=" in text
