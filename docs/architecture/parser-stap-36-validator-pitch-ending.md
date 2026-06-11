# Stap 36 - validator pitch-marker eindcontrole

Deze stap voegt een semantische validatie toe.

## Nieuwe foutcodes

```text
VSA-SEMANTIC-MISSING-FINAL-PITCH-MARKER
VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER
```

## Regel

Als een VSA-frase begint met een pitch-marker en gezongen materiaal bevat, dan moet de frase eindigen met een niet-lege pitch-marker.

Ongeldig:

```text
[:] {/Hei_}{/lig_} is de Heer. [:]
```

Geldig:

```text
[:] {/Hei_}{/lig_} is de Heer. [\\:]
```

## Waarom

Dit voorkomt dat demo's en voorbeelden syntactisch door de parser komen maar muzikaal/semantisch verdacht blijven.
