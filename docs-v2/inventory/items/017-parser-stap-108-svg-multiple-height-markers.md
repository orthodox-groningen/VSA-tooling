# 017 — Stap 108 - SVG-rendering van meerdere hoogte-markeringen

## Huidige locatie

```text
docs/architecture/parser-stap-108-svg-multiple-height-markers.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

De parser en semantische validator accepteren meerdere hoogte-markeringen. Deze stap borgt dat de SVG-rendering ze ook allemaal zichtbaar houdt. Voor: [:] tekst [/:] meer [//:] einde moet SVG-rendering bevatten: - drie `vsa-pitch-marker` units; - drie `vsa-pitch-marker-dash` lijnen; - hoogte-glyphs voor de niet-lege hoogte-markeringen;

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
