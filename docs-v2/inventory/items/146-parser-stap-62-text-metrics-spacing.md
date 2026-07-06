# 146 — Stap 62 - text metrics en spacing

## Huidige locatie

```text
docs/architecture/parser-stap-62-text-metrics-spacing.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze stap introduceert een eenvoudige letterklasse-gebaseerde tekstbreedtemeting. De vorige estimator gebruikte ongeveer: aantal tekens × font_size × factor Dat veroorzaakt overlap en ongelijkmatige spacing. Tekens krijgen verschillende breedte-units: - smal: `i`, `l`, interpunctie; - breed: `m`, `w`, `M`, `W`;

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
