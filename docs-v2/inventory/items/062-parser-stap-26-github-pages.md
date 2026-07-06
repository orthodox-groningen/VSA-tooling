# 062 — Stap 26 - GitHub Pages publicatie

## Huidige locatie

```text
docs/architecture/parser-stap-26-github-pages.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze stap voegt toe: .github/workflows/pages-demo.yml De workflow doet: pytest ↓ vsa validate ↓ vsa build-markdown ↓ hugo build ↓ deploy-pages In GitHub: Actions → Deploy Hugo demo to GitHub Pages → Run workflow In de repo: Settings → Pages → Build and deployment → Source → GitHub Actions Zolang de demo nog experimenteel is, is handmatig deployen veiliger dan automatisch publiceren bij elke push.

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
