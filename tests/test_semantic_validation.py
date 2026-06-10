from vsa.parser import Parser
from vsa.semantic_validator import SemanticValidator


def test_modifier_count_mismatch():
    doc = Parser(r"{/&\tekst_}").parse()

    diagnostics = SemanticValidator(doc).validate()

    assert diagnostics.has_errors()

    assert diagnostics.items[0].code == "VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH"


def test_valid_matching_modifiers():
    doc = Parser(r"{/&\tekst_&_}").parse()

    diagnostics = SemanticValidator(doc).validate()

    assert not diagnostics.has_errors()
