from .ast import TextNode, ScopeNode, PitchMarkerNode
from .scope_layout import build_scope_layout, estimate_text_width


def measure_document_width(document, left_margin: float = 40.0, right_margin: float = 40.0):
    width = left_margin

    for node in document.nodes:
        if isinstance(node, TextNode):
            width += estimate_text_width(node.text, 20)

        elif isinstance(node, ScopeNode):
            layout = build_scope_layout(node)
            width += layout.width + 4

        elif isinstance(node, PitchMarkerNode):
            marker_width = max(34.0, max(len(node.height_modifier), 1) * 28.0)
            width += marker_width + 8

    width += right_margin

    return max(120.0, width)
