# 165 — Stap 77 - path normalization fix

## Huidige locatie

```text
docs/architecture/parser-stap-77-path-normalization-fix.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

`regenerate-missing-vsa-images.py` werkte goed vanuit de echte build, maar de tests gaven relatieve paden door. Fix: html = normalize_path(html) rel = html.relative_to(PUBLIC.resolve()) Daarmee werken relatieve én absolute paden.

## Relaties met andere documenten

Nog te detailleren tijdens inhoudelijke consolidatie.

## Overlap met andere documenten

Nog te detailleren tijdens inhoudelijke consolidatie.

## Voorgestelde bestemming

```text
docs-v2/history/parser/
```

## Inventarisatiestatus

Eerste classificatie op basis van bestandsnaam, locatie en documentkop.

## Opmerkingen

Geen inhoud migreren in fase 1; alleen classificeren en later controleren.
