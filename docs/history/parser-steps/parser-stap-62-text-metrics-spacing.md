# Stap 62 - text metrics en spacing

Deze stap introduceert een eenvoudige letterklasse-gebaseerde tekstbreedtemeting.

## Waarom

De vorige estimator gebruikte ongeveer:

```text
aantal tekens × font_size × factor
```

Dat veroorzaakt overlap en ongelijkmatige spacing.

## Nieuwe benadering

Tekens krijgen verschillende breedte-units:

- smal: `i`, `l`, interpunctie;
- breed: `m`, `w`, `M`, `W`;
- spaties;
- hoofdletters;
- cijfers;
- normale letters.

## Nog later

Echte font metrics blijft gewenst:

- Pillow;
- browser/SVG text measurement;
- cachebare font-metrics engine;
- exact dezelfde meting voor layout en SVG-rendering.
