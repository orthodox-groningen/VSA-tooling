# Stap 54 - fillerhoogte en optische scope-gap

Deze stap verwerkt de visuele observaties na stap 53.

## Wijzigingen

- EHM-hoogte blijft ongewijzigd.
- Filler-lines staan niet meer op EHM-hoogte, maar op tekst/dash-hoogte.
- Er komt een kleine optische gap tussen aanpalende gemodificeerde scopes.
- Dit moet overlap zoals `me{\\de}{/eeu_}wi{\ge}` verminderen.
- Single-EHM glyphbreedte blijft gecapt op accentbreedte.

## Test

```cmd
scripts\retry.cmd vsa-step54-filler-and-optical-gap.zip
```
