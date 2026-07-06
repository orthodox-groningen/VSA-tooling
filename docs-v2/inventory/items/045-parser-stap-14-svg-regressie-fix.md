# 045 — Stap 14 fix - SVG regressietests robuuster

## Huidige locatie

```text
docs/architecture/parser-stap-14-svg-regressie-fix.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

De eerste SVG-regressietest vergeleek de volledige SVG exact. Dat is te vroeg, omdat de renderer-layout nog verandert. Daarom gebruiken we voorlopig metadata: { "contains_text": ["Hei", "lig"], "min_lines": 4, "min_circles": 0 } Later, zodra de layout stabiel is, kunnen we weer exacte `expected.svg` regressies afdwingen.

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
