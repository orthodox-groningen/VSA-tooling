from pathlib import Path

from vsa.validation_runner import validate_file


def test_validate_valid_vsa_file(tmp_path: Path):
    file = tmp_path / "valid.vsa"
    file.write_text("{tekst}", encoding="utf-8")

    result = validate_file(file)

    assert result.ok


def test_validate_invalid_vsa_file(tmp_path: Path):
    file = tmp_path / "invalid.vsa"
    file.write_text(r"{/&\tekst_}", encoding="utf-8")

    result = validate_file(file)

    assert not result.ok
    assert result.messages[0].code == "VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH"


def test_validate_markdown_block(tmp_path: Path):
    file = tmp_path / "valid.md"
    file.write_text(
        """# Titel

::: vsa-notatie
{tekst}
:::
""",
        encoding="utf-8",
    )

    result = validate_file(file)

    assert result.ok


def test_validate_invalid_markdown_block(tmp_path: Path):
    file = tmp_path / "invalid.md"
    file.write_text(
        r"""# Titel

::: vsa-notatie
{/&\tekst_}
:::
""",
        encoding="utf-8",
    )

    result = validate_file(file)

    assert not result.ok
    assert "blok-1" in result.messages[0].source
