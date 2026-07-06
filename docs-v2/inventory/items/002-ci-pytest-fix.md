# 002 — CI pytest fix

## Huidige locatie

```text
docs/architecture/ci-pytest-fix.md
```

## Documenttype

architectuur

## Doelgroep

ontwikkelaar / architect

## Inhoudelijke samenvatting

GitHub Actions gaf: No module named pytest Daarom installeert `scripts\\ci.cmd` nu zelf: python -m pip install --upgrade pip python -m pip install -e . python -m pip install pytest Daarmee is `ci.cmd` zelfstandig bruikbaar: scripts\\ci.cmd zowel lokaal als in GitHub Actions.

## Relaties met andere documenten

Nog te detailleren tijdens inhoudelijke consolidatie.

## Overlap met andere documenten

Nog te detailleren tijdens inhoudelijke consolidatie.

## Voorgestelde bestemming

```text
docs-v2/architecture/
```

## Inventarisatiestatus

Eerste classificatie op basis van bestandsnaam, locatie en documentkop.

## Opmerkingen

Geen inhoud migreren in fase 1; alleen classificeren en later controleren.
