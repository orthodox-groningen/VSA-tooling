from pathlib import Path

from vsa.validation_runner import validate_file


def test_validate_file_accepts_missing_final_pitch_marker(tmp_path: Path):
    path = tmp_path / "valid.vsa"
    path.write_text(r"[:] {/Hei_}{/lig_} is de Heer.", encoding="utf-8")

    result = validate_file(path)

    assert result.ok


def test_validate_file_accepts_empty_final_pitch_marker(tmp_path: Path):
    path = tmp_path / "valid.vsa"
    path.write_text(r"[:] {/Hei_}{/lig_} is de Heer. [:]", encoding="utf-8")

    result = validate_file(path)

    assert result.ok


def test_validate_file_accepts_directional_final_pitch_marker(tmp_path: Path):
    path = tmp_path / "valid.vsa"
    path.write_text(r"[:] {/Hei_}{/lig_} is de Heer. [\\:]", encoding="utf-8")

    result = validate_file(path)

    assert result.ok
