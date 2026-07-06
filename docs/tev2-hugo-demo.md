# TEv2 in de Hugo-demo

De Hugo-demo in `examples/hugo-demo` is ingericht als TEv2 scope met een
Scope Administration File (`saf.yaml`), TEv2 toolconfiguratie
(`terminology-config.yaml`), curated texts in
`content-source/terminologie/`, en een glossariumbron in
`content-source/glossarium.md`.

## Tools

De benodigde TEv2 CLI-tools zijn npm dev-dependencies:

- `@tno-terminology-design/mrgt`
- `@tno-terminology-design/hrgt`
- `@tno-terminology-design/trrt`
- `@tno-terminology-design/mrg-import`

Ze zijn gepind op `1.2.0`, omdat dat de nieuwste gepubliceerde npm-versie is.
De TEv2 tools-repository bevat inmiddels nieuwere bronversies, maar die zijn op
dit moment niet als npm package beschikbaar.

## Commando's

Gebruik vanuit de repository-root:

```cmd
npm install
npm run tev2:mrgt
npm run tev2:hrgt
npm run tev2:trrt
```

Of voer de hele TEv2-stap voor de Hugo-demo uit:

```cmd
npm run tev2:hugo
```

De bestaande Hugo-build roept `scripts\tev2-hugo.cmd` aan nadat VSA de
gegenereerde Markdown heeft gemaakt en voordat Hugo de site bouwt.

## Pipeline

1. MRGT leest `examples/hugo-demo/saf.yaml` en de curated texts in
   `examples/hugo-demo/content-source/terminologie`, en genereert MRG-bestanden in
   `examples/hugo-demo/glossaries`.
   Niet-term pagina's zoals `_index.md` hebben `excludeFromMRG: yes`, zodat ze
   wel Hugo-content zijn maar niet in de MRG terechtkomen. Het top-level
   glossarium staat buiten de curatedir en wordt daarom niet door MRGT gelezen.
2. HRGT verwerkt MRGRefs in `generated/hugo/content/glossarium.md` en eventuele
   MRGRefs onder `generated/hugo/content/terminologie/**/*.md`.
3. TRRT verwerkt TermRefs in `generated/hugo/content/**/*.md`, zodat de Hugo-site
   links en hoverteksten uit de TEv2 MRG gebruikt.

De gegenereerde MRG-bestanden en `generated/` output worden niet gecommit.
