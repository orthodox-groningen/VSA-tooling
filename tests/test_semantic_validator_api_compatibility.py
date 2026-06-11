from vsa.parser import Parser
from vsa.semantic_validator import SemanticValidator


def test_semantic_validator_keeps_constructor_document_api():
    document = Parser("{tekst}").parse()

    result = SemanticValidator(document).validate()

    assert hasattr(result, "items")
    assert hasattr(result, "diagnostics")


def test_semantic_validator_result_items_are_diagnostics():
    document = Parser(r"{/&\tekst_}").parse()

    result = SemanticValidator(document).validate()

    assert len(result.items) == 1
    assert result.items[0].code == "VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH"
