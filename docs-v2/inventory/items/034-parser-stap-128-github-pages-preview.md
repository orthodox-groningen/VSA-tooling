# 034 — Stap 128 - automatische GitHub Pages preview

## Huidige locatie

```text
docs/architecture/parser-stap-128-github-pages-preview.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Bij elke commit wordt automatisch een preview-site gebouwd en gepubliceerd onder: https://orthodox-groningen.github.io/preview/ Productie blijft handmatig. De workflow `.github/workflows/pages-preview.yml`: 1. draait tests; 2. valideert VSA-content; 3. genereert Hugo-content en SVG; 4. bouwt Hugo met `baseURL` op `/preview/`;

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
