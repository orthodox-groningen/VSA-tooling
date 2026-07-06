# Stap 75 - navigatie na verplaatsen praktijk

De praktijkvoorbeelden staan nu op:

```text
examples\hugo-demo\content-source\praktijk
```

Niet meer op:

```text
examples\hugo-demo\content-source\voorbeelden\praktijk
```

## Wijzigingen

- home-navigatie linkt naar `./praktijk/`;
- `_index.md` voor `praktijk`;
- link/asset checker voor gegenereerde Hugo output.

## Scripts

```cmd
python scripts\apply-step75-navigation-praktijk-moved.py
python scripts\check-hugo-links-and-assets.py
```
