# VSA stap 34 - GitHub Pages SVG URL fix

Probleem op GitHub Pages:

```text
https://orthodox-groningen.github.io/vsa/...
```

maar de site staat onder:

```text
https://orthodox-groningen.github.io/VSA-tooling/
```

Dus de SVG moet worden:

```text
https://orthodox-groningen.github.io/VSA-tooling/vsa/...
```

Oorzaak:

- `vsa build-markdown` genereert shortcode-bron met `src="/vsa/..."`;
- de shortcode gaf die URL door aan `relURL`;
- met een voorloopslash blijft de URL domein-root gericht.

Fix:

- de shortcode verwijdert eerst de voorloopslash;
- daarna wordt `relURL` toegepast.

Daardoor werkt zowel lokaal als op GitHub Pages.
