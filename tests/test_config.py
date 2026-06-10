from pathlib import Path

from vsa.config import load_config


def test_load_missing_config_returns_defaults(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    config = load_config()

    assert config.rendering.max_line_width == 800.0
    assert config.hugo.assets_url_prefix == "/vsa"


def test_load_config_file(tmp_path: Path):
    config_file = tmp_path / "vsa.toml"

    config_file.write_text(
        """[rendering]
max-line-width = 600

[hugo]
assets-url-prefix = "/generated-vsa"
""",
        encoding="utf-8",
    )

    config = load_config(config_file)

    assert config.rendering.max_line_width == 600.0
    assert config.hugo.assets_url_prefix == "/generated-vsa"
