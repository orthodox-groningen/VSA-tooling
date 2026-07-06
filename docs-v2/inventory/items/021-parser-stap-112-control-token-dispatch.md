# 021 — Stap 112 - Control token dispatch

## Huidige locatie

```text
docs/architecture/parser-stap-112-control-token-dispatch.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

De parser krijgt een afzonderlijke dispatch-laag voor bracket-tokens. [<EHM>:]  -> Height marker [/]       -> Control token [*]       -> Control token [/?]      -> Control token [*?]      -> Control token anders     -> parserfout - daadwerkelijke parsercode - SVG-rendering - MusicXML-rendering Deze stap legt alleen het contract vast.

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
