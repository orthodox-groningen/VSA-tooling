# Stap 43 - policy stabilization

## Huidige stabiele policy

```text
[:]  == geldige neutrale hoogte-markering
[-:] == expliciete neutrale hoogte-markering
[~:] == expliciete neutrale hoogte-markering
```

Dus:

- `[:]` is ook aan het einde geldig;
- `[:]` aan het einde is geen lege of betekenisloze final pitchmarker;
- ontbrekende final pitchmarker is toegestaan;
- ontbrekende final pitchmarker betekent: geen expliciete eindtooncontrole;
- oude regels voor `VSA-SEMANTIC-MISSING-FINAL-PITCH-MARKER` en `VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER` zijn obsolete.

Eindtooncontrole is een aparte semantische regel die alleen kan worden toegepast wanneer er een expliciete eindmarkering aanwezig is.
