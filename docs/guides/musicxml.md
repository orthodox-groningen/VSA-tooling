# MusicXML

Met `vsa musicxml` exporteer je VSA naar `.mxl` of `.musicxml`.

## Snel starten

```cmd
vsa musicxml mijn-lied.vsa mijn-lied.mxl
```

Zonder extensie krijg je standaard `.mxl`:

```cmd
vsa musicxml mijn-lied.vsa output\mijn-lied
```

Platte MusicXML:

```cmd
vsa musicxml mijn-lied.vsa mijn-lied.musicxml
```

Of expliciet:

```cmd
vsa musicxml mijn-lied.vsa mijn-lied --format musicxml
```

## Map exporteren

```cmd
vsa musicxml content-source\praktijk output\mxl
```

## Exportprofielen

| Profiel     | Doel                                            |
| ----------- | ----------------------------------------------- |
| `playback`  | afspelen in Coria of importeren in MuseScore    |
| `engraving` | verder bewerken als partituur                   |

Standaard gebruikt de tool `playback`.

```cmd
vsa musicxml lied.vsa lied.mxl --musicxml-profile engraving
```

## Frontmatter

De meeste instellingen staan in YAML-frontmatter bovenaan het `.vsa`-bestand.

```yaml
---
muziek:
  do: F4
  mode: major
  tempo: 132
  musicxml-profile: playback
identificatie:
  title: Tropaar van de zondag, toon 3
  composer: Traditioneel
  tone: "3"
---
```

## Belangrijke instellingen

| Instelling          | Betekenis                                      | Standaard  |
| ------------------- | ---------------------------------------------- | ---------- |
| `do`                | grondtoon, bijvoorbeeld `F4`                   | `F4`       |
| `mode`              | `major` of `minor`                             | `major`    |
| `tempo`             | tempo in BPM                                   | `100`      |
| `meter`             | maatsoort, bijvoorbeeld `4/4`                  | —          |
| `reciting-mode`     | reciteergedrag voor ongescopte tekst           | `quarters` |
| `musicxml-profile`  | `playback` of `engraving`                      | `playback` |

## Coria-links in content-source

```markdown
:::include "tropaar-zondag-toon-3.vsa" alt="Tropaar" scale="85%":::
:::coria "tropaar-zondag-toon-3.vsa" label="Oefenen in Coria":::
```

Als `{stem}.coria.html` naast de `.vsa` staat, wordt daarnaar gelinkt. Anders wordt een MXL-link gebruikt.

## Bronnen

Gebaseerd op:

- `docs/guides/musicxml-export.md`
