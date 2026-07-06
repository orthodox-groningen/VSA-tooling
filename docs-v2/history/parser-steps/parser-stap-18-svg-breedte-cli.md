# Stap 18 - SVG regelbreedte via CLI

Deze stap maakt de maximale SVG-regelbreedte instelbaar.

## Commando's

```cmd
vsa svg input.vsa output.svg --max-line-width 600
vsa process content generated\vsa --max-line-width 600
vsa build-markdown content-source content-generated static\vsa --max-line-width 600
```

## Waarom

De juiste breedte hangt af van de context:

```text
websitekolom  → smaller
desktop       → standaard
print/PDF     → breder
```

De default blijft `800`.
