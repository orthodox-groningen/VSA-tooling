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


def test_prefixed_ehm_scope_is_wider_than_plain():
    plain = build_scope_layout(Parser(r"{/ge}").parse().nodes[0])
    prefixed = build_scope_layout(Parser(r"{+/ge}").parse().nodes[0])

    assert prefixed.width > plain.width
    assert prefixed.prefix_extra > 0


def test_prefixed_ehm_filler_width_unchanged():
    """prefix_extra must not inflate filler_width — filler is only for melisma."""
    plain = build_scope_layout(Parser(r"{/ge_}").parse().nodes[0])
    prefixed = build_scope_layout(Parser(r"{+/ge_}").parse().nodes[0])

    assert prefixed.filler_width == plain.filler_width
