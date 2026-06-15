from pathlib import Path


def test_todo_mentions_bracket_tokens_are_not_supported_yet():
    text = Path("docs/todo.md").read_text(encoding="utf-8")

    assert "[/?]" in text
    assert "nog niet ondersteund" in text
    assert "bracket-token dispatch" in text.lower()
