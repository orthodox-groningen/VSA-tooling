# Publicatiearchitectuur

Publicatie bestaat uit lokale build, Hugo-demo, preview-output en productie-output.

## Publicatiestromen

| Stroom             | Doel                                             |
| ------------------ | ------------------------------------------------ |
| Lokale build       | Snel controleren of tooling en demo werken.      |
| Hugo-demo          | VSA-output tonen in documentatiecontext.         |
| Preview Pages      | Branch- of previewpublicatie onder `/preview/`.  |
| Productie Pages    | Handmatige of gecontroleerde productiepublicatie. |

## Publicatiecontrole

Voor publicatie moet output gecontroleerd worden.

| Controle             | Reden                                                |
| -------------------- | ---------------------------------------------------- |
| `index.html` bestaat | Sitebuild is daadwerkelijk voltooid.                 |
| Links bestaan        | Geen gebroken interne verwijzingen publiceren.       |
| Base-URL klopt       | GitHub Pages-projectpad moet correct zijn.           |
| Geen oude comments   | Verouderde SVG plain-text metadata mag niet terugkomen. |
| Geen fouttekst       | Browser/XML-foutmeldingen mogen niet gepubliceerd worden. |

## Hergebruik

Andere repositories moeten de VSA-rendering kunnen gebruiken via een herbruikbare workflow of via installatie van de tool uit de repository.
