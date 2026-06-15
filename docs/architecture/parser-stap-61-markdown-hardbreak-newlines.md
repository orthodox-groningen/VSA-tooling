# Stap 61 - Markdown hardbreak newlines

De toon-8 bestanden gebruiken Markdown hardbreaks: twee spaties vóór newline.

Voorbeelden in de bron:

```markdown
... {\ge_}.  
Drie ...
```

Binnen `vsa-notatie` is dat geen extra muzikale of typografische inhoud.
De twee spaties moeten vóór rendering worden verwijderd, terwijl de newline
als harde VSA-regelgrens behouden blijft.

## Wijziging

- `preserve_vsa_source_newlines()` stript trailing whitespace vóór newline.
- `split_text_node()` doet dezelfde defensieve normalisatie.
- regressietests voor toon-8-achtige bron.
