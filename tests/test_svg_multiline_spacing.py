from vsa.parser import Parser
from vsa.svg_line_layout import build_lines


def test_multiline_does_not_keep_large_unbreakable_textnode():
    source = r"[:] {/Hei_}{/lig_} is de Heer, en heilig is Zijn Naam. {/Heer_} ontferm U over ons. {/A_}{/men_} [:]"

    document = Parser(source).parse()

    # Met echte DejaVu/Pillow metrics is deze regel compacter.
    # Met 660 testen we nog steeds dat gewone tekstnodes niet als één groot
    # onbreekbaar blok worden behandeld.
    lines = build_lines(document, max_width=660)

    assert len(lines) >= 2


def test_multiline_keeps_reasonable_line_widths():
    source = r"[:] {/Hei_}{/lig_} is de Heer, en heilig is Zijn Naam. {/Heer_} ontferm U over ons. {/A_}{/men_} [:]"

    document = Parser(source).parse()
    lines = build_lines(document, max_width=660)

    assert all(line.width <= 700 for line in lines)
