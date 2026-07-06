# 104 — Stap 40 - CLI version import fix

## Huidige locatie

```text
docs/architecture/parser-stap-40-cli-version-import-fix.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

De vorige patch gebruikte: from .version import __version__ Maar `src/vsa/version.py` bestaat niet. De CLI gebruikt nu: importlib.metadata.version("vsa-tool") met fallback: 0.1.0

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
