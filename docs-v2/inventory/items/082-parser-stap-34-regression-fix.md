# 082 — Stap 34 - regressiefix

## Huidige locatie

```text
docs/architecture/parser-stap-34-regression-fix.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze patch herstelt regressies uit stap 34. De parser negeert nog steeds VSA-markers in code fences, maar ondersteunt opnieuw: do="C4" mode="minor" en defaults zoals: do = F4 Oude tests verwachtten root-absolute links zoals: /voorbeelden/basis/ maar de demo gebruikt nu bewust relatieve links en Hugo `relURL`.

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
