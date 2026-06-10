from pathlib import Path
import pytest

from vsa.markdown_processor import process_path, ProcessValidationError


def test_process_valid_file_generates_svg(tmp_path: Path):
    content = tmp_path / "content"
    output = tmp_path / "out"

    content.mkdir()

    (content / "valid.md").write_text(
        """::: vsa-notatie
{tekst}
:::
""",
        encoding="utf-8",
    )

    result = process_path(content, output)

    assert len(result.blocks) == 1
    assert len(list(output.glob("*.svg"))) == 1


def test_process_invalid_file_raises_and_generates_nothing(tmp_path: Path):
    content = tmp_path / "content"
    output = tmp_path / "out"

    content.mkdir()

    (content / "invalid.md").write_text(
        r"""::: vsa-notatie
{/&\tekst_}
:::
""",
        encoding="utf-8",
    )

    with pytest.raises(ProcessValidationError) as exc:
        process_path(content, output)

    assert len(exc.value.messages) == 1
    assert exc.value.messages[0].code == "VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH"
    assert not output.exists()


def test_process_directory_reports_all_validation_errors(tmp_path: Path):
    content = tmp_path / "content"
    output = tmp_path / "out"

    content.mkdir()

    (content / "invalid-1.md").write_text(
        r"""::: vsa-notatie
{/&\tekst_}
:::
""",
        encoding="utf-8",
    )

    (content / "invalid-2.md").write_text(
        r"""::: vsa-notatie
{/&\woord_}
:::
""",
        encoding="utf-8",
    )

    with pytest.raises(ProcessValidationError) as exc:
        process_path(content, output)

    codes = [message.code for message in exc.value.messages]

    assert codes.count("VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH") == 2
    assert not output.exists()
