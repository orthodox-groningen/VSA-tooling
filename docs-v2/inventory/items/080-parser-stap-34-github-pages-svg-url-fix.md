# 080 — Stap 34 - GitHub Pages SVG URL fix

## Huidige locatie

```text
docs/architecture/parser-stap-34-github-pages-svg-url-fix.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Op GitHub Pages stond de site onder: /VSA-tooling/ maar SVG's werden geladen vanaf: /vsa/... Dat gaf 404. De shortcode normaliseert nu: {{ $src = replaceRE "^/" "" $src }} en gebruikt daarna: {{ $src | relURL }} Daarmee wordt: /vsa/voorbeeld.svg correct: /VSA-tooling/vsa/voorbeeld.svg bij publicatie onder GitHub Pages.

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
