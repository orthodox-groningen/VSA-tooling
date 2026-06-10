class VSAError(Exception):
    pass


class VSASyntaxError(VSAError):
    def __init__(self, message: str, position: int | None = None):
        self.message = message
        self.position = position

        if position is None:
            super().__init__(message)
        else:
            super().__init__(f"{message} at position {position}")


class VSASemanticError(VSAError):
    pass
