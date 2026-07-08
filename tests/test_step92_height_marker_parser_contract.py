from pathlib import Path

CONTRACT = Path("docs/history/parser-steps/parser-stap-92-height-marker-parser-contract.md")


def test_step92_contract_exists():
    assert CONTRACT.exists()


def test_step92_contract_defines_bracket_directive_end_token():
    text = CONTRACT.read_text(encoding="utf-8")
    assert "bracket-directive" in text
    assert "samengestelde eindtoken" in text
    assert ":]" in text
    assert "niet als twee losse tekens" in text


def test_step92_contract_repeats_strict_marker_shape():
    text = CONTRACT.read_text(encoding="utf-8")
    assert "[<EHM>:]" in text
    assert "geldige EHM" in text


def test_step92_contract_lists_valid_multiple_marker_examples():
    text = CONTRACT.read_text(encoding="utf-8")
    assert "[//:] {\\Heer}, [\\:] ontferm {/U}." in text
    assert "Heer, [:] {\\ont}ferm [\\:] {/U}." in text


def test_step92_contract_rejects_ampersand_in_pitch_marker():
    text = CONTRACT.read_text(encoding="utf-8")
    assert "[/&\\:] fout" in text
    assert "`&` is geen EHM-teken" in text


def test_step92_contract_rejects_length_modifier_in_pitch_marker():
    text = CONTRACT.read_text(encoding="utf-8")
    assert "[_:] fout" in text
    assert "`_` is geen EHM" in text


def test_step92_contract_rejects_non_ehm_modifier():
    text = CONTRACT.read_text(encoding="utf-8")
    assert "[//\\:] fout" in text
    assert "`//\\` is geen EHM" in text


def test_step92_contract_says_missing_end_token_is_not_marker():
    text = CONTRACT.read_text(encoding="utf-8")
    assert "[/] fout of waarschuwing" in text
    assert "eindigt niet op `:]`" in text


def test_step92_contract_says_ast_allows_more_than_one_pitch_marker():
    text = CONTRACT.read_text(encoding="utf-8")
    assert "niet uitgaan van maximaal één pitch marker" in text
    assert "geordende tokenstroom" in text
    assert "eerste pitch marker krijgt geen ander tokentype" in text
