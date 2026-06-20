# Stap 36 - validator pitch-marker eindcontrole

## Status

Deze oorspronkelijke stap is **verouderd**.

De foutcode `VSA-SEMANTIC-MISSING-FINAL-PITCH-MARKER` is obsolete: het ontbreken van een eindmarkering is syntactisch én semantisch toegestaan.

De foutcode `VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER` is eveneens obsolete voor `[:]`: een lege hoogte-markering betekent een neutrale hoogte en is semantisch gelijkwaardig aan `[-:]` c.q. `[~:]`.

## Huidige policy

Syntactisch geldig:

```text
[:] {/Hei_}{/lig_} is de Heer. [:]
[:] {/Hei_}{/lig_} is de Heer.
[:] {/Hei_}{/lig_} is de Heer. [-:]
[:] {/Hei_}{/lig_} is de Heer. [~:]
[:] {/Hei_}{/lig_} is de Heer. [\:]
```

Semantisch:

- geen eindmarkering betekent: geen expliciete eindtooncontrole;
- `[:]` aan het einde betekent: expliciete neutrale eindhoogte;
- `[:]`, `[-:]` en `[~:]` zijn voor eindhoogtecontrole equivalent;
- een niet-neutrale eindmarkering, bijvoorbeeld `[//:]`, kan later worden gecontroleerd tegen de berekende eindtoon.

## Niet meer gebruiken

Deze stap mag niet meer worden gelezen als actuele validator-specificatie.
Actuele regels staan in de algemene specificatie en in de latere pitch-marker policy-documentatie.
