from pathlib import Path

from vsa.validation_runner import validate_file


def test_validate_file_reports_empty_final_pitch_marker(tmp_path: Path):
    path = tmp_path / "invalid.vsa"
    path.write_text(r"[:] {/Hei_}{/lig_} is de Heer. [:]", encoding="utf-8")

    result = validate_file(path)

    assert not result.ok
    assert any(
        message.code == "VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER"
        for message in result.messages
    )


def test_validate_file_reports_missing_final_pitch_marker(tmp_path: Path):
    path = tmp_path / "invalid.vsa"
    path.write_text(r"[:] {/Hei_}{/lig_} is de Heer.", encoding="utf-8")

    result = validate_file(path)

    assert not result.ok
    assert any(
        message.code == "VSA-SEMANTIC-MISSING-FINAL-PITCH-MARKER"
        for message in result.messages
    )


def test_validate_file_accepts_final_pitch_marker(tmp_path: Path):
    path = tmp_path / "valid.vsa"
    path.write_text(r"[:] {/Hei_}{/lig_} is de Heer. [\\:]", encoding="utf-8")

    result = validate_file(path)

    assert result.ok
