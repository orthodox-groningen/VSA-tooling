from vsa.parser import Parser
from vsa.svg_line_layout import build_lines


def test_multiline_does_not_keep_large_unbreakable_textnode():
    source = r"[:] {/Hei_}{/lig_} is de Heer, en heilig is Zijn Naam. {/Heer_} ontferm U over ons. {/A_}{/men_} [:]"

    document = Parser(source).parse()

    lines = build_lines(document, max_width=800)

    assert len(lines) >= 2

    # De eerste regel mag niet kunstmatig extreem veel ongebruikte ruimte hebben.
    assert lines[0].width > 650
