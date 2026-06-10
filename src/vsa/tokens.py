from dataclasses import dataclass


@dataclass
class Token:
    type: str
    value: str
    position: int
    line: int
    column: int
