# 092 — Stap 36 - validator pitch-marker eindcontrole

## Huidige locatie

```text
docs/architecture/parser-stap-36-validator-pitch-ending.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze oorspronkelijke stap is **verouderd**. De foutcode `VSA-SEMANTIC-MISSING-FINAL-PITCH-MARKER` is obsolete: het ontbreken van een eindmarkering is syntactisch én semantisch toegestaan. De foutcode `VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER` is eveneens obsolete voor `[:]`: een lege hoogte-markering betekent een neutrale hoogte en is semantisch gelijkwaardig aan `[-:]` c.q. `[~:]`.

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
