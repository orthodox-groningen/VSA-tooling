# 139 — Stap 57 - preserve VSA block newlines

## Huidige locatie

```text
docs/architecture/parser-stap-57-preserve-vsa-block-newlines.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze stap adresseert het verschil tussen voorbeelden waar bron-newlines wel of niet zichtbaar doorwerken in de SVG-rendering. De SVG-layout respecteert inmiddels `CR`, `LF` en `CRLF`, maar de aanvoer vanuit Markdown/Hugo kan newlines eerder al normaliseren naar spaties. Toegevoegd: - `src/vsa/markdown_vsa_blocks.py`

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
