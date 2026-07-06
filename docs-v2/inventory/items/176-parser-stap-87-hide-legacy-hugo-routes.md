# 176 — Stap 87 - legacy Hugo-routes verbergen

## Huidige locatie

```text
docs/architecture/parser-stap-87-hide-legacy-hugo-routes.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

De linkchecker vond oude routes zoals: /voorbeelden/praktijk/... /zondag/... Deze links stonden niet letterlijk in `content-source`. Ze ontstonden doordat Hugo oude content nog als gewone pagina's publiceerde. Oplossing: draft: true vsa_nav_exclude: true Script: python scripts\hide-legacy-hugo-routes.py

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
