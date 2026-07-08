# Stap 80 - retire step78 navigation model

## Besluit

Stap 78 is vervangen door stap 79.

Stap 78 gebruikte:

```html
<!-- VSA-INDEX-NAV-START -->
<!-- VSA-INDEX-NAV-END -->
```

Stap 79 gebruikt expliciete placeholders:

```html
<!-- VSA-NAV:HOME -->
<!-- VSA-NAV:UP -->
<!-- VSA-NAV:SIBLINGS -->
<!-- VSA-NAV:CHILDREN -->
<!-- VSA-NAV:PAGES -->
```

## Reden

Stap 79 is explicieter:

- gebruiker bepaalt zelf waar navigatie komt;
- werkt voor `_index.md` en gewone `.md`;
- scripts overschrijven geen redactionele content;
- alleen gegenereerde blokken onder placeholders worden aangepast.

## Testwijziging

`tests/test_step78_index_nav_blocks_only.py` controleert nu alleen nog dat het oude model niet meer leidend is.
