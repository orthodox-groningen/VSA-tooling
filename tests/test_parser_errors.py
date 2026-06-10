import pytest

from vsa.errors import VSASyntaxError
from vsa.parser import Parser


@pytest.mark.parametrize(
    "source",
    [
        "{}",
        "{tekst",
        "{te kst}",
        "{te/tekst}",
        "{tekst&&_}",
    ],
)
def test_parser_syntax_errors(source):
    with pytest.raises(VSASyntaxError):
        Parser(source).parse()
