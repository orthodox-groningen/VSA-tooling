from docs_contracts import doc, read_doc, assert_terms


def test_todo_document_exists():
    assert doc("todo_addendum").exists()


def test_todo_mentions_bracket_token_dispatch():
    text = read_doc("todo_addendum")

    assert_terms(text, ("Bracket-token dispatch", "[/?]", "MusicXML"))


def test_todo_mentions_newline_policy():
    text = read_doc("todo_addendum")

    assert_terms(text, ("CR", "LF", "bronregelgrenzen"))
