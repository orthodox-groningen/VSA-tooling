# Stap 43 - rich diagnostics metadata

Diagnostics hebben nu extra velden:

```python
category: str = "general"
hint_nl: str = ""
doc_url: str = ""
```

## Waarom

Dit bereidt voor op:

- betere CLI-output;
- JSON diagnostics;
- demo-site weergave;
- IDE/LSP integratie;
- latere autofix/suggesties.

## Voorbeeld

```text
code      = VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER
category  = semantic
hint_nl   = Vervang de afsluitende [:] door [\\:]
doc_url   = docs/guides/validation.md
```

## Compatibiliteit

Bestaande code die alleen gebruikt:

```python
code
message_nl
line
column
severity
```

blijft werken.
