from vsa.parser import Parser
from vsa.position_builder import PositionBuilder


def test_single_position_defaults():
    doc = Parser("{tekst}").parse()

    positions = PositionBuilder(doc).build()

    assert len(positions) == 1

    assert positions[0].ehm == "~"
    assert positions[0].elm == "~"


def test_missing_length_expands_to_height_count():
    doc = Parser(r"{/&\tekst}").parse()

    positions = PositionBuilder(doc).build()

    assert len(positions) == 2

    assert positions[0].elm == "~"
    assert positions[1].elm == "~"


def test_compound_positions():
    doc = Parser(r"{/&\&/tekst_&~&~}").parse()

    positions = PositionBuilder(doc).build()

    assert len(positions) == 3

    assert positions[0].ehm == "/"
    assert positions[1].ehm == "\\"
    assert positions[2].ehm == "/"
