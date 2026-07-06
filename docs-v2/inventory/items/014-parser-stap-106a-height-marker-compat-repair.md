# 014 — Stap 106a - repair HeightMarker compatibiliteit

## Huidige locatie

```text
docs/architecture/parser-stap-106a-height-marker-compat-repair.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Een echte aparte `HeightMarkerNode` brak bestaande parser-, renderer- en SVG-tests. De huidige renderer en validator herkennen hoogte-markeringen nog via `PitchMarkerNode`. `HeightMarkerNode` blijft voorlopig een compatibele alias: HeightMarkerNode = PitchMarkerNode Een echte aparte class komt pas nadat renderer, validator en regressie-AST's gelijktijdig zijn gemigreerd.

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
