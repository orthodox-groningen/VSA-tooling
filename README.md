# VSA stap 16 - SVG autosizing

Deze stap verbetert de SVG-renderer.

Voorheen:

```text
width="1200"
```

Nu:

```text
width = berekende inhoudsbreedte + marges
```

Voordelen:

- SVG's worden minder breed dan nodig;
- beter bruikbaar in Markdown/Hugo;
- output past beter bij korte zangregels;
- latere layoutstappen worden eenvoudiger.

Nog niet inbegrepen:

- automatische regelafbreking;
- responsive CSS;
- exacte fontmeting.
