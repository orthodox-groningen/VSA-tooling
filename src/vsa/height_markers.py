from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from vsa.ast import Document, HeightMarkerNode, PitchMarkerNode


HeightMarkerRole = Literal["start_height", "local_height"]


@dataclass(frozen=True)
class HeightMarkerRef:
    node: PitchMarkerNode
    index: int
    role: HeightMarkerRole

    @property
    def height_modifier(self) -> list[str]:
        return self.node.height_modifier or []

    @property
    def ehm(self) -> list[str]:
        return self.height_modifier

    @property
    def is_start_marker(self) -> bool:
        return self.role == "start_height"

    @property
    def is_local_marker(self) -> bool:
        return self.role == "local_height"


HeightMarkerInfo = HeightMarkerRef


def is_height_marker_node(node: object) -> bool:
    return isinstance(node, HeightMarkerNode)


def height_marker_refs(document: Document) -> list[HeightMarkerRef]:
    refs: list[HeightMarkerRef] = []

    for index, node in enumerate(document.nodes):
        if is_height_marker_node(node):
            role: HeightMarkerRole = "start_height" if not refs else "local_height"
            refs.append(HeightMarkerRef(node=node, index=index, role=role))

    return refs


def height_marker_nodes(document: Document) -> list[PitchMarkerNode]:
    return [ref.node for ref in height_marker_refs(document)]


def height_markers(document: Document) -> list[HeightMarkerRef]:
    return height_marker_refs(document)


def iter_height_markers(document: Document):
    yield from height_marker_refs(document)


def first_height_marker(document: Document) -> HeightMarkerRef | None:
    refs = height_marker_refs(document)
    return refs[0] if refs else None


def last_height_marker(document: Document) -> HeightMarkerRef | None:
    refs = height_marker_refs(document)
    return refs[-1] if refs else None


def local_height_markers(document: Document) -> list[HeightMarkerRef]:
    return [ref for ref in height_marker_refs(document) if ref.role == "local_height"]
