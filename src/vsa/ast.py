from dataclasses import dataclass, field
from typing import List, Optional, Union, Dict, Any


@dataclass
class TextNode:
    text: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": "TextNode",
            "text": self.text,
        }


@dataclass
class ScopeNode:
    height_modifier: List[str]
    text: str
    length_modifier: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": "ScopeNode",
            "height_modifier": self.height_modifier,
            "text": self.text,
            "length_modifier": self.length_modifier,
        }


@dataclass
class PitchMarkerNode:
    height_modifier: Optional[List[str]] = None
    start: Optional[int] = None
    end: Optional[int] = None

    @property
    def ehm(self) -> List[str]:
        return self.height_modifier or []

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": "PitchMarkerNode",
            "height_modifier": self.height_modifier or [],
        }


# Compatibele naam voor de nieuwe terminologie.
# Nog geen aparte class: renderer, validator en bestaande tests behandelen
# hoogte-markeringen voorlopig nog als PitchMarkerNode.
HeightMarkerNode = PitchMarkerNode


Node = Union[TextNode, ScopeNode, PitchMarkerNode]


@dataclass
class Document:
    nodes: List[Node] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": "Document",
            "nodes": [node.to_dict() for node in self.nodes],
        }
