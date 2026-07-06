# 085 — Stap 35 - URL policy fix

## Huidige locatie

```text
docs/architecture/parser-stap-35-url-policy-fix.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze stap legt het URL-beleid vast. Voor lokaal gebruik: baseURL = / Voor deploy naar GitHub Pages: https://<owner>.github.io/<repo>/ In GitHub Actions: --baseURL "https://${{ github.repository_owner }}.github.io/${{ github.event.repository.name }}/" Gebruik niet: github.server_url/github.repository want dat verwijst naar GitHub zelf, niet naar GitHub Pages.

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
