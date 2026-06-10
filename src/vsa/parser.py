"""
Eerste parser-skelet voor VSA.

Nog niet geïmplementeerd.
"""

from .ast import Document


class Parser:
    def __init__(self, text: str):
        self.text = text

    def parse(self) -> Document:
        raise NotImplementedError("Parser nog niet geïmplementeerd.")
