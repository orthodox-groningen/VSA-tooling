# 150 — Stap 66 - Pillow dependency en CI font setup

## Huidige locatie

```text
docs/architecture/parser-stap-66-pillow-dependency-ci.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze stap maakt Pillow expliciet als rendering dependency. - `requirements-rendering.txt` - `scripts/install-rendering-deps.cmd` - `scripts/apply-step66-pillow-dependency-ci.py` - tests voor dependency/documentatie GitHub Actions moet: - name: Install rendering fonts run: sudo apt-get update && sudo apt-get install -y fonts-dejavu-core

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
