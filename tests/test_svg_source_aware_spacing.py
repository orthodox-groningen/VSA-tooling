from vsa.parser import Parser
from vsa.svg_line_layout import WhitespaceNode, iter_layout_nodes
from vsa.svg_renderer import SVGRenderer


def test_text_node_splits_whitespace_as_layout_unit():
    document = Parser("de Heer").parse()

    nodes = list(iter_layout_nodes(document))

    assert any(isinstance(node, WhitespaceNode) for node in nodes)


def test_svg_spacing_preserves_space_between_scopes_and_text():
    document = Parser(r"{/de} {/Heer} heeft").parse()

    svg = SVGRenderer().render_document(document)

    # We testen hier indirect: de tekstitems moeten afzonderlijk blijven,
    # en whitespace moet als x-advance meetellen.
    assert "Heer" in svg
    assert "heeft" in svg
    assert 'xml:space="preserve"' in svg


def test_space_prevents_scope_scope_sticking():
    document = Parser(r"ge{na_}{\de} {\ge}").parse()

    nodes = list(iter_layout_nodes(document))

    assert any(isinstance(node, WhitespaceNode) for node in nodes)
