# Stap 78 - alleen navigatieblokken in `_index.md`

## Besluit

`_index.md` pagina's zijn redactionele content.

Buildscripts mogen daarom niet de volledige `_index.md` overschrijven.

## Wel automatisch

Alleen een expliciet afgebakend navigatieblok:

```html
<!-- VSA-INDEX-NAV-START -->
...
<!-- VSA-INDEX-NAV-END -->
```

mag automatisch worden bijgewerkt.

## Scripts

```cmd
python scripts\update-index-navigation-blocks.py
python scripts\apply-step78-index-nav-blocks-only.py
```

## Vervangt

- `apply-step71-hugo-index-navigation.py`
- `apply-step75-navigation-praktijk-moved.py`

Die scripts schreven te veel redactionele inhoud.
