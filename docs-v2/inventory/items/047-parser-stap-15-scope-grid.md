# 047 — Stap 15 - scope-grid rendering

## Huidige locatie

```text
docs/architecture/parser-stap-15-scope-grid.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze stap maakt de SVG-renderer meer in lijn met het VSA-gridmodel. Een scope wordt niet langer behandeld als één los tekstblok met één modifierlaag, maar als: bovenrij     EHM per kolom tekstlaag    zangelement onderrij     ELM per kolom Voorbeeld: {/&\&/tekst_&~&~} wordt: kolom 1: /   _ kolom 2: \   ~

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
