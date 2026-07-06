# 013 — Stap 105 - parser koppelen aan bracket token stream

## Huidige locatie

```text
docs/architecture/parser-stap-105-parser-bracket-token-stream.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

De parser gebruikt voor hoogte-markeringen dezelfde bracket-token infrastructuur als toekomstige bracket-directives. `Parser._parse_pitch_marker()` gebruikt nu: bracket_token_stream(...) De parser accepteert alleen tokens met: kind = pitch_marker Andere bracket-directives, zoals `[_:]` of `[/&\:]`, worden als ongeldige hoogte-markering afgewezen.

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
