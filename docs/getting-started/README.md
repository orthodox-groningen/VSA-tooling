# Overzicht

Doel: snel controleren of de VSA-tool lokaal werkt. Uitgebreidere uitleg:
[Gebruikershandleiding](../guides/user-guide.md).

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

```cmd
vsa validate examples\minimal\050_svg_demo.vsa
```

Bij succes: `OK`.

## 5. SVG genereren

```cmd
vsa svg examples\minimal\050_svg_demo.vsa generated\vsa\050_svg_demo.svg
```

## Volgende stappen

| Doel                                      | Pagina                                              |
| ----------------------------------------- | --------------------------------------------------- |
| Brede uitleg van de CLI                   | [Gebruikershandleiding](../guides/user-guide.md)    |
| Het juiste commando per taak              | [CLI-taken](../guides/cli-taken.md)                 |
| Foutmeldingen begrijpen                   | [Validatie](../guides/validation.md)                |
| Tool hergebruiken in een andere repo      | [Integratie](../guides/reuse-vsa-tooling.md)        |
