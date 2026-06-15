from vsa.markdown_newline_policy import preserve_vsa_source_newlines
from vsa.markdown_vsa_blocks import extract_vsa_blocks_preserving_newlines
from vsa.parser import Parser
from vsa.svg_line_layout import build_lines


def test_markdown_hardbreak_spaces_before_newline_are_stripped():
    source = "eerste  \ntweede"

    assert preserve_vsa_source_newlines(source) == "eerste\ntweede"


def test_vsa_block_with_markdown_hardbreaks_preserves_real_lines():
    markdown = r"""::: vsa-notatie
[:] Uit {/de} {/ho}{/ge} zijt {\Gij} neergedaald, o Barm{\har}ti{\ge_}.  
Drie {/da}{/gen} {/zijt} Gij {\in} het graf ge{\ble_}{\ven_}  
om {/ons} {/van} {/het} lij{\den} \te ver{\los_}{\sen_}.  
Gij {/zijt} {/ons} {/le}ven {\en} onze verrijzenis, Heer, {\e_}re zij {\U_}. [:]
:::
"""

    block = extract_vsa_blocks_preserving_newlines(markdown)[0]

    assert "  \n" not in block.source
    assert block.source.count("\n") == 3


def test_tropaar_toon_8_like_source_yields_four_layout_lines_without_wrapping():
    source = preserve_vsa_source_newlines(
        r"""[:] Uit {/de} {/ho}{/ge} zijt {\Gij} neergedaald, o Barm{\har}ti{\ge_}.  
Drie {/da}{/gen} {/zijt} Gij {\in} het graf ge{\ble_}{\ven_}  
om {/ons} {/van} {/het} lij{\den} \te ver{\los_}{\sen_}.  
Gij {/zijt} {/ons} {/le}ven {\en} onze verrijzenis, Heer, {\e_}re zij {\U_}. [:]"""
    )

    document = Parser(source).parse()
    lines = build_lines(document, max_width=3000)

    assert len(lines) == 4


def test_no_line_contains_drie_after_first_hardbreak():
    source = preserve_vsa_source_newlines(
        r"""[:] Uit {/de} {/ho}{/ge} zijt {\Gij} neergedaald, o Barm{\har}ti{\ge_}.  
Drie {/da}{/gen} {/zijt} Gij {\in} het graf"""
    )

    document = Parser(source).parse()
    lines = build_lines(document, max_width=3000)

    assert len(lines) == 2
    first_line_texts = [
        getattr(item.node, "text", "")
        for item in lines[0].items
    ]

    assert "Drie" not in first_line_texts
