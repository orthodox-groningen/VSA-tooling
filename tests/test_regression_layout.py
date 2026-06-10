from pathlib import Path


def test_regression_directories_exist():
    base = Path("examples/regression")

    assert base.exists()

    subdirs = [p for p in base.iterdir() if p.is_dir()]

    assert len(subdirs) > 0

    for directory in subdirs:
        assert (directory / "input.vsa").exists()
        assert (directory / "expected-ast.json").exists()
        assert (directory / "expected-validation.json").exists()
