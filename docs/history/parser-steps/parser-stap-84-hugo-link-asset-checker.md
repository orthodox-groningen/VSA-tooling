# Stap 84 - Hugo link- en assetchecker

Na de Hugo-build controleert `scripts\check-hugo-links-and-assets.py` de gegenereerde `public` site.

Controleert:

- interne `href` links;
- `<img src>` assets;
- ontbrekende SVG's;
- oude routes zoals `/zondag/` en `/voorbeelden/praktijk/`.
