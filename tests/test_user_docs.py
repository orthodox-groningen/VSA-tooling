from pathlib import Path


def test_user_guide_exists():
    assert Path("docs/user-guide.md").exists()


def test_cli_reference_exists():
    assert Path("docs/cli-reference.md").exists()


def test_user_guide_mentions_core_commands():
    text = Path("docs/user-guide.md").read_text(encoding="utf-8")

    assert "vsa validate" in text
    assert "vsa svg" in text
    assert "vsa build-markdown" in text


def test_cli_reference_mentions_output_modes():
    text = Path("docs/cli-reference.md").read_text(encoding="utf-8")

    assert "--output-mode img" in text
    assert "--output-mode shortcode" in text


def test_docs_explain_assets_dir():
    text = Path("docs/cli-reference.md").read_text(encoding="utf-8")

    assert "<assets-dir>" in text
    assert "doelmap voor gegenereerde SVG-bestanden" in text.lower()


def test_docs_explain_file_path_vs_url_path():
    text = Path("docs/user-guide.md").read_text(encoding="utf-8")

    assert "Bestandspad versus URL-pad" in text
    assert "generated\\static\\vsa" in text
    assert "/vsa" in text


def test_user_guide_explains_validate_checks():
    text = Path("docs/user-guide.md").read_text(encoding="utf-8")

    assert "Wat wordt gecontroleerd?" in text
    assert "VSA-SYNTAX-EMPTY-SCOPE" in text
    assert "Wat doe je na een fout?" in text


def test_cli_reference_explains_outputs_and_errors():
    text = Path("docs/cli-reference.md").read_text(encoding="utf-8")

    assert "Succesoutput" in text
    assert "Foutoutput" in text
    assert "Veelvoorkomende foutcodes" in text
    assert "Diagnosevolgorde" in text


def test_user_guide_is_substantial():
    text = Path("docs/user-guide.md").read_text(encoding="utf-8")

    assert len(text.splitlines()) > 300


def test_cli_reference_is_substantial():
    text = Path("docs/cli-reference.md").read_text(encoding="utf-8")

    assert len(text.splitlines()) > 250
