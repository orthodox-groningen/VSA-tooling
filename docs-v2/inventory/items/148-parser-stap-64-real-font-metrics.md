# 148 — Stap 64 - real font metrics

## Huidige locatie

```text
docs/architecture/parser-stap-64-real-font-metrics.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze stap introduceert echte font metrics via Pillow als dat beschikbaar is. De renderer gebruikte tot nu toe geschatte tekstbreedtes. Dat veroorzaakte: - overlap; - ongelijkmatige spacing; - onvoorspelbare wrapping; - noodzaak tot heuristische tuning. `src/vsa/text_metrics.py` probeert eerst echte tekstmeting:

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
