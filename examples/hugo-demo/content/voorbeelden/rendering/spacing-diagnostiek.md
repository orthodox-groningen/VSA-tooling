---
title: "Spacing diagnostiek"
---

# Spacing diagnostiek

<!-- VSA-METRICS-START -->
## Metrics van deze build

| Kenmerk | Waarde |
|---|---|
| Font | `DejaVu Sans` |
| Backend | `pillow` |
| Real metrics | `True` |
| Fontpad | `assets\fonts\DejaVuSans.ttf` |
| Fontgrootte | `20` |
| Ascent | `19.0` |
| Descent | `5.0` |
| Breedte `iiii` | `24.0` |
| Breedte `mmmm` | `76.0` |
| Breedte `eeu` | `37.0` |
| Breedte `baard` | `58.0` |

<!-- VSA-METRICS-END -->

Deze pagina bevat kleine, gerichte voorbeelden om SVG-spacing, tekstmeting en overlap te inspecteren.

Gebruik deze pagina bij wijzigingen aan:

- tekstbreedtemeting;
- scope-breedtes;
- optische gaps;
- filler-lines;
- regelafbreking.

## 1. Aanpalende scopes binnen één woord

<img class="vsa-notation" src="/vsa/voorbeelden-rendering-spacing-diagnostiek-block-1.svg" alt="VSA notatie">

```text
[:] me{\\de}{/eeu_}wi{\ge} [:]
```

Let op:

- geen overlap tussen `me` en `de`;
- geen overlap tussen `eeu` en `wi`;
- het woord moet wel visueel één woord blijven.

## 2. Niet afbreken midden in een woord

<img class="vsa-notation" src="/vsa/voorbeelden-rendering-spacing-diagnostiek-block-2.svg" alt="VSA notatie">

```text
[:] eerstge{/bo_}re{\ne_} [:]
```

Let op:

- geen harde breuk tussen `bo`, `re`, `ne`;
- spacing moet compact maar leesbaar blijven.

## 3. Korte scope gevolgd door gewone tekst

<img class="vsa-notation" src="/vsa/voorbeelden-rendering-spacing-diagnostiek-block-3.svg" alt="VSA notatie">

```text
[:] {/ge}{/&/o}pen{baard_} [:]
```

Let op:

- geen overlap tussen `o` en `pen`;
- filler-space na multi-EHM scope mag de volgende tekst niet raken.

## 4. Twee gemodificeerde scopes naast elkaar

<img class="vsa-notation" src="/vsa/voorbeelden-rendering-spacing-diagnostiek-block-4.svg" alt="VSA notatie">

```text
[:] ge{\ble_}{\ven_} [:]
```

Let op:

- `ble` en `ven` moeten duidelijk gescheiden zijn;
- ELMs mogen staarten niet raken.

## 5. Multi-EHM filler

<img class="vsa-notation" src="/vsa/voorbeelden-rendering-spacing-diagnostiek-block-5.svg" alt="VSA notatie">

```text
[:] {\ge}{/&/&/&\&\&\&/schon..&..&..&..&..&..&~}{\ken__} [:]
```

Let op:

- multi-EHM glyphs moeten afzonderlijk leesbaar zijn;
- filler-line moet op tekst/dash-hoogte staan;
- `ken` mag niet aan de filler-line vastplakken.

## 6. Bronregels blijven regels

<img class="vsa-notation" src="/vsa/voorbeelden-rendering-spacing-diagnostiek-block-6.svg" alt="VSA notatie">

```text
[:] eerste regel met {/tekst_}  
tweede regel met {/tekst_}  
derde regel met {/tekst_} [:]
```

Let op:

- fysieke bronregels blijven afzonderlijke SVG-regels;
- Markdown hardbreak-spaties vóór newline veroorzaken geen doorlopende regel.
