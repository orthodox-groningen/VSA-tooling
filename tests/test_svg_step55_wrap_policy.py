from vsa.parser import Parser
from vsa.svg_line_layout import HardBreakNode, build_lines, iter_layout_nodes


def test_source_newline_is_hard_break_node():
    document = Parser("eerste\ntweede").parse()
    nodes = list(iter_layout_nodes(document))

    assert any(isinstance(node, HardBreakNode) for node in nodes)


def test_source_newline_forces_layout_break():
    document = Parser("eerste\ntweede").parse()
    lines = build_lines(document, max_width=800)

    assert len(lines) == 2


def test_crlf_source_newline_forces_layout_break():
    document = Parser("eerste\r\ntweede").parse()
    lines = build_lines(document, max_width=800)

    assert len(lines) == 2


def test_no_midword_wrapping_still_holds():
    document = Parser(r"eerstge{/bo_}re{\ne_}").parse()
    lines = build_lines(document, max_width=120)

    assert len(lines) == 1
