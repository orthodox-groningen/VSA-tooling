from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class TextNode:
    text: str


@dataclass
class ScopeNode:
    height_modifier: List[str]
    text: str
    length_modifier: List[str]


@dataclass
class PitchMarkerNode:
    height_modifier: Optional[List[str]] = None


Node = Union[TextNode, ScopeNode, PitchMarkerNode]


@dataclass
class Document:
    nodes: List[Node] = field(default_factory=list)
