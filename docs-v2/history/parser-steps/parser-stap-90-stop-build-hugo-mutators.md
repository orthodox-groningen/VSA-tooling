# Stap 90 - stop build-hugo mutators

## Probleem

Oude apply-scripts bleven `scripts\build-hugo.cmd` muteren.

Specifiek konden regels zoals deze midden in het `hugo ^` blok terechtkomen:

```cmd
python scripts\regenerate-missing-vsa-images.py
python scripts\check-hugo-links-and-assets.py
```

## Besluit

Deze oude apply-scripts zijn nu gedeactiveerd:

```text
scripts\apply-step76-regenerate-missing-vsa-images.py
scripts\apply-step84-hugo-link-asset-checker.py
scripts\apply-step86-clean-build-regenerate-check.py
```

Ze blijven bestaan voor historische tests, maar wijzigen geen bestanden meer.
