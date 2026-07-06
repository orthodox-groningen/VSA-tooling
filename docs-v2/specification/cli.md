# CLI-contract

Status: **eerste werkversie**.

## Scope

Dit document beschrijft het command-line contract van de VSA-tooling.

De details worden in een latere stap verder geconsolideerd uit de bestaande CLI-, build- en gebruikersdocumentatie.

## Basisgedrag

De CLI leest VSA-bronbestanden en produceert één of meer afgeleide artefacten.

Bekende uitvoervormen:

- SVG;
- JSON/AST;
- Markdown/Hugo-output;
- diagnostiek.

## Validatie

De CLI moet syntactische en semantische problemen rapporteren.

Waar mogelijk wordt recoverable diagnostiek verzameld in plaats van na de eerste fout te stoppen.

## Output-modi

Output-modi worden expliciet gekozen via configuratie of command-line opties.

Bekende modi zijn onder andere:

- `image`;
- `shortcode`;
- JSON/debug-output.

## Exitgedrag

Een definitief CLI-contract moet vastleggen:

- wanneer exitcode `0` wordt gebruikt;
- wanneer syntactische fouten een non-zero exitcode geven;
- wanneer semantische fouten een non-zero exitcode geven;
- hoe waarschuwingen worden gerapporteerd;
- hoe recoverable diagnostiek in JSON wordt opgenomen.

## Open consolidatiepunt

Dit bestand is nog bewust beperkt.

De volgende fase moet dit document aanvullen op basis van de bestaande CLI-, Hugo-, build- en testdocumentatie.
