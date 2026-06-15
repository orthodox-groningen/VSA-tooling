from vsa.parser import Parser
from vsa.scope_layout import build_scope_layout


def test_single_scope_has_positive_width():
    document = Parser("{tekst}").parse()
    layout = build_scope_layout(document.nodes[0])

    assert layout.width > 0


def test_multi_modifier_scope_gets_filler_width():
    document = Parser(r"{/&/&/&/schon}").parse()
    layout = build_scope_layout(document.nodes[0])

    assert layout.filler_width > 0


def test_short_scope_not_forced_to_old_large_width():
    document = Parser(r"{/i_}").parse()
    layout = build_scope_layout(document.nodes[0])

    assert layout.width < 20
