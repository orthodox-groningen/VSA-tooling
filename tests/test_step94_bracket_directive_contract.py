from pathlib import Path


CONTRACT = Path("docs/history/parser-steps/parser-stap-94-bracket-directive-contract.md")


def test_step94_contract_exists():
    assert CONTRACT.exists()


def test_step94_contract_defines_end_token():
    text = CONTRACT.read_text(encoding="utf-8")

    assert "[<EHM>:]" in text
    assert ":]" in text
    assert "één eindtoken" in text


def test_step94_contract_rejects_tokenizing_colon_and_bracket_separately():
    text = CONTRACT.read_text(encoding="utf-8")

    assert '"[" + <EHM> + ":]"' in text
    assert '"[" + <EHM> + ":" + "]"' in text
    assert "Niet:" in text


def test_step94_contract_does_not_switch_to_curly_marker_syntax():
    text = CONTRACT.read_text(encoding="utf-8")

    assert "Geen overstap naar `{<EHM>:}`" in text
    assert "`{...}` is al in gebruik" in text
