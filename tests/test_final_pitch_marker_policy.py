from vsa.parser import Parser
from vsa.semantic_validator import SemanticValidator


def _codes(source):
    document = Parser(source).parse()
    result = SemanticValidator(document).validate()
    return [item.code for item in result.items]


def test_missing_final_pitch_marker_is_allowed():
    assert _codes(r"[:] {tekst}") == []


def test_empty_final_pitch_marker_is_allowed():
    assert _codes(r"[:] {tekst} [:]") == []


def test_dash_final_pitch_marker_is_allowed():
    assert _codes(r"[:] {tekst} [-:]") == []


def test_directional_final_pitch_marker_is_allowed_when_consistent():
    # [\:] start = -1, {\tekst} delta = -1, computed = -2; [\\:] = -2 → consistent
    assert _codes(r"[\:] {\tekst} [\\:]") == []
