# Hugo navigatie-placeholders

## Doel

Navigatie in de Hugo-demo wordt niet meer gedaan door volledige pagina's te genereren.

De markdownpagina blijft redactionele content. Alleen expliciete navigatie-placeholders worden automatisch ingevuld.

Dit geldt voor:

- `_index.md`;
- gewone `.md` pagina's.

## Basisprincipe

Plaats handmatig een marker op de plek waar je navigatie wilt.

Voorbeeld:

```markdown
# Praktijkvoorbeelden

Eigen introductietekst.

<!-- VSA-NAV:HOME -->
<!-- VSA-NAV:UP -->
<!-- VSA-NAV:SIBLINGS -->
<!-- VSA-NAV:CHILDREN -->
<!-- VSA-NAV:PAGES -->
<!-- VSA-NAV:PAGES-HERE -->
```

Daarna vult het buildscript direct onder elke marker een gegenereerd blok in.

## Beschikbare markers

### Home

```html
<!-- VSA-NAV:HOME -->
```

Genereert een link naar de homepage van de demo.

### Omhoog

```html
<!-- VSA-NAV:UP -->
```

Genereert een link naar de bovenliggende sectie.

### Siblings

```html
<!-- VSA-NAV:SIBLINGS -->
```

Genereert links naar pagina's en secties op hetzelfde niveau.

De huidige pagina zelf wordt overgeslagen.

### Children

```html
<!-- VSA-NAV:CHILDREN -->
```

Genereert links naar onderliggende secties, dus submappen met een `_index.md`.

### Pages

```html
<!-- VSA-NAV:PAGES -->
```

Genereert links naar gewone `.md` pagina's in dezelfde map.

Als een map én een pagina dezelfde naam hebben, bijvoorbeeld `cli.md` en `cli/_index.md`, krijgt de sectie voorrang.

### Pages-Here

```html
<!-- VSA-NAV:PAGES-HERE -->
```

Genereert links naar bestanden (geen mappen) met de extensi `.md` in dezelfde map (uitgezonderd `_index.md`).

## Pagina of sectie uit navigatie houden

Zet dit in de frontmatter:

```yaml
vsa_nav_exclude: true
```

Dat is bedoeld voor interne demo-bronnen, zoals tijdelijk of historisch voorbeeldmateriaal dat niet in de normale navigatie hoort.

## Gegenereerde blokken

Het script maakt blokken zoals:

```html
<!-- VSA-NAV-GENERATED:HOME-START -->
...
<!-- VSA-NAV-GENERATED:HOME-END -->
```

Pas deze gegenereerde inhoud niet handmatig aan.

Je mag wel:

- markers verwijderen;
- markers verplaatsen;
- markers toevoegen;
- redactionele tekst erboven/eronder aanpassen.

## Buildscript

De build hoort dit script aan te roepen:

```cmd
python scripts\update-nav-placeholders.py
```

## Stabilisatie

Voor opschonen van oude navigatie-artefacten:

```cmd
python scripts\stabilize-hugo-navigation.py
```

## Verouderd model

Dit oude model is vervangen en moet niet meer gebruikt worden:

```html
<!-- VSA-INDEX-NAV-START -->
<!-- VSA-INDEX-NAV-END -->
```
