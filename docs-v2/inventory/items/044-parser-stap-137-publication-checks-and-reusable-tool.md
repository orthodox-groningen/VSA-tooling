# 044 — Stap 137 - publicatiechecks en herbruikbare VSA-tool

## Huidige locatie

```text
docs/architecture/parser-stap-137-publication-checks-and-reusable-tool.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Twee zaken worden vastgelegd: 1. preview/productie-output wordt vóór deployment gecontroleerd; 2. andere repositories kunnen de VSA-rendering makkelijk gebruiken. Nieuw script: scripts/check-publication-output.py Controleert: - `index.html` bestaat; - interne `href`/`src` verwijzingen bestaan; - absolute paden gebruiken het juiste GitHub Pages projectpad;

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
