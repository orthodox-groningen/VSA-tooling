from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
CONTENT_ROOT = ROOT / "examples" / "hugo-demo" / "content-source"

NAV_TYPES = ("HOME", "UP", "SIBLINGS", "CHILDREN", "PAGES")
MARKER_RE = re.compile(r"<!-- VSA-NAV:(HOME|UP|SIBLINGS|CHILDREN|PAGES) -->")
GENERATED_RE = re.compile(
    r"\n*<!-- VSA-NAV-GENERATED:(HOME|UP|SIBLINGS|CHILDREN|PAGES)-START -->"
    r".*?"
    r"<!-- VSA-NAV-GENERATED:\1-END -->\n*",
    re.DOTALL,
)


def main() -> None:
    if not CONTENT_ROOT.exists():
        print(f"Niet gevonden: {CONTENT_ROOT}")
        raise SystemExit(1)

    changed = []

    for path in sorted(CONTENT_ROOT.rglob("*.md")):
        original = path.read_text(encoding="utf-8")
        text = update_placeholders(path, original)

        if text != original:
            path.write_text(text.rstrip() + "\n", encoding="utf-8")
            changed.append(path)

    print("Hugo navigatie-placeholders bijgewerkt.")
    if changed:
        for path in changed:
            print(f"- {path.relative_to(ROOT)}")
    else:
        print("Geen wijzigingen nodig.")


def update_placeholders(path: Path, text: str) -> str:
    # Oude gegenereerde inhoud wordt altijd verwijderd en daarna opnieuw opgebouwd.
    text = GENERATED_RE.sub("\n", text)

    lines = text.splitlines()
    out = []

    for line in lines:
        out.append(line)
        match = MARKER_RE.fullmatch(line.strip())
        if match:
            nav_type = match.group(1)
            out.append(render_generated_block(path, nav_type))

    return "\n".join(out) + "\n"


def render_generated_block(path: Path, nav_type: str) -> str:
    lines = [
        f"<!-- VSA-NAV-GENERATED:{nav_type}-START -->",
    ]

    items = navigation_items(path, nav_type)

    if items:
        for label, link in items:
            lines.append(f"- [{label}]({link})")
    else:
        lines.append(f"<!-- Geen items voor {nav_type}. -->")

    lines.append(f"<!-- VSA-NAV-GENERATED:{nav_type}-END -->")
    return "\n".join(lines)


def navigation_items(path: Path, nav_type: str) -> list[tuple[str, str]]:
    current_route = route_parts_for_path(path)
    current_dir = path.parent

    if nav_type == "HOME":
        if current_route == ():
            return []
        return [("Home", relative_url(current_route, ()))]

    if nav_type == "UP":
        if current_route == ():
            return []
        return [("Omhoog", relative_url(current_route, current_route[:-1]))]

    if nav_type == "SIBLINGS":
        return sibling_items(path, current_route, current_dir)

    if nav_type == "CHILDREN":
        return child_section_items(current_route, current_dir)

    if nav_type == "PAGES":
        return child_page_items(path, current_route, current_dir)

    return []


def sibling_items(path: Path, current_route: tuple[str, ...], current_dir: Path) -> list[tuple[str, str]]:
    if current_dir == CONTENT_ROOT:
        return []

    parent_dir = current_dir.parent
    items: list[tuple[str, str]] = []

    for child in sorted(parent_dir.iterdir(), key=lambda p: p.name.lower()):
        if not child.is_dir() or child == current_dir or child.name.startswith("."):
            continue
        index = child / "_index.md"
        if index.exists() and not is_nav_excluded(index):
            target = route_parts_for_directory(child)
            items.append((page_title(index), relative_url(current_route, target)))

    sibling_section_names = {
        child.name.lower()
        for child in parent_dir.iterdir()
        if child.is_dir() and (child / "_index.md").exists()
    }

    for sibling in sorted(parent_dir.glob("*.md"), key=lambda p: p.name.lower()):
        if sibling.name.lower() == "_index.md" or sibling == path:
            continue
        if is_nav_excluded(sibling):
            continue
        if sibling.stem.lower() in sibling_section_names:
            # Vermijd dubbele navigatie wanneer zowel cli.md als cli/_index.md bestaan.
            continue
        target = route_parts_for_path(sibling)
        items.append((page_title(sibling), relative_url(current_route, target)))

    return dedupe_items(items)


def child_section_items(current_route: tuple[str, ...], current_dir: Path) -> list[tuple[str, str]]:
    items: list[tuple[str, str]] = []

    for child in sorted(current_dir.iterdir(), key=lambda p: p.name.lower()):
        if not child.is_dir() or child.name.startswith("."):
            continue
        index = child / "_index.md"
        if index.exists() and not is_nav_excluded(index):
            target = route_parts_for_directory(child)
            items.append((page_title(index), relative_url(current_route, target)))

    return dedupe_items(items)


def child_page_items(path: Path, current_route: tuple[str, ...], current_dir: Path) -> list[tuple[str, str]]:
    items: list[tuple[str, str]] = []
    child_section_names = {
        child.name.lower()
        for child in current_dir.iterdir()
        if child.is_dir() and (child / "_index.md").exists()
    }

    for page in sorted(current_dir.glob("*.md"), key=lambda p: p.name.lower()):
        if page.name.lower() == "_index.md" or page == path:
            continue
        if is_nav_excluded(page):
            continue
        if page.stem.lower() in child_section_names:
            continue
        target = route_parts_for_path(page)
        items.append((page_title(page), relative_url(current_route, target)))

    return dedupe_items(items)


def route_parts_for_directory(directory: Path) -> tuple[str, ...]:
    return tuple(directory.relative_to(CONTENT_ROOT).parts)


def route_parts_for_path(path: Path) -> tuple[str, ...]:
    rel = path.relative_to(CONTENT_ROOT)

    if path.name.lower() == "_index.md":
        return tuple(rel.parent.parts)

    return tuple(rel.with_suffix("").parts)


def relative_url(from_route: tuple[str, ...], to_route: tuple[str, ...]) -> str:
    common = 0
    for a, b in zip(from_route, to_route):
        if a != b:
            break
        common += 1

    ups = [".."] * (len(from_route) - common)
    downs = list(to_route[common:])
    parts = ups + downs

    if not parts:
        return "./"

    return "/".join(parts) + "/"


def page_title(path: Path) -> str:
    data = frontmatter(path)

    if "title" in data and data["title"].strip():
        return data["title"].strip()

    text = path.read_text(encoding="utf-8")
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()

    return title_for_slug(path.stem)


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if not lines or lines[0].strip() != "---":
        return {}

    data: dict[str, str] = {}

    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")

    return data


def is_nav_excluded(path: Path) -> bool:
    data = frontmatter(path)
    value = data.get("vsa_nav_exclude", "").strip().lower()
    return value in {"true", "yes", "1", "ja"}


def title_for_slug(slug: str) -> str:
    special = {"vsa": "VSA", "svg": "SVG", "cli": "CLI"}
    return " ".join(
        special.get(part.lower(), part.capitalize())
        for part in slug.replace("_", "-").split("-")
    )


def dedupe_items(items: list[tuple[str, str]]) -> list[tuple[str, str]]:
    seen = set()
    result = []

    for item in items:
        key = item[1]
        if key in seen:
            continue
        seen.add(key)
        result.append(item)

    return result


if __name__ == "__main__":
    main()
