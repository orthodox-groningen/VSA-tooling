# Stap 36 - compatibele pitch-marker eindcontrole

## Status

Deze oorspronkelijke stap is **verouderd**.

De destijds genoemde foutcodes zijn niet langer actuele semantische regels:

```text
VSA-SEMANTIC-MISSING-FINAL-PITCH-MARKER
VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER
```

## Huidige policy

Een eindmarkering is optioneel.

```text
[:] {/Hei_}{/lig_} is de Heer.
```

is geldig.

Een lege eindmarkering is geen semantische fout. `[:]` betekent een neutrale hoogte en is equivalent aan `[-:]` c.q. `[~:]`.

```text
[:] {/Hei_}{/lig_} is de Heer. [:]
[:] {/Hei_}{/lig_} is de Heer. [-:]
[:] {/Hei_}{/lig_} is de Heer. [~:]
```

zijn semantisch geldig als expliciete neutrale eindhoogte.

Een niet-neutrale eindmarkering, bijvoorbeeld `[\:]` of `[//:]`, kan later worden gecontroleerd tegen de berekende eindtoon.
