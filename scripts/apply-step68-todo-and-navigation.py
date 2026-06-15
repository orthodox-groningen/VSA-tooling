from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TODO = ROOT / "docs/todo.md"
CONTENT_ROOT = ROOT / "examples/hugo-demo/content-source"

START = "<!-- VSA-NAV-START -->"
END = "<!-- VSA-NAV-END -->"


TODO_BLOCK = """
### 4.6 Woord-georiënteerde SVG-layout

Status: `Later`

De huidige SVG-renderer werkt met losse render-units:

- vrije tekst;
- zangelementen/scopes;
- pitchmarkers;
- whitespace.

Dat is inmiddels bruikbaar, maar bij woorden die uit meerdere tekst- en scopefragmenten bestaan,
blijven kleine kieren zichtbaar. Voorbeelden:

- `me{\\\\de}{/eeu_}wi{\\ge}`;
- `eerstge{/bo_}re{\\ne_}`;
- `ge{\\ble_}{\\ven_}`;
- `{/ge}{/&/o}pen{baard_}`;
- `schon...ken` met filler.

Waarschijnlijk vraagt dit om een aparte woord-georiënteerde layoutfase:

```text
bronsegmenten → woordcluster → tekst als geheel meten → glyphs per segment positioneren
```

Dat is geen kleine tuningstap maar een grotere rendererarchitectuurstap.

Voor nu is de huidige rendering voldoende bruikbaar; dit punt later opnieuw oppakken.
"""


def main() -> None:
    update_todo()
    update_navigation()
    print("Stap 68 toegepast.")


def update_todo() -> None:
    TODO.parent.mkdir(parents=True, exist_ok=True)

    if TODO.exists():
        text = TODO.read_text(encoding="utf-8")
    else:
        text = "# TODO lijst\n"

    if "Woord-georiënteerde SVG-layout" not in text:
        if "## 4. SVG-rendering" in text:
            text = text.replace("## 5. CLI professionaliseren", TODO_BLOCK + "\n## 5. CLI professionaliseren")
        else:
            text = text.rstrip() + "\n\n## SVG-rendering\n\n" + TODO_BLOCK

    TODO.write_text(text.rstrip() + "\n", encoding="utf-8")


def update_navigation() -> None:
    if not CONTENT_ROOT.exists():
        print(f"Niet gevonden: {CONTENT_ROOT}")
        return

    pages = sorted(CONTENT_ROOT.rglob("*.md"))

    for page in pages:
        if page.name.lower() == "_index.md":
            continue

        text = page.read_text(encoding="utf-8")
        nav = build_nav_block(page, pages)

        if START in text and END in text:
            before = text.split(START, 1)[0].rstrip()
            after = text.split(END, 1)[1].lstrip()
            text = before + "\n\n" + nav + "\n\n" + after
        else:
            text = insert_after_first_heading(text, nav)

        page.write_text(text.rstrip() + "\n", encoding="utf-8")


def build_nav_block(page: Path, all_pages: list[Path]) -> str:
    siblings = [
        other for other in all_pages
        if other.parent == page.parent and other != page and other.name.lower() != "_index.md"
    ]

    sibling_lines = []
    for sibling in sorted(siblings):
        title = page_title(sibling)
        rel = relative_link(page, sibling)
        sibling_lines.append(f"- [{title}]({rel})")

    parent = parent_link(page)

    lines = [
        START,
        "## Navigatie",
        "",
        f"- [Home]({relative_to_home(page)})",
    ]

    if parent:
        lines.append(f"- [Omhoog]({parent})")

    if sibling_lines:
        lines.append("- Zelfde map:")
        lines.extend(f"  {line}" for line in sibling_lines)

    lines.append(END)

    return "\n".join(lines)


def insert_after_first_heading(text: str, nav: str) -> str:
    lines = text.splitlines()

    # Houd YAML-frontmatter aan het begin ongemoeid en plaats navigatie na eerste H1.
    in_frontmatter = False
    if lines and lines[0].strip() == "---":
        in_frontmatter = True

    for index, line in enumerate(lines):
        if in_frontmatter and index > 0 and line.strip() == "---":
            in_frontmatter = False
            continue

        if not in_frontmatter and line.startswith("# "):
            return "\n".join(lines[: index + 1]) + "\n\n" + nav + "\n\n" + "\n".join(lines[index + 1 :])

    return nav + "\n\n" + text


def page_title(path: Path) -> str:
    text = path.read_text(encoding="utf-8")

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("title:"):
            return stripped.split(":", 1)[1].strip().strip('"')

    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()

    return path.stem.replace("-", " ").title()


def parent_link(page: Path) -> str | None:
    parent = page.parent

    if parent == CONTENT_ROOT:
        return None

    index_page = parent / "_index.md"
    if index_page.exists():
        return "./"

    return "../"


def relative_to_home(page: Path) -> str:
    depth = len(page.parent.relative_to(CONTENT_ROOT).parts)
    if depth == 0:
        return "./"
    return "../" * depth


def relative_link(from_page: Path, to_page: Path) -> str:
    # Voor Hugo pretty URLs: sibling pagina x.md staat op ./x/
    if from_page.parent == to_page.parent:
        return f"../{to_page.stem}/" if from_page.stem == "index" else f"./{to_page.stem}/"

    rel = to_page.relative_to(from_page.parent)
    return str(rel.with_suffix("")).replace("\\", "/") + "/"


if __name__ == "__main__":
    main()
