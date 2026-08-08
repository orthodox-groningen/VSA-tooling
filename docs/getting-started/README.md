# Overzicht

Doel: snel controleren of de [VSA-tooling](@bron) lokaal werkt. Uitgebreidere
uitleg: [Gebruikershandleiding](../guides/user-guide.md).

## 1. Repo-root

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
```

## 2. Omgeving

```cmd
scripts\bootstrap.cmd
```

## 3. Installatie controleren

```cmd
vsa --version
```

Verwachte vorm: `vsa 0.1.0` (of hoger).

## 4. Valideren

De [validator](@) controleert of [VSA-notatie](@bron) bruikbaar is
([`vsa validate`](../reference/cli/validate.md)):

```cmd
vsa validate examples\minimal\001_plain_text.vsa
```

Bij succes: `OK`.

## 5. SVG genereren

Met [`vsa svg`](../reference/cli/svg.md) (zelfde schone demo; rijkere
SVG-voorbeelden zoals `050_svg_demo.vsa` mogen op `validate` falen — zie
[`vsa svg`](../reference/cli/svg.md)):

```cmd
vsa svg examples\minimal\001_plain_text.vsa generated\vsa\001_plain_text.svg
```

## Volgende stappen

| Doel                                      | Pagina                                              |
| ----------------------------------------- | --------------------------------------------------- |
| Brede uitleg van de CLI                   | [Gebruikershandleiding](../guides/user-guide.md)    |
| Het juiste commando per taak              | [CLI-taken](../guides/cli-taken.md)                 |
| Foutmeldingen begrijpen                   | [Validatie](../guides/validation.md)                |
| Tool hergebruiken in een andere repo      | [Integratie](../integratie/index.md)                |
| Docs lokaal met TermRefs                  | [TEv2 in tool-docs](../guides/tev2-docs.md)         |
