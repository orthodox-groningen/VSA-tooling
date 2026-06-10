from pathlib import Path

from vsa.config import load_config
from vsa.markdown_builder import build_markdown_site


def test_build_markdown_uses_config_values_when_passed(tmp_path: Path):
    config_file = tmp_path / "vsa.toml"
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    assets_dir = tmp_path / "assets"

    input_dir.mkdir()

    config_file.write_text(
        """[rendering]
max-line-width = 300

[hugo]
assets-url-prefix = "/custom-vsa"
""",
        encoding="utf-8",
    )

    (input_dir / "demo.md").write_text(
        """::: vsa-notatie
{tekst}
:::
""",
        encoding="utf-8",
    )

    config = load_config(config_file)

    result = build_markdown_site(
        input_dir,
        output_dir,
        assets_dir,
        assets_url_prefix=config.hugo.assets_url_prefix,
        max_line_width=config.rendering.max_line_width,
    )

    assert len(result.svg_files) == 1

    rewritten = (output_dir / "demo.md").read_text(encoding="utf-8")

    assert 'src="/custom-vsa/demo-block-1.svg"' in rewritten
