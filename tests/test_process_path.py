from pathlib import Path

from vsa.markdown_processor import process_path


def test_process_path_accepts_single_file(tmp_path: Path):
    input_file = tmp_path / "demo.md"
    output_dir = tmp_path / "out"

    input_file.write_text(
        """::: vsa-notatie
{tekst}
:::
""",
        encoding="utf-8",
    )

    result = process_path(input_file, output_dir)

    assert len(result.blocks) == 1
    assert Path(result.blocks[0].output_file).exists()


def test_process_path_accepts_directory(tmp_path: Path):
    content = tmp_path / "content"
    output_dir = tmp_path / "out"

    (content / "zondag").mkdir(parents=True)

    (content / "zondag" / "toon-1.md").write_text(
        """::: vsa-notatie
{een}
:::
""",
        encoding="utf-8",
    )

    (content / "zondag" / "toon-2.md").write_text(
        """::: vsa-notatie
{twee}
:::
""",
        encoding="utf-8",
    )

    result = process_path(content, output_dir)

    assert len(result.blocks) == 2

    generated = sorted(output_dir.glob("*.svg"))

    assert len(generated) == 2
    assert any("zondag-toon-1-block-1.svg" in str(path) for path in generated)
    assert any("zondag-toon-2-block-1.svg" in str(path) for path in generated)
