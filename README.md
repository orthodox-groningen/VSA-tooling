# VSA stap 27 - preview en productie scheiden

Deze stap bereidt preview/productie-publicatie voor.

Nieuw:

- aparte build scripts voor preview en productie;
- aparte GitHub Actions workflow met keuze `preview` of `production`;
- productie draait standaard nog zonder automatische publicatie;
- preview blijft geschikt voor GitHub Pages demo.

Doel:

```text
preview     = veilig testen
production  = later echte site-output
```
