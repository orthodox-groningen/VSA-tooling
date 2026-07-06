# 185 — Stap 95 - bracket-directive scanner

## Huidige locatie

```text
docs/architecture/parser-stap-95-bracket-directive-scanner.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Eerst een kleine geïsoleerde parserbouwsteen toevoegen voordat de bestaande parser wordt aangepast. Bestand: src/vsa/bracket_directive.py Een bracket-directive heeft vorm: [<body>:] Het eindtoken is: :] Een pitch marker is een bracket-directive waarvan `<body>` een geldige EHM is. Voorbeelden: [:] [/:]

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
