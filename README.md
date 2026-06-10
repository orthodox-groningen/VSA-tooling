# VSA stap 11 - Markdown build met SVG-verwijzingen

Deze stap voegt een nieuw commando toe:

```cmd
vsa build-markdown input-dir output-dir assets-dir
```

Doel:

```text
content/*.md met ::: vsa-notatie
  ↓
validatie
  ↓
SVG genereren
  ↓
Markdown kopiëren/herschrijven
  ↓
output Markdown met <img src="...">
```

Dit is een praktische Hugo-route:

```text
content-source/
  ↓
vsa build-markdown
  ↓
content-generated/
  ↓
hugo build
```

Nog niet inbegrepen:

- Hugo shortcodes;
- render hooks;
- finale SVG-layout.
