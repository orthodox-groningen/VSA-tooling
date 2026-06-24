from vsa.parser import Parser
from vsa.semantic_validator import SemanticValidator


def _codes(source):
    document = Parser(source).parse()
    result = SemanticValidator(document).validate()
    return [diagnostic.code for diagnostic in result.items]


def test_valid_phrase_with_consistent_final_pitch_marker():
    # start=0, {/Hei}+1, {/lig}+1 → computed=2; [//:]= 2 → consistent
    assert _codes(r"[:] {/Hei_}{/lig_} is de Heer. [//:]") == []


def test_phrase_with_initial_pitch_marker_may_omit_final_pitch_marker():
    assert _codes(r"[:] {/Hei_}{/lig_} is de Heer.") == []


def test_neutral_final_pitch_marker_is_valid_when_pitch_returns_to_zero():
    # {/Hei} rises +1, {\lig} falls -1 → net = 0; [:] = 0 → consistent
    assert _codes(r"[:] {/Hei_}{\lig_} is de Heer. [:]") == []


def test_plain_text_without_initial_pitch_marker_is_not_checked():
    assert _codes(r"{/Hei_}{/lig_} is de Heer.") == []


def test_initial_and_final_empty_pitch_markers_without_sung_material_are_allowed():
    assert _codes(r"[:] tekst [:]") == []
