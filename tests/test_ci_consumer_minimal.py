from pathlib import Path


def test_ci_consumer_minimal_input_exists():
    assert Path("examples/consumer-minimal/content-source/smoke.md").exists()
    assert Path("examples/consumer-minimal/content-source/fragment.vsa").exists()


def test_ci_script_exists():
    assert Path("scripts/ci.cmd").exists()
