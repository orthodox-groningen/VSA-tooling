# Parser stap 4 - Markdown blokken

Deze stap haalt VSA-blokken uit Markdown.

Doel:

```text
Markdown
  ↓
parse_markdown_blocks()
  ↓
VSABlock[]
  ↓
Parser(block.body)
  ↓
AST
```

Een blok bevat:

```text
metadata
body
start_line
end_line
```

De metadata krijgt defaultwaarden uit de specificatie:

```text
do="F4"
mode="major"
tempo="100"
validate-ending="true"
duration-model="default"
```

Dit is de basis voor latere Hugo-integratie.
