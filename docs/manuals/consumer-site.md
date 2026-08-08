# Consumer-site — waar hoort wat

!!! note "Voor wie / wanneer"
    **Voor:** consumer-site builder (P4) die wil weten wat in welke repo hoort.
    **Wanneer:** je hangt Hugo + `vsa-tool` aan elkaar.
    **Niet:** een volledige Hugo-cursus — die hoort bij
    [VSA-demo](https://github.com/orthodox-groningen/VSA-demo).

**Antwoord in het kort:** tooling = package/CLI; presentatievoorbeeld =
VSA-demo; [zangstukken](@bron)/org-specs = [bron-repository](@bron).

## Waar hoort wat

| Repo                                                           | Rol                                          |
| -------------------------------------------------------------- | -------------------------------------------- |
| **[VSA-tooling](@bron)** (deze docs)                           | Package, CLI, specs, fixtures                |
| **[VSA-demo](https://github.com/orthodox-groningen/VSA-demo)** | Voorbeeld-Hugo-site + Pages                  |
| **[bron](https://github.com/orthodox-groningen/bron)**         | [Zangstukken](@bron) en org-specs            |

## Minimale keten (tooling)

```text
content-source/*.md  (+ .vsa)
        ↓
  vsa validate
        ↓
  vsa build-markdown  →  content/ + static/vsa/
        ↓
  hugo  →  public/
```

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
vsa validate examples\consumer-minimal\content-source
vsa build-markdown examples\consumer-minimal\content-source generated\ci\content generated\ci\static\vsa
```

## Lokaal (voorbeeldconsumer)

```cmd
cd /d C:\Git\orthodox-groningen\VSA-demo
scripts\bootstrap.cmd
scripts\serve-hugo.cmd
```

Documentatie: [VSA-demo README](https://github.com/orthodox-groningen/VSA-demo/blob/main/README.md).

## Zie ook

- Installatie en CI: [Integratie — reuse](../guides/reuse-vsa-tooling.md)
- CLI: [CLI-taken](../guides/cli-taken.md), [CLI-referentie](../reference/cli/index.md)
- Navigatie-placeholders: [hugo-navigation-placeholders](../guides/hugo-navigation-placeholders.md)
