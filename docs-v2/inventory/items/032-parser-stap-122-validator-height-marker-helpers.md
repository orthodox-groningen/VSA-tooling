# 032 — Stap 122 - Validator aansluiten op height marker helpers

## Huidige locatie

```text
docs/architecture/parser-stap-122-validator-height-marker-helpers.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

De semantische validator gebruikt voortaan de centrale helperlaag voor hoogte-markeringen. Bij initialisatie verzamelt de validator: self.height_markers = height_marker_refs(document) en exposeert dat intern via: validator._height_markers() Deze stap verandert nog geen validatieregels. Wel is nu vastgelegd dat latere validatorregels niet rechtstreeks naar `PitchMarkerNode` of `HeightMarkerNode` hoeven te kijken.

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
