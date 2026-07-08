# Stap 64 - real font metrics

Deze stap introduceert echte font metrics via Pillow als dat beschikbaar is.

## Waarom

De renderer gebruikte tot nu toe geschatte tekstbreedtes.
Dat veroorzaakte:

- overlap;
- ongelijkmatige spacing;
- onvoorspelbare wrapping;
- noodzaak tot heuristische tuning.

## Nieuwe aanpak

`src/vsa/text_metrics.py` probeert eerst echte tekstmeting:

```python
ImageDraw.textlength(text, font=font)
```

Als Pillow of het font niet beschikbaar is, valt de code terug op de estimator uit stap 62.

## Volgende tuning

Na deze stap kan typografische tuning beter gebaseerd worden op echte maten:

- scope-gaps;
- filler-lengtes;
- EHM/ELM positionering;
- compacte woordclusters.
