from pathlib import Path

from vsa.cli import main


def test_cli_validate_without_config_fails_on_semantic_error(tmp_path: Path):
    path = tmp_path / "invalid.vsa"
    path.write_text(r"[:] {tekst} [:]", encoding="utf-8")

    exit_code = main(["validate", str(path)])

    assert exit_code == 1


def test_cli_validate_with_config_allows_warning(tmp_path: Path):
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

    exit_code = main(["validate", str(path), "--config", str(config_file)])

    assert exit_code == 0


def test_cli_validate_with_config_keeps_syntax_error_fatal(tmp_path: Path):
    config_file = tmp_path / "vsa.toml"
    path = tmp_path / "invalid.vsa"

    config_file.write_text(
        """
[validation.severity]
VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER = "warning"
""",
        encoding="utf-8",
    )
    path.write_text("{onafgesloten", encoding="utf-8")

    exit_code = main(["validate", str(path), "--config", str(config_file)])

    assert exit_code == 1


def test_cli_validate_prints_warning(capsys, tmp_path: Path):
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

    exit_code = main(["validate", str(path), "--config", str(config_file)])
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "WARNING" in output
    assert "VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER" in output
