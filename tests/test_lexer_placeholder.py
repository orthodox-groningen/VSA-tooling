from vsa.lexer import Lexer


def test_lexer_placeholder():
    lexer = Lexer("{tekst}")

    assert lexer.tokenize() == []
