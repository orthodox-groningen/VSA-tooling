# Stap 79 - expliciete navigatie-placeholders

## Besluit

Navigatie wordt niet meer automatisch in volledige pagina's geschreven.

De gebruiker plaatst expliciete markers:

```html
<!-- VSA-NAV:HOME -->
<!-- VSA-NAV:UP -->
<!-- VSA-NAV:SIBLINGS -->
<!-- VSA-NAV:CHILDREN -->
<!-- VSA-NAV:PAGES -->
```

De build vult alleen het bijbehorende gegenereerde blok onder die marker.

## Documentatie

Gebruikersdocumentatie staat in:

```text
docs/hugo-navigation-placeholders.md
```

## Scripts

```cmd
python scripts\migrate-index-navigation-placeholders.py
python scripts\update-nav-placeholders.py
python scripts\apply-step79-explicit-nav-placeholders.py
```

## Belangrijk

- redactionele tekst blijft ongemoeid;
- werkt op `_index.md` en gewone `.md`;
- gegenereerde inhoud is afgebakend met `VSA-NAV-GENERATED:*`.
