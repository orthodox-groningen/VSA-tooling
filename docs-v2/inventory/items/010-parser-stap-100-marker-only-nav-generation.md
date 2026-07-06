# 010 — Stap 100 - marker-only navigatiegeneratie

## Huidige locatie

```text
docs/architecture/parser-stap-100-marker-only-nav-generation.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

`content-source` is redactionele broncontent. Scripts mogen daarin niet automatisch frontmatter, titels, headings of vrije markdown herschrijven. Alleen dit mag worden vervangen of ingevoegd: <!-- VSA-NAV:<TYPE> --> <!-- VSA-NAV-GENERATED:<TYPE>-START --> ... <!-- VSA-NAV-GENERATED:<TYPE>-END --> `build-hugo.cmd` draait navigatiegeneratie alleen op `generated\hugo\content`.

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
