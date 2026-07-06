# Stap 58 - echte pipeline-newlines

Stap 57 voegde helpers toe, maar het zichtbare probleem bleef bestaan.
Conclusie: de echte Hugo/SVG-pipeline gebruikte die helper nog niet, of
normaliseerde VSA-source eerder al naar één tekststroom.

## Deze stap

- voegt `scripts/apply-step58-real-pipeline-newlines.py` toe;
- voegt `src/vsa/markdown_newline_policy.py` toe;
- test dat `src/vsa` geen verdachte newline-naar-spatie normalisatie bevat;
- test een toon-8-achtig voorbeeld op layoutniveau.

## Bracket-wraptokens

Nog niet geïmplementeerd:

- `[/]`
- `[*]`
- `[/?]`
- `[*?]`

Reden: bracket-token dispatch in parser staat in `docs/todo.md`.
