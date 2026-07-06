# 059 — Stap 23 - Hugo workflow

## Huidige locatie

```text
docs/architecture/parser-stap-23-hugo-workflow.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze stap voegt een volledige workflow toe. scripts\serve-hugo.cmd scripts\build-hugo.cmd Workflow: .github/workflows/hugo.yml Pipeline: validate ↓ pytest ↓ vsa build-markdown ↓ hugo ↓ artifact/site content-source/ ↓ generated/hugo/content/ generated/hugo/static/vsa/ ↓ Hugo site

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
