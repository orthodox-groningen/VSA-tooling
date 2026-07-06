# Stap 14 - SVG regressietests

Deze stap introduceert vaste SVG-regressietests.

Per testmap:

```text
input.vsa
expected.svg
.svg-regression
```

De marker `.svg-regression` bepaalt dat de map door de SVG-regressietest wordt meegenomen.

## Waarom een markerbestand?

Niet elke regressiemap heeft al SVG-output.

Met een marker kunnen we geleidelijk SVG-tests toevoegen zonder oude incomplete mappen te breken.

## Bij bewuste rendererwijzigingen

Als de renderer bewust verandert:

```cmd
vsa svg examples\regression\svg-basic\input.vsa examples\regression\svg-basic\expected.svg
```

Daarna tests opnieuw draaien.
