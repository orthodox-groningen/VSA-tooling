# Stap 68 - TODO en Hugo navigatie

## TODO

Toegevoegd aan `docs/todo.md`:

- woord-georiënteerde SVG-layout;
- huidige segment-gebaseerde renderer is bruikbaar maar laat kleine kieren binnen woorden;
- later onderzoeken als grotere rendererarchitectuurstap.

## Hugo navigatie

Toegevoegd script:

```cmd
python scripts\apply-step68-todo-and-navigation.py
```

Het script voegt aan markdownpagina's onder `examples/hugo-demo/content-source` een navigatieblok toe met:

- Home;
- Omhoog;
- sibling-pagina's in dezelfde map.

De blokken zijn gemarkeerd met:

```html
<!-- VSA-NAV-START -->
<!-- VSA-NAV-END -->
```
