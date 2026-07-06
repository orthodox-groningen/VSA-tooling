# 084 — Stap 34 - test en link fix

## Huidige locatie

```text
docs/architecture/parser-stap-34-test-en-link-fix.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze patch herstelt regressies door de subpad-veilige linkwijziging. Metadata werkt opnieuw voor: do="C4" mode="minor" en defaults via: effective_metadata() Tests verwachten niet langer root-absolute links zoals: /voorbeelden/basis/ maar controleren op subpad-veilige Hugo-oplossingen: relURL voorbeelden/basis/

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
