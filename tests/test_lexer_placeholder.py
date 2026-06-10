import pytest

from vsa.lexer import Lexer


def test_lexer_placeholder():
    lexer = Lexer("{tekst}")

    with pytest.raises(NotImplementedError):
        lexer.tokenize()
