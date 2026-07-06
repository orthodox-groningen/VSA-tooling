# 077 — Stap 32 - responsive demo en branch-aware builds

## Huidige locatie

```text
docs/architecture/parser-stap-32-responsive-branch-builds.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze stap voegt toe: examples/hugo-demo/static/css/site.css .github/workflows/site-build.yml De demo-site bevat nu CSS voor: - telefoon; - tablet; - laptop; - groot scherm. Belangrijkste regels: max-width: 100%; overflow-x: auto; @media (max-width: 600px) Nieuwe workflow: Site build Gedrag: | Event | Branch | Target |

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
