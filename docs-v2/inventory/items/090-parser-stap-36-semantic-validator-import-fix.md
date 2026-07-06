# 090 — Stap 36 - semantic validator import fix

## Huidige locatie

```text
docs/architecture/parser-stap-36-semantic-validator-import-fix.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

De vorige stap introduceerde: from .ast import DocumentNode, PitchMarkerNode, ScopeNode Maar `DocumentNode` bestaat niet in deze repo. De validator gebruikt nu geen directe AST-class imports meer. In plaats daarvan kijkt hij naar: type(node).__name__ en naar bestaande node-eigenschappen zoals: height_modifier

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
