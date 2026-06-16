# Stap 71 - Hugo index-navigatie

Stap 68 probeerde navigatie toe te voegen door alle pagina's te herschrijven.
Dat was te grof.

Stap 71 doet het voorzichtiger:

- `_index.md` per relevante map;
- overzicht van child-mappen en child-pagina's;
- alleen een klein navigatieblok op de homepagina;
- geen injectie in alle voorbeeldpagina's.

## Script

```cmd
python scripts\apply-step71-hugo-index-navigation.py
```

## Controle

```cmd
python -m pytest tests\test_step71_hugo_index_navigation.py -v
```
