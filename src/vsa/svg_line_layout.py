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


def split_text_node(node: TextNode):
    text = node.text.lstrip()

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


def measure_node(node):
    if isinstance(node, TextNode):
        return estimate_text_width(node.text, 20)

    if isinstance(node, ScopeNode):
        return build_scope_layout(node).width + 4

    if isinstance(node, PitchMarkerNode):
        return max(34.0, max(len(node.height_modifier), 1) * 28.0) + 8

    return 0.0


def build_lines(document, max_width: float = 800.0):
    lines = []
    current = LayoutLine()

    for node in iter_layout_nodes(document):
        width = measure_node(node)

        if current.items and current.width + width > max_width:
            lines.append(current)
            current = LayoutLine()

            if isinstance(node, TextNode):
                node = TextNode(text=node.text.lstrip())
                width = measure_node(node)

        current.items.append(LayoutItem(node=node, width=width))
        current.width += width

    if current.items:
        lines.append(current)

    return lines
