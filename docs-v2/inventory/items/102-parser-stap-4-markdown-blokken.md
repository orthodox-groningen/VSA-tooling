# 102 — Parser stap 4 - Markdown blokken

## Huidige locatie

```text
docs/architecture/parser-stap-4-markdown-blokken.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze stap haalt VSA-blokken uit Markdown. Doel: Markdown ↓ parse_markdown_blocks() ↓ VSABlock[] ↓ Parser(block.body) ↓ AST Een blok bevat: metadata body start_line end_line De metadata krijgt defaultwaarden uit de specificatie: do="F4" mode="major" tempo="100" validate-ending="true" duration-model="default"

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
