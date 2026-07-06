# Validatiearchitectuur

Validatie controleert de AST op regels die verder gaan dan zuivere syntax.

## Validatielagen

| Laag                  | Controleert                                               |
| --------------------- | --------------------------------------------------------- |
| Parser                | Herkenbare syntax en structurele AST-opbouw.              |
| Semantische validator | Consistentie van modifiers, markers en scopes.            |
| Publicatiecheck       | Outputkwaliteit, links, base-URL en publiceerbaarheid.    |

## Recoverable validatie

De validator verzamelt waar mogelijk meerdere fouten in één run. Dat is belangrijk voor gebruikersdocumentatie en CI, omdat één fout anders steeds de volgende fouten verbergt.

## Voorbeelden van semantische controles

| Controle                         | Regel                                                        |
| -------------------------------- | ------------------------------------------------------------ |
| Modifieraantallen                | Hoogte- en lengtemodifiers moeten dezelfde posities beschrijven. |
| Eindmarkering                    | Ontbrekende eindmarkering is toegestaan.                     |
| Neutrale eindmarkering           | `[:]`, `[-:]` en `[~:]` zijn neutraal equivalent.            |
| Niet-neutrale eindmarkering      | Kan later tegen berekende eindtoon worden gecontroleerd.     |
| Scope-inhoud                     | Lege of inconsistent gemarkeerde scopes leveren diagnostiek. |

## Diagnostiek

Diagnostiek moet bruikbaar zijn voor CLI, tests en eventueel editorintegratie.

| Eigenschap        | Doel                                         |
| ----------------- | -------------------------------------------- |
| Code              | Stabiele herkenning in tests en documentatie. |
| Severity          | Onderscheid tussen fout, waarschuwing en info. |
| Locatie           | Terugwijzen naar bronregel en kolom.          |
| Context           | Uitleg geven zonder broninhoud te herschrijven. |
