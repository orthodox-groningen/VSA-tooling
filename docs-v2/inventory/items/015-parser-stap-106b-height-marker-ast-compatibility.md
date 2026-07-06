# 015 — Stap 106b - HeightMarker/PitchMarker AST-compatibiliteit

## Huidige locatie

```text
docs/architecture/parser-stap-106b-height-marker-ast-compatibility.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze stap legt expliciet vast dat `HeightMarkerNode` voorlopig een alias blijft van `PitchMarkerNode`. Een echte aparte `HeightMarkerNode` brak bestaande onderdelen: - parserregressies; - SVG-layout; - SVG-rendering; - bestaande AST-serialisatie. Daarom blijft de runtime-compatibiliteit voorlopig: HeightMarkerNode is PitchMarkerNode

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
