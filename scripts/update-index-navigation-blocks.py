from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT_ROOT = ROOT / "examples" / "hugo-demo" / "content-source"

START = "<!-- VSA-INDEX-NAV-START -->"
END = "<!-- VSA-INDEX-NAV-END -->"


def main() -> None:
    if not CONTENT_ROOT.exists():
        print(f"Niet gevonden: {CONTENT_ROOT}")
        raise SystemExit(1)

    changed = []

    for index in sorted(CONTENT_ROOT.rglob("_index.md")):
        original = index.read_text(encoding="utf-8")
        text = upsert_navigation_block(index, original)

        if text != original:
            index.write_text(text.rstrip() + "\n", encoding="utf-8")
            changed.append(index)

    print("Stap 78: _index navigatieblokken bijgewerkt.")
    if changed:
        for path in changed:
            print(f"- {path.relative_to(ROOT)}")
    else:
        print("Geen wijzigingen nodig.")


def upsert_navigation_block(index: Path, text: str) -> str:
    block = build_navigation_block(index.parent)

    if START in text and END in text:
        before = text.split(START, 1)[0].rstrip()
        after = text.split(END, 1)[1].lstrip()
        return before + "\n\n" + block + "\n\n" + after

    return insert_after_first_heading(text, block)


def build_navigation_block(directory: Path) -> str:
    lines = [
        START,
        "## Navigatie",
        "",
    ]

    if directory != CONTENT_ROOT:
        lines.append(f"- [Home]({relative_link(directory, CONTENT_ROOT)})")
        lines.append(f"- [Omhoog]({relative_link(directory, directory.parent)})")

    siblings = sibling_sections(directory)
    if siblings:
        lines.append("")
        lines.append("### Zelfde niveau")
        for sibling in siblings:
            lines.append(f"- [{title_for_index(sibling)}]({relative_link(directory, sibling.parent)})")

    child_dirs = child_sections(directory)
    if child_dirs:
        lines.append("")
        lines.append("### Secties")
        for child in child_dirs:
            lines.append(f"- [{title_for_index(child / '_index.md')}]({relative_link(directory, child)})")

    child_pages = child_content_pages(directory)
    if child_pages:
        lines.append("")
        lines.append("### Pagina's")
        for page in child_pages:
            lines.append(f"- [{page_title(page)}]({relative_link(directory, page.with_suffix(''))})")

    lines.append(END)
    return "\n".join(lines)


def insert_after_first_heading(text: str, block: str) -> str:
    lines = text.splitlines()
    in_frontmatter = bool(lines and lines[0].strip() == "---")

    for index, line in enumerate(lines):
        if in_frontmatter and index > 0 and line.strip() == "---":
            in_frontmatter = False
            continue

        if not in_frontmatter and line.startswith("# "):
            return "\n".join(lines[: index + 1]) + "\n\n" + block + "\n\n" + "\n".join(lines[index + 1 :])

    return block + "\n\n" + text


def sibling_sections(directory: Path) -> list[Path]:
    if directory == CONTENT_ROOT:
        return []

    return [
        child / "_index.md"
        for child in sorted(directory.parent.iterdir(), key=lambda p: p.name.lower())
        if child.is_dir()
        and child != directory
        and not child.name.startswith(".")
        and (child / "_index.md").exists()
    ]


def child_sections(directory: Path) -> list[Path]:
    return [
        child
        for child in sorted(directory.iterdir(), key=lambda p: p.name.lower())
        if child.is_dir()
        and not child.name.startswith(".")
        and (child / "_index.md").exists()
    ]


def child_content_pages(directory: Path) -> list[Path]:
    return [
        page
        for page in sorted(directory.glob("*.md"), key=lambda p: p.name.lower())
        if page.name.lower() != "_index.md"
    ]


def title_for_index(index: Path) -> str:
    if not index.exists():
        return title_for_slug(index.parent.name)

    return page_title(index)


def page_title(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    in_frontmatter = False

    for line in text.splitlines():
        stripped = line.strip()

        if stripped == "---":
            in_frontmatter = not in_frontmatter
            continue

        if in_frontmatter and stripped.startswith("title:"):
            return stripped.split(":", 1)[1].strip().strip('"')

    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()

    return title_for_slug(path.stem)


def title_for_slug(slug: str) -> str:
    special = {"vsa": "VSA", "svg": "SVG", "cli": "CLI"}
    return " ".join(
        special.get(part.lower(), part.capitalize())
        for part in slug.replace("_", "-").split("-")
    )


def relative_link(from_directory: Path, to_path: Path) -> str:
    from_rel = from_directory.relative_to(CONTENT_ROOT)

    if to_path == CONTENT_ROOT:
        return "./" if not from_rel.parts else "../" * len(from_rel.parts)

    to_rel = to_path.relative_to(CONTENT_ROOT)

    from_parts = from_rel.parts
    to_parts = to_rel.parts

    common = 0
    for a, b in zip(from_parts, to_parts):
        if a != b:
            break
        common += 1

    ups = [".."] * (len(from_parts) - common)
    downs = list(to_parts[common:])
    parts = ups + downs

    if not parts:
        return "./"

    return "/".join(parts) + "/"


if __name__ == "__main__":
    main()
