# 073 — Stap 30 - Hugo home/section layout fix

## Huidige locatie

```text
docs/architecture/parser-stap-30-hugo-home-section-fix.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Hugo had wel `single.html`, maar geen layouts voor: home section Daardoor werden wel pagina's zoals: /voorbeelden/basis/ gebouwd, maar niet: / en niet: /voorbeelden/ Deze patch voegt toe: layouts/_default/home.html layouts/_default/list.html

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
