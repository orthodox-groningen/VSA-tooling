from vsa.parser import Parser
from vsa.semantic_validator import SemanticValidator


def _codes(source):
    document = Parser(source).parse()
    result = SemanticValidator(document).validate()
    return [diagnostic.code for diagnostic in result.items]


def test_valid_phrase_with_final_pitch_marker():
    assert _codes(r"[:] {/Hei_}{/lig_} is de Heer. [\\:]") == []


def test_phrase_with_initial_pitch_marker_must_end_with_pitch_marker():
    assert (
        "VSA-SEMANTIC-MISSING-FINAL-PITCH-MARKER"
        in _codes(r"[:] {/Hei_}{/lig_} is de Heer.")
    )


def test_empty_final_pitch_marker_after_sung_material_is_invalid():
    assert (
        "VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER"
        in _codes(r"[:] {/Hei_}{/lig_} is de Heer. [:]")
    )


def test_plain_text_without_initial_pitch_marker_is_not_checked():
    assert _codes(r"{/Hei_}{/lig_} is de Heer.") == []


def test_initial_and_final_empty_pitch_markers_without_sung_material_are_allowed():
    assert _codes(r"[:] tekst [:]") == []
