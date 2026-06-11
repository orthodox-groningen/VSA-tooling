from pathlib import Path

import pytest

from vsa.config import load_config
from vsa.markdown_builder import build_markdown_site
from vsa.markdown_processor import ProcessValidationError, process_path


def _write_warning_config(path: Path):
    path.write_text(
        """
[validation.severity]
VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH = "warning"
""",
        encoding="utf-8",
    )


def test_process_path_without_config_still_fails_on_semantic_error(tmp_path: Path):
    input_file = tmp_path / "demo.md"
    output_dir = tmp_path / "out"

    input_file.write_text(
        r"""::: vsa-notatie
{/&\tekst_}
:::
""",
        encoding="utf-8",
    )

    with pytest.raises(ProcessValidationError):
        process_path(input_file, output_dir)


def test_process_path_uses_configured_warning(tmp_path: Path):
    config_file = tmp_path / "vsa.toml"
    input_file = tmp_path / "demo.md"
    output_dir = tmp_path / "out"

    _write_warning_config(config_file)

    input_file.write_text(
        r"""::: vsa-notatie
{/&\tekst_}
:::
""",
        encoding="utf-8",
    )

    config = load_config(config_file)
    result = process_path(input_file, output_dir, config=config)

    assert len(result.blocks) == 1


def test_build_markdown_without_config_still_fails_on_semantic_error(tmp_path: Path):
    input_dir = tmp_path / "content"
    output_dir = tmp_path / "generated"
    assets_dir = tmp_path / "assets"

    input_dir.mkdir()

    (input_dir / "demo.md").write_text(
        r"""::: vsa-notatie
{/&\tekst_}
:::
""",
        encoding="utf-8",
    )

    with pytest.raises(ProcessValidationError):
        build_markdown_site(input_dir, output_dir, assets_dir)


def test_build_markdown_uses_configured_warning(tmp_path: Path):
    config_file = tmp_path / "vsa.toml"
    input_dir = tmp_path / "content"
    output_dir = tmp_path / "generated"
    assets_dir = tmp_path / "assets"

    input_dir.mkdir()
    _write_warning_config(config_file)

    (input_dir / "demo.md").write_text(
        r"""::: vsa-notatie
{/&\tekst_}
:::
""",
        encoding="utf-8",
    )

    config = load_config(config_file)
    result = build_markdown_site(input_dir, output_dir, assets_dir, config=config)

    assert len(result.markdown_files) == 1
    assert len(result.svg_files) == 1
