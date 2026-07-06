# Validatiearchitectuur

## Doel

De validator controleert semantische regels nadat de parser een AST heeft opgebouwd.

## Verantwoordelijkheden

De validator controleert onder andere:

- of hoogte- en lengtemodifiers hetzelfde aantal posities beschrijven;
- of markerconstructies semantisch geldig zijn;
- of control tokens op toegestane plekken voorkomen;
- of diagnostics de juiste severity krijgen.

## Diagnostics

Validatie levert gestructureerde diagnostics op. Waar mogelijk zijn fouten herstelbaar, zodat meerdere problemen tegelijk gerapporteerd kunnen worden.

## Parser versus validator

De parser stopt niet onnodig vroeg op semantische problemen. Hij levert een bruikbaar AST aan, waarna de validator alle relevante semantische problemen verzamelt.

## Traceerbaarheid

Gebaseerd op onder meer:

- `docs/architecture/parser-stap-19-validate-map.md`
- `docs/architecture/parser-stap-37-diagnostic-severity.md`
- `docs/architecture/parser-stap-43-rich-diagnostics-metadata.md`
- `docs/architecture/parser-stap-107-semantic-multiple-height-markers.md`
- `docs/architecture/parser-stap-121-height-marker-validator-contract.md`
- `docs/architecture/parser-stap-122-validator-height-marker-helpers.md`
