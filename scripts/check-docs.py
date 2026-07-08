from __future__ import annotations

import hashlib
import os
import re
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REPORTS = DOCS / "reports"
REPORTS.mkdir(parents=True, exist_ok=True)

EXTERNAL_SCHEMES = ("http://", "https://", "mailto:", "tel:")
LINK_RE = re.compile(r"(?<!!)(?:\[[^\]]*\]\(([^)]+)\))")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def md_files() -> list[Path]:
    return sorted(DOCS.rglob("*.md"))


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")


def slugify_heading(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE).strip().lower()
    text = re.sub(r"\s+", "-", text)
    return text


def anchors_for(p: Path) -> set[str]:
    anchors = set()
    for _, title in HEADING_RE.findall(read(p)):
        anchors.add(slugify_heading(title))
    return anchors


def split_link(raw: str) -> tuple[str, str]:
    raw = raw.strip().strip('"').strip("'")
    if "#" in raw:
        path, anchor = raw.split("#", 1)
        return unquote(path), unquote(anchor)
    return unquote(raw), ""


def iter_links(p: Path):
    text = FENCE_RE.sub("", read(p))
    for m in LINK_RE.finditer(text):
        target = m.group(1).strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        yield target


def write_report(name: str, title: str, body: str) -> None:
    (REPORTS / name).write_text(f"# {title}\n\n{body.rstrip()}\n", encoding="utf-8")


def table(headers: list[str], rows: list[list[str]]) -> str:
    column_count = len(headers)
    normalized_rows = []
    for row in rows:
        cells = [str(c).replace("\n", "<br>") for c in row]
        if len(cells) < column_count:
            cells += [""] * (column_count - len(cells))
        elif len(cells) > column_count:
            cells = cells[:column_count - 1] + ["; ".join(cells[column_count - 1:])]
        normalized_rows.append(cells)

    widths = [len(h) for h in headers]
    for row in normalized_rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))

    out = []
    out.append("| " + " | ".join(headers[i].ljust(widths[i]) for i in range(column_count)) + " |")
    out.append("| " + " | ".join("-" * widths[i] for i in range(column_count)) + " |")
    for row in normalized_rows:
        out.append("| " + " | ".join(row[i].ljust(widths[i]) for i in range(column_count)) + " |")
    return "\n".join(out)


def check_links(files: list[Path]) -> dict:
    problems = []
    inbound = defaultdict(set)
    anchors_cache = {}

    for p in files:
        for raw in iter_links(p):
            target, anchor = split_link(raw)
            if not target and anchor:
                dest = p
            elif target.startswith(EXTERNAL_SCHEMES) or target.startswith("#") and not target.startswith("##"):
                continue
            elif target.startswith("/"):
                dest = ROOT / target.lstrip("/")
            else:
                dest = (p.parent / target).resolve()

            if target.startswith(EXTERNAL_SCHEMES):
                continue
            if raw.startswith("#"):
                dest = p
                anchor = raw[1:]

            if not dest.exists():
                problems.append([rel(p), raw, "Doelbestand bestaat niet"])
                continue
            if dest.is_dir():
                dest = dest / "README.md"
                if not dest.exists():
                    problems.append([rel(p), raw, "Doelmap heeft geen README.md"])
                    continue
            if dest.suffix.lower() == ".md":
                inbound[dest].add(p)
                if anchor:
                    anchors_cache.setdefault(dest, anchors_for(dest))
                    if anchor and anchor not in anchors_cache[dest]:
                        problems.append([rel(p), raw, "Anchor bestaat mogelijk niet"])

    body = "Geen problemen gevonden." if not problems else table(["Bron", "Link", "Probleem"], problems)
    write_report("link-check.md", "Linkcontrole", body)
    return {"link_problems": len(problems), "inbound": inbound}


def check_readmes() -> dict:
    rows = []
    for d in sorted([p for p in DOCS.rglob("*") if p.is_dir()] + [DOCS]):
        if d.name == ".git":
            continue
        if not (d / "README.md").exists():
            rows.append([rel(d), "README.md ontbreekt"])
    body = "Geen ontbrekende README-bestanden gevonden." if not rows else table(["Map", "Probleem"], rows)
    write_report("readme-check.md", "README-controle", body)
    return {"missing_readmes": len(rows)}


def normalize(text: str) -> str:
    text = FENCE_RE.sub("", text).lower()
    text = re.sub(r"[^a-z0-9а-яёà-ÿ]+", " ", text, flags=re.UNICODE)
    return re.sub(r"\s+", " ", text).strip()


