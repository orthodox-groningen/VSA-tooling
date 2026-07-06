# 127 — Stap 50 - inline text-flow renderer

## Huidige locatie

```text
docs/architecture/parser-stap-50-inline-text-flow-renderer.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze stap verandert de SVG-rendering richting normale lopende tekst. - Spaties tellen weer mee in breedtemeting. - SVG-tekst gebruikt `xml:space="preserve"`. - Scopes krijgen standaard geen extra gap. - Glyphs worden overlays boven/onder de tekst. - Regels en marges zijn compacter. De renderer moet visueel lijken op:

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
