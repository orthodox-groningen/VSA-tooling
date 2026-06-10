# VSA stap 21 fix - shortcode opt-in

Deze patch herstelt backwards compatibility.

Probleem:

- `build_markdown_site()` gebruikte ineens standaard `shortcode`;
- bestaande tests en bestaande workflow verwachten standaard `<img>`.

Fix:

- default output blijft `img`;
- shortcode blijft beschikbaar via:

```cmd
--output-mode shortcode
```

Dus:

```cmd
vsa build-markdown ...
```

geeft `<img>`.

En:

```cmd
vsa build-markdown ... --output-mode shortcode
```

geeft Hugo-shortcodes.
