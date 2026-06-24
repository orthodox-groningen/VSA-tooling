from pathlib import Path

from vsa.block_parser import parse_markdown_blocks
from vsa.markdown_builder import build_markdown_site


def test_parse_markdown_blocks_ignores_vsa_markers_inside_backtick_fence():
    markdown = """# Demo

```markdown
::: vsa-notatie
{dit-is-een-voorbeeld}
:::
```

::: vsa-notatie
{echt}
:::
"""

    blocks = parse_markdown_blocks(markdown)

    assert len(blocks) == 1
    assert blocks[0].body == "{echt}"


def test_parse_markdown_blocks_ignores_vsa_markers_inside_tilde_fence():
    markdown = """# Demo

~~~markdown
::: vsa-notatie
{dit-is-een-voorbeeld}
:::
~~~

::: vsa-notatie
{echt}
:::
"""

    blocks = parse_markdown_blocks(markdown)

    assert len(blocks) == 1
    assert blocks[0].body == "{echt}"


def test_build_markdown_keeps_code_fenced_vsa_example_literal(tmp_path: Path):
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    assets_dir = tmp_path / "assets"

    input_dir.mkdir()

    (input_dir / "demo.md").write_text(
        """# Demo

````markdown
::: vsa-notatie
{voorbeeld}
:::
````

::: vsa-notatie
{echt}
:::
""",
        encoding="utf-8",
    )

    result = build_markdown_site(input_dir, output_dir, assets_dir)

    rewritten = (output_dir / "demo.md").read_text(encoding="utf-8")

    assert "::: vsa-notatie\n{voorbeeld}\n:::" in rewritten
    assert rewritten.count('<img class="vsa-notation"') == 1
    assert len(result.svg_files) == 1


def test_demo_markdown_page_keeps_bron_markdown_as_code_example():
    text = Path("examples/hugo-demo/content-source/voorbeelden/markdown.md").read_text(encoding="utf-8")

    assert "````markdown" in text
    assert "[:] {/Hei_}{/lig_} is de Heer. [//:]" in text
