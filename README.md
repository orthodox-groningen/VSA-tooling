# VSA stap 8 - Markdown verwerken naar SVG

Deze stap voegt een eerste `process` commando toe.

Doel:

```text
Markdown met ::: vsa-notatie blokken
  ↓
VSA parser
  ↓
SVG renderer
  ↓
gegenereerde SVG-bestanden
```

Dit is de eerste echte stap richting Hugo-integratie.

## Voorbeeld

```cmd
vsa process examples\minimal\031_markdown_block_metadata.md generated\vsa
```

Dat maakt bijvoorbeeld:

```text
generated\vsa\031_markdown_block_metadata-block-1.svg
```

Nog niet inbegrepen:

- Markdown herschrijven;
- shortcodes invoegen;
- Hugo render hooks;
- nette SVG-layout.
