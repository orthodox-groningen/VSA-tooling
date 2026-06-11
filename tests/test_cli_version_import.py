from vsa.cli import main


def test_cli_version_does_not_require_vsa_version_module(capsys):
    exit_code = main(["--version"])
    output = capsys.readouterr().out

    assert exit_code == 0
    assert output.startswith("vsa ")
