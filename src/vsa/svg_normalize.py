import re


def normalize_svg(svg: str) -> str:
    svg = svg.replace("\r\n", "\n")
    svg = re.sub(r">\s+<", "><", svg)
    svg = re.sub(r"\s+", " ", svg)
    return svg.strip()
