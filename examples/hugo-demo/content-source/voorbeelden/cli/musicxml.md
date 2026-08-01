---
title: "CLI: vsa musicxml"
---

# CLI: `vsa musicxml`

- [Home](../../../)
- [CLI overzicht](../)
- [Vorige: vsa svg](../svg/)
- [Volgende: vsa blocks](../blocks/)

## Waarvoor gebruik je dit?

Gebruik `vsa musicxml` om VSA om te zetten naar MusicXML voor MuseScore of
[Coria](https://coria.nl). Standaard schrijft het tool **`.mxl`** (gecomprimeerd)
met het **playback**-profiel — geoptimaliseerd voor afspelen zonder handmatige
opschoning.

## Input

Een `.vsa`-bestand met optionele YAML-frontmatter:

```yaml
---
muziek:
  do: F4
  mode: major
  tempo: 132
identificatie:
  title: Tropaar van de zondag, toon 3
  composer: Traditioneel
---
[:] Ter{/&/wijl_&_} ...
```

## Commando

Standaard (`.mxl`):

```cmd
vsa musicxml examples\minimal\valid-demo.vsa output.mxl
```

Platte MusicXML:

```cmd
vsa musicxml examples\minimal\valid-demo.vsa output.musicxml
```

## Opties

| Optie | Betekenis |
|-------|-----------|
| `--do F4` | Grondtoon overschrijven |
| `--mode major` | Modus overschrijven |
| `--tempo 132` | Tempo overschrijven |
| `--musicxml-profile playback` | Coria/MuseScore (default) |
| `--musicxml-profile engraving` | Partituurbewerking met typografie |
| `--format musicxml` | Platte `.musicxml` i.p.v. `.mxl` |

## Verwachte output

Enkel `.vsa`-bestand:

```text
MusicXML geschreven naar: output.mxl
```

Hele map (zoals in de site-build):

```text
32 MXL-bestand(en) geschreven
```

## Coria-link op de demo-site

In **content-source** (niet als Hugo-shortcode):

```markdown
:::coria "tropaar-zondag-toon-3.vsa" label="Oefenen in Coria":::
```

Voorbeeld op `praktijk/zondagen/zondag-toon-3.md` naast de `:::include` van hetzelfde `.vsa`-bestand.

Coria-HTML (`*.coria.html`) staat naast de `.vsa` in content-source; build kopieert naar `static/coria/`.

Zie [gebruikersdocumentatie MusicXML](https://github.com/orthodox-groningen/VSA-tooling/blob/main/docs/guides/musicxml-export.md).

## Profielen

- **`playback`** (default): MIDI-instrument, voice/stem, beaming — werkt in Coria.
- **`engraving`**: expliciete maatstrepen, typografie in `<defaults>`, gedetailleerde melisma-lijnen.

Zie [gebruikersdocumentatie MusicXML](https://github.com/orthodox-groningen/VSA-tooling/blob/main/docs/guides/musicxml-export.md)
voor alle instelbare velden en Coria-integratie.
