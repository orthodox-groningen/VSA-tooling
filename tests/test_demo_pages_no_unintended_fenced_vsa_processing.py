from pathlib import Path

from vsa.block_parser import parse_markdown_blocks


def test_markdown_demo_has_one_real_vsa_block_only():
    text = Path("examples/hugo-demo/content-source/voorbeelden/markdown.md").read_text(encoding="utf-8")

    blocks = parse_markdown_blocks(text)

    assert len(blocks) == 1
    assert blocks[0].body == r"[:] {/Hei_}{/lig_} is de Heer. [//:]"


def test_all_demo_pages_ignore_vsa_markers_inside_code_fences():
    for path in Path("examples/hugo-demo/content-source").rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        blocks = parse_markdown_blocks(text)

        for block in blocks:
            assert "```" not in block.body
            assert "````" not in block.body
            assert "~~~" not in block.body
