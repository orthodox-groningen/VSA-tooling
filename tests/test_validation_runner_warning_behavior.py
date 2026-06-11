from pathlib import Path

from vsa.validation_runner import validate_file


def test_semantic_error_still_fails_validation_for_now(tmp_path: Path):
    path = tmp_path / "semantic-error.vsa"

    path.write_text(
        r"{/&\tekst_}",
        encoding="utf-8",
    )

    result = validate_file(path)

    assert not result.ok
    assert result.has_errors()


def test_syntax_error_still_fails_validation(tmp_path: Path):
    path = tmp_path / "invalid.vsa"

    path.write_text(
        r"{onafgesloten",
        encoding="utf-8",
    )

    result = validate_file(path)

    assert not result.ok
    assert result.has_errors()
