from pathlib import Path

from vsa.validation_runner import validate_path


GOOD_EXAMPLE_PATHS = [
    Path("examples/hugo-demo/content-source"),
    Path("examples/site-demo"),
    Path("examples/minimal/valid-demo.vsa"),
    Path("examples/minimal/scope-demo.vsa"),
    Path("examples/minimal/valid-block-demo.md"),
    Path("examples/minimal/100_multiline_demo.vsa"),
]


EXPECTED_FAIL_DIR = Path("examples/expected-fail")


def test_all_curated_good_examples_validate():
    for path in GOOD_EXAMPLE_PATHS:
        assert path.exists(), f"Ontbrekend voorbeeld: {path}"

        result = validate_path(path)

        assert result.ok, [
            f"{message.source}: {message.code}: {message.message_nl}"
            for message in result.messages
        ]


def test_expected_fail_examples_do_fail():
    assert EXPECTED_FAIL_DIR.exists()

    expected_fail_files = sorted(EXPECTED_FAIL_DIR.glob("*.vsa"))

    assert expected_fail_files, "Geen expected-fail voorbeelden gevonden"

    for path in expected_fail_files:
        result = validate_path(path)

        assert not result.ok, f"{path} had moeten falen"


def test_expected_fail_examples_are_isolated_from_good_examples():
    assert EXPECTED_FAIL_DIR.exists()
    assert (EXPECTED_FAIL_DIR / "README.md").exists()
