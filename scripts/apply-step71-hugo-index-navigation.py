from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT_ROOT = ROOT / "examples" / "hugo-demo" / "content-source"

START = "<!-- VSA-SITE-NAV-START -->"
END = "<!-- VSA-SITE-NAV-END -->"

GENERATED_NOTE = "<!-- Gegenereerd door scripts/apply-step71-hugo-index-navigation.py -->"


def main() -> None:
    if not CONTENT_ROOT.exists():
        print(f"Niet gevonden: {CONTENT_ROOT}")
        raise SystemExit(1)

    created = []

    for directory in relevant_directories():
        create_index_page(directory)
        created.append(directory / "_index.md")

    update_home_page()

    print("Stap 71: Hugo index-navigatie bijgewerkt.")
    for path in created:
        print(f"- {path.relative_to(ROOT)}")


def relevant_directories() -> list[Path]:
    dirs = {CONTENT_ROOT}

    for path in CONTENT_ROOT.rglob("*.md"):
        if should_skip(path):
            continue

        dirs.add(path.parent)

    return sorted(dirs, key=lambda p: str(p).lower())


def should_skip(path: Path) -> bool:
    rel = path.relative_to(CONTENT_ROOT)
    parts = set(rel.parts)

    if path.name.startswith("."):
        return True

    if "drafts" in parts:
        return True

    return False


def create_index_page(directory: Path) -> None:
    index = directory / "_index.md"
    rel = directory.relative_to(CONTENT_ROOT)

    title = "Home" if directory == CONTENT_ROOT else title_for_directory(directory)

    child_dirs = [
        child for child in sorted(directory.iterdir(), key=lambda p: p.name.lower())
        if child.is_dir() and not child.name.startswith(".") and has_markdown_content(child)
    ]

    child_pages = [
        child for child in sorted(directory.glob("*.md"), key=lambda p: p.name.lower())
        if child.name.lower() != "_index.md" and not child.name.startswith(".")
    ]

    lines = [
        "---",
        f'title: "{title}"',
        "---",
        "",
        f"# {title}",
        "",
        GENERATED_NOTE,
        "",
    ]

    if directory != CONTENT_ROOT:
        lines.extend([
            f"- [Home]({relative_link(directory, CONTENT_ROOT)})",
            f"- [Omhoog]({relative_link(directory, directory.parent)})",
            "",
        ])

    if child_dirs:
        lines.extend(["## Secties", ""])
        for child in child_dirs:
            lines.append(f"- [{title_for_directory(child)}]({relative_link(directory, child)})")
        lines.append("")

    if child_pages:
        lines.extend(["## Pagina's", ""])
        for page in child_pages:
            lines.append(f"- [{page_title(page)}]({relative_link(directory, page_route_path(page))})")
        lines.append("")

    if not child_dirs and not child_pages:
        lines.append("Deze sectie bevat nog geen pagina's.")
        lines.append("")

    index.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def update_home_page() -> None:
    home = CONTENT_ROOT / "_index.md"

    if not home.exists():
        create_index_page(CONTENT_ROOT)
        return

    text = home.read_text(encoding="utf-8")

    block = "\n".join([
        START,
        "## Navigatie",
        "",
        "- [Voorbeelden](./voorbeelden/)",
        "- [Praktijkvoorbeelden](./voorbeelden/praktijk/)",
        "- [Renderingvoorbeelden](./voorbeelden/rendering/)",
        END,
    ])

    if START in text and END in text:
        before = text.split(START, 1)[0].rstrip()
        after = text.split(END, 1)[1].lstrip()
        text = before + "\n\n" + block + "\n\n" + after
    else:
        text = insert_after_first_h1(text, block)

    home.write_text(text.rstrip() + "\n", encoding="utf-8")


def insert_after_first_h1(text: str, block: str) -> str:
    lines = text.splitlines()
    in_frontmatter = bool(lines and lines[0].strip() == "---")

    for index, line in enumerate(lines):
        if in_frontmatter and index > 0 and line.strip() == "---":
            in_frontmatter = False
            continue

        if not in_frontmatter and line.startswith("# "):
            return "\n".join(lines[: index + 1]) + "\n\n" + block + "\n\n" + "\n".join(lines[index + 1 :])

    return block + "\n\n" + text


def has_markdown_content(directory: Path) -> bool:
    return any(path.suffix.lower() == ".md" for path in directory.rglob("*.md"))


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


def title_for_directory(path: Path) -> str:
    if path == CONTENT_ROOT:
        return "Home"

    return title_for_slug(path.name)


def title_for_slug(slug: str) -> str:
    special = {
        "vsa": "VSA",
        "svg": "SVG",
        "cli": "CLI",
    }

    words = []
    for part in slug.replace("_", "-").split("-"):
        words.append(special.get(part.lower(), part.capitalize()))

    return " ".join(words)


def page_route_path(page: Path) -> Path:
    # Hugo pretty route voor foo.md is foo/.
    return page.with_suffix("")


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
