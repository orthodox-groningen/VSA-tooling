from pathlib import Path


def test_test_step71_hugo_index_navigation_obsolete_policy():
    assert Path("scripts/OBSOLETE_SCRIPTS.md").exists()
