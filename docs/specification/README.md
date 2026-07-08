# Specificatie

Deze map bevat de geconsolideerde specificatie van VSA versie 1.0.

VSA (Vereenvoudigde Slavische Accentnotatie) is een tekstgebaseerde domeinspecifieke taal (Domain-Specific Language, DSL) voor het beschrijven van Slavische accentnotatie.

De taal definieert een eenduidige, machineleesbare en menselijk leesbare notatie waarmee zangstukken kunnen worden vastgelegd, gevalideerd en gerenderd. De specificatie beschrijft uitsluitend de taal en haar semantiek; implementaties kunnen vrij zijn in programmeertaal, architectuur en interne representatie, zolang zij voldoen aan de conformance-eisen van deze specificatie.

De specificatie beschrijft wat de notatie en tooling moeten betekenen. Architectuurkeuzes, implementatiegeschiedenis en gebruikershandleidingen staan buiten deze map.

## Documenten

| Document          | Inhoud                                                             |
| ----------------- | ------------------------------------------------------------------ |
| `overview.md`     | doel, scope, terminologie en status                                |
| `syntax.md`       | VSA-syntax, bloksyntax, modifiers, pitchmarkers en EBNF            |
| `semantics.md`    | muzikale betekenis van scopes, modifiers, posities en tooncontext  |
| `validation.md`   | validatieregels, foutcategorieën en severity-model                 |
| `directives.md`   | control tokens, comments, includes en document-samenstelling       |
| `rendering.md`    | SVG-rendering, glyphmodel, layout, configuratie en export          |
| `cli.md`          | CLI-contract voor gebruikers- en buildcommando's                   |
| `traceability.md` | herkomst van de geconsolideerde onderdelen                         |
| `conformance.md`  | criteria waaraan parser, validator, renderer en CLI moeten voldoen |
