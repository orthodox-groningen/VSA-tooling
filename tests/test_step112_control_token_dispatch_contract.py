from vsa.ast import ControlTokenNode

CONTROL_TOKEN_MAP = {
    "[*]": "phrase_rest",
    "[/]": "phrase_boundary",
    "[*?]": "optional_phrase_rest",
    "[/?]": "optional_phrase_boundary",
}

def test_control_token_mapping_contract():
    assert CONTROL_TOKEN_MAP["[*]"] == "phrase_rest"
    assert CONTROL_TOKEN_MAP["[/]"] == "phrase_boundary"

def test_control_token_node_can_hold_all_reserved_tokens():
    for token, meaning in CONTROL_TOKEN_MAP.items():
        node = ControlTokenNode(token=token, meaning=meaning)
        assert node.token == token
        assert node.meaning == meaning
