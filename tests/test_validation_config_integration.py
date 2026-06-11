from pathlib import Path

from vsa.config import load_config
from vsa.validation_runner import validate_file, validate_path


def test_validate_file_without_semantic_errors_is_ok(tmp_path: Path):
    path = tmp_path / "valid.vsa"
    path.write_text(r"[:] {tekst} [:]", encoding="utf-8")

    result = validate_file(path)

    assert result.ok
    assert result.messages == []


def test_validate_file_with_modifier_mismatch_is_error_by_default(tmp_path: Path):
    path = tmp_path / "invalid.vsa"
    path.write_text(r"{/&\tekst_}", encoding="utf-8")

    result = validate_file(path)

    assert not result.ok
    assert result.has_errors()


def test_validate_file_uses_warning_override_for_modifier_mismatch(tmp_path: Path):
    config_file = tmp_path / "vsa.toml"
    path = tmp_path / "warning.vsa"

    config_file.write_text(
        """
[validation.severity]
VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH = "warning"
""",
        encoding="utf-8",
    )

    path.write_text(r"{/&\tekst_}", encoding="utf-8")

    config = load_config(config_file)
    result = validate_file(path, config=config)

    assert result.ok
    assert result.has_warnings()


def test_validate_path_uses_configured_warning_severity_for_directory(tmp_path: Path):
    config_file = tmp_path / "vsa.toml"
    content = tmp_path / "content"

    content.mkdir()

    config_file.write_text(
        """
[validation.severity]
VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH = "warning"
""",
        encoding="utf-8",
    )

    (content / "one.vsa").write_text(r"{/&\tekst_}", encoding="utf-8")

    config = load_config(config_file)
    result = validate_path(content, config=config)

    assert result.ok
    assert result.has_warnings()
