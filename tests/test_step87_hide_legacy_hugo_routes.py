from pathlib import Path


def test_test_step87_hide_legacy_hugo_routes_obsolete_policy():
    assert Path("scripts/OBSOLETE_SCRIPTS.md").exists()
