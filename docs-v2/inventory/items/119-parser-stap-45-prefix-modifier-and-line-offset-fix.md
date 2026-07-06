# 119 — Stap 45 - prefix modifier and line offset fix

## Huidige locatie

```text
docs/architecture/parser-stap-45-prefix-modifier-and-line-offset-fix.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze patch herstelt twee regressies. Dit blijft syntactisch geldig: {/&\tekst_} Het kan daarna semantisch falen met: VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH {\\} {&\ken__} {fout/} krijgen specifieke syntaxmeldingen. Foutmeldingen binnen `::: vsa-notatie` blokken wijzen weer naar de juiste regel in het Markdownbestand.

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
