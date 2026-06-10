from dataclasses import dataclass
from pathlib import Path
import re

from .block_parser import parse_markdown_blocks
from .svg_renderer import SVGRenderer


@dataclass
class ProcessedBlock:
    source_file: str
    block_index: int
    output_file: str


@dataclass
class ProcessResult:
    blocks: list[ProcessedBlock]


def process_markdown_file(input_path: str | Path, output_dir: str | Path, base_dir: str | Path | None = None) -> ProcessResult:
    input_path = Path(input_path)
    output_dir = Path(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    markdown = input_path.read_text(encoding="utf-8")
    blocks = parse_markdown_blocks(markdown)

    processed = []

    stem = _output_stem(input_path, base_dir)

    for index, block in enumerate(blocks, start=1):
        document = block.parse_body()
        svg = SVGRenderer().render_document(document)

        output_name = f"{stem}-block-{index}.svg"
        output_path = output_dir / output_name

        output_path.write_text(svg, encoding="utf-8")

        processed.append(
            ProcessedBlock(
                source_file=str(input_path),
                block_index=index,
                output_file=str(output_path),
            )
        )

    return ProcessResult(blocks=processed)


def process_path(input_path: str | Path, output_dir: str | Path) -> ProcessResult:
    input_path = Path(input_path)
    output_dir = Path(output_dir)

    all_blocks = []

    if input_path.is_file():
        result = process_markdown_file(input_path, output_dir)
        all_blocks.extend(result.blocks)

    elif input_path.is_dir():
        markdown_files = sorted(
            list(input_path.rglob("*.md")) +
            list(input_path.rglob("*.markdown"))
        )

        for markdown_file in markdown_files:
            result = process_markdown_file(
                markdown_file,
                output_dir,
                base_dir=input_path,
            )
            all_blocks.extend(result.blocks)

    else:
        raise FileNotFoundError(f"Pad niet gevonden: {input_path}")

    return ProcessResult(blocks=all_blocks)


def _output_stem(input_path: Path, base_dir: str | Path | None):
    if base_dir is None:
        return _safe_name(input_path.stem)

    relative = input_path.relative_to(base_dir)
    without_suffix = relative.with_suffix("")
    parts = without_suffix.parts

    return _safe_name("-".join(parts))


def _safe_name(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9_-]+", "-", value)
    value = value.strip("-")

    return value or "vsa"
