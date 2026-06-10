from vsa.parser import Parser
from vsa.scope_layout import build_scope_layout


def _first_scope(source):
    document = Parser(source).parse()
    return document.nodes[0]


def test_scope_layout_plain_scope_has_one_column():
    node = _first_scope("{tekst}")

    layout = build_scope_layout(node)

    assert len(layout.columns) == 1
    assert layout.columns[0].ehm == "~"
    assert layout.columns[0].elm == "~"


def test_scope_layout_compound_modifiers_have_columns():
    node = _first_scope(r"{/&\&/tekst_&~&~}")

    layout = build_scope_layout(node)

    assert len(layout.columns) == 3
    assert layout.columns[0].ehm == "/"
    assert layout.columns[0].elm == "_"
    assert layout.columns[1].ehm == "\\"
    assert layout.columns[1].elm == "~"
    assert layout.columns[2].ehm == "/"
    assert layout.columns[2].elm == "~"


def test_scope_layout_missing_length_expands_with_hidden_defaults():
    node = _first_scope(r"{/&\tekst}")

    layout = build_scope_layout(node)

    assert len(layout.columns) == 2
    assert layout.columns[0].elm == "~"
    assert layout.columns[1].elm == "~"
