from pathlib import Path


USER_GUIDE = Path("docs/user-guide.md")
CLI_REFERENCE = Path("docs/cli-reference.md")


def _read(path: Path):
    return path.read_text(encoding="utf-8")


def test_user_guide_exists():
    assert USER_GUIDE.exists()


def test_cli_reference_exists():
    assert CLI_REFERENCE.exists()


def test_user_guide_mentions_core_commands():
    text = _read(USER_GUIDE)

    assert "vsa validate" in text
    assert "vsa svg" in text
    assert "vsa build-markdown" in text
    assert "vsa process" in text
    assert "vsa blocks" in text
    assert "vsa parse --ast" in text


def test_cli_reference_mentions_core_commands():
    text = _read(CLI_REFERENCE)

    assert "vsa validate" in text
    assert "vsa svg" in text
    assert "vsa build-markdown" in text
    assert "vsa process" in text
    assert "vsa blocks" in text
    assert "vsa parse" in text


def test_cli_reference_mentions_output_modes():
    text = _read(CLI_REFERENCE)

    assert "--output-mode img" in text
    assert "--output-mode shortcode" in text


def test_user_guide_explains_validate_purpose_and_checks():
    text = _read(USER_GUIDE)

    assert "Waarvoor gebruik je dit?" in text
    assert "Wat wordt gecontroleerd?" in text
    assert "scope is goed afgesloten" in text
    assert "scope is niet leeg" in text
    assert "geen whitespace binnen scope" in text
    assert "hoogte- en lengte-modifiers" in text


def test_user_guide_explains_validate_success_and_failure():
    text = _read(USER_GUIDE)

    assert "Wat is de output bij succes?" in text
    assert "Wat is de output bij fouten?" in text
    assert "OK" in text
    assert "Exitcode" in text
    assert "Wat doe je na een fout?" in text


def test_user_guide_explains_parse_ast_output():
    text = _read(USER_GUIDE)

    assert "Wat is AST?" in text
    assert "Met `--ast` krijg je JSON" in text
    assert "Zonder `--ast` krijg je alleen" in text
    assert "PitchMarkerNode" in text
    assert "ScopeNode" in text
    assert "TextNode" in text


def test_user_guide_explains_blocks_json_output():
    text = _read(USER_GUIDE)

    assert "VSA-blokken inspecteren" in text
    assert "Output zonder `--json`" in text
    assert "Met JSON" in text
    assert "start_line" in text
    assert "end_line" in text
    assert "metadata" in text
    assert "body" in text
    assert "ast" in text


def test_user_guide_explains_assets_dir_and_url_prefix():
    text = _read(USER_GUIDE)

    assert "Wat is `<assets-dir>`?" in text
    assert "fysieke map waar SVG-bestanden worden geschreven" in text
    assert "generated\\static\\vsa" in text
    assert "Bestandspad versus URL-pad" in text
    assert "--assets-url-prefix" in text
    assert "/vsa" in text


def test_cli_reference_explains_assets_dir():
    text = _read(CLI_REFERENCE)

    assert "<assets-dir>" in text
    assert "doelmap voor gegenereerde SVG-bestanden" in text
    assert "generated\\static\\vsa" in text


def test_cli_reference_explains_validate_outputs_and_errors():
    text = _read(CLI_REFERENCE)

    assert "Succesoutput" in text
    assert "Foutoutput" in text
    assert "Veelvoorkomende foutcodes" in text
    assert "VSA-SYNTAX-EMPTY-SCOPE" in text
    assert "VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH" in text
    assert "Wat doe je bij fouten?" in text


def test_cli_reference_explains_defaults_and_precedence():
    text = _read(CLI_REFERENCE)

    assert "Defaults" in text
    assert "Voorrang" in text
    assert "max-line-width" in text
    assert "assets-url-prefix" in text
    assert "output-mode" in text


def test_docs_explain_troubleshooting_or_diagnosis():
    user_text = _read(USER_GUIDE)
    cli_text = _read(CLI_REFERENCE)

    assert "Als iets fout gaat" in user_text
    assert "Diagnosevolgorde" in cli_text
    assert "scripts\\test.cmd" in user_text
    assert "vsa validate" in cli_text


def test_user_guide_is_substantial():
    text = _read(USER_GUIDE)

    assert len(text.splitlines()) > 200


def test_cli_reference_is_substantial():
    text = _read(CLI_REFERENCE)

    assert len(text.splitlines()) > 200
