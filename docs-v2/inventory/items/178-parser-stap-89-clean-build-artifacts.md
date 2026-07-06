# 178 — Stap 89 - clean build artifacts

## Huidige locatie

```text
docs/architecture/parser-stap-89-clean-build-artifacts.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Oude routes bleven verschijnen doordat generated output niet volledig werd opgeschoond vóór een nieuwe Hugo-build. Daarnaast was `build-hugo.cmd` kwetsbaar voor patchscripts die regels midden in een `hugo ^` blok invoegden. `build-hugo.cmd` is opnieuw compact gemaakt en gebruikt nu: python scripts\clean-hugo-build-artifacts.py

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
