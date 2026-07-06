# Stap 8 - Markdown verwerken naar SVG

Deze stap introduceert:

```cmd
vsa process input.md output-dir
```

Het commando:

1. leest een Markdownbestand;
2. vindt alle `::: vsa-notatie` blokken;
3. rendert elk blok naar SVG;
4. schrijft SVG-bestanden naar de opgegeven uitvoermap.

## Waarom dit belangrijk is

Dit is de technische brug naar Hugo.

Voor Hugo wil je uiteindelijk:

```text
content/*.md
  ↓
vsa process
  ↓
assets/generated-vsa/*.svg
  ↓
hugo build
```

Nog niet opgelost:

- automatisch Markdown herschrijven;
- links naar gegenereerde SVG invoegen;
- shortcode/render-hook strategie.
