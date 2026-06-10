from dataclasses import dataclass
from pathlib import Path
import re

from .block_parser import START_MARKER, END_MARKER, parse_markdown_blocks
from .svg_renderer import SVGRenderer
from .validation_runner import validate_file
from .markdown_processor import ProcessValidationError


@dataclass
class MarkdownBuildResult:
    markdown_files: list[str]
    svg_files: list[str]


def build_markdown_site(
    input_dir: str | Path,
    output_dir: str | Path,
    assets_dir: str | Path,
    assets_url_prefix: str = "/vsa",
    max_line_width: float = 800.0,
) -> MarkdownBuildResult:
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    assets_dir = Path(assets_dir)

    markdown_files = sorted(
        list(input_dir.rglob("*.md")) +
        list(input_dir.rglob("*.markdown"))
    )

    all_messages = []

    for markdown_file in markdown_files:
        validation = validate_file(markdown_file)

        if not validation.ok:
            all_messages.extend(validation.messages)

    if all_messages:
        raise ProcessValidationError(all_messages)

    output_dir.mkdir(parents=True, exist_ok=True)
    assets_dir.mkdir(parents=True, exist_ok=True)

    written_markdown = []
    written_svg = []

    for markdown_file in markdown_files:
        relative = markdown_file.relative_to(input_dir)
        target_markdown = output_dir / relative
        target_markdown.parent.mkdir(parents=True, exist_ok=True)

        source = markdown_file.read_text(encoding="utf-8")
        rewritten, svg_paths = _rewrite_markdown_file(
            source=source,
            source_relative=relative,
            assets_dir=assets_dir,
            assets_url_prefix=assets_url_prefix,
            max_line_width=max_line_width,
        )

        target_markdown.write_text(rewritten, encoding="utf-8")

        written_markdown.append(str(target_markdown))
        written_svg.extend(str(path) for path in svg_paths)

    return MarkdownBuildResult(
        markdown_files=written_markdown,
        svg_files=written_svg,
    )


def _rewrite_markdown_file(
    source: str,
    source_relative: Path,
    assets_dir: Path,
    assets_url_prefix: str,
    max_line_width: float,
):
    blocks = parse_markdown_blocks(source)
    lines = source.splitlines()

    result_lines = []
    svg_paths = []

    index = 0
    block_index = 0

    while index < len(lines):
        if lines[index].strip() != START_MARKER:
            result_lines.append(lines[index])
            index += 1
            continue

        block_index += 1

        index += 1

        while index < len(lines) and lines[index].strip() != END_MARKER:
            index += 1

        if index >= len(lines):
            break

        end_index = index

        block = blocks[block_index - 1]

        svg_name = _svg_name(source_relative, block_index)
        svg_path = assets_dir / svg_name
        svg_path.parent.mkdir(parents=True, exist_ok=True)

        document = block.parse_body()

        renderer = SVGRenderer()
        renderer.max_line_width = max_line_width

        svg = renderer.render_document(document)
        svg_path.write_text(svg, encoding="utf-8")

        svg_paths.append(svg_path)

        img_src = f"{assets_url_prefix.rstrip('/')}/{svg_name.replace(chr(92), '/')}"
        alt = f"VSA notatie blok {block_index}"

        result_lines.append(f'<img class="vsa-notation" src="{img_src}" alt="{alt}">')

        index = end_index + 1

    return "\n".join(result_lines) + "\n", svg_paths


def _svg_name(source_relative: Path, block_index: int):
    without_suffix = source_relative.with_suffix("")
    stem = "-".join(without_suffix.parts)
    stem = _safe_name(stem)

    return f"{stem}-block-{block_index}.svg"


def _safe_name(value: str):
    value = value.lower()
    value = re.sub(r"[^a-z0-9_-]+", "-", value)
    value = value.strip("-")

    return value or "vsa"
