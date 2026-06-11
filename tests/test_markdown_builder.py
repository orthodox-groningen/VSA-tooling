from pathlib import Path

from vsa.markdown_builder import build_markdown_site


def test_build_markdown_site_rewrites_vsa_block(tmp_path: Path):
    input_dir = tmp_path / "content-source"
    output_dir = tmp_path / "content-generated"
    assets_dir = tmp_path / "static" / "vsa"

    input_dir.mkdir()

    (input_dir / "demo.md").write_text(
        """# Demo

Voor de notatie.

::: vsa-notatie
[:] {/Hei_}{/lig_} is de Heer. [\\\\:]
:::

Na de notatie.
""",
        encoding="utf-8",
    )

    result = build_markdown_site(input_dir, output_dir, assets_dir)

    assert len(result.markdown_files) == 1
    assert len(result.svg_files) == 1

    rewritten = (output_dir / "demo.md").read_text(encoding="utf-8")

    assert "::: vsa-notatie" not in rewritten
    assert '<img class="vsa-notation"' in rewritten
    assert 'src="/vsa/demo-block-1.svg"' in rewritten

    svg = (assets_dir / "demo-block-1.svg").read_text(encoding="utf-8")

    assert "Hei" in svg
