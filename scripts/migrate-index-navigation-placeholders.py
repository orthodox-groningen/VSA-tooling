from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
CONTENT_ROOT = ROOT / "examples" / "hugo-demo" / "content-source"

OLD_NOTES = [
    "<!-- Gegenereerd door scripts/apply-step71-hugo-index-navigation.py -->",
    "<!-- Gegenereerd door scripts/apply-step75-navigation-praktijk-moved.py -->",
]
OLD_BLOCK_PATTERNS = [
    re.compile(r"\n*<!-- VSA-INDEX-NAV-START -->.*?<!-- VSA-INDEX-NAV-END -->\n*", re.DOTALL),
    re.compile(r"\n*<!-- VSA-SITE-NAV-START -->.*?<!-- VSA-SITE-NAV-END -->\n*", re.DOTALL),
    re.compile(r"\n*<!-- VSA-NAV-START -->.*?<!-- VSA-NAV-END -->\n*", re.DOTALL),
]


def main() -> None:
    changed = []

    for index in sorted(CONTENT_ROOT.rglob("_index.md")):
        original = index.read_text(encoding="utf-8")
        text = migrate_index(index, original)

        if text != original:
            index.write_text(text.rstrip() + "\n", encoding="utf-8")
            changed.append(index)

    print("Stap 79: _index navigatie-placeholders gemigreerd.")
    if changed:
        for path in changed:
            print(f"- {path.relative_to(ROOT)}")
    else:
        print("Geen wijzigingen nodig.")


def migrate_index(index: Path, text: str) -> str:
    was_whole_generated = any(note in text for note in OLD_NOTES)

    for note in OLD_NOTES:
        text = text.replace(note, "")

    for pattern in OLD_BLOCK_PATTERNS:
        text = pattern.sub("\n", text)

    text = re.sub(r"\n{4,}", "\n\n\n", text)

    if "<!-- VSA-NAV:" in text:
        return text

    placeholder_block = placeholder_block_for_index(index)

    if was_whole_generated:
        text = keep_frontmatter_and_h1(index, text)

    return insert_after_first_heading(text, placeholder_block)


def placeholder_block_for_index(index: Path) -> str:
    lines = []

    if index.parent != CONTENT_ROOT:
        lines.extend([
            "<!-- VSA-NAV:HOME -->",
            "<!-- VSA-NAV:UP -->",
            "",
            "<!-- VSA-NAV:SIBLINGS -->",
            "",
        ])

    lines.extend([
        "<!-- VSA-NAV:CHILDREN -->",
        "",
        "<!-- VSA-NAV:PAGES -->",
    ])

    return "\n".join(lines)


def keep_frontmatter_and_h1(index: Path, text: str) -> str:
    frontmatter = extract_frontmatter(text)
    title = extract_title(text) or title_for_slug(index.parent.name if index.parent != CONTENT_ROOT else "Home")

    lines = []
    if frontmatter:
        lines.append(frontmatter.strip())
        lines.append("")
    else:
        lines.extend(["---", f'title: "{title}"', "---", ""])

    lines.append(f"# {title}")
    lines.append("")
    lines.append("Deze pagina kan redactioneel worden aangevuld. Het navigatiegedeelte hieronder wordt automatisch bijgewerkt.")
    return "\n".join(lines)


def extract_frontmatter(text: str) -> str | None:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None

    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return "\n".join(lines[: index + 1])

    return None


def extract_title(text: str) -> str | None:
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

    return None


def insert_after_first_heading(text: str, block: str) -> str:
    lines = text.splitlines()
    in_frontmatter = bool(lines and lines[0].strip() == "---")

    for index, line in enumerate(lines):
        if in_frontmatter and index > 0 and line.strip() == "---":
            in_frontmatter = False
            continue

        if not in_frontmatter and line.startswith("# "):
            return "\n".join(lines[: index + 1]) + "\n\n" + block + "\n\n" + "\n".join(lines[index + 1:])

    return block + "\n\n" + text


def title_for_slug(slug: str) -> str:
    special = {"vsa": "VSA", "svg": "SVG", "cli": "CLI"}
    return " ".join(
        special.get(part.lower(), part.capitalize())
        for part in slug.replace("_", "-").split("-")
    )


if __name__ == "__main__":
    main()
