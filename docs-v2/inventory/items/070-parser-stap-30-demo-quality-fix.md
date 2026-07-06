# 070 — Stap 30 - demo quality fix

## Huidige locatie

```text
docs/architecture/parser-stap-30-demo-quality-fix.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze patch herstelt twee problemen in de demo-site. Hugo-template `single.html` voegde een titel toe: <h1>{{ .Title }}</h1> maar de Markdownpagina's bevatten zelf ook: Daarom ontstonden dubbele titels. De template laat nu alleen de inhoud zien. De demo gebruikte: [:] ... [:] Dat is voor dit voorbeeld semantisch niet gewenst.

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
