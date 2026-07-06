# Renderingarchitectuur

## Doel

Renderers zetten een gevalideerd AST om naar uitvoerformaten.

## Uitvoerformaten

- SVG;
- Markdown/Hugo;
- shortcode-output;
- JSON/diagnostics.

## Principe

Rendering volgt het AST en de validatieresultaten. De renderer voert geen semantische reparaties uit en bevat geen speciale parserlogica.

## SVG

SVG-rendering is positioneel: tekst, hoogte-informatie en lengtemodifiers worden op basis van hun posities in het grid geplaatst.

## Hugo

Hugo-output gebruikt expliciete output-modi, zodat dezelfde broninhoud als afbeelding, shortcode of andere representatie kan worden gepubliceerd.

## Traceerbaarheid

Gebaseerd op onder meer:

- `docs/architecture/parser-stap-13-svg-glyphs.md`
- `docs/architecture/parser-stap-15-scope-grid.md`
- `docs/architecture/parser-stap-16-svg-autosize.md`
- `docs/architecture/parser-stap-21-hugo-shortcodes.md`
- `docs/architecture/parser-stap-22-config-output-mode.md`
- `docs/architecture/parser-stap-46-rendering-specs.md`
- `docs/architecture/parser-stap-47-svg-rendering-baseline.md`
- `docs/architecture/parser-stap-108-svg-multiple-height-markers.md`
