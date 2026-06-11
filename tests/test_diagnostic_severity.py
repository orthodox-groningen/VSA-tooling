from vsa.diagnostics import DiagnosticCollection
from vsa.parser import Parser
from vsa.semantic_validator import SemanticValidator


def test_diagnostic_defaults_to_error():
    diagnostics = DiagnosticCollection()

    diagnostics.add(
        code="TEST",
        message_nl="Test",
        line=1,
        column=1,
    )

    assert diagnostics.items[0].severity == "error"


def test_diagnostic_collection_detects_warning():
    diagnostics = DiagnosticCollection()

    diagnostics.add(
        code="TEST",
        message_nl="Test",
        line=1,
        column=1,
        severity="warning",
    )

    assert diagnostics.has_warnings()
    assert diagnostics.has_errors()
    assert not diagnostics.has_fatal_errors()


def test_semantic_modifier_mismatch_is_error_for_now():
    document = Parser(r"{/&\tekst_}").parse()

    result = SemanticValidator(document).validate()

    assert result.items[0].severity == "error"


def test_final_pitch_marker_policy_produces_no_diagnostic():
    document = Parser(r"[:] {tekst} [:]").parse()

    result = SemanticValidator(document).validate()

    assert result.items == []


def test_semantic_errors_are_fatal_for_now():
    document = Parser(r"{/&\tekst_}").parse()

    result = SemanticValidator(document).validate()

    assert result.has_errors()
    assert result.has_fatal_errors()
    assert not result.ok
