from pathlib import Path

from vsa.cli import main


def test_cli_version_smoke(capsys):
    exit_code = main(["--version"])
    output = capsys.readouterr().out

    assert exit_code == 0
    assert output.startswith("vsa ")


def test_cli_blocks_json_smoke(capsys, tmp_path: Path):
    path = tmp_path / "demo.md"

    path.write_text(
        """::: vsa-notatie
{tekst}
:::
""",
        encoding="utf-8",
    )

    exit_code = main(["blocks", str(path), "--json"])
    output = capsys.readouterr().out

    assert exit_code == 0
    assert '"body": "{tekst}"' in output


def test_cli_parse_ast_smoke(capsys, tmp_path: Path):
    path = tmp_path / "demo.vsa"
    path.write_text("{tekst}", encoding="utf-8")

    exit_code = main(["parse", str(path), "--ast"])
    output = capsys.readouterr().out

    assert exit_code == 0
    assert '"type": "Document"' in output