def check_duplicates(files: list[Path]) -> dict:
    hashes = defaultdict(list)
    token_sets = {}
    for p in files:
        n = normalize(read(p))
        tokens = set(n.split())
        token_sets[p] = tokens
        if len(n) > 80:
            hashes[hashlib.sha256(n.encode()).hexdigest()].append(p)

    exact_rows = []
    for group in hashes.values():
        if len(group) > 1:
            exact_rows.append([", ".join(rel(p) for p in group), "Exacte tekstduplicatie"])

    similar_rows = []
    candidates = [p for p in files if len(token_sets[p]) > 80]
    for i, a in enumerate(candidates):
        ta = token_sets[a]
        for b in candidates[i + 1:]:
            tb = token_sets[b]
            union = len(ta | tb)
            if not union:
                continue
            score = len(ta & tb) / union
            if score >= 0.72:
                similar_rows.append([rel(a), rel(b), f"{score:.2f}"])
                if len(similar_rows) >= 100:
                    break
        if len(similar_rows) >= 100:
            break

    parts = []
    parts.append("## Exacte duplicaten\n")
    parts.append("Geen exacte duplicaten gevonden." if not exact_rows else table(["Bestanden", "Probleem"], exact_rows))
    parts.append("\n## Verdachte overlap\n")
    parts.append("Geen sterke overlap gevonden." if not similar_rows else table(["Document A", "Document B", "Score"], similar_rows))
    write_report("duplicate-content.md", "Duplicaatcontrole", "\n".join(parts))
    return {"exact_duplicates": len(exact_rows), "similar_pairs": len(similar_rows)}

def check_orphans(files: list[Path], inbound: dict) -> dict:
    entry = {
        DOCS / "README.md",
        DOCS / "getting-started" / "README.md",
        DOCS / "guides" / "README.md",
        DOCS / "specification" / "README.md",
        DOCS / "architecture" / "README.md",
        DOCS / "reference" / "README.md",
        DOCS / "history" / "README.md",
        DOCS / "inventory" / "README.md",
    }
    rows = []
    for p in files:
        if p in entry or p.name == "README.md":
            continue
        if not inbound.get(p):
            rows.append([rel(p), "Geen inkomende markdown-link gevonden"])
    body = "Geen verweesde documenten gevonden." if not rows else table(["Document", "Opmerking"], rows)
    write_report("orphan-documents.md", "Verweesde documenten", body)
    return {"orphans": len(rows)}


def check_terminology(files: list[Path]) -> dict:
    """Check terminology without reporting pure casing differences.

    Terms such as AST/ast/Ast are matched case-insensitively and treated as the
    same term. Pure casing variation is intentionally silent; this report should
    only contain real terminology findings, such as TODO/TBD headings.
    """
    canonical_terms = ["VSA", "TEv2", "CLI", "AST", "JSON", "SVG", "Hugo", "Markdown", "EBNF"]
    rows = []

    # Case-insensitive inventory pass. This deliberately does not emit rows for
    # casing variants; the pass is kept so future synonym checks can reuse the
    # same normalized counts without reintroducing case-only findings.
    for p in files:
        text = read(p)
        normalized_counts = {}
        for term in canonical_terms:
            pattern = re.compile(re.escape(term), re.IGNORECASE)
            count = len(pattern.findall(text))
            if count:
                normalized_counts[term.lower()] = normalized_counts.get(term.lower(), 0) + count

        for _, h in HEADING_RE.findall(text):
            if "todo" in h.lower() or "tbd" in h.lower():
                rows.append([rel(p), "TODO/TBD in kop", h])

    body = (
        "Geen opvallende terminologieproblemen gevonden."
        if not rows
        else table(["Document", "Signaal", "Tekst"], rows[:200])
    )
    write_report("terminology-check.md", "Terminologiecontrole", body)
    return {"terminology_findings": len(rows)}


def check_empty(files: list[Path]) -> dict:
    rows = []
    for p in files:
        text = read(p).strip()
        if len(text) < 80:
            rows.append([rel(p), str(len(text))])
    body = "Geen lege of vrijwel lege documenten gevonden." if not rows else table(["Document", "Tekens"], rows)
    write_report("short-documents.md", "Lege of korte documenten", body)
    return {"short_docs": len(rows)}


def main() -> int:
    if not DOCS.exists():
        raise SystemExit("docs niet gevonden. Voer dit script uit vanuit de repository-root.")
    files = md_files()
    link = check_links(files)
    readmes = check_readmes()
    dup = check_duplicates(files)
    orphan = check_orphans(files, link["inbound"])
    term = check_terminology(files)
    short = check_empty(files)

    summary_rows = [
        ["Markdown-documenten", str(len(files)), "In scope"],
        ["Linkproblemen", str(link["link_problems"]), "Zie link-check.md"],
        ["Ontbrekende README's", str(readmes["missing_readmes"]), "Zie readme-check.md"],
        ["Exacte duplicaten", str(dup["exact_duplicates"]), "Zie duplicate-content.md"],
        ["Sterke overlap", str(dup["similar_pairs"]), "Zie duplicate-content.md"],
        ["Verweesde documenten", str(orphan["orphans"]), "Zie orphan-documents.md"],
        ["Terminologievondsten", str(term["terminology_findings"]), "Zie terminology-check.md"],
        ["Korte documenten", str(short["short_docs"]), "Zie short-documents.md"],
    ]
    write_report("phase3-review.md", "Fase-3 review", table(["Controle", "Aantal", "Rapport"], summary_rows))
    write_report("migration-status.md", "Migratiestatus", "Fase 3 is reviewbaar. Corrigeer eerst de bevindingen in de rapporten voordat `docs/` de nieuwe `docs/` wordt.")
    write_report("missing-content.md", "Mogelijk ontbrekende inhoud", "Deze automatische controle kan inhoudelijke volledigheid niet bewijzen. Gebruik dit rapport samen met `inventory/`, `migration/` en de oude `docs/` als handmatige eindcontrole.")
    print("Rapporten geschreven naar docs\\reports")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
