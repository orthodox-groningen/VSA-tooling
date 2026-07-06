# 009 — Stap 10 - process valideert vóór SVG-generatie

## Huidige locatie

```text
docs/architecture/parser-stap-10-process-valideert.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze stap maakt `vsa process` geschikt voor CI. vsa process content generated\vsa doet nu: 1. alle Markdownbestanden zoeken 2. alle VSA-blokken valideren 3. bij fouten stoppen 4. alleen bij OK SVG-bestanden genereren Een buildproces mag geen site genereren op basis van ongeldige VSA. Daarom is dit gedrag belangrijk voor:

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
