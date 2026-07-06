# 180 — Stap 90 - stop build-hugo mutators

## Huidige locatie

```text
docs/architecture/parser-stap-90-stop-build-hugo-mutators.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Oude apply-scripts bleven `scripts\build-hugo.cmd` muteren. Specifiek konden regels zoals deze midden in het `hugo ^` blok terechtkomen: python scripts\regenerate-missing-vsa-images.py python scripts\check-hugo-links-and-assets.py Deze oude apply-scripts zijn nu gedeactiveerd: scripts\apply-step76-regenerate-missing-vsa-images.py

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
