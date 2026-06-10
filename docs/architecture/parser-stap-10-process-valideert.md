# Stap 10 - process valideert vóór SVG-generatie

Deze stap maakt `vsa process` geschikt voor CI.

## Gedrag

```cmd
vsa process content generated\vsa
```

doet nu:

```text
1. alle Markdownbestanden zoeken
2. alle VSA-blokken valideren
3. bij fouten stoppen
4. alleen bij OK SVG-bestanden genereren
```

## Waarom

Een buildproces mag geen site genereren op basis van ongeldige VSA.

Daarom is dit gedrag belangrijk voor:

- Hugo;
- GitHub Actions;
- lokale controle vóór commit.
