from dataclasses import dataclass
from pathlib import Path
import re
import shutil

from .block_parser import START_MARKER, END_MARKER, parse_markdown_blocks
from .config import VSAConfig
from .markdown_directives import process_directives
from .markdown_include import resolve_includes
from .svg_renderer import SVGRenderer
from .validation_runner import validate_file
from .markdown_processor import ProcessValidationError


CONTENT_ASSET_SUFFIXES = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".gif",
}


@dataclass
class MarkdownBuildResult:
    markdown_files: list[str]
    svg_files: list[str]
    static_files: list[str]


def build_markdown_site(
    input_dir,
    output_dir,
    assets_dir,
    assets_url_prefix="/vsa",
    max_line_width=800.0,
    output_mode="img",
    config: VSAConfig | None = None,
):
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    assets_dir = Path(assets_dir)

    markdown_files = sorted(
        list(input_dir.rglob("*.md")) +
        list(input_dir.rglob("*.markdown"))
    )

    all_messages = []

    for markdown_file in markdown_files:
        validation = validate_file(markdown_file, config=config)

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
        source = resolve_includes(source, source_path=markdown_file)
        source = process_directives(source)

        rewritten, svg_paths = _rewrite_markdown_file(
            source=source,
            source_relative=relative,
            assets_dir=assets_dir,
            assets_url_prefix=assets_url_prefix,
            max_line_width=max_line_width,
            output_mode=output_mode,
        )

        target_markdown.write_text(rewritten, encoding="utf-8")

        written_markdown.append(str(target_markdown))
        written_svg.extend(str(path) for path in svg_paths)

    written_static = _copy_content_assets(input_dir, output_dir)

    return MarkdownBuildResult(
        markdown_files=written_markdown,
        svg_files=written_svg,
        static_files=written_static,
    )


def _copy_content_assets(input_dir: Path, output_dir: Path) -> list[str]:
    written_static: list[str] = []

    for source in sorted(input_dir.rglob("*")):
        if not source.is_file():
            continue

        suffix = source.suffix.lower()
        if suffix in {".md", ".markdown"}:
            continue
        if suffix not in CONTENT_ASSET_SUFFIXES:
            continue

        relative = source.relative_to(input_dir)
        target = output_dir / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        written_static.append(str(target))

    return written_static


def _rewrite_markdown_file(
    source,
    source_relative,
    assets_dir,
    assets_url_prefix,
    max_line_width,
    output_mode,
):
    blocks = parse_markdown_blocks(source)
    lines = source.splitlines()

    result_lines = []
    svg_paths = []

    index = 0
    block_index = 0
    in_code_fence = False
    fence_marker = ""

    while index < len(lines):
        stripped = lines[index].strip()
        fence = _opening_or_closing_fence(stripped)

        if fence:
            if not in_code_fence:
                in_code_fence = True
                fence_marker = fence
            elif _closes_fence(stripped, fence_marker):
                in_code_fence = False
                fence_marker = ""

            result_lines.append(lines[index])
            index += 1
            continue

        if in_code_fence or stripped != START_MARKER:
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

        renderer = SVGRenderer()
        renderer.max_line_width = max_line_width

        svg = renderer.render_document(block.parse_body())
        svg_path.write_text(svg, encoding="utf-8")

        svg_paths.append(svg_path)

        img_src = f"{assets_url_prefix.rstrip('/')}/{svg_name.replace(chr(92), '/')}"

        if output_mode == "shortcode":
            replacement = f'{{{{< vsa src="{img_src}" >}}}}'
        else:
            replacement = (
                f'<img class="vsa-notation" '
                f'src="{img_src}" alt="VSA notatie">'
            )

        result_lines.append(replacement)

        index = end_index + 1

    return "\n".join(result_lines) + "\n", svg_paths


def _svg_name(source_relative, block_index):
    without_suffix = source_relative.with_suffix("")
    stem = "-".join(without_suffix.parts)
    stem = _safe_name(stem)

    return f"{stem}-block-{block_index}.svg"


def _safe_name(value):
    value = value.lower()
    value = re.sub(r"[^a-z0-9_-]+", "-", value)
    value = value.strip("-")

    return value or "vsa"


def _opening_or_closing_fence(stripped: str):
    if stripped.startswith("```"):
        return "```"

    if stripped.startswith("~~~"):
        return "~~~"

    return ""


def _closes_fence(stripped: str, fence_marker: str):
    return stripped.startswith(fence_marker)
