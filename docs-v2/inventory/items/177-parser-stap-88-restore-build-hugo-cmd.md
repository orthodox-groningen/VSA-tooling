# 177 — Stap 88 - herstel `build-hugo.cmd`

## Huidige locatie

```text
docs/architecture/parser-stap-88-restore-build-hugo-cmd.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Een eerdere patch voegde regels in midden in een CMD-regelcontinuatie: hugo ^ python scripts\... --source ... Daardoor zag Hugo `python` als subcommand en werden `--source` enzovoort losse CMD-commando's. `build-hugo.cmd` is volledig vervangen door een schone versie. De linkchecker wordt voorlopig handmatig gedraaid:

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
