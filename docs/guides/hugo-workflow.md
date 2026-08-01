# Hugo-workflow

Deze pagina beschrijft de gebruikerskant van de Hugo-demo.

## Hoofdindeling

```text
content-source/
├── kerkmuziek-tradities/
├── liturgikon-notatie/
├── zangstuk-identificatie/
├── lokaal/
├── voorbeelden/
└── praktijk/
```

## Buildgedrag

`build-markdown` verwerkt bron-Markdown en genereert publiceerbare Hugo-content.

```text
content-source
  ↓
vsa build-markdown
  ↓
content + static assets
  ↓
Hugo build
```

## Navigatie-placeholders

Plaats expliciete markers waar automatisch gegenereerde navigatie moet komen.

```html
<!-- VSA-NAV:HOME -->
<!-- VSA-NAV:UP -->
<!-- VSA-NAV:SIBLINGS -->
<!-- VSA-NAV:CHILDREN -->
<!-- VSA-NAV:PAGES -->
<!-- VSA-NAV:PAGES-HERE -->
```

Gegenereerde navigatieblokken niet handmatig aanpassen.

## Pagina uitsluiten van navigatie

```yaml
vsa_nav_exclude: true
```

## Lokale preview

```cmd
scripts\build-hugo.cmd
```

```cmd
scripts\serve-hugo.cmd
```

## Bronnen

Gebaseerd op:

- [hugo-site-structure.md](hugo-site-structure.md)
- [hugo-navigation-placeholders.md](hugo-navigation-placeholders.md)
- [user-guide.md](user-guide.md)
