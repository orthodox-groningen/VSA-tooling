"""Nederlandse lettergreep-splitsing voor reciteer-tekst."""

from vsa.dutch_syllables import recite_syllables, split_dutch_word


def test_elia_recite_words() -> None:
    assert split_dutch_word("Voorloper") == ["Voor", "lo", "per"]
    assert split_dutch_word("grondslag") == ["grond", "slag"]
    assert split_dutch_word("genezing") == ["ge", "ne", "zing"]
    assert split_dutch_word("opwellen") == ["op", "wel", "len"]
    assert split_dutch_word("tweede") == ["twee", "de"]
    assert split_dutch_word("gezonden") == ["ge", "zon", "den"]
    assert split_dutch_word("hoge") == ["ho", "ge"]
    assert split_dutch_word("rijke") == ["rij", "ke"]
    assert split_dutch_word("allen") == ["al", "len"]
    assert split_dutch_word("Gij") == ["Gij"]
    assert split_dutch_word("waart") == ["waart"]


def test_existing_hyphens_win() -> None:
    assert recite_syllables("voor-beeld") == [("voor", "begin"), ("beeld", "end")]
    assert recite_syllables("Gij") == [("Gij", "single")]
    assert recite_syllables("komst,")[0][0].endswith(",") or recite_syllables("komst,") == [
        ("komst,", "single")
    ]
