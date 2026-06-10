# Stap 30 - static assets fix

De demo-site toonde wel tekst en invoer, maar geen SVG-plaatjes.

Oorzaak:

```text
<img src="/vsa/voorbeeld.svg">
```

verwijst naar een URL onder Hugo static output.

Maar de SVG-bestanden stonden niet in:

```text
examples/hugo-demo/static/vsa
```

Daardoor kopieerde Hugo ze niet mee naar de site.

De scripts schrijven SVG's nu naar:

```text
examples/hugo-demo/static/vsa
```

Hugo publiceert die dan als:

```text
/vsa/...
```
