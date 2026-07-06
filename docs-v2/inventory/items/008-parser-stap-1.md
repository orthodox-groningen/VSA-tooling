# 008 — Parser stap 1

## Huidige locatie

```text
docs/architecture/parser-stap-1.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze stap maakt van VSA-brontekst een eenvoudige AST. Ondersteunde nodes: Document TextNode ScopeNode PitchMarkerNode Voorbeeld: {/tekst_} wordt: { "type": "Document", "nodes": [ { "type": "ScopeNode", "height_modifier": ["/"], "text": "tekst", "length_modifier": ["_"] } ] } scripts\test.cmd En: .venv\Scripts\activate

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
