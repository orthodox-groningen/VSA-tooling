from pathlib import Path


def test_test_step72_nested_vsa_image_refs_obsolete_policy():
    assert Path("scripts/OBSOLETE_SCRIPTS.md").exists()
