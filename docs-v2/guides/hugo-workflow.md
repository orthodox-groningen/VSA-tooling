# Hugo-workflow

Deze pagina beschrijft de gebruikerskant van de Hugo-demo.

## Hoofdindeling

```text
content-source/
├── kerkmuziek-tradities/
├── liturgikon-notatie/
├── zangstuk-identificatie/
├── lokaal/
├── sjablonen/
├── samenstellingen/
├── voorbeelden/
└── praktijk/
```

## Buildgedrag

`build-markdown` slaat deze mappen over:

```text
sjablonen/
samenstellingen/
```

De workflow is:

```text
vsa resolve-catalogus
  ↓
opgeloste inhoud kopiëren naar publishbare map
  ↓
vsa build-markdown
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

Gegenereerde blokken niet handmatig aanpassen.

## Pagina uitsluiten van navigatie

```yaml
vsa_nav_exclude: true
```

## Bronnen

Gebaseerd op:

- `docs/hugo-site-structure.md`
- `docs/hugo-navigation-placeholders.md`
- `docs/user-guide.md`
