import re
from enum import Enum, auto


class DirectiveError(Exception):
    pass


class _State(Enum):
    NORMAL = auto()
    WEB_ONLY = auto()
    PRINT_ONLY = auto()
    KEEP_TOGETHER = auto()


_SIMPLE_OPENING = {
    ":::web-only:::": (_State.WEB_ONLY, "web-only"),
    ":::print-only:::": (_State.PRINT_ONLY, "print-only"),
}

_CLOSING = {
    ":::end-web-only:::": _State.WEB_ONLY,
    ":::end-print-only:::": _State.PRINT_ONLY,
    ":::end-keep-together:::": _State.KEEP_TOGETHER,
}

_SHORTCODE = {
    _State.WEB_ONLY: "web-only",
    _State.PRINT_ONLY: "print-only",
    _State.KEEP_TOGETHER: "keep-together",
}

_KEEP_TOGETHER_OPEN = re.compile(r"^:::keep-together(?:\s+(.+?))?:::$")
_SCALE_ATTR = re.compile(r'scale="([^"]+)"')


def process_directives(text: str) -> str:
    """Transform pagebreak, web-only, print-only and keep-together directives.

    :::pagebreak:::                                    → <div class="pagebreak"></div>
    :::web-only:::      ... :::end-web-only:::         → {{< web-only >}} ... {{< /web-only >}}
    :::print-only:::    ... :::end-print-only:::       → {{< print-only >}} ... {{< /print-only >}}
    :::keep-together::: ... :::end-keep-together:::    → {{< keep-together >}} ... {{< /keep-together >}}
    :::keep-together scale="70%"::: ...                → {{< keep-together scale="70%" >}} ...

    The optional scale parameter on keep-together controls the print width of
    .vsa-notation elements within the block (e.g. scale="70%" renders SVGs at
    70% of the page width, proportionally reducing their height).

    Code fences are respected: directives inside fences are not processed.
    Raises DirectiveError for unclosed blocks, mismatched end markers, or stray
    end markers outside any open block.
    """
    lines = text.splitlines()
    result_lines: list[str] = []
    in_code_fence = False
    fence_marker = ""
    state = _State.NORMAL

    for line in lines:
        stripped = line.strip()

        fence = _opening_or_closing_fence(stripped)
        if fence:
            if not in_code_fence:
                in_code_fence = True
                fence_marker = fence
            elif _closes_fence(stripped, fence_marker):
                in_code_fence = False
                fence_marker = ""
            result_lines.append(line)
            continue

        if in_code_fence:
            result_lines.append(line)
            continue

        if stripped == ":::pagebreak:::":
            result_lines.append('<div class="pagebreak"></div>')
            continue

        if stripped in _SIMPLE_OPENING:
            new_state, name = _SIMPLE_OPENING[stripped]
            if state != _State.NORMAL:
                current_name = _SHORTCODE[state]
                raise DirectiveError(
                    f"Geneste directives zijn niet toegestaan:"
                    f" ':::{name}:::' binnen open ':::{current_name}:::'"
                )
            state = new_state
            result_lines.append(_opening_shortcode(name))
            continue

        kt_match = _KEEP_TOGETHER_OPEN.match(stripped)
        if kt_match:
            if state != _State.NORMAL:
                current_name = _SHORTCODE[state]
                raise DirectiveError(
                    f"Geneste directives zijn niet toegestaan:"
                    f" ':::keep-together:::' binnen open ':::{current_name}:::'"
                )
            state = _State.KEEP_TOGETHER
            scale = _parse_scale(kt_match.group(1))
            if scale:
                result_lines.append(_opening_shortcode("keep-together", f'scale="{scale}"'))
            else:
                result_lines.append(_opening_shortcode("keep-together"))
            continue

        if stripped in _CLOSING:
            expected_state = _CLOSING[stripped]
            end_tag = stripped
            if state == _State.NORMAL:
                raise DirectiveError(
                    f"'{end_tag}' zonder overeenkomend openingsblok"
                )
            if state != expected_state:
                current_name = _SHORTCODE[state]
                raise DirectiveError(
                    f"Verkeerde sluitingstag: verwacht ':::end-{current_name}:::',"
                    f" maar zag '{end_tag}'"
                )
            name = _SHORTCODE[state]
            result_lines.append(_closing_shortcode(name))
            state = _State.NORMAL
            continue

        result_lines.append(line)

    if state != _State.NORMAL:
        name = _SHORTCODE[state]
        raise DirectiveError(
            f"Niet-gesloten blok: ':::{name}:::' zonder ':::end-{name}:::'"
        )

    return "\n".join(result_lines) + "\n"


def _parse_scale(params_str: str | None) -> str | None:
    if not params_str:
        return None
    m = _SCALE_ATTR.search(params_str)
    return m.group(1) if m else None


def _opening_shortcode(name: str, params: str = "") -> str:
    if params:
        return "{{< " + name + " " + params + " >}}"
    return "{{< " + name + " >}}"


def _closing_shortcode(name: str) -> str:
    return "{{< /" + name + " >}}"


def _opening_or_closing_fence(stripped: str) -> str:
    if stripped.startswith("```"):
        return "```"
    if stripped.startswith("~~~"):
        return "~~~"
    return ""


def _closes_fence(stripped: str, fence_marker: str) -> bool:
    return stripped.startswith(fence_marker)
