# 094 — Stap 37 - optie A: semantiek blijft error

## Huidige locatie

```text
docs/architecture/parser-stap-37-option-a-semantic-errors.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

We behouden de severity-infrastructuur, maar zetten semantische diagnostics voorlopig terug op `error`. De bestaande toolchain verwacht: semantische fout → validate faalt → process stopt Dat geldt voor: - `validate_path`; - `process_markdown`; - `ProcessValidationError`; - CI; - expected-fail tests. Diagnostics hebben nu wel een veld:

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
