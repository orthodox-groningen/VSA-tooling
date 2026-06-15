from pathlib import Path
import subprocess
import sys


SCRIPT = Path("scripts/revert-step68-navigation.py")
CONTENT_ROOT = Path("examples/hugo-demo/content-source")


def test_revert_step69_script_exists():
    assert SCRIPT.exists()


def test_revert_step69_script_runs():
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Stap 69" in result.stdout


def test_no_injected_vsa_nav_blocks_remain():
    if not CONTENT_ROOT.exists():
        return

    offenders = []
    for path in CONTENT_ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if "VSA-NAV-START" in text or "VSA-NAV-END" in text:
            offenders.append(str(path))

    assert offenders == []


def test_todo_keeps_word_oriented_layout_item_if_present():
    todo = Path("docs/todo.md")
    if not todo.exists():
        return

    text = todo.read_text(encoding="utf-8")

    assert "Woord-georiënteerde SVG-layout" in text
