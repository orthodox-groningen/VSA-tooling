from vsa.parser import Parser
from vsa.svg_line_layout import build_lines


def test_short_document_stays_one_line():
    source = "{tekst}"

    document = Parser(source).parse()

    lines = build_lines(document, max_width=300)

    assert len(lines) == 1


def test_long_document_wraps():
    source = " ".join(["{tekst}"] * 40)

    document = Parser(source).parse()

    lines = build_lines(document, max_width=300)

    assert len(lines) > 1


def test_line_widths_respect_limit():
    source = " ".join(["{tekst}"] * 20)

    document = Parser(source).parse()

    lines = build_lines(document, max_width=300)

    assert all(line.width <= 340 for line in lines)
