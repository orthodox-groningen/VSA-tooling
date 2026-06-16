# Stap 72 - fix nested VSA image refs

Bug:

```text
examples\hugo-demo\content-source\voorbeelden\praktijk\weekdagen\woensdag.md
```

genereert SVG:

```text
examples\hugo-demo\public\vsa\voorbeelden-praktijk-weekdagen-woensdag-block-1.svg
```

maar HTML verwees naar:

```html
<img class="vsa-notation" src="/vsa/voorbeelden-praktijk-donderdag-block-1.svg">
```

Deze stap voegt een repair/check-script toe dat VSA image refs baseert op het volledige relatieve pagina-pad.
