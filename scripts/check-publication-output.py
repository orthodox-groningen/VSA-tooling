from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag, urlparse

# Absolute paden naar andere org-Pages op hetzelfde github.io-host
# (TEv2 localize maakt https://…/bron/terms/… → /bron/terms/…).
_EXTERNAL_SITE_PREFIXES = (
    "/bron/",
)


class RefCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refs: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        values = dict(attrs)
        for attr in ("href", "src"):
            value = values.get(attr)
            if value:
                self.refs.append((attr, value))


def main() -> int:
    args = parse_args()
    site_dir = Path(args.site_dir)
    url_prefix = _normalize_prefix(args.url_prefix)

    errors: list[str] = []

    if not site_dir.exists():
        errors.append(f"site-dir bestaat niet: {site_dir}")
    elif not (site_dir / "index.html").exists():
        errors.append(f"index.html ontbreekt in: {site_dir}")

    if errors:
        return _report(errors)

    html_files = sorted(site_dir.rglob("*.html"))
    if not html_files:
        errors.append(f"geen HTML-bestanden gevonden in: {site_dir}")
        return _report(errors)

    for html_file in html_files:
        text = html_file.read_text(encoding="utf-8", errors="replace")

        if "This page contains the following errors:" in text:
            errors.append(f"{html_file}: browser/XML-fouttekst gevonden")

        if "<!-- plain-text:" in text:
            errors.append(f"{html_file}: oude plain-text SVG metadata-comment gevonden")

        parser = RefCollector()
        parser.feed(text)

        for attr, ref in parser.refs:
            _check_ref(errors, site_dir, html_file, attr, ref, url_prefix)

    return _report(errors, ok_message=f"Publicatiecontrole OK: {len(html_files)} HTML-bestand(en).")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Controleer gebouwde publicatie-output.")
    parser.add_argument("--site-dir", required=True)
    parser.add_argument(
        "--url-prefix",
        required=True,
        help="Publiek URL-pad waaronder de site draait, bv. /VSA-tooling/preview/",
    )
    return parser.parse_args()


def _normalize_prefix(prefix: str) -> str:
    if not prefix.startswith("/"):
        prefix = "/" + prefix
    if not prefix.endswith("/"):
        prefix += "/"
    return prefix


def _is_external_site_path(path_ref: str) -> bool:
    """True for root-relative links to another org Pages site (e.g. /bron/…)."""
    return any(path_ref == p.rstrip("/") or path_ref.startswith(p) for p in _EXTERNAL_SITE_PREFIXES)


def _check_ref(
    errors: list[str],
    site_dir: Path,
    html_file: Path,
    attr: str,
    ref: str,
    url_prefix: str,
) -> None:
    if ref.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
        return

    parsed = urlparse(ref)
    if parsed.scheme:
        return

    path_ref, _fragment = urldefrag(ref)
    if not path_ref:
        return

    if path_ref.startswith("/"):
        if _is_external_site_path(path_ref):
            return
        if not path_ref.startswith(url_prefix):
            errors.append(
                f"{html_file}: {attr}='{ref}' mist URL-prefix {url_prefix}"
            )
            return
        local = path_ref[len(url_prefix):]
        target = site_dir / local
    else:
        target = html_file.parent / path_ref

    if path_ref.endswith("/") or ref.endswith("/"):
        target = target / "index.html"
    if target.is_dir():
        target = target / "index.html"

    if not target.exists():
        errors.append(
            f"{html_file}: {attr}='{ref}' verwijst naar ontbrekend bestand {target}"
        )


def _report(errors: list[str], ok_message: str = "Publicatiecontrole OK.") -> int:
    if errors:
        print("Publicatiecontrole: fouten gevonden")
        for error in errors:
            print(f"- {error}")
        return 1

    print(ok_message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
