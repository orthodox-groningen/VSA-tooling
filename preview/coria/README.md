# Coria HTML-bestanden (handmatig)

Plaats Coria-export-HTML **naast het bijbehorende `.vsa`-bestand** in content-source,
met extensie **`.coria.html`**:

```text
content-source/praktijk/zondagen/
  tropaar-zondag-toon-3.vsa
  tropaar-zondag-toon-3.coria.html   ← uit Coria downloaden
  zondag-toon-3.md
```

`vsa build-markdown` kopieert deze naar `static/coria/…/tropaar-zondag-toon-3.html`.

In Markdown (zelfde map als het `.vsa`-bestand):

```markdown
:::coria "tropaar-zondag-toon-3.vsa" label="Oefenen in Coria":::
```

Zie [docs/guides/musicxml-export.md](../../../../docs/guides/musicxml-export.md).
