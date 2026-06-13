# VSA Rendering Configuration Model (Draft 1)

## 1. Doel

Dit document beschrijft het configuratiemodel voor VSA-rendering.

Het document definieert:

- configuratiebronnen;
- overridevolgorde;
- themes;
- geldigheidscontrole;
- rendererdiagnostics;
- toekomstige uitbreidbaarheid.

---

# 2. Configuratielagen

De effectieve renderingconfiguratie wordt opgebouwd uit lagen.

Volgorde:

```text
1. ingebouwde defaults
2. theme defaults
3. projectconfig
4. user override
5. CLI override
```

Latere lagen overschrijven eerdere lagen.

---

# 3. Ingebouwde defaults

De renderer bevat ingebouwde defaults voor:

- font;
- font-size;
- line-gap;
- spacing;
- glyphkleuren;
- glyphbreedtes;
- pitchmarkerstijl;
- wrappingtokens;
- fallbackgedrag.

Rendering moet ook zonder configbestand werken.

---

# 4. Themes

Een theme is een benoemde set renderingkeuzes.

Voorbeelden:

```text
default
liturgikon
minimal
debug
high-contrast
```

Themes mogen instellen:

- kleuren;
- glyphvormen;
- spacing;
- line-gap;
- connectorstijl;
- pitchmarkerstijl;
- debugvisualisatie.

Themes mogen niet wijzigen:

- VSA-syntax;
- parsergedrag;
- semantische betekenis.

---

# 5. Projectconfig

Projectconfiguratie staat standaard in:

```text
vsa.toml
```

Voorbeeld:

```toml
[rendering.svg]
theme = "liturgikon"
alignment = "left"
font-family = "Noto Serif"
font-size = 24
max-line-width = 900
```

---

# 6. User override

Een user override is bedoeld voor lokale voorkeuren.

Voorbeelden:

- groter font;
- high contrast;
- andere kleuren;
- debugtheme.

Deze laag hoort niet noodzakelijk in Git.

---

# 7. CLI override

CLI overrides hebben hoogste prioriteit.

Voorbeelden:

```cmd
vsa svg input.vsa output.svg --font-size 28
vsa build-markdown content generated static\vsa --config vsa.toml
```

CLI overrides moeten beperkt blijven tot veelgebruikte opties.

---

# 8. Merge-regels

Configuratie wordt deep-merged.

Voorbeeld:

```toml
[rendering.svg.glyphs.upper]
color = "black"
width-factor = 0.60
```

Een override:

```toml
[rendering.svg.glyphs.upper]
color = "blue"
```

wijzigt alleen `color`.

`width-factor` blijft uit de vorige laag bestaan.

---

# 9. Config-validatie

Voor rendering wordt de effectieve config gevalideerd.

Ongeldig:

- negatieve afstanden;
- nulbreedte glyphs;
- onbekende alignmentwaarden;
- lege fontnaam;
- lege kleurwaarde;
- line-gap kleiner dan minimum;
- wraptokens die VSA-syntax breken;
- overlappende tokens;
- onbekende fallbackstrategie.

Bij fout:

```text
VSA-RENDER-CONFIG-ERROR
```

Rendering stopt.

---

# 10. Voorbeeldconfig

```toml
[rendering.svg]
theme = "liturgikon"
alignment = "left"
font-family = "Noto Serif"
font-size = 24
max-line-width = 900

[rendering.svg.spacing]
text-gap = 0.20
scope-gap = 0.12
pitch-marker-gap = 0.35

[rendering.svg.lines]
line-gap = 1.35
min-line-gap = 1.15

[rendering.svg.glyphs.upper]
color = "black"
width-factor = 0.60
offset-y = -0.30
stroke-width-factor = 0.055

[rendering.svg.glyphs.lower]
color = "red"
width-factor = 0.80
offset-y = 0.18
stroke-width-factor = 0.055

[rendering.svg.pitch-marker]
gap-before = 0.35
gap-after = 0.35
dash-width-factor = 0.45

[rendering.svg.wrapping.tokens]
forced-line-break = ["[/]", "[*]"]
preferred-break = ["[/?]", "[*?]"]
nonbreaking-start = "[="
nonbreaking-end = "=]"
```

---

# 11. Geldige tokenconfiguratie

Wraptokens en toekomstige layouttokens moeten:

- niet leeg zijn;
- uniek zijn;
- niet ambigu overlappen;
- bestaande VSA-syntax niet breken;
- vóór parser/rendering gevalideerd worden.

Ongeldig:

```toml
[rendering.svg.wrapping.tokens]
forced-line-break = ["[:]"]
```

Omdat `[:]` al een pitchmarker is.

---

# 12. Rendererdiagnostics

Configvalidatie produceert diagnostics.

Voorbeelden:

| Code | Betekenis |
|---|---|
| `VSA-RENDER-CONFIG-ERROR` | ongeldige config |
| `VSA-RENDER-UNKNOWN-THEME` | theme bestaat niet |
| `VSA-RENDER-INVALID-TOKEN` | token breekt syntax |
| `VSA-RENDER-INVALID-COLOR` | kleurwaarde ongeldig |

---

# 13. Theme inheritance

Themes mogen erven.

Voorbeeld:

```text
liturgikon-high-contrast
→ liturgikon
→ defaults
```

Theme inheritance gebruikt dezelfde deep-merge regels.

Cyclische theme inheritance is ongeldig.

---

# 14. Future-proofing

Het configuratiemodel moet later uitbreidbaar zijn voor:

- MusicXML;
- SATB;
- editorintegratie;
- interactive SVG;
- printprofielen;
- custom glyphsets.

Nieuwe secties mogen worden toegevoegd zonder bestaande config te breken.

---

# 15. Open ontwerpvragen

Nog nader uit te werken:

- locatie van user override;
- distributie van themes;
- schemaformaat;
- JSON-schema of TOML-schema;
- CLI-optiebeleid;
- theme packaging.
