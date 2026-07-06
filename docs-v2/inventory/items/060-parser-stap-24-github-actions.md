# 060 — Stap 24 - GitHub Actions opschonen

## Huidige locatie

```text
docs/architecture/parser-stap-24-github-actions.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze stap splitst workflows. .github/workflows/vsa-ci.yml Draait op Windows: scripts\ci.cmd Doel: - Python package installeren; - tests draaien; - demo-content valideren; - demo Markdown/SVG genereren. .github/workflows/hugo-demo.yml Draait op Ubuntu: pytest vsa validate vsa build-markdown hugo build

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
