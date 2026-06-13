from vsa.parser import Parser
from vsa.svg_line_layout import LineLayoutSettings, build_lines


def test_line_layout_includes_scope_gap():
    document = Parser(r"{a}{b}").parse()

    compact = build_lines(
        document,
        max_width=800,
        settings=LineLayoutSettings(scope_gap=0),
    )
    spaced = build_lines(
        document,
        max_width=800,
        settings=LineLayoutSettings(scope_gap=10),
    )

    assert spaced[0].width > compact[0].width


def test_line_layout_includes_pitch_marker_gap():
    document = Parser(r"[:] [:]").parse()

    compact = build_lines(
        document,
        max_width=800,
        settings=LineLayoutSettings(pitch_marker_gap=0),
    )
    spaced = build_lines(
        document,
        max_width=800,
        settings=LineLayoutSettings(pitch_marker_gap=10),
    )

    assert spaced[0].width > compact[0].width
