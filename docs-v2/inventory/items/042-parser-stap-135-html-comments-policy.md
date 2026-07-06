# 042 — Stap 135 - HTML-commentaar in VSA-notatie

## Huidige locatie

```text
docs/architecture/parser-stap-135-html-comments-policy.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

HTML-commentaar binnen VSA-notatie wordt broncommentaar. Commentaar van de vorm `<!-- ... -->` binnen VSA-notatie blijft in de oorspronkelijke bron staan, maar wordt genegeerd bij: - parsing; - syntaxvalidatie; - semantische validatie; - SVG-rendering; - afgeleide artefacten. Nieuwe helper: src/vsa/vsa_comments.py

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
