# Stap 100 - marker-only navigatiegeneratie

`content-source` is redactionele broncontent.

Scripts mogen daarin niet automatisch frontmatter, titels, headings of vrije markdown herschrijven.

Alleen dit mag worden vervangen of ingevoegd:

```text
<!-- VSA-NAV:<TYPE> -->
<!-- VSA-NAV-GENERATED:<TYPE>-START -->
...
<!-- VSA-NAV-GENERATED:<TYPE>-END -->
```

`build-hugo.cmd` draait navigatiegeneratie alleen op `generated\hugo\content`.
