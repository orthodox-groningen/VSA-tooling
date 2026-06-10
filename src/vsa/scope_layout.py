from dataclasses import dataclass


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


def build_scope_layout(node, minimum_column_width: float = 28.0, text_font_size: float = 20.0):
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

    text_width = estimate_text_width(node.text, text_font_size)
    grid_width = max(text_width, count * minimum_column_width)
    column_width = grid_width / count

    columns = [
        ScopeColumn(
            ehm=hm[index],
            elm=lm[index],
            width=column_width,
        )
        for index in range(count)
    ]

    return ScopeLayout(
        text=node.text,
        width=grid_width,
        columns=columns,
    )


def estimate_text_width(text: str, font_size: float):
    return max(8.0, len(text) * font_size * 0.55)
