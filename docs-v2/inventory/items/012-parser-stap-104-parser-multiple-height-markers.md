# 012 — Stap 104 - parseracceptatie voor meerdere hoogte-markeringen

## Huidige locatie

```text
docs/architecture/parser-stap-104-parser-multiple-height-markers.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

De parser accepteert meerdere hoogte-markeringen binnen één VSA-bron. Voorbeeld: [:] begin [/:] midden [//:] einde De bestaande `PitchMarkerNode` blijft behouden om renderer, validator en bestaande tests compatibel te houden. Daarnaast is een alias toegevoegd: HeightMarkerNode = PitchMarkerNode Zo kan documentatie en toekomstige code over hoogte-markeringen spreken zonder bestaande AST-consumenten te breken.

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
