# Stap 27 - preview en productie

Deze stap maakt onderscheid tussen:

```text
preview
production
```

## Preview

```cmd
scripts\build-preview.cmd
```

Doel:

- snel controleren;
- demo bekijken;
- geschikt voor GitHub Pages.

## Production candidate

```cmd
scripts\build-production.cmd
```

Doel:

- productieachtige output;
- minified Hugo build;
- bredere SVG-regelbreedte.

## GitHub Actions

Handmatig starten:

```text
Actions → Build target → Run workflow
```

Kies:

```text
preview
production
```

Voorlopig wordt productie nog alleen als artifact gemaakt, niet automatisch gepubliceerd.
