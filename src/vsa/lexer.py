"""
Voorlopig is er nog geen aparte lexer nodig.

De parser leest de tekst direct. Dit bestand blijft bestaan omdat de architectuur
later waarschijnlijk wel een echte lexer krijgt.
"""


class Lexer:
    def __init__(self, text: str):
        self.text = text

    def tokenize(self):
        return []
