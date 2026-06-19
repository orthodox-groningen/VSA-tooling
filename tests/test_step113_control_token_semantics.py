from vsa.ast import ControlTokenNode


CONTROL_TOKEN_MEANINGS = {
    "[*]": "phrase_rest",
    "[/]": "phrase_boundary",
    "[*?]": "optional_phrase_rest",
    "[/?]": "optional_phrase_boundary",
}


def test_control_token_semantic_mapping_is_explicit():
    assert CONTROL_TOKEN_MEANINGS == {
        "[*]": "phrase_rest",
        "[/]": "phrase_boundary",
        "[*?]": "optional_phrase_rest",
        "[/?]": "optional_phrase_boundary",
    }


def test_control_token_nodes_store_abstract_meaning_not_renderer_behavior():
    node = ControlTokenNode(token="[/]", meaning=CONTROL_TOKEN_MEANINGS["[/]"])

    assert node.to_dict() == {
        "type": "ControlTokenNode",
        "token": "[/]",
        "meaning": "phrase_boundary",
    }


def test_optional_control_tokens_are_marked_as_optional_in_meaning():
    assert CONTROL_TOKEN_MEANINGS["[*?]"].startswith("optional_")
    assert CONTROL_TOKEN_MEANINGS["[/?]"].startswith("optional_")


def test_hard_control_tokens_are_not_marked_as_optional():
    assert not CONTROL_TOKEN_MEANINGS["[*]"].startswith("optional_")
    assert not CONTROL_TOKEN_MEANINGS["[/]"].startswith("optional_")
