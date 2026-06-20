import pytest

from vsa.ast import ControlTokenNode
from vsa.bracket_token_stream import BracketToken, bracket_token_stream
from vsa.errors import VSASyntaxError
from vsa.parser import Parser


CONTROL_TOKEN_REGISTRY = {
    "[*]": {
        "meaning": "phrase_rest",
        "strength": "hard",
    },
    "[/]": {
        "meaning": "phrase_boundary",
        "strength": "hard",
    },
    "[*?]": {
        "meaning": "optional_phrase_rest",
        "strength": "soft",
    },
    "[/?]": {
        "meaning": "optional_phrase_boundary",
        "strength": "soft",
    },
}


def test_control_token_registry_is_explicit_and_renderer_independent():
    assert CONTROL_TOKEN_REGISTRY == {
        "[*]": {
            "meaning": "phrase_rest",
            "strength": "hard",
        },
        "[/]": {
            "meaning": "phrase_boundary",
            "strength": "hard",
        },
        "[*?]": {
            "meaning": "optional_phrase_rest",
            "strength": "soft",
        },
        "[/?]": {
            "meaning": "optional_phrase_boundary",
            "strength": "soft",
        },
    }


def test_registry_can_create_control_token_nodes_without_parser_activation():
    for token, metadata in CONTROL_TOKEN_REGISTRY.items():
        node = ControlTokenNode(
            token=token,
            meaning=metadata["meaning"],
        )

        assert node.to_dict() == {
            "type": "ControlTokenNode",
            "token": token,
            "meaning": metadata["meaning"],
        }


def test_registry_does_not_activate_control_tokens_in_bracket_token_stream():
    assert bracket_token_stream("[/] tekst") == [
        BracketToken(kind="text", start=0, end=9, value="[/] tekst")
    ]


def test_registry_does_not_activate_control_tokens_in_parser():
    for token in CONTROL_TOKEN_REGISTRY:
        with pytest.raises(VSASyntaxError):
            Parser(token).parse()


def test_height_marker_syntax_remains_separate_from_control_token_registry():
    assert "[:]" not in CONTROL_TOKEN_REGISTRY
    assert "[/:]" not in CONTROL_TOKEN_REGISTRY
    assert Parser("[:] [/:]").parse().nodes[0].height_modifier == []
    assert Parser("[:] [/:]").parse().nodes[2].height_modifier == ["/"]
