from vsa.parser import Parser


def test_parser_placeholder():
    parser = Parser("{tekst}")
    document = parser.parse()

    assert document.to_dict()["type"] == "Document"
