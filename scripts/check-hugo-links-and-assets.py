from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import sys
from typing import NamedTuple


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

try:
    from repo_root import find_repo_root
except Exception:
    def find_repo_root(start: Path | None = None) -> Path:
        current = (start or Path.cwd()).resolve()
        for candidate in [current, *current.parents]:
            if (candidate / "pyproject.toml").exists() and (
                candidate / "src" / "vsa"
            ).exists():
                return candidate
        return Path(__file__).resolve().parents[1]


ROOT = find_repo_root(Path(__file__).resolve())
PUBLIC = ROOT / "examples" / "hugo-demo" / "public"

FORBIDDEN_ROUTES = ["/zondag/", "/voorbeelden/praktijk/"]


class LinkRef(NamedTuple):
    html: Path
    attr: str
    value: str
    tag: str


class LinkParser(HTMLParser):
    def __init__(self, html: Path):
        super().__init__(convert_charrefs=True)
        self.html = html
        self.refs: list[LinkRef] = []

    def handle_starttag(self, tag: str, attrs):
        data = dict(attrs)

        for attr in ("href", "src"):
            value = data.get(attr)
            if value:
                self.refs.append(LinkRef(self.html, attr, value, tag))


def main() -> None:
    if not PUBLIC.exists():
        print(f"Niet gevonden: {PUBLIC}")
        print("Draai eerst scripts\\build-hugo.cmd")
        raise SystemExit(2)

    refs = collect_refs()
    broken: list[LinkRef] = []
    forbidden: list[LinkRef] = []

    for ref in refs:
        if should_skip(ref.value):
            continue

        if is_forbidden_route(ref.value):
            forbidden.append(ref)
        elif not resolves(ref):
            broken.append(ref)

    if broken or forbidden:
        print("Hugo link/asset checker: fouten gevonden.")

        if forbidden:
            print()
            print("Verboden/oude routes:")
            for ref in forbidden:
                print(format_ref(ref))

        if broken:
            print()
            print("Kapotte links/assets:")
            for ref in broken:
                print(format_ref(ref))
                suggestion = suggest(ref.value)
                if suggestion:
                    print(f"  mogelijk bedoeld: {suggestion}")

        raise SystemExit(1)

    print(f"Hugo link/asset checker: OK ({len(refs)} verwijzingen gecontroleerd).")


def collect_refs() -> list[LinkRef]:
    refs: list[LinkRef] = []

    for html in sorted(PUBLIC.rglob("*.html")):
        parser = LinkParser(html)
        parser.feed(html.read_text(encoding="utf-8", errors="ignore"))
        refs.extend(parser.refs)

    return refs


def should_skip(value: str) -> bool:
    value = value.strip()
    clean = strip_fragment_query(value)

    return (
        not value
        or value.startswith("#")
        or value.startswith("http://")
        or value.startswith("https://")
        or value.startswith("mailto:")
        or value.startswith("tel:")
        or value.startswith("data:")
        or value.startswith("javascript:")
        or clean == "/livereload.js"
    )


def strip_fragment_query(value: str) -> str:
    return value.split("#", 1)[0].split("?", 1)[0]


def is_forbidden_route(value: str) -> bool:
    clean = strip_fragment_query(value)
    return any(clean == route or clean.startswith(route) for route in FORBIDDEN_ROUTES)


def resolves(ref: LinkRef) -> bool:
    clean = strip_fragment_query(ref.value)

    if clean.startswith("/"):
        candidate = PUBLIC / clean.lstrip("/")
    else:
        candidate = (ref.html.parent / clean).resolve()

    try:
        candidate.relative_to(PUBLIC.resolve())
    except ValueError:
        return False

    if candidate.exists():
        return True

    if clean.endswith("/") or candidate.suffix == "":
        return (candidate / "index.html").exists()

    return False


def format_ref(ref: LinkRef) -> str:
    html = ref.html.relative_to(ROOT)
    return f"- {html}: <{ref.tag} {ref.attr}=\"{ref.value}\">"


def suggest(value: str) -> str | None:
    clean = Path(strip_fragment_query(value)).name

    if not clean:
        return None

    matches = list(PUBLIC.rglob(clean))
    if matches:
        return "/" + str(matches[0].relative_to(PUBLIC)).replace("\\", "/")

    return None


if __name__ == "__main__":
    main()
