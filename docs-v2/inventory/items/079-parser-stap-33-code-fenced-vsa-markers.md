# 079 — Stap 33 - VSA markers in Markdown-codeblokken negeren

## Huidige locatie

```text
docs/architecture/parser-stap-33-code-fenced-vsa-markers.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Probleem: Een documentatievoorbeeld zoals: ::: vsa-notatie {voorbeeld} ::: werd toch verwerkt als echt VSA-blok. Oorzaak: De block parser zocht puur naar: ::: vsa-notatie zonder rekening te houden met fenced codeblocks. Fix: - `parse_markdown_blocks()` houdt code fences bij; - `build-markdown` doet hetzelfde tijdens herschrijven;

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
