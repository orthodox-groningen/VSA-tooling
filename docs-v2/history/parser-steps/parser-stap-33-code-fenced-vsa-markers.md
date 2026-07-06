# Stap 33 - VSA markers in Markdown-codeblokken negeren

Probleem:

Een documentatievoorbeeld zoals:

````markdown
```markdown
::: vsa-notatie
{voorbeeld}
:::
```
````

werd toch verwerkt als echt VSA-blok.

Oorzaak:

De block parser zocht puur naar:

```text
::: vsa-notatie
```

zonder rekening te houden met fenced codeblocks.

Fix:

- `parse_markdown_blocks()` houdt code fences bij;
- `build-markdown` doet hetzelfde tijdens herschrijven;
- markers binnen ``` of ~~~ worden genegeerd;
- alleen echte VSA-blokken buiten code fences worden SVG.
