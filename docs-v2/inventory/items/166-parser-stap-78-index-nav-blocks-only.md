# 166 — Stap 78 - alleen navigatieblokken in `_index.md`

## Huidige locatie

```text
docs/architecture/parser-stap-78-index-nav-blocks-only.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

`_index.md` pagina's zijn redactionele content. Buildscripts mogen daarom niet de volledige `_index.md` overschrijven. Alleen een expliciet afgebakend navigatieblok: <!-- VSA-INDEX-NAV-START --> ... <!-- VSA-INDEX-NAV-END --> mag automatisch worden bijgewerkt. python scripts\update-index-navigation-blocks.py

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
