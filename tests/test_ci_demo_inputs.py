from pathlib import Path


def test_ci_demo_input_exists():
    path = Path("examples/hugo-demo/content-source/zondag/toon-1.md")

    assert path.exists()


def test_ci_script_exists():
    path = Path("scripts/ci.cmd")

    assert path.exists()
