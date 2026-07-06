# 096 — Stap 37 - severity regressiefix

## Huidige locatie

```text
docs/architecture/parser-stap-37-severity-regression-fix.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze patch herstelt regressies na introductie van severity-levels. `has_errors()` blijft backward-compatible: zijn er diagnostics? Nieuwe methode: has_fatal_errors() betekent: zijn er diagnostics met severity error? `ValidationResult.ok` wordt alleen `False` bij echte errors. Warnings worden verzameld maar laten validatie slagen.

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
