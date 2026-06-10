# VSA stap 4 - Markdown blokken

Deze stap voegt ondersteuning toe voor VSA-blokken in Markdown:

```markdown
::: vsa-notatie
do="F4"
mode="major"

[:] {tekst} [:]
:::
```

Ondersteund:

- VSA-blokken vinden in Markdown;
- blokmetadata parsen;
- defaultwaarden toepassen;
- VSA-body doorgeven aan de bestaande parser;
- CLI-commando `blocks` toevoegen.

Nog niet inbegrepen:

- SVG-rendering;
- MusicXML-export;
- Hugo build integratie.
