from pathlib import Path

from .parser import Parser
from .svg_renderer import SVGRenderer


def export_svg(input_path: str, output_path: str):
    text = Path(input_path).read_text(encoding="utf-8")

    document = Parser(text).parse()

    svg = SVGRenderer().render_document(document)

    Path(output_path).write_text(svg, encoding="utf-8")
