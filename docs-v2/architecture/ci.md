# CI-architectuur

## Doel

CI bewaakt parsergedrag, rendering, documentatievoorbeelden en publicatiekwaliteit.

## Testlagen

| Laag | Doel |
|------|------|
| Parsertests | AST en tokenverwerking controleren |
| Validatietests | Diagnostics en semantische regels controleren |
| Renderingtests | SVG/Markdown/Hugo-output controleren |
| Documentatietests | Voorbeelden en documentstructuur controleren |
| Publicatietests | Preview/productie-output controleren |

## Betrouwbaarheid

CI moet regressies vroeg zichtbaar maken. Documentatievoorbeelden zijn onderdeel van de kwaliteitscontrole en mogen niet losstaan van de implementatie.

## Traceerbaarheid

Gebaseerd op onder meer:

- `docs/architecture/ci-pytest-fix.md`
- `docs/architecture/ci-reliability.md`
- `docs/architecture/parser-stap-12-ci.md`
- `docs/architecture/parser-stap-30-doc-test-fix.md`
- `docs/architecture/parser-stap-130-gh-pages-workflow-tests.md`
