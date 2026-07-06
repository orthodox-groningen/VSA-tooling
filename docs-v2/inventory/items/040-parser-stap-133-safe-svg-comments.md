# 040 — Stap 133 - veilige SVG-comments

## Huidige locatie

```text
docs/architecture/parser-stap-133-safe-svg-comments.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

SVG-output bevatte metadata-comments zoals: <!-- plain-text: ... --> Wanneer de brontekst zelf een Markdown/HTML-comment bevatte, kon de geëscapete tekst nog steeds `--` bevatten. XML/SVG-comments mogen geen dubbele hyphen bevatten. Voorbeeld van foutmelding in de browser: Double hyphen within comment

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
