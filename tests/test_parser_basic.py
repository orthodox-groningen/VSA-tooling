from vsa.parser import Parser


def test_parse_plain_text():
    doc = Parser("gewone tekst").parse()

    assert doc.to_dict() == {
        "type": "Document",
        "nodes": [
            {
                "type": "TextNode",
                "text": "gewone tekst",
            }
        ],
    }


def test_parse_plain_scope():
    doc = Parser("{tekst}").parse()

    assert doc.to_dict() == {
        "type": "Document",
        "nodes": [
            {
                "type": "ScopeNode",
                "height_modifier": [],
                "text": "tekst",
                "length_modifier": [],
            }
        ],
    }


def test_parse_scope_with_height_and_length():
    doc = Parser("{/tekst_}").parse()

    assert doc.to_dict()["nodes"][0] == {
        "type": "ScopeNode",
        "height_modifier": ["/"],
        "text": "tekst",
        "length_modifier": ["_"],
    }


def test_parse_pitch_marker():
    doc = Parser("[:] {tekst}").parse()

    assert doc.to_dict()["nodes"][0] == {
        "type": "PitchMarkerNode",
        "height_modifier": [],
    }
