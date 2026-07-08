from pathlib import Path


USER_GUIDE = Path("docs/guides")
CLI_REFERENCE = Path("docs/reference/cli.md")
CLI_SPEC = Path("docs/specification/cli.md")
CONFIG_REFERENCE = Path("docs/reference/config.md")
VALIDATION_SPEC = Path("docs/specification/validation.md")
OUTPUTS_REFERENCE = Path("docs/reference/outputs.md")


def _read(path: Path):
    return path.read_text(encoding="utf-8")


def _read_many(*paths: Path):
    return "\n".join(_read(path) for path in paths)


def test_user_guide_exists():
    assert Path("docs/guides/quick-start.md").exists()
    assert Path("docs/guides/validation.md").exists()
    assert Path("docs/guides/cli-taken.md").exists()


def test_cli_reference_exists():
    assert CLI_REFERENCE.exists()


def test_user_guide_mentions_core_commands():
    text = _read_many(
        Path("docs/guides/quick-start.md"),
        Path("docs/guides/cli-taken.md"),
    )

    assert "vsa validate" in text
    assert "vsa svg" in text
    assert "vsa build-markdown" in text
    assert "vsa process" in text
    assert "vsa blocks" in text
    assert "vsa parse <bestand.vsa> --ast" in text


def test_cli_reference_mentions_core_commands():
    text = _read(CLI_REFERENCE)

    assert "vsa validate" in text
    assert "vsa svg" in text
    assert "vsa build-markdown" in text
    assert "vsa process" in text
    assert "vsa blocks" in text
    assert "vsa parse" in text


def test_cli_reference_mentions_output_modes():
    text = _read_many(CLI_REFERENCE, CONFIG_REFERENCE)

    assert "--output-mode img" in text
    assert "--output-mode shortcode" in text


def test_user_guide_explains_validate_purpose_and_checks():
    text = _read_many(Path("docs/guides/validation.md"), VALIDATION_SPEC)

    assert "Waarvoor gebruik je dit?" in text
    assert "Wat wordt gecontroleerd?" in text
    assert "scope is goed afgesloten" in text
    assert "scope is niet leeg" in text
    assert "geen whitespace binnen scope" in text
    assert "hoogte- en lengteposities" in text


def test_user_guide_explains_validate_success_and_failure():
    text = _read_many(Path("docs/guides/validation.md"), VALIDATION_SPEC, CLI_SPEC)

    assert "Succesoutput" in text
    assert "Foutoutput" in text
    assert "OK" in text
    assert "Exitcode" in text
    assert "Aanpak bij fouten" in text


def test_user_guide_explains_parse_ast_output():
    text = _read_many(CLI_SPEC, Path("docs/specification/overview.md"))

    assert "Abstract Syntax Tree" in text
    assert "`--ast`" in text
    assert "toon de interne structuur als JSON" in text
    assert "PitchMarkerNode" in text
    assert "ScopeNode" in text
    assert "TextNode" in text


def test_user_guide_explains_blocks_json_output():
    text = _read_many(CLI_SPEC, OUTPUTS_REFERENCE)

    assert "VSA-blokken in een Markdownbestand vinden" in text
    assert "zonder `--json`" in text
    assert "--json" in text
    assert "start_line" in text
    assert "end_line" in text
    assert "metadata" in text
    assert "body" in text
    assert "ast" in text


def test_user_guide_explains_assets_dir_and_url_prefix():
    text = _read_many(CLI_SPEC, CONFIG_REFERENCE)

    assert "<assets-dir>" in text
    assert "doelmap voor gegenereerde SVG-bestanden" in text
    assert "generated/static/vsa" in text or "generated\\static\\vsa" in text
    assert "URL-prefix" in text
    assert "--assets-url-prefix" in text
    assert "/vsa" in text


def test_cli_reference_explains_assets_dir():
    text = _read_many(CLI_REFERENCE, CLI_SPEC)

    assert "<assets-dir>" in text
    assert "doelmap voor gegenereerde svg" in text.lower()
    assert "generated/static/vsa" in text or "generated\\static\\vsa" in text


def test_cli_reference_explains_validate_outputs_and_errors():
    text = _read_many(CLI_REFERENCE, CLI_SPEC, Path("docs/reference/diagnostics.md"))

    assert "Succesoutput" in text
    assert "Foutoutput" in text
    assert "Veelvoorkomende foutcodes" in text
    assert "VSA-SYNTAX-EMPTY-SCOPE" in text
    assert "VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH" in text
    assert "Wat doe je bij fouten?" in text


def test_cli_reference_explains_defaults_and_precedence():
    text = _read_many(CLI_REFERENCE, CONFIG_REFERENCE)

    assert "Defaults" in text
    assert "Voorrang" in text
    assert "max-line-width" in text
    assert "assets-url-prefix" in text
    assert "output-mode" in text


def test_docs_explain_troubleshooting_or_diagnosis():
    user_text = _read_many(
        Path("docs/guides/quick-start.md"),
        Path("docs/guides/validation.md"),
    )
    cli_text = _read(CLI_REFERENCE)

    assert "Aanpak bij fouten" in user_text
    assert "Diagnosevolgorde" in cli_text
    assert "scripts\\ci.cmd" in user_text
    assert "vsa validate" in cli_text


def test_user_guide_is_substantial():
    text = _read_many(*Path("docs/guides").glob("*.md"))

    assert len(text.splitlines()) > 200


def test_cli_reference_is_substantial():
    text = _read_many(CLI_REFERENCE, CONFIG_REFERENCE, CLI_SPEC)

    assert len(text.splitlines()) > 200
