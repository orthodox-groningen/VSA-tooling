# 018 — Stap 109 - voorbereiding wraptoken dispatch

## Huidige locatie

```text
docs/architecture/parser-stap-109-wraptoken-dispatch.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

De parser gebruikt nu bracket-directives met het expliciete eindtoken `:]`. Voordat wraptokens zoals: - `[/]` - `[*]` - `[/?]` - `[*?]` worden toegevoegd, moet bracket-token dispatch centraal plaatsvinden. - architectuur vastgelegd; - regressietest toegevoegd; - nog geen functionele wijziging. Stap 110 implementeert daadwerkelijke dispatch van bracket-tokens.

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
