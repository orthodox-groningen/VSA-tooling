# Volgende stap na stap 43

Maak JSON-output voor diagnostics.

Bijvoorbeeld:

```cmd
vsa validate bestand.vsa --json
```

met output:

```json
{
  "ok": false,
  "messages": [
    {
      "code": "VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER",
      "severity": "error",
      "category": "semantic",
      "hint_nl": "Vervang de afsluitende [:] door [\\\\:]."
    }
  ]
}
```
