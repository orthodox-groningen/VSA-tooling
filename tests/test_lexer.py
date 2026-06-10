from vsa.lexer import Lexer


def test_lexer_returns_tokens():
    lexer = Lexer("{tekst}")

    tokens = lexer.tokenize()

    assert len(tokens) > 0

    assert tokens[0].value == "{"
    assert tokens[-1].value == "}"


def test_lexer_tracks_line_and_column():
    lexer = Lexer("{a}\n{b}")

    tokens = lexer.tokenize()

    second_scope_open = tokens[4]

    assert second_scope_open.line == 2
    assert second_scope_open.column == 1
