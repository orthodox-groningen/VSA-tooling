"""Corpus-VSA voor tropaar toon 4: stanza-telling en extractie uit onderzoeksdoc."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

# Volgorde = sectie Toon 4 in onderzoeks-troparen-en-kondaken.md.
CORPUS_ENTRIES: tuple[tuple[str, str, str], ...] = (
    ("T4-01", "johannes-voorloper", "Geboorte Johannes Voorloper"),
    ("T4-02", "johannes-shanghai", "Johannes Shanghai / San Francisco"),
    ("T4-03", "hh-martelaren", "HH. Martelaren"),
    ("T4-04", "mantel-moeder-gods", "Mantel Moeder Gods"),
    ("T4-05", "h-marina", "H. Marina"),
    ("T4-06", "profeet-elia", "Profeet Elia"),
    ("T4-07", "geboorte-moeder-gods", "Geboorte Moeder Gods"),
    ("T4-07a", "geboorte-moeder-gods-liturgikon", "Geboorte Moeder Gods (Liturgikon)"),
    ("T4-08", "tempelgang-welbehagen", "Tempelgang (begin welbehagen)"),
    ("T4-09", "tempelgang-alreine-tempel", "Tempelgang (alreine Tempel)"),
    ("T4-10", "apostel-andreas", "Apostel Andreas"),
    ("T4-11", "nicolaas-van-myra", "Nicolaas van Myra"),
    ("T4-12", "engelen-maandag", "Engelen (Maandag)"),
)

_STANZA_TRAIL = re.compile(r"\*+\s*$")
_FRONTMATTER = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)


@dataclass(frozen=True)
class CorpusPiece:
    piece_id: str
    slug: str
    title: str
    body: str

    @property
    def stanza_count(self) -> int:
        return count_stanzas(self.body)

    def filename_stem(self) -> str:
        return f"{self.piece_id}-{self.slug}"


def strip_frontmatter(text: str) -> str:
    return _FRONTMATTER.sub("", text, count=1).strip()


def count_stanzas(body: str) -> int:
    """Tel tekstregels (template-frasen): `*` aan regel-einde; laatste regel telt mee."""
    body = strip_frontmatter(body)
    lines = [
        ln.strip()
        for ln in body.splitlines()
        if ln.strip() and not ln.strip().startswith("<!--")
    ]
    if not lines:
        return 0
    count = sum(1 for ln in lines if _STANZA_TRAIL.search(ln))
    if not _STANZA_TRAIL.search(lines[-1]):
        count += 1
    return count


def extract_toon4_vsa_blocks(markdown_path: Path) -> list[str]:
    """Ruwe VSA-teksten uit `## Toon 4` … `## Toon 8` (volgorde corpus)."""
    text = markdown_path.read_text(encoding="utf-8")
    try:
        start = text.index("## Toon 4")
        end = text.index("## Toon 8")
    except ValueError as exc:
        raise ValueError(f"missing Toon 4/8 headings in {markdown_path}") from exc
    section = text[start:end]
    blocks: list[str] = []
    for match in re.finditer(r"::: vsa-notatie\n(.*?):::", section, re.DOTALL):
        raw = match.group(1).strip()
        # HTML-commentaar blijft in de bron (parser negeert het bij zingen).
        blocks.append(raw)
    return blocks


def load_corpus(markdown_path: Path) -> list[CorpusPiece]:
    blocks = extract_toon4_vsa_blocks(markdown_path)
    if len(blocks) != len(CORPUS_ENTRIES):
        raise ValueError(
            f"expected {len(CORPUS_ENTRIES)} Toon-4 blocks, got {len(blocks)}"
        )
    return [
        CorpusPiece(piece_id=entry[0], slug=entry[1], title=entry[2], body=block)
        for entry, block in zip(CORPUS_ENTRIES, blocks, strict=True)
    ]


def write_vsa_file(piece: CorpusPiece, path: Path) -> None:
    """Schrijf .vsa met YAML-frontmatter (geen lyrics-mapping; alleen brontekst)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    content = (
        "---\n"
        f"title: {piece.title}\n"
        "do: F4\n"
        "mode: major\n"
        "genre: tropaar\n"
        "tone: 4\n"
        "template: tropaar-toon-4\n"
        f"corpus_id: {piece.piece_id}\n"
        "---\n\n"
        f"{piece.body}\n"
    )
    path.write_text(content, encoding="utf-8")
