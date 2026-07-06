# 083 — Stap 34 - shortcode voorbeeld escape fix

## Huidige locatie

```text
docs/architecture/parser-stap-34-shortcode-example-escape-fix.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Hugo voert shortcodes uit, ook als ze in documentatie als voorbeeld bedoeld zijn. Daarom is dit fout in documentatie: {{< vsa src="/vsa/demo-block-1.svg" >}} Gebruik in documentatie: {{</* vsa src="/vsa/demo-block-1.svg" */>}} Dan toont Hugo het voorbeeld zonder de shortcode uit te voeren.

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
