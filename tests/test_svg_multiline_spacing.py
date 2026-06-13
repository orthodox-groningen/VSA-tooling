from vsa.parser import Parser
from vsa.svg_line_layout import build_lines


def test_multiline_does_not_keep_large_unbreakable_textnode():
    source = r"[:] {/Hei_}{/lig_} is de Heer, en heilig is Zijn Naam. {/Heer_} ontferm U over ons. {/A_}{/men_} [:]"

    document = Parser(source).parse()

    # De renderer is compacter geworden; met 700 testen we nog steeds dat
    # gewone tekstnodes niet als één groot onbreekbaar blok worden behandeld.
    lines = build_lines(document, max_width=700)

    assert len(lines) >= 2


def test_multiline_keeps_scopes_as_units():
    source = r"[:] {/Hei_}{/lig_} is de Heer [:]"

    document = Parser(source).parse()

    lines = build_lines(document, max_width=80)

    assert len(lines) >= 2
    assert all(line.items for line in lines)
