# 074 — Stap 30 - static assets fix

## Huidige locatie

```text
docs/architecture/parser-stap-30-static-assets-fix.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

De demo-site toonde wel tekst en invoer, maar geen SVG-plaatjes. Oorzaak: <img src="/vsa/voorbeeld.svg"> verwijst naar een URL onder Hugo static output. Maar de SVG-bestanden stonden niet in: examples/hugo-demo/static/vsa Daardoor kopieerde Hugo ze niet mee naar de site. De scripts schrijven SVG's nu naar:

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
