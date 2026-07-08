# Stap 69 - herstel kapotte navigatie

Stap 68 voegde navigatieblokken rechtstreeks in alle Hugo contentpagina's in.
Dat bleek te grof en kon links of SVG assetverwijzingen breken.

## Herstel

```cmd
python scripts\revert-step68-navigation.py
```

Dit verwijdert alle blokken tussen:

```html
<!-- VSA-NAV-START -->
<!-- VSA-NAV-END -->
```

## Besluit

Navigatie later opnieuw aanpakken via:

- handmatige overzichtspagina's;
- `_index.md` per map;
- Hugo templates;
- tests op concrete links en concrete gegenereerde assetpaden.

Niet meer blind elke pagina herschrijven.
