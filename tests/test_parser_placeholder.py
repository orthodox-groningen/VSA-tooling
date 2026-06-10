import pytest

from vsa.parser import Parser


def test_parser_placeholder():
    parser = Parser("{tekst}")

    with pytest.raises(NotImplementedError):
        parser.parse()
