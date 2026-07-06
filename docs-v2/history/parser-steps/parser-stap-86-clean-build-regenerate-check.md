# Stap 86 - clean Hugo build, SVG regeneratie, linkcheck

## Probleem

De linkchecker vond HTML-verwijzingen naar SVG's die niet bestaan.

## Buildvolgorde

De build moet zijn:

```text
public opschonen
navigatie-placeholders bijwerken
Hugo build
ontbrekende VSA SVG's regenereren
link/assets checken
```

## Scripts

```cmd
python scripts\clean-hugo-public.py
python scripts\regenerate-missing-vsa-images.py
python scripts\check-hugo-links-and-assets.py
```
