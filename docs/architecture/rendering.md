# Renderingarchitectuur

Rendering zet een gevalideerde AST om naar concrete output.

## Outputvormen

| Output       | Doel                                                   |
| ------------ | ------------------------------------------------------ |
| SVG          | Visuele VSA-weergave.                                  |
| JSON         | Inspectie, tests en debugging van parser/AST-output.   |
| Markdown     | Gebruik in documentatie en Hugo-content.               |
| Hugo         | Demo- en publicatiesite.                               |

## SVG-rendering

De SVG-renderer gebruikt de AST positioneel. Tekst, scopes, hoogte-informatie en lengte-informatie worden in een layoutmodel geplaatst.

Belangrijke ontwerpkeuzes:

- geen semantiek in SVG-code stoppen;
- tekstspacing bronbewust behandelen;
- multiline-layout en autosizing als rendererzorg beschouwen;
- diagnostiek niet verbergen achter visuele output;
- veilige metadata gebruiken en oude plain-text comments vermijden.

## Layout

| Aspect             | Architectuurkeuze                                      |
| ------------------ | ------------------------------------------------------ |
| Scope-grid         | Scope-inhoud wordt op vaste visuele posities geplaatst. |
| Tekstflow          | Inline tekst blijft in bronvolgorde.                   |
| Spacing            | Spacing wordt berekend met tekstmetrics waar beschikbaar. |
| Breedte            | SVG-breedte kan automatisch of via CLI/config worden bepaald. |
| Comments           | SVG-comments mogen geen onveilige of foutgevoelige plain text bevatten. |
