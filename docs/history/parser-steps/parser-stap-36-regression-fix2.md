# Stap 36 regressiefix 2

De eerste pitch-marker validatie veroorzaakte regressies:

- VSA-block bodies werden leeg;
- SVG generatie gaf lege SVG's;
- `has_errors()` verdween;
- sommige minimal examples werden onterecht ongeldig.

Deze patch herstelt compatibiliteit.
