from pathlib import Path

from vsa.validation_runner import validate_file, validate_path


def test_validate_file_without_config_remains_backwards_compatible(tmp_path: Path):
    path = tmp_path / "invalid.vsa"

    path.write_text(r"{/&\tekst_}", encoding="utf-8")

    result = validate_file(path)

    assert not result.ok
    assert result.has_errors()


def test_validate_path_without_config_remains_backwards_compatible(tmp_path: Path):
    content = tmp_path / "content"
    content.mkdir()

    (content / "invalid.vsa").write_text(r"{/&\tekst_}", encoding="utf-8")

    result = validate_path(content)

    assert not result.ok
    assert result.has_errors()
