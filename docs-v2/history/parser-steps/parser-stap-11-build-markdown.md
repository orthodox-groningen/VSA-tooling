# Stap 11 - Markdown build met SVG-verwijzingen

Deze stap introduceert:

```cmd
vsa build-markdown content-source content-generated static\vsa
```

Het commando:

1. valideert alle Markdownbestanden;
2. genereert SVG-bestanden;
3. schrijft nieuwe Markdownbestanden;
4. vervangt VSA-blokken door `<img>` verwijzingen.

## Hugo-route

Voor lokaal testen met Hugo:

```text
content-source/
  ↓
vsa build-markdown
  ↓
content-generated/
  ↓
hugo build met contentDir = content-generated
```

Of eenvoudiger:

```text
content-source/
  ↓
vsa build-markdown
  ↓
content/
```

waarbij `content/` gegenereerd is en niet handmatig bewerkt wordt.
