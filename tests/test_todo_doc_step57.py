from docs_contracts import read_doc, assert_terms


def test_todo_mentions_bracket_tokens_are_not_supported_yet():
    text = read_doc("todo_addendum")

    assert_terms(text, ("[/?]", "nog niet ondersteund"))
    assert "bracket-token dispatch" in text.lower()
