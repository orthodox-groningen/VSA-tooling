from vsa.height_markers import HeightMarkerRef
from vsa.parser import Parser
from vsa.semantic_validator import SemanticValidator


def test_semantic_validator_collects_height_markers_via_helper_layer():
    document = Parser("[:] tekst [/:] meer [//:]").parse()
    validator = SemanticValidator(document)

    markers = validator._height_markers()

    assert all(isinstance(marker, HeightMarkerRef) for marker in markers)
    assert [marker.height_modifier for marker in markers] == [[], ["/"], ["//"]]
    assert [marker.role for marker in markers] == [
        "start_height",
        "local_height",
        "local_height",
    ]


def test_semantic_validator_accepts_multiple_height_markers_after_helper_integration():
    document = Parser("[:] tekst [/:] meer [//:]").parse()
    validator = SemanticValidator(document)

    result = validator.validate()

    assert result.ok
    assert not result.has_errors()


def test_semantic_validator_accepts_document_without_height_markers_after_helper_integration():
    document = Parser("gewone tekst {tekst}").parse()
    validator = SemanticValidator(document)

    assert validator._height_markers() == []
    assert validator.validate().ok
