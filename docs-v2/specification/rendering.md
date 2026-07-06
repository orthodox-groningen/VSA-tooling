# Rendering

Status: **geconsolideerde werkversie**.

## Scope

Dit document beschrijft de visuele rendering van VSA, met nadruk op SVG.

De rendering-specificatie bepaalt niet de muzikale betekenis van VSA-constructies.

## Rendering-principes

SVG-rendering moet:

- goed leesbaar zijn;
- muzikaal scanbaar zijn;
- compact maar luchtig ogen;
- schaalbaar zijn;
- geschikt zijn voor schermweergave en print.

## Render-runs

Een VSA-regel wordt gerenderd als reeks render-runs.

Voorbeelden:

- vrije tekst;
- zangelementen;
- hoogte-markeringen;
- whitespace;
- interpunctie.

## Layout

Default rendering gebruikt:

- links uitgelijnde regels;
- natuurlijke tekstspatiëring;
- compacte glyphs;
- consistente verticale uitlijning.

Toegestane regeluitlijningen:

- `left`;
- `right`;
- `center`;
- `justify`.

Default is `left`.

## Wrapping

Default wrapping gebruikt natuurlijke grenzen:

1. expliciete regeleinden;
2. whitespace;
3. interpunctie;
4. grenzen tussen render-runs;
5. optionele interne zangelementgrenzen.

De renderer mag modifiers niet losmaken van hun tekst.

Glyphgroepen worden niet gesplitst.

## Hoogte-markeringen

Alle hoogte-markeringen worden voor SVG-rendering gelijk behandeld.

Er is geen visueel onderscheid tussen eerste, latere of laatste hoogte-markering.

Regel:

```text
hoogte-markering in bron -> hoogte-marker-glyph op die renderpositie
```

## Commentaar

Commentaar heeft geen invloed op layout, spacing of rendering.

Commentaar komt niet in de SVG-output terecht.

## Configuratie

Rendering-configuratie hoort apart van de taalsemantiek te blijven.

Renderer-specifieke instellingen mogen de betekenis van de VSA-bron niet wijzigen.
