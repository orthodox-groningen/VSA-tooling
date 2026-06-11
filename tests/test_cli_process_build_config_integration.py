from pathlib import Path

from vsa.cli import main


def _write_warning_config(path: Path):
    path.write_text(
        """
[validation.severity]
VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER = "warning"
""",
        encoding="utf-8",
    )


def test_cli_process_uses_configured_warning(tmp_path: Path):
    config_file = tmp_path / "vsa.toml"
    input_file = tmp_path / "demo.md"
    output_dir = tmp_path / "out"

    _write_warning_config(config_file)

    input_file.write_text(
        r"""::: vsa-notatie
[:] {tekst} [:]
:::
""",
        encoding="utf-8",
    )

    exit_code = main(
        [
            "process",
            str(input_file),
            str(output_dir),
            "--config",
            str(config_file),
        ]
    )

    assert exit_code == 0


def test_cli_build_markdown_uses_configured_warning(tmp_path: Path):
    config_file = tmp_path / "vsa.toml"
    input_dir = tmp_path / "content"
    output_dir = tmp_path / "generated"
    assets_dir = tmp_path / "assets"

    input_dir.mkdir()
    _write_warning_config(config_file)

    (input_dir / "demo.md").write_text(
        r"""::: vsa-notatie
[:] {tekst} [:]
:::
""",
        encoding="utf-8",
    )

    exit_code = main(
        [
            "build-markdown",
            str(input_dir),
            str(output_dir),
            str(assets_dir),
            "--config",
            str(config_file),
        ]
    )

    assert exit_code == 0
