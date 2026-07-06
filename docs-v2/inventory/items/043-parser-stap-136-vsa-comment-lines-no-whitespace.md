# 043 — Stap 136 - comment-only regels zonder extra whitespace

## Huidige locatie

```text
docs/architecture/parser-stap-136-vsa-comment-lines-no-whitespace.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

HTML-commentaar binnen `::: vsa-notatie` werd genegeerd, maar een commentaarregel kon nog als lege regel doorwerken in afgeleide artefacten. Voorbeeld: <!-- Liturgikon, 270 --> moet geen extra verticale ruimte in SVG veroorzaken. - Commentaar dat een hele regel inneemt verdwijnt inclusief de regelafbreking.

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
