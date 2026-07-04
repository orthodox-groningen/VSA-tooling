from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from vsa.ast import Document, HeightMarkerNode, PitchMarkerNode

# Halftoon-prefixen: canonical "#" = +0.5, canonical "b" = -0.5
_SHARP_CANONICAL = "#"
_FLAT_CANONICAL = "b"
_SHARP_PREFIX_CHARS: frozenset[str] = frozenset("+#♯")
_FLAT_PREFIX_CHARS: frozenset[str] = frozenset("b♭")


def _pitch_of_ehm(ehm: str) -> float:
    """Berekent de pitchbijdrage van één EHM-waarde als float (halftoon = ±0.5)."""
    if not ehm:
        return 0.0
    halftone = 0.0
    base = ehm
    if ehm[0] in _SHARP_PREFIX_CHARS:
        halftone, base = +0.5, ehm[1:]
    elif ehm[0] in _FLAT_PREFIX_CHARS:
        halftone, base = -0.5, ehm[1:]
    return halftone + base.count("/") - base.count("\\")


def _pitch_of_ehm_list(ehm_list: list[str]) -> float:
    """Berekent de cumulatieve pitchbijdrage van een lijst EHM-waarden."""
    return sum(_pitch_of_ehm(e) for e in ehm_list)


def _format_pitch_delta(delta: float) -> str:
    if delta == int(delta):
        return str(int(delta))
    return str(delta)


def height_marker_mismatch_detail(declared: float, computed: float) -> str:
    """Compacte diagnostische tekst: computed = marker ± N."""
    delta = computed - declared
    if delta == 0:
        return "computed = marker"
    sign = "+" if delta > 0 else "-"
    return f"computed = marker {sign} {_format_pitch_delta(abs(delta))}"


def _marker_for_pitch(pitch: float) -> str:
    """Geeft de canonieke hoogte-markeringsstring voor een gegeven pitchwaarde.

    Voorbeelden: 0 → '[:]', 2 → '[//:]', -1.5 → '[b\\:]', 0.5 → '[+-:]'
    """
    if pitch == 0.0:
        return "[:]"
    n = int(pitch)       # truncatie naar nul (bijv. int(-2.5) == -2)
    half = pitch - n     # 0.0 of ±0.5
    backslash = "\\"
    if half == 0.0:
        if n > 0:
            return f"[{'/' * n}:]"
        return f"[{backslash * abs(n)}:]"
    # Halftoon-geval
    if pitch > 0:
        # +0.5 → [+-:], +1.5 → [+/:], +2.5 → [+//:]
        return "[+-:]" if n == 0 else f"[+{'/' * n}:]"
    else:
        # -0.5 → [b-:], -1.5 → [b\:], -2.5 → [b\\:]
        return "[b-:]" if n == 0 else f"[b{backslash * abs(n)}:]"


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
