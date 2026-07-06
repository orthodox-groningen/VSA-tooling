# 141 — Stap 59 - inspect Hugo SVG usage

## Huidige locatie

```text
docs/architecture/parser-stap-59-inspect-hugo-svg-usage.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Uit `findstr` bleek dat de SVG voor tropaar toon 8 al meerdere renderregels bevat. Daarmee lijkt de renderer zelf bron-newlines te respecteren. Het resterende probleem zit vermoedelijk in: - welke SVG de HTML-pagina toont; - browsercache; - CSS-scaling; - img/object/embed gebruik; - oude assets die nog in `public` staan;

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
