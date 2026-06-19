from pathlib import Path


def test_test_step69_revert_navigation_obsolete_policy():
    assert Path("scripts/OBSOLETE_SCRIPTS.md").exists()
