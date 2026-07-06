# 182 — Stap 92 - parsercontract voor meerdere hoogte-markeringen

## Huidige locatie

```text
docs/architecture/parser-stap-92-height-marker-parser-contract.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Dit document legt vast wat de parser moet accepteren en afwijzen wanneer meerdere hoogte-markeringen worden ondersteund. Een constructie tussen `[` en `:]` wordt gezien als een bracket-directive. Het einde van zo'n directive is het samengestelde eindtoken: :] Dus de parser behandelt dit niet als twee losse tekens:

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
