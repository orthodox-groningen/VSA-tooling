# Stap 52 - source-aware spacing

Deze stap voegt expliciete whitespace-render-units toe aan de SVG-layout.

## Waarom

Bronspaties moeten visueel meetellen tussen render-units.

Voorbeelden:

```text
{/de} {/Heer} heeft
ge{na_}{\de} {\ge}
```

mogen niet renderen als:

```text
deHeerheeft
genadege
```
