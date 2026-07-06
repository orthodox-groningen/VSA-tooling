# 048 — Stap 16 - SVG autosizing

## Huidige locatie

```text
docs/architecture/parser-stap-16-svg-autosize.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze stap verwijdert de vaste SVG-breedte van `1200px`. De breedte wordt nu berekend op basis van: linkermarge + breedte van TextNodes + breedte van ScopeNodes + breedte van PitchMarkerNodes + rechtermarge De SVG krijgt ook een `viewBox`. Voor Hugo en Markdown is een vaste breedte onhandig. Een korte regel zoals:

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
