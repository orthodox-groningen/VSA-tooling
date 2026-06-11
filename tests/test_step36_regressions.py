from vsa.block_parser import parse_markdown_blocks
from vsa.parser import Parser
from vsa.semantic_validator import SemanticValidator


def test_block_parser_keeps_vsa_body():
    markdown = """
::: vsa-notatie
[:] {tekst} [:]
:::
"""

    blocks = parse_markdown_blocks(markdown)

    assert blocks[0].body == "[:] {tekst} [:]"


def test_semantic_validation_result_has_errors_method():
    document = Parser(r"{/&\tekst_}").parse()

    result = SemanticValidator(document).validate()

    assert result.has_errors()


def test_short_pitch_marker_examples_are_still_allowed():
    document = Parser(r"[:] {tekst}").parse()

    result = SemanticValidator(document).validate()

    assert result.ok
