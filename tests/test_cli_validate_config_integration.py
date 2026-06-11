from pathlib import Path

from vsa.cli import main


def test_cli_validate_without_config_succeeds_when_final_marker_is_omitted(tmp_path: Path):
    path = tmp_path / "valid.vsa"
    path.write_text(r"[:] {tekst}", encoding="utf-8")

    exit_code = main(["validate", str(path)])

    assert exit_code == 0


def test_cli_validate_with_valid_final_marker_is_ok(tmp_path: Path):
    path = tmp_path / "valid.vsa"
    path.write_text(r"[:] {tekst} [:]", encoding="utf-8")

    exit_code = main(["validate", str(path)])

    assert exit_code == 0


def test_cli_validate_config_still_handles_semantic_warning(capsys, tmp_path: Path):
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

    exit_code = main(["validate", str(path), "--config", str(config_file)])
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "WARNING" in output
    assert "VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH" in output
