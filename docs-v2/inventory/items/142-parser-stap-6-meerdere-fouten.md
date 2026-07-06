# 142 — Parser stap 6 - meerdere fouten

## Huidige locatie

```text
docs/architecture/parser-stap-6-meerdere-fouten.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze stap maakt `vsa validate` geschikter voor echt gebruik. Voorbeeld: {} {te kst} tekst} {open leidt niet meer tot alleen de eerste fout, maar tot een lijst. RecoverableSyntaxValidator ↓ alle syntaxdiagnostics verzamelen ↓ alleen bij syntax OK: Parser ↓ SemanticValidator Semantische validatie kan meerdere fouten verzamelen zolang de AST geldig is.

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
