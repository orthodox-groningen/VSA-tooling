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


def process_markdown_file(input_path: str | Path, output_dir: str | Path) -> ProcessResult:
    input_path = Path(input_path)
    output_dir = Path(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    markdown = input_path.read_text(encoding="utf-8")
    blocks = parse_markdown_blocks(markdown)

    processed = []

    stem = _safe_name(input_path.stem)

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


def _safe_name(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9_-]+", "-", value)
    value = value.strip("-")

    return value or "vsa"
