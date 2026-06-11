from vsa.parser import Parser
from vsa.semantic_validator import (
    SemanticValidationOptions,
    SemanticValidator,
)


def test_semantic_validator_defaults_to_error():
    document = Parser(r"[:] {tekst} [:]").parse()

    result = SemanticValidator(document).validate()

    assert result.items[0].severity == "error"
    assert result.has_fatal_errors()


def test_semantic_validator_can_override_severity_to_warning():
    document = Parser(r"[:] {tekst} [:]").parse()

    result = SemanticValidator(
        document,
        SemanticValidationOptions(
            severity_overrides={
                "VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER": "warning",
            }
        ),
    ).validate()

    assert result.items[0].severity == "warning"
    assert result.has_errors()
    assert result.has_warnings()
    assert not result.has_fatal_errors()
    assert result.ok


def test_semantic_validator_can_override_modifier_mismatch_to_warning():
    document = Parser(r"{/&\tekst_}").parse()

    result = SemanticValidator(
        document,
        SemanticValidationOptions(
            severity_overrides={
                "VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH": "warning",
            }
        ),
    ).validate()

    assert result.items[0].severity == "warning"
    assert result.ok
