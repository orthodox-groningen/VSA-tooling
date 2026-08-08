# Starten — lokaal ontwikkelen

Deze pagina helpt je om de [VSA-tooling](@bron) **lokaal** te laten werken
(omgeving, eerste `vsa`-commando’s). Uitgebreidere procedures:
[Handleidingen](../manuals/index.md).

!!! note "Voor wie"
    Voor notatie-auteurs en wie de CLI lokaal wil draaien — niet voor
    koorzangers die een dienst oefenen (parochie-site; zie [Home](../index.md)).

## Wie ben je? (kort)

| Ik wil …                         | Ga naar                                                         |
| -------------------------------- | --------------------------------------------------------------- |
| Alleen lokaal opstarten          | Stappen 1–5 hieronder                                           |
| Foutmeldingen begrijpen          | [Validatie](../guides/validation.md)                            |
| SVG / Hugo-publicatie            | [SVG exporteren](../guides/svg-export.md)                       |
| Tour van typische taken          | [Gebruikershandleiding](../guides/user-guide.md)                |

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
| Tour + links naar de juiste pagina’s      | [Gebruikershandleiding](../guides/user-guide.md)    |
| Het juiste commando per taak              | [CLI-taken](../guides/cli-taken.md)                 |
| Foutmeldingen begrijpen                   | [Validatie](../guides/validation.md)                |
| Tool hergebruiken in een andere repo      | [Integratie](../integratie/index.md)                |
| Docs lokaal met TermRefs                  | [TEv2 in tool-docs](../guides/tev2-docs.md)         |
