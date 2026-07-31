from vsa.markdown_vsa_blocks import (
    extract_vsa_blocks_preserving_newlines,
    normalize_newlines_preserving_line_boundaries,
)
from vsa.parser import Parser
from vsa.svg_line_layout import build_lines


def test_extract_colon_fenced_vsa_block_preserves_lf_newlines():
    markdown = """# Demo

::: vsa-notatie
[:] eerste regel
tweede regel
:::
"""

    blocks = extract_vsa_blocks_preserving_newlines(markdown)

    assert len(blocks) == 1
    assert blocks[0].source == "[:] eerste regel\ntweede regel"


def test_extract_backtick_fenced_vsa_block_preserves_lf_newlines():
    markdown = """# Demo

```vsa
[:] eerste regel
tweede regel
```
"""

    blocks = extract_vsa_blocks_preserving_newlines(markdown)

    assert len(blocks) == 1
    assert blocks[0].source == "[:] eerste regel\ntweede regel"


def test_normalize_crlf_and_cr_without_joining_lines():
    source = "eerste\r\ntweede\rderde"

    assert normalize_newlines_preserving_line_boundaries(source) == "eerste\ntweede\nderde"


def test_preserved_newlines_force_svg_layout_lines():
    markdown = """::: vsa-notatie
[:] eerste regel
tweede regel
:::
"""

    block = extract_vsa_blocks_preserving_newlines(markdown)[0]
    document = Parser(block.source).parse()
    lines = build_lines(document, max_width=2000)

    assert len(lines) == 2


def test_tone8_like_multiline_block_keeps_physical_lines():
    markdown = r"""::: vsa-notatie
[:] Uit {/de} {/ho}{/ge} zijt {\Gij} neergedaald, o Barm{\har_}ti{\ge_}.
Drie {/da}{/gen} {/zijt} Gij {\in} het graf ge{\ble_}{\ven_}
Gij {/zijt} {/ons} {/le}ven {\en} onze verrijzenis, Heer, {\e_}re zij {\U_}. [:]
:::
"""

    block = extract_vsa_blocks_preserving_newlines(markdown)[0]
    document = Parser(block.source).parse()
    lines = build_lines(document, max_width=2000)

    assert len(lines) == 3
