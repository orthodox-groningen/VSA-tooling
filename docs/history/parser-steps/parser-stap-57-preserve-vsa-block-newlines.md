# Stap 57 - preserve VSA block newlines

Deze stap adresseert het verschil tussen voorbeelden waar bron-newlines wel
of niet zichtbaar doorwerken in de SVG-rendering.

## Probleem

De SVG-layout respecteert inmiddels `CR`, `LF` en `CRLF`, maar de aanvoer vanuit
Markdown/Hugo kan newlines eerder al normaliseren naar spaties.

## Wijziging

Toegevoegd:

- `src/vsa/markdown_vsa_blocks.py`
- `src/vsa/markdown_newline_policy.py`
- tests voor newline-preservatie
- apply/check-script voor verdachte `" ".join(...)` normalisatie

## Belangrijk

VSA-source mag nooit via `" ".join(lines)` worden doorgegeven aan de parser of renderer.
Gebruik newline-preservatie:

```python
"\n".join(lines)
```

of geef de ruwe blocktekst door.
