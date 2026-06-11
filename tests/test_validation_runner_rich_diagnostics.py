from pathlib import Path

from vsa.validation_runner import validate_file, validate_path


def test_validation_message_carries_semantic_metadata(tmp_path: Path):
    path = tmp_path / "invalid.vsa"

    path.write_text(r"{/&\tekst_}", encoding="utf-8")

    result = validate_file(path)

    message = result.messages[0]

    assert message.category == "semantic"
    assert message.hint_nl
    assert message.doc_url


def test_path_not_found_has_path_category(tmp_path: Path):
    result = validate_path(tmp_path / "missing.vsa")

    message = result.messages[0]

    assert message.category == "path"
    assert message.hint_nl


def test_validation_message_defaults_are_backwards_compatible():
    from vsa.validation_runner import ValidationMessage

    message = ValidationMessage(
        source="x",
        code="TEST",
        message_nl="Test",
    )

    assert message.severity == "error"
    assert message.category == "general"
    assert message.hint_nl == ""
    assert message.doc_url == ""
