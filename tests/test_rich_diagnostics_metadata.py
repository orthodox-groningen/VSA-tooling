from vsa.diagnostics import DiagnosticCollection
from vsa.parser import Parser
from vsa.semantic_validator import SemanticValidator


def test_diagnostic_defaults_keep_backwards_compatibility():
    diagnostics = DiagnosticCollection()

    diagnostics.add(
        code="TEST",
        message_nl="Test",
        line=1,
        column=1,
    )

    diagnostic = diagnostics.items[0]

    assert diagnostic.severity == "error"
    assert diagnostic.category == "general"
    assert diagnostic.hint_nl == ""
    assert diagnostic.doc_url == ""


def test_diagnostic_accepts_rich_metadata():
    diagnostics = DiagnosticCollection()

    diagnostics.add(
        code="TEST",
        message_nl="Test",
        line=1,
        column=1,
        severity="warning",
        category="semantic",
        hint_nl="Doe iets anders.",
        doc_url="docs/test.md",
    )

    diagnostic = diagnostics.items[0]

    assert diagnostic.severity == "warning"
    assert diagnostic.category == "semantic"
    assert diagnostic.hint_nl == "Doe iets anders."
    assert diagnostic.doc_url == "docs/test.md"


def test_semantic_modifier_mismatch_contains_category_hint_and_doc_url():
    document = Parser(r"{/&\tekst_}").parse()

    result = SemanticValidator(document).validate()

    diagnostic = result.items[0]

    assert diagnostic.category == "semantic"
    assert diagnostic.hint_nl
    assert diagnostic.doc_url
