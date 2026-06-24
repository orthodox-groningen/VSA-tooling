from pathlib import Path

from vsa.parser import Parser
from vsa.semantic_validator import SemanticValidator
from vsa.validation_runner import validate_file


def validate_source(source: str):
    document = Parser(source).parse()
    return SemanticValidator(document).validate()


def test_semantic_validator_accepts_multiple_height_markers():
    # No scopes between markers → no pitch delta; all markers at pitch 0 → consistent
    result = validate_source("[:] tekst [:] meer tekst [:] einde")

    assert result.ok
    assert not result.has_errors()


def test_semantic_validator_accepts_text_before_first_height_marker():
    result = validate_source("tekst vóór [:] tekst na")

    assert result.ok
    assert not result.has_errors()


def test_semantic_validator_accepts_text_between_and_after_height_markers():
    # Text nodes carry no pitch delta; both markers at pitch 0 → consistent
    result = validate_source("begin [:] midden [:] einde")

    assert result.ok
    assert not result.has_errors()


def test_semantic_validator_accepts_document_without_height_markers():
    result = validate_source("gewone tekst {tekst}")

    assert result.ok
    assert not result.has_errors()


def test_validate_file_accepts_multiple_height_markers(tmp_path: Path):
    # No scopes → no pitch change; all markers at pitch 0 → consistent
    path = tmp_path / "multiple-height-markers.vsa"
    path.write_text("[:] tekst [:] meer tekst [:] einde", encoding="utf-8")

    result = validate_file(path)

    assert result.ok
