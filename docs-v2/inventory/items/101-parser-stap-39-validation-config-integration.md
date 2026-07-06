# 101 — Stap 39 - validation config integration

## Huidige locatie

```text
docs/architecture/parser-stap-39-validation-config-integration.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze stap sluit severity-overrides aan op de validatielaag. config = load_config("vsa.toml") validate_file("bestand.vsa", config=config) validate_path("map", config=config) [validation.severity] VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER = "warning" Zonder config: semantic diagnostics = error Met override:

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
