from pathlib import Path

from vsa.markdown_processor import process_markdown_file


def test_process_markdown_file_generates_svg(tmp_path: Path):
    input_file = tmp_path / "demo.md"
    output_dir = tmp_path / "out"

    input_file.write_text(
        """# Demo

::: vsa-notatie
[:] {/Hei_}{/lig_} is de Heer. [:]
:::
""",
        encoding="utf-8",
    )

    result = process_markdown_file(input_file, output_dir)

    assert len(result.blocks) == 1

    output_file = Path(result.blocks[0].output_file)

    assert output_file.exists()

    svg = output_file.read_text(encoding="utf-8")

    assert svg.startswith("<svg")
    assert "Hei" in svg
    assert "is de Heer" in svg


def test_process_markdown_file_generates_multiple_svg_files(tmp_path: Path):
    input_file = tmp_path / "demo.md"
    output_dir = tmp_path / "out"

    input_file.write_text(
        """::: vsa-notatie
{een}
:::

::: vsa-notatie
{twee}
:::
""",
        encoding="utf-8",
    )

    result = process_markdown_file(input_file, output_dir)

    assert len(result.blocks) == 2
