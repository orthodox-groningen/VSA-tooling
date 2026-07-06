# 081 — Stap 34 - links en responsive layout fix

## Huidige locatie

```text
docs/architecture/parser-stap-34-links-responsive-fix.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

De demo gebruikte absolute links zoals: /voorbeelden/ Dat werkt lokaal op root, maar niet op GitHub Pages onder: /VSA-tooling/ Daarom gebruikt de template nu: {{ "voorbeelden/" | relURL }} Markdownpagina's gebruiken relatieve links. Voor VSA-afbeeldingen gebruikt de demo nu shortcode-output. De shortcode past `relURL` toe:

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
