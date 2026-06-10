# VSA stap 23 - Hugo workflow en GitHub Actions

Deze stap voegt een echte build-workflow toe.

Nieuw:

- `scripts/build-hugo.cmd`
- `scripts/serve-hugo.cmd`
- `.github/workflows/hugo.yml`
- voorbeeld `package.json`
- voorbeeld Hugo config
- voorbeeld Hugo directory-structuur

Doel:

```text
Markdown met VSA
    ↓
vsa build-markdown
    ↓
gegenereerde Hugo content + SVG
    ↓
hugo
    ↓
site
```

Hiermee wordt de repo bruikbaar voor:

- lokale Hugo preview;
- GitHub Actions preview builds;
- productie builds.
