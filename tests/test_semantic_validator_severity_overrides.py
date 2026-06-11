from vsa.parser import Parser
from vsa.semantic_validator import (
    SemanticValidationOptions,
    SemanticValidator,
)


def test_semantic_validator_defaults_modifier_mismatch_to_error():
    document = Parser(r"{/&\tekst_}").parse()

    result = SemanticValidator(document).validate()

    assert result.items[0].severity == "error"


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


def test_valid_final_pitch_marker_has_no_diagnostic():
    document = Parser(r"[:] {tekst} [:]").parse()

    result = SemanticValidator(document).validate()

    assert result.items == []
