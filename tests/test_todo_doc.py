from pathlib import Path


def test_todo_document_exists():
    assert Path("docs/history/addenda/todo.md").exists()


def test_todo_mentions_bracket_token_dispatch():
    text = Path("docs/history/addenda/todo.md").read_text(encoding="utf-8")

    assert "Bracket-token dispatch" in text
    assert "[/?]" in text
    assert "MusicXML" in text


def test_todo_mentions_newline_policy():
    text = Path("docs/history/addenda/todo.md").read_text(encoding="utf-8")

    assert "CR" in text
    assert "LF" in text
    assert "bronregelgrenzen" in text
