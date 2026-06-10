from pathlib import Path

from vsa.validation_runner import validate_file


def test_validate_reports_multiple_syntax_errors(tmp_path: Path):
    file = tmp_path / "multiple.vsa"
    file.write_text("{}\n{te kst}\ntekst}\n{open", encoding="utf-8")

    result = validate_file(file)

    codes = [message.code for message in result.messages]

    assert not result.ok
    assert "VSA-SYNTAX-EMPTY-SCOPE" in codes
    assert "VSA-SYNTAX-WHITESPACE-IN-SCOPE" in codes
    assert "VSA-SYNTAX-UNEXPECTED-CLOSE-BRACE" in codes
    assert "VSA-SYNTAX-UNCLOSED-SCOPE" in codes


def test_validate_reports_multiple_semantic_errors(tmp_path: Path):
    file = tmp_path / "multiple-semantic.vsa"
    file.write_text(r"{/&\tekst_} {/&\woord_}", encoding="utf-8")

    result = validate_file(file)

    codes = [message.code for message in result.messages]

    assert not result.ok
    assert codes.count("VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH") == 2
