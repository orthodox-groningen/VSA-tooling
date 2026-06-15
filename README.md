# Stap 63 - rendering spacing diagnostics

Deze stap voegt een diagnostische Hugo-pagina toe voor spacing/overlap inspectie.

Doel:

- snel zien of stap 62 verbetering geeft;
- bekende probleemgevallen bij elkaar zetten;
- later makkelijk regressies herkennen.

## Nieuwe pagina

```text
/voorbeelden/rendering/spacing-diagnostiek/
```

Met voorbeelden rond:

- `me{\\de}{/eeu_}wi{\ge}`;
- `eerstge{/bo_}re{\ne_}`;
- `{/ge}{/&/o}pen{baard_}`;
- `ge{\ble_}{\ven_}`;
- filler-lines bij multi-EHM scopes.

## Test

```cmd
scripts\retry.cmd vsa-step63-rendering-spacing-diagnostics.zip
```
