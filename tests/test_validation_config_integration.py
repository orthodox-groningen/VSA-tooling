from pathlib import Path

from vsa.config import load_config
from vsa.validation_runner import validate_file, validate_path


def test_validate_file_defaults_semantic_issue_to_error(tmp_path: Path):
    path = tmp_path / "invalid.vsa"
    path.write_text(r"[:] {tekst} [:]", encoding="utf-8")

    result = validate_file(path)

    assert not result.ok
    assert result.has_errors()


def test_validate_file_uses_configured_warning_severity(tmp_path: Path):
    config_file = tmp_path / "vsa.toml"
    path = tmp_path / "warning.vsa"

    config_file.write_text(
        """
[validation.severity]
VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER = "warning"
""",
        encoding="utf-8",
    )

    path.write_text(r"[:] {tekst} [:]", encoding="utf-8")

    config = load_config(config_file)
    result = validate_file(path, config=config)

    assert result.ok
    assert not result.has_errors()
    assert result.has_warnings()
    assert result.messages[0].severity == "warning"


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
    (content / "two.md").write_text(
        r"""::: vsa-notatie
{/&\woord_}
:::
""",
        encoding="utf-8",
    )

    config = load_config(config_file)
    result = validate_path(content, config=config)

    assert result.ok
    assert not result.has_errors()
    assert result.has_warnings()
    assert len(result.messages) == 2
    assert {message.severity for message in result.messages} == {"warning"}


def test_syntax_error_still_fails_even_with_semantic_warning_config(tmp_path: Path):
    config_file = tmp_path / "vsa.toml"
    path = tmp_path / "invalid.vsa"

    config_file.write_text(
        """
[validation.severity]
VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH = "warning"
""",
        encoding="utf-8",
    )

    path.write_text("{onafgesloten", encoding="utf-8")

    config = load_config(config_file)
    result = validate_file(path, config=config)

    assert not result.ok
    assert result.has_errors()
    assert not result.has_warnings()
