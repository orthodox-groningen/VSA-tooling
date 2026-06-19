from pathlib import Path


def test_test_step75_navigation_praktijk_moved_obsolete_policy():
    assert Path("scripts/OBSOLETE_SCRIPTS.md").exists()
