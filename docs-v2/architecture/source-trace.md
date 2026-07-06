# Herkomst architectuurconsolidatie

Deze architectuurdocumenten zijn geconsolideerd uit de bestaande documentatie onder `docs/`, zonder de oude documenten te verwijderen.

## Belangrijkste bronclusters

| Nieuw document      | Belangrijkste brondocumenten / bronclusters                              |
| ------------------- | ------------------------------------------------------------------------- |
| `overview.md`       | `docs/architecture/parser-fases.md`, algemene parser-stappen              |
| `parser.md`         | `parser-fases.md`, parser-stappen rond tokenization, scopes en dispatch   |
| `ast.md`            | `height-marker-model.md`, AST-contractstappen rond markers                |
| `directives.md`     | stappen 109, 111-116 en bracket/control-token ontwerp                     |
| `validation.md`     | validatorstappen, severitybeleid en pitch-marker policy                   |
| `rendering.md`      | SVG-, layout-, spacing- en metadata-stappen                               |
| `publication.md`    | GitHub Pages-, Hugo-, preview/productie- en publicatiecheckstappen         |
| `ci.md`             | `ci-reliability.md`, CI-fixdocumenten en workflowdocumentatie             |

## Behoud van geschiedenis

De vele `parser-stap-*.md` documenten blijven relevant als ontwerpgeschiedenis. In de nieuwe structuur horen zij uiteindelijk onder `docs-v2/history/`, met verwijzing vanuit de geconsolideerde architectuur.
