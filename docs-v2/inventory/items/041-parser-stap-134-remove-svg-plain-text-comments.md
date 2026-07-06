# 041 — Stap 134 - plain-text comments verwijderen uit SVG

## Huidige locatie

```text
docs/architecture/parser-stap-134-remove-svg-plain-text-comments.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

SVG-output bevatte metadata-comments van de vorm: <!-- plain-text: ... --> Dat is niet gewenst: commentaar uit of over de bron hoort niet als SVG-output te worden gegenereerd. De `plain-text` comment-output is volledig uit `SVGRenderer.render_document()` verwijderd. De zichtbare `<text>` rendering blijft ongewijzigd.

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
