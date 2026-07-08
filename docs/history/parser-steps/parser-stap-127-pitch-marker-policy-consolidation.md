# Stap 127 - pitch-marker policy consolidatie

## Aanleiding

De oude documentatie rond eind-pitchmarkers bevatte twee inmiddels obsolete semantische foutcodes:

```text
VSA-SEMANTIC-MISSING-FINAL-PITCH-MARKER
VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER
```

Die regels passen niet meer bij de actuele syntax en semantiek.

## Syntax

De volgende vorm is syntactisch geldig:

```text
[:] {/Hei_}{/lig_} is de Heer. [:]
```

Ook een zangstuk zonder eindmarkering is syntactisch geldig:

```text
[:] {/Hei_}{/lig_} is de Heer.
```

## Semantiek

Een ontbrekende eindmarkering is toegestaan en betekent:

```text
geen expliciete eindtooncontrole
```

Een eindmarkering `[:]` is niet leeg in semantische zin. Zij betekent neutrale hoogte en is equivalent aan:

```text
[-:]
[~:]
```

Daarom is `VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER` voor `[:]` obsolete.

## Eindtooncontrole

Eindtooncontrole kan later worden toegepast wanneer een expliciete eindmarkering aanwezig is.

Voorbeeld:

```text
[:] tekst [//:]
```

kan semantisch worden gecontroleerd als de berekende eindtoon bekend is.

## Actuele regels

- beginmarkering: optioneel, maar betekenisvol als zij aanwezig is;
- eindmarkering: optioneel;
- ontbrekende eindmarkering: geldig;
- `[:]` als eindmarkering: geldig en neutraal;
- `[:]`, `[-:]` en `[~:]`: equivalent voor neutrale hoogte;
- niet-neutrale eindmarkering: later controleerbaar tegen berekende eindtoon.
