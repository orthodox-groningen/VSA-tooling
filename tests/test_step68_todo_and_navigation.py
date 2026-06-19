from pathlib import Path


def test_test_step68_todo_and_navigation_obsolete_policy():
    assert Path("scripts/OBSOLETE_SCRIPTS.md").exists()
