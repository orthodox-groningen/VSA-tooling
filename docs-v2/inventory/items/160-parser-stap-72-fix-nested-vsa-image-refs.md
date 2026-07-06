# 160 — Stap 72 - fix nested VSA image refs

## Huidige locatie

```text
docs/architecture/parser-stap-72-fix-nested-vsa-image-refs.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Bij pagina's in subdirectories werd soms naar een verkeerde SVG verwezen. Voorbeeld: content-source\praktijk\weekdagen\woensdag.md moet verwijzen naar: /vsa/voorbeelden-praktijk-weekdagen-woensdag-block-1.svg Toegevoegd: python scripts\repair-vsa-image-refs.py Dit script herleidt de SVG naam uit het volledige relatieve pagina-pad.

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
