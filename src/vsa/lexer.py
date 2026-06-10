from .tokens import Token


SPECIAL_CHARS = "{}[]"


class Lexer:
    def __init__(self, text: str):
        self.text = text

    def tokenize(self):
        tokens = []

        line = 1
        column = 1
        position = 0

        for ch in self.text:
            if ch in SPECIAL_CHARS:
                tokens.append(
                    Token(
                        type="SYMBOL",
                        value=ch,
                        position=position,
                        line=line,
                        column=column,
                    )
                )

            elif ch.isspace():
                tokens.append(
                    Token(
                        type="WHITESPACE",
                        value=ch,
                        position=position,
                        line=line,
                        column=column,
                    )
                )

            else:
                tokens.append(
                    Token(
                        type="TEXT",
                        value=ch,
                        position=position,
                        line=line,
                        column=column,
                    )
                )

            if ch == "\n":
                line += 1
                column = 1
            else:
                column += 1

            position += 1

        return tokens
