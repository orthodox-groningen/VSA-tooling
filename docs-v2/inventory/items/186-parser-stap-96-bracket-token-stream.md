# 186 — Stap 96 - bracket token stream

## Huidige locatie

```text
docs/architecture/parser-stap-96-bracket-token-stream.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

De bracket-directive scanner uit stap 95 wordt uitgebreid met een tokenstroom-bouwsteen. Bestand: src/vsa/bracket_token_stream.py De tokenstroom kent voorlopig drie soorten tokens: text directive pitch_marker `text` is gewone tekst buiten bracket-directives. `directive` is een geldige bracket-directive waarvan de inhoud geen EHM is.

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
