class VSAError(Exception):
    pass


class VSASyntaxError(VSAError):
    pass


class VSASemanticError(VSAError):
    pass
