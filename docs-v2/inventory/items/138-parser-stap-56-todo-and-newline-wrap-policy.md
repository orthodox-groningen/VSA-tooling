# 138 — Stap 56 - TODO en newline wrap policy

## Huidige locatie

```text
docs/architecture/parser-stap-56-todo-and-newline-wrap-policy.md
```

## Documenttype

TODO / open punten

## Doelgroep

maintainer

## Inhoudelijke samenvatting

Deze stap voegt `docs/todo.md` toe en corrigeert de SVG-layoutpolicy. Wel: - CR; - LF; - CRLF; - bron-newline als harde regelgrens. Niet: - `[/]`; - `[*]`; - `[/?]`; - `[*?]`. Die tokens vragen eerst om bracket-token dispatch in de parser.

## Relaties met andere documenten

Nog te detailleren tijdens inhoudelijke consolidatie.

## Overlap met andere documenten

Nog te detailleren tijdens inhoudelijke consolidatie.

## Voorgestelde bestemming

```text
docs-v2/inventory/open-points.md of latere TODO-consolidatie
```

## Inventarisatiestatus

Eerste classificatie op basis van bestandsnaam, locatie en documentkop.

## Opmerkingen

Geen inhoud migreren in fase 1; alleen classificeren en later controleren.
