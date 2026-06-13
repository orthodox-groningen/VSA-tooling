# Stap 51 - wrap regression fix

Deze stap herstelt wrapping na de strengere woordafbreekregel.

## Regel

- niet breken binnen gemodificeerde woorddelen;
- wel breken tussen losse ongemodificeerde scopes zoals `{tekst} {tekst}`;
- `SVGRenderer.max_line_width` wordt weer gebruikt.
