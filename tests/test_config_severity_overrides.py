from pathlib import Path

from vsa.config import load_config


def test_config_defaults_to_no_severity_overrides():
    config = load_config()

    assert config.validation.severity == {}


def test_config_reads_validation_severity_overrides(tmp_path: Path):
    config_file = tmp_path / "vsa.toml"

    config_file.write_text(
        """
[validation.severity]
VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER = "warning"
VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH = "error"
""",
        encoding="utf-8",
    )

    config = load_config(config_file)

    assert (
        config.validation.severity["VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER"]
        == "warning"
    )
    assert (
        config.validation.severity["VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH"]
        == "error"
    )


def test_config_rejects_unknown_severity(tmp_path: Path):
    config_file = tmp_path / "vsa.toml"

    config_file.write_text(
        """
[validation.severity]
VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER = "info"
""",
        encoding="utf-8",
    )

    try:
        load_config(config_file)
    except ValueError as exc:
        assert "Onbekende severity" in str(exc)
    else:
        raise AssertionError("ValueError verwacht")
