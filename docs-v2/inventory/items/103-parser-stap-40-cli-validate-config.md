# 103 — Stap 40 - CLI validate gebruikt severity-config

## Huidige locatie

```text
docs/architecture/parser-stap-40-cli-validate-config.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze stap sluit de validatieconfig aan op de CLI. vsa validate bestand.vsa --config vsa.toml [validation.severity] VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER = "warning" Zonder config: semantische diagnostic = error exitcode = 1 Met config: specifieke semantische diagnostic = warning exitcode = 0 Syntax-errors blijven altijd fatal.

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
