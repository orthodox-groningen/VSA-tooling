# 184 — Stap 94 - bracket-directive contract

## Huidige locatie

```text
docs/architecture/parser-stap-94-bracket-directive-contract.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Voor hoogte-markeringen gebruiken we de bestaande bracketvorm: [<EHM>:] Dit wordt gezien als een gespecialiseerde bracket-directive. De parser moet het einde van de directive zien als één eindtoken: :] Dus niet als twee losse syntaxelementen: : ] Hierdoor kan later extra syntax tussen `[` en `:]` worden toegevoegd zonder dat de parser hoeft te raden of `:` en `]` apart bedoeld zijn.

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
