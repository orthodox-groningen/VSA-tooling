# 172 — Stap 83 - stop muterende workflow-tests

## Huidige locatie

```text
docs/architecture/parser-stap-83-stop-mutating-workflow-tests.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

`build-hugo.cmd` draait de test-suite. Een aantal tests voerde apply-scripts uit die echte bestanden in de repo aanpassen. Dat is gevaarlijk, omdat een gewone test-run dan de working tree vervuilt. Voorbeeld: .github\workflows\*.yml kreeg bij herhaalde runs steeds extra lege regels. Tests mogen geen `apply-step*.py` scripts op de echte repo uitvoeren.

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
