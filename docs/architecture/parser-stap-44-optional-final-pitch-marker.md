# Stap 44 - optional final pitch marker

Final pitchmarkers zijn optioneel.

## Geldig

```text
[:] {tekst}
[:] {tekst} [:]
[:] {tekst} [-:]
[:] {tekst} [\:]
```

## Semantiek

Als een final pitchmarker ontbreekt, betekent dat:

```text
geen expliciete eindmarkering
```

Als `[:]` aan het einde staat, betekent dat:

```text
expliciete neutrale eindmarkering
```

Eindtooncontrole komt later als aparte semantische regel.
