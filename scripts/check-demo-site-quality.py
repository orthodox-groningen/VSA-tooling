from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag, urlparse

PROJECT_PREFIX = "/VSA-tooling/"
PREVIEW_PREFIX = "/VSA-tooling/preview/"
FORBIDDEN_ROOT_PREFIXES = ("/preview/", "/voorbeelden/", "/praktijk/", "/zondag/")


class LinkExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refs: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        values = dict(attrs)
        for attr in ("href", "src"):
            value = values.get(attr)
            if value:
                self.refs.append((attr, value))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Controleer gebouwde Hugo demo-site.")
    parser.add_argument("--site-dir", default="examples/hugo-demo/public")
    parser.add_argument("--mode", choices=("preview", "production"), default="preview")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    site_dir = Path(args.site_dir)
    errors: list[str] = []

    if not site_dir.exists():
        print(f"Niet gevonden: {site_dir}")
        print("Draai eerst scripts\\build-hugo.cmd of de GitHub Pages workflow.")
        return 2

    html_files = sorted(site_dir.rglob("*.html"))
    if not (site_dir / "index.html").exists():
        errors.append(f"Ontbreekt: {site_dir / 'index.html'}")
    if not html_files:
        errors.append(f"Geen HTML-bestanden gevonden in {site_dir}")

    expected_prefix = PREVIEW_PREFIX if args.mode == "preview" else PROJECT_PREFIX

    for html_file in html_files:
        text = html_file.read_text(encoding="utf-8", errors="replace")

        if args.mode == "preview" and ('href="/preview/' in text or 'src="/preview/' in text):
            errors.append(f"{html_file}: root-preview link gevonden; verwacht {PREVIEW_PREFIX}")

        if args.mode == "production" and ('href="/preview/' in text or 'src="/preview/' in text):
            errors.append(f"{html_file}: preview-link gevonden in productie-output")

        for forbidden in FORBIDDEN_ROOT_PREFIXES:
            if f'href="{forbidden}' in text or f'src="{forbidden}' in text:
                errors.append(f"{html_file}: root-link gevonden {forbidden}; verwacht project-site prefix")

        parser = LinkExtractor()
        parser.feed(text)
        for attr, ref in parser.refs:
            check_ref(errors, site_dir, html_file, attr, ref, expected_prefix)

    if errors:
        print("Demo-site kwaliteitscontrole: fouten gevonden")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Demo-site kwaliteitscontrole: OK ({len(html_files)} HTML-bestand(en) gecontroleerd, mode={args.mode}).")
    return 0


def check_ref(errors: list[str], site_dir: Path, html_file: Path, attr: str, ref: str, expected_prefix: str) -> None:
    if ref.startswith(("http://", "https://", "mailto:", "tel:", "#")):
        return

    parsed = urlparse(ref)
    if parsed.scheme:
        return

    path_ref, _fragment = urldefrag(ref)
    if not path_ref:
        return

    if path_ref.startswith("/"):
        if not path_ref.startswith(expected_prefix):
            errors.append(f"{html_file}: {attr}='{ref}' mist verwachte prefix {expected_prefix}")
            return
        target = site_dir / path_ref[len(expected_prefix):]
    else:
        target = html_file.parent / path_ref

    if path_ref.endswith("/") or ref.endswith("/"):
        target = target / "index.html"
    if target.is_dir():
        target = target / "index.html"
    if not target.exists():
        errors.append(f"{html_file}: {attr}='{ref}' verwijst naar ontbrekend bestand {target}")


if __name__ == "__main__":
    raise SystemExit(main())
