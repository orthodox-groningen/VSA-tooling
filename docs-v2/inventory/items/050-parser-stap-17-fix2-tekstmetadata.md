# 050 — Stap 17 fix 2 - tekstmetadata in SVG

## Huidige locatie

```text
docs/architecture/parser-stap-17-fix2-tekstmetadata.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Door tekstwrapping wordt een gewone tekstnode gesplitst in woorden. Dat is goed voor layout, maar lastig voor regressietests en debugging. Daarom schrijft de SVG-renderer de originele tekstnode ook als commentaar: <!-- plain-text: is de Heer. --> Dit verandert de zichtbare output niet, maar maakt het makkelijker om te controleren dat gewone tekst behouden blijft.

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
