# Parser stap 1

Deze stap maakt van [VSA](@)-brontekst een eenvoudige [AST](@).

Ondersteunde nodes:

```text
Document
TextNode
ScopeNode
PitchMarkerNode
```

Voorbeeld:

```text
{/tekst_}
```

wordt:

```json
{
  "type": "Document",
  "nodes": [
    {
      "type": "ScopeNode",
      "height_modifier": ["/"],
      "text": "tekst",
      "length_modifier": ["_"]
    }
  ]
}
```

## Bewijs dat het werkt

```cmd
scripts\test.cmd
```

En:

```cmd
.venv\Scripts\activate
vsa examples\minimal\013_height_and_length.vsa --ast
```
