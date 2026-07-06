# 187 — Stap 97 - repair bracket token stream

## Huidige locatie

```text
docs/architecture/parser-stap-97-repair-bracket-token-stream.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Stap 96 filterde tokens met lege `value` weg. Dat is fout, want de pitch marker: [:] heeft een lege EHM-body en is juist geldig. `bracket_token_stream()` retourneert nu alle tokens. Lege teksttokens worden niet geproduceerd door de bestaande cursorlogica; lege pitch-marker bodies blijven behouden. Toegevoegd:

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
