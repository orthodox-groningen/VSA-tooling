from vsa.parser import Parser
from vsa.scope_layout import build_scope_layout, estimate_text_width
from vsa.svg_line_layout import build_lines


def test_eeu_scope_gets_more_width_than_de_scope():
    eeu = Parser(r"{/eeu_}").parse().nodes[0]
    de = Parser(r"{\\de}").parse().nodes[0]

    assert build_scope_layout(eeu).width > build_scope_layout(de).width


def test_known_overlap_case_stays_single_word_but_has_stable_width():
    document = Parser(r"me{\\de}{/eeu_}wi{\ge}").parse()
    lines = build_lines(document, max_width=3000)

    assert len(lines) == 1
    assert lines[0].width > 90


def test_bore_case_stays_single_word():
    document = Parser(r"eerstge{/bo_}re{\ne_}").parse()
    lines = build_lines(document, max_width=120)

    assert len(lines) == 1


def test_pen_baard_width_is_not_too_compact():
    assert estimate_text_width("pen", 20) + estimate_text_width("baard", 20) > 75


def test_plain_long_text_still_wraps():
    document = Parser(" ".join(["{tekst}"] * 40)).parse()
    lines = build_lines(document, max_width=300)

    assert len(lines) > 1
