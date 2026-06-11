from pathlib import Path

from vsa.validation_runner import validate_file


def test_valid_prefix_modifiers_are_not_syntax_errors(tmp_path: Path):
    path = tmp_path / "edge-cases.md"
    path.write_text(
        r"""::: vsa-notatie
{/&\tekst_}
:::
""",
        encoding="utf-8",
    )

    result = validate_file(path)
    assert not result.ok
    assert result.messages[0].code == "VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH"


def test_empty_sung_text_scope_reports_specific_error(tmp_path: Path):
    path = tmp_path / "edge-cases.md"
    path.write_text(
        r"""::: vsa-notatie
[:] tekst
{\\}de wachters
:::
""",
        encoding="utf-8",
    )

    result = validate_file(path)
    message = result.messages[0]
    assert message.code == "VSA-SYNTAX-EMPTY-SUNG-TEXT"
    assert message.line == 3
    assert message.column == 1


def test_invalid_alignment_marker_reports_specific_error(tmp_path: Path):
    path = tmp_path / "edge-cases.md"
    path.write_text(
        r"""::: vsa-notatie
[:] tekst
{&\ken__}.
:::
""",
        encoding="utf-8",
    )

    result = validate_file(path)
    message = result.messages[0]
    assert message.code == "VSA-SYNTAX-INVALID-ALIGNMENT-MARKER"
    assert "`&`" in message.message_nl
    assert message.line == 3
    assert message.column == 2


def test_modifier_in_sung_text_has_specific_error(tmp_path: Path):
    path = tmp_path / "edge-cases.md"
    path.write_text(
        r"""::: vsa-notatie
[:] tekst
{fout/}
:::
""",
        encoding="utf-8",
    )

    result = validate_file(path)
    message = result.messages[0]
    assert message.code == "VSA-SYNTAX-MODIFIER-IN-SUNG-TEXT"
    assert message.line == 3
    assert message.column > 1
