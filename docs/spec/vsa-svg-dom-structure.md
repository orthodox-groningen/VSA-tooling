# VSA SVG DOM Structure Specification (Draft 1)

## 1. Doel

Dit document beschrijft de SVG-DOM-structuur voor VSA-rendering.

Doelen:

- consistente SVG-output;
- CSS-stylebaarheid;
- debugbaarheid;
- testbaarheid;
- toekomstige editor- en hoverfunctionaliteit.

Dit document definieert geen visuele stijl. Stijl komt uit renderingconfiguratie en themes.

---

# 2. Basisstructuur

Minimale structuur:

```xml
<svg class="vsa-svg" xmlns="http://www.w3.org/2000/svg">
  <g class="vsa-score">
    <g class="vsa-line">
      <g class="vsa-unit">
        ...
      </g>
    </g>
  </g>
</svg>
```

---

# 3. Root `<svg>`

De root bevat:

- `class="vsa-svg"`;
- `xmlns`;
- `viewBox`;
- `width` en/of `height` indien nodig;
- optioneel `role="img"`.

Voorbeeld:

```xml
<svg class="vsa-svg"
     xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 900 120">
</svg>
```

---

# 4. Score group

Alle inhoud staat binnen:

```xml
<g class="vsa-score">
```

Deze groep vertegenwoordigt één gerenderd VSA-document of VSA-blok.

---

# 5. Line groups

Elke renderregel krijgt:

```xml
<g class="vsa-line" data-vsa-line="1">
```

Line groups bevatten render-units.

Line groups mogen via `transform="translate(x y)"` gepositioneerd worden.

---

# 6. Render-unit groups

Elke render-unit krijgt:

```xml
<g class="vsa-unit">
```

Aanbevolen attributen:

```xml
data-vsa-unit="scope"
data-vsa-source-start="..."
data-vsa-source-end="..."
```

Mogelijke unittypes:

| Type | Betekenis |
|---|---|
| `text` | vrije tekst |
| `scope` | zangelement |
| `pitch-marker` | pitchmarker |
| `wrap-token` | niet-zichtbare wrapinstructie |
| `nonbreaking-group` | non-breaking group |

---

# 7. Text nodes

Tekst wordt gerenderd met:

```xml
<text class="vsa-text">...</text>
```

Voor zangelementen kan de gezongen tekst apart worden geclassificeerd:

```xml
<text class="vsa-sung-text">...</text>
```

Vrije tekst:

```xml
<text class="vsa-free-text">...</text>
```

---

# 8. Glyph groups

Glyphs worden gegroepeerd in:

```xml
<g class="vsa-glyph-group">
```

Specifiek:

```xml
<g class="vsa-upper-glyphs">
<g class="vsa-lower-glyphs">
```

Gekoppelde glyphs via `&` staan binnen één glyphgroep.

---

# 9. Individual glyphs

Elke glyph krijgt een semantische klasse.

Voorbeelden:

```xml
<path class="vsa-glyph vsa-upper-glyph vsa-glyph-rise" />
<path class="vsa-glyph vsa-upper-glyph vsa-glyph-fall" />
<line class="vsa-glyph vsa-lower-glyph vsa-glyph-length" />
```

Aanbevolen data-attributen:

```xml
data-vsa-glyph="/"
data-vsa-position="2"
```

---

# 10. Pitchmarkers

Pitchmarkers krijgen:

```xml
<g class="vsa-unit vsa-pitch-marker">
```

Binnen een pitchmarker:

```xml
<line class="vsa-pitch-marker-dash" />
<g class="vsa-pitch-marker-upper-glyph">...</g>
```

`[:]` bevat alleen de compacte markerlijn.

`[/:]` bevat markerlijn plus bovenglyph.

---

# 11. Debug layers

Debug-output mag optionele lagen bevatten:

```xml
<g class="vsa-debug vsa-debug-bounds">
<g class="vsa-debug vsa-debug-anchors">
<g class="vsa-debug vsa-debug-wrap">
```

Debuglagen zijn standaard uitgeschakeld.

---

# 12. CSS-klassen

Minimale CSS-klassen:

```text
vsa-svg
vsa-score
vsa-line
vsa-unit
vsa-text
vsa-free-text
vsa-sung-text
vsa-glyph
vsa-glyph-group
vsa-upper-glyphs
vsa-lower-glyphs
vsa-pitch-marker
vsa-pitch-marker-dash
```

---

# 13. Style strategy

Default mag styling inline zijn voor zelfstandige SVG-output.

Daarnaast moet class-based styling mogelijk blijven.

Aanbevolen:

- geometrie in SVG-attributen;
- kleur/stroke via CSS of theme;
- debugstyling via CSS-klassen.

---

# 14. IDs

Stabiele ids zijn optioneel.

Als ids worden gegenereerd, moeten ze deterministic zijn binnen één rendering.

Aanbevolen vorm:

```text
vsa-line-1
vsa-unit-1-3
vsa-glyph-1-3-2
```

---

# 15. Toekomstige interactiviteit

De structuur moet geschikt blijven voor:

- hover diagnostics;
- source mapping;
- editorselectie;
- synced playback;
- click-to-source;
- debug overlays.

Daarom mogen renderers data-attributen toevoegen zolang ze geen bestaande output breken.

---

# 16. Open ontwerpvragen

Nog nader uit te werken:

- exacte source-map attributen;
- ARIA/accessible SVG;
- CSS packaging;
- interactive mode;
- debug theme classes.
