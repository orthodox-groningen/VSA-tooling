from pathlib import Path
import pytest

from vsa.config import load_config


def test_config_default_output_mode_is_img(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    config = load_config()

    assert config.hugo.output_mode == "img"


def test_config_loads_shortcode_output_mode(tmp_path: Path):
    config_file = tmp_path / "vsa.toml"

    config_file.write_text(
        '''[hugo]
output-mode = "shortcode"
''',
        encoding="utf-8",
    )

    config = load_config(config_file)

    assert config.hugo.output_mode == "shortcode"


def test_config_rejects_invalid_output_mode(tmp_path: Path):
    config_file = tmp_path / "vsa.toml"

    config_file.write_text(
        '''[hugo]
output-mode = "invalid"
''',
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        load_config(config_file)
