# 152 — Stap 67 - script path fix

## Huidige locatie

```text
docs/architecture/parser-stap-67-script-path-fix.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

`update-spacing-diagnostics-metadata.py` werd soms uitgevoerd met globale Python. Dan was `src/vsa` niet importeerbaar. Het script voegt nu zelf `src` toe aan `sys.path`.

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
