from pathlib import Path

FILES = {
    "src/vsa/scope_layout.py": r"""
from dataclasses import dataclass


MIN_GLYPH_CELL_WIDTH = 14.0


@dataclass
class ScopeColumn:
    ehm: str
    elm: str
    width: float


@dataclass
class ScopeLayout:
    text: str
    width: float
    columns: list[ScopeColumn]
    text_width: float = 0.0
    filler_width: float = 0.0


def build_scope_layout(
    node,
    minimum_column_width: float = MIN_GLYPH_CELL_WIDTH,
    text_font_size: float = 20.0,
):
    hm = node.height_modifier or []
    lm = node.length_modifier or []

    if not hm and not lm:
        hm = ["~"]
        lm = ["~"]
    elif hm and not lm:
        lm = ["~"] * len(hm)
    elif lm and not hm:
        hm = ["~"] * len(lm)

    count = max(len(hm), len(lm), 1)

    if len(hm) == 1 and count > 1:
        hm = hm * count

    if len(lm) == 1 and count > 1:
        lm = lm * count

    text = node.text
    text_width = estimate_scope_text_width(text, text_font_size)

    if count <= 1:
        grid_width = text_width
    else:
        grid_width = max(text_width, count * minimum_column_width)

    column_width = grid_width / count
    filler_width = max(0.0, grid_width - text_width)

    columns = [
        ScopeColumn(
            ehm=hm[index],
            elm=lm[index],
            width=column_width,
        )
        for index in range(count)
    ]

    return ScopeLayout(
        text=text,
        width=grid_width,
        columns=columns,
        text_width=text_width,
        filler_width=filler_width,
    )


def estimate_scope_text_width(text: str, font_size: float):
    if text == "":
        return max(4.0, font_size * 0.25)

    return max(4.0, len(text) * font_size * 0.50)


def estimate_text_width(text: str, font_size: float, preserve_whitespace: bool = True):
    if text == "":
        return 0.0

    visible = text if preserve_whitespace else text.strip()

    if visible == "":
        return 0.0

    return len(visible) * font_size * 0.50
""",
    "src/vsa/svg_line_layout.py": r"""
from dataclasses import dataclass, field
import re

from .ast import TextNode, ScopeNode, PitchMarkerNode
from .scope_layout import build_scope_layout, estimate_text_width


@dataclass
class LayoutItem:
    node: object
    width: float


@dataclass
class LayoutLine:
    items: list[LayoutItem] = field(default_factory=list)
    width: float = 0.0


@dataclass
class LineLayoutSettings:
    font_size: float = 20.0
    text_gap: float = 0.0
    scope_gap: float = 0.0
    pitch_marker_width: float = 20.0
    pitch_marker_gap: float = 2.0


def split_text_node(node: TextNode):
    text = node.text

    if text == "":
        return []

    parts = re.findall(r"\S+\s*", text)

    return [
        TextNode(text=part)
        for part in parts
        if part != ""
    ]


def iter_layout_nodes(document):
    for node in document.nodes:
        if isinstance(node, TextNode):
            yield from split_text_node(node)
        else:
            yield node


def measure_node(node, settings: LineLayoutSettings | None = None):
    settings = settings or LineLayoutSettings()

    if isinstance(node, TextNode):
        return estimate_text_width(
            node.text,
            settings.font_size,
            preserve_whitespace=True,
        ) + settings.text_gap

    if isinstance(node, ScopeNode):
        return build_scope_layout(node).width + settings.scope_gap

    if isinstance(node, PitchMarkerNode):
        marker_width = max(
            settings.pitch_marker_width,
            max(len(node.height_modifier), 1) * settings.pitch_marker_width,
        )
        return marker_width + settings.pitch_marker_gap

    return 0.0


def build_lines(
    document,
    max_width: float = 800.0,
    settings: LineLayoutSettings | None = None,
):
    settings = settings or LineLayoutSettings()
    lines = []
    current = LayoutLine()

    for node in iter_layout_nodes(document):
        width = measure_node(node, settings=settings)

        if (
            current.items
            and current.width + width > max_width
            and _may_break_before(current.items[-1].node, node)
        ):
            lines.append(current)
            current = LayoutLine()

            if isinstance(node, TextNode):
                node = TextNode(text=node.text.lstrip())
                width = measure_node(node, settings=settings)

        current.items.append(LayoutItem(node=node, width=width))
        current.width += width

    if current.items:
        lines.append(current)

    return lines


def _may_break_before(previous_node, next_node):
    if isinstance(previous_node, PitchMarkerNode):
        return True

    if isinstance(previous_node, TextNode):
        return previous_node.text.endswith((" ", "\t", "\n", "\r"))

    if isinstance(next_node, TextNode):
        return next_node.text[:1].isspace()

    return False
""",
    "tests/test_svg_textflow_overlays.py": r"""
from vsa.parser import Parser
from vsa.scope_layout import build_scope_layout
from vsa.svg_line_layout import build_lines
from vsa.svg_renderer import SVGRenderer


def test_multi_ehm_scope_creates_filler_space():
    document = Parser(r"{/&/&/&/schon}").parse()
    layout = build_scope_layout(document.nodes[0])

    assert layout.filler_width > 0


def test_no_midword_wrapping():
    document = Parser(r"eerstge{/bo_}re{\ne_}").parse()
    lines = build_lines(document, max_width=120)

    assert len(lines) == 1


def test_word_wrapping_allows_break_after_space():
    document = Parser(r"eerste woord tweede").parse()
    lines = build_lines(document, max_width=90)

    assert len(lines) >= 2


def test_scope_spacing_preserves_word_gap_in_svg_text():
    document = Parser(r"grote ge{na_}{\de} {\ge}").parse()
    svg = SVGRenderer().render_document(document)

    assert "grote " in svg
    assert 'xml:space="preserve"' in svg
""",
}

for rel, content in FILES.items():
    path = Path(rel)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"wrote {path}")

print("Stap 51 force-apply gereed.")
