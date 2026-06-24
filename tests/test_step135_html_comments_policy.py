from xml.etree import ElementTree

from vsa.parser import Parser
from vsa.recoverable_syntax_validator import RecoverableSyntaxValidator
from vsa.semantic_validator import SemanticValidator
from vsa.svg_renderer import SVGRenderer
from vsa.vsa_comments import strip_vsa_html_comments


def test_strip_vsa_html_comments_removes_comments_completely():
    assert strip_vsa_html_comments("a<!-- comment -->b") == "ab"


def test_parser_ignores_html_comments_without_changing_source_variable():
    source = "voor <!-- commentaar --> na"

    document = Parser(source).parse()

    assert source == "voor <!-- commentaar --> na"
    assert [node.text for node in document.nodes if type(node).__name__ == "TextNode"] == ["voor  na"]


def test_validation_ignores_braces_inside_html_comments():
    diagnostics = RecoverableSyntaxValidator("tekst <!-- { kapot --> verder").validate()

    assert not diagnostics.has_errors()


def test_semantic_validation_ignores_modifier_mismatch_inside_html_comments():
    document = Parser("goed <!-- {/fout__} --> {/ok_}").parse()

    result = SemanticValidator(document).validate()

    assert result.ok


def test_svg_artifact_contains_no_html_comment_or_comment_text():
    document = Parser("tekst <!-- geheim commentaar --> einde").parse()

    svg = SVGRenderer().render_document(document)

    assert "<!--" not in svg
    assert "geheim commentaar" not in svg
    assert "tekst" in svg
    assert "einde" in svg
    ElementTree.fromstring(svg)
