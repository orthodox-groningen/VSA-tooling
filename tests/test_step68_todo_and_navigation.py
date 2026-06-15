from pathlib import Path
import subprocess
import sys


SCRIPT = Path("scripts/apply-step68-todo-and-navigation.py")


def test_step68_apply_script_exists():
    assert SCRIPT.exists()


def test_step68_script_mentions_word_oriented_layout():
    text = SCRIPT.read_text(encoding="utf-8")

    assert "Woord-georiënteerde SVG-layout" in text
    assert "woordcluster" in text


def test_step68_script_mentions_navigation_markers():
    text = SCRIPT.read_text(encoding="utf-8")

    assert "VSA-NAV-START" in text
    assert "Navigatie" in text


def test_step68_apply_script_runs():
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Stap 68 toegepast" in result.stdout


def test_todo_contains_word_oriented_layout_after_apply():
    text = Path("docs/todo.md").read_text(encoding="utf-8")

    assert "Woord-georiënteerde SVG-layout" in text


def test_spacing_diagnostics_has_navigation_after_apply():
    path = Path("examples/hugo-demo/content-source/voorbeelden/rendering/spacing-diagnostiek.md")

    if not path.exists():
        return

    text = path.read_text(encoding="utf-8")

    assert "VSA-NAV-START" in text
    assert "## Navigatie" in text
