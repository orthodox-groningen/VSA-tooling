# 072 — Stap 30 - documentatietest fix

## Huidige locatie

```text
docs/architecture/parser-stap-30-doc-test-fix.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

De demo-site tests waren groen, maar `test_user_docs.py` faalde op twee te specifieke tekstverwachtingen. De tests zijn nu minder kwetsbaar: - ze controleren nog steeds of `<assets-dir>` goed wordt uitgelegd; - ze controleren nog steeds of validatiechecks worden uitgelegd; - ze eisen niet meer één exacte hoofdlettergevoelige formulering.

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
