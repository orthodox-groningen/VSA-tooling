# 188 — Stap 98 - real font metrics afdwingen + stap 92 test fix

## Huidige locatie

```text
docs/architecture/parser-stap-98-real-font-metrics-and-step92-test-fix.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

`build-hugo.cmd` gebruikt `.venv\Scripts\python.exe` als die bestaat. Na `update-spacing-diagnostics-metadata.py` draait: scripts\assert-real-font-metrics.py Als real metrics niet actief zijn, stopt de build. De stap-92 test is aangepast aan de huidige formulering: `_` is geen EHM.

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
