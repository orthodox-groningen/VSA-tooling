from pathlib import Path

from vsa.validation_runner import validate_path


GOOD_EXAMPLE_PATHS = [
    Path("examples/hugo-demo/content-source"),
    Path("examples/minimal"),
    Path("examples/site-demo"),
]


EXPECTED_FAIL_FILES = [
    Path("examples/expected-fail/semantic-mismatch.vsa"),
    Path("examples/expected-fail/empty-scope.vsa"),
    Path("examples/expected-fail/unclosed-scope.vsa"),
]


def test_all_good_examples_validate():
    for path in GOOD_EXAMPLE_PATHS:
        result = validate_path(path)

        assert result.ok, [
            f"{message.source}: {message.code}: {message.message_nl}"
            for message in result.messages
        ]


def test_expected_fail_examples_do_fail():
    for path in EXPECTED_FAIL_FILES:
        result = validate_path(path)

        assert not result.ok, f"{path} had moeten falen"


def test_expected_fail_examples_are_isolated_from_good_examples():
    assert Path("examples/expected-fail").exists()
    assert Path("examples/expected-fail/README.md").exists()
