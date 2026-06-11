# Stap 37 - optie A: semantiek blijft error

Deze patch kiest de conservatieve route.

Wat blijft:

- `Diagnostic.severity`;
- `DiagnosticCollection.has_warnings()`;
- `ValidationMessage.severity`;
- infrastructuur voor latere configureerbare severities.

Wat verandert terug:

- semantische diagnostics zijn voorlopig weer `error`;
- `ValidationResult.ok` wordt dus weer `False` bij semantische fouten;
- `process_markdown` faalt weer vóór SVG-generatie bij semantische fouten;
- bestaande tests en CI-logica blijven stabiel.

Later kunnen we per foutcode configureerbaar maken:

```toml
[vsa.validation]
VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER = "warning"
```
