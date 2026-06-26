import re
from pathlib import Path

INCLUDE_PATTERN = re.compile(r"^:::include\s+(.+?):::$")


class IncludeError(Exception):
    pass


def resolve_includes(
    text: str,
    source_path: Path,
    include_stack: list[Path] | None = None,
) -> str:
    """Resolve :::include path::: directives recursively.

    Supports .md/.markdown (recursive), .vsa (wrapped as vsa-notatie block),
    and .svg (as <img src>). Detects circular references via include_stack.
    Code fences are respected: directives inside fences are not processed.
    """
    if include_stack is None:
        include_stack = [source_path.resolve()]

    lines = text.splitlines()
    result_lines: list[str] = []
    in_code_fence = False
    fence_marker = ""

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

        match = INCLUDE_PATTERN.match(stripped)
        if not match:
            result_lines.append(line)
            continue

        rel_path = match.group(1).strip()
        included_path = (source_path.parent / rel_path).resolve()

        if included_path in include_stack:
            chain = " → ".join(str(p) for p in include_stack) + f" → {included_path}"
            raise IncludeError(f"Kringverwijzing gedetecteerd: {chain}")

        if not included_path.exists():
            raise IncludeError(
                f"Bestand niet gevonden: '{rel_path}' (vanuit {source_path})"
            )

        suffix = included_path.suffix.lower()

        if suffix not in (".md", ".markdown", ".vsa", ".svg"):
            raise IncludeError(
                f"Onbekend bestandstype '{suffix}' voor include:"
                f" '{rel_path}' (vanuit {source_path})"
            )

        raw = included_path.read_text(encoding="utf-8")

        if suffix in (".md", ".markdown"):
            expanded = resolve_includes(
                raw,
                source_path=included_path,
                include_stack=include_stack + [included_path],
            )
            result_lines.extend(expanded.splitlines())
        elif suffix == ".vsa":
            result_lines.append("::: vsa-notatie")
            result_lines.extend(raw.splitlines())
            result_lines.append(":::")
        elif suffix == ".svg":
            result_lines.append(f'<img src="{rel_path}" class="vsa-notation" />')

    return "\n".join(result_lines) + "\n"


def _opening_or_closing_fence(stripped: str) -> str:
    if stripped.startswith("```"):
        return "```"
    if stripped.startswith("~~~"):
        return "~~~"
    return ""


def _closes_fence(stripped: str, fence_marker: str) -> bool:
    return stripped.startswith(fence_marker)
