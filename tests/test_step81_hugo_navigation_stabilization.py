from pathlib import Path


def test_test_step81_hugo_navigation_stabilization_obsolete_policy():
    assert Path("scripts/OBSOLETE_SCRIPTS.md").exists()
