from pathlib import Path


def test_test_step78_index_nav_blocks_only_obsolete_policy():
    assert Path("scripts/OBSOLETE_SCRIPTS.md").exists()
