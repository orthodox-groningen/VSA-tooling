from pathlib import Path


def test_test_step79_explicit_nav_placeholders_obsolete_policy():
    assert Path("scripts/OBSOLETE_SCRIPTS.md").exists()
