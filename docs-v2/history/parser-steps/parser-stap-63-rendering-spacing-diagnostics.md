# Stap 63 - rendering spacing diagnostics

Deze stap voegt een diagnostische Hugo-pagina toe voor bekende spacing- en overlapgevallen.

## Nieuwe pagina

```text
examples/hugo-demo/content-source/voorbeelden/rendering/spacing-diagnostiek.md
```

Doel:

- stap-62 tekstmeting visueel beoordelen;
- bekende regressiegevallen zichtbaar maken;
- toekomstige rendererwijzigingen sneller beoordelen.

## Voorbeelden

- `me{\\de}{/eeu_}wi{\ge}`
- `eerstge{/bo_}re{\ne_}`
- `{/ge}{/&/o}pen{baard_}`
- `ge{\ble_}{\ven_}`
- multi-EHM filler-lines
- Markdown hardbreaks
