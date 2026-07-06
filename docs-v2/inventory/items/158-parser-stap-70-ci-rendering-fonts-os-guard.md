# 158 — Stap 70 - CI rendering fonts OS guard

## Huidige locatie

```text
docs/architecture/parser-stap-70-ci-rendering-fonts-os-guard.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

GitHub Actions faalde omdat Linux-only fontinstallatie ook op Windows runners draaide. Fout: sudo apt-get update && sudo apt-get install -y fonts-dejavu-core Windows heeft geen `sudo`. Alle `Install rendering fonts` stappen krijgen: if: runner.os == 'Linux' python scripts\apply-step70-ci-rendering-fonts-os-guard.py

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
