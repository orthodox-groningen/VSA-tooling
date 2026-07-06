# 097 — Stap 38 - config output-mode regressiefix

## Huidige locatie

```text
docs/architecture/parser-stap-38-config-output-mode-regression-fix.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Stap 38 verving `config.py` en verloor daardoor bestaande validatie op: [hugo] output-mode = "..." Deze patch herstelt: img shortcode als enige geldige waarden. Onbekende waarden geven weer: ValueError

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
