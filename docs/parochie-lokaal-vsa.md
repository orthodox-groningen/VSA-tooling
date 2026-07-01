# Parochie-lokaal — VSA-tooling

**Algemene handleiding (canoniek):** [bron/docs/manuals/parochie-lokaal-zangstukken.md](https://github.com/orthodox-groningen/bron/blob/main/docs/manuals/parochie-lokaal-zangstukken.md)

Terminologie: [bron/docs/specs/terminologie.md](https://github.com/orthodox-groningen/bron/blob/main/docs/specs/terminologie.md).

Dit document beschrijft alleen wat **specifiek voor VSA-tooling en de Hugo-demo** geldt.

---

## Demo-voorbeeld

```text
examples/hugo-demo/content-source/lokaal/antifoon-1-weekdagen/
```

---

## VSA-includes in samenstellingen

Relatief pad vanuit het markdown-bestand:

```markdown
:::include svg "../../lokaal/antifoon-1-weekdagen/liturgikon-weekdagen/hemelum/repr/hemelum.vsa" alt="1e antifoon (Hemelum)":::
```

Inline (kort fragment):

```markdown
::: vsa-notatie
…
:::
```

**Opmerking:** annotaties in `.vsa` als `<!-- … -->` (HTML-comment), niet als `[//:]` — dat laatste is een hoogte-markering.

---

## Build-pipeline (VSA-tooling)

| Stap             | Parochie-lokaal                  |
| ---------------- | -------------------------------- |
| Sync bron        | Niet nodig — bestanden in git    |
| `vsa validate`   | Deelt `content-source` recursief |
| `build-markdown` | Includes op relatief pad         |
| Hugo             | Ongewijzigd                      |

Lokaal bouwen:

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
scripts\build-hugo.cmd
scripts\serve-hugo.cmd
```

---

## Hugo-demo structuur

Zie [hugo-site-structure.md](hugo-site-structure.md) voor `lokaal/` naast `praktijk/` en `voorbeelden/`.
