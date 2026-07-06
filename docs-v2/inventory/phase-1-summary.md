# Fase 1 — eindoverzicht inventarisatie

## Status

Fase 1 is afgerond op inventarisatieniveau. De bestaande `docs/`-map is niet gewijzigd.

## Omvang

- Geïnventariseerde markdown-documenten: 224
- Inventory-bestanden: 228
- Bronmap: `docs/`
- Werkmap: `docs-v2/inventory/`

## Classificatie

| Type | Aantal |
|------|-------:|
| algemene documentatie | 8 |
| architectuur | 8 |
| handleiding / voorbeeld | 3 |
| ontwikkelgeschiedenis / parserstap | 182 |
| proces / todo | 4 |
| specificatie | 19 |

## Conclusie

De documentatie bestaat grotendeels uit ontwikkelgeschiedenis rond parser-, renderer-, Hugo- en CI-stappen. Die inhoud moet behouden blijven, maar hoort in de nieuwe structuur vooral onder `history/`. De actuele specificatie, architectuur en gebruikershandleiding moeten daaruit worden geconsolideerd.

## Advies voor fase 2

1. Ontwerp eerst de definitieve `docs-v2/` hoofdstructuur.
2. Verplaats historische parser-stappen conceptueel naar `history/parser/`.
3. Maak daarna pas geconsolideerde documenten voor specificatie, architectuur en handleidingen.
4. Wijzig `docs/` nog niet voordat `docs-v2/` inhoudelijk compleet is.
