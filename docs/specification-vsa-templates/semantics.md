# Semantiek

## Do-context en modus

Zoals in [VSA](@):

- `do` — absolute scientific pitch van de grondtoon;
- `mode` — intervalstructuur van de ladder (`major`, `minor`, …).

Samen vormen zij de [do-context](@). Alle `pitches` in
[template-events](template-event@) zijn [laddergraden](laddergraad@) binnen die
context. Export naar MusicXML (later) resolvet graad → klinkende toon via
dezelfde ladderlogica als VSA.

Optionele `key_signature` is afleidbaar uit `do`+`mode` en is geen primaire
bron van waarheid.

## Duration

Duur gebruikt [enkelvoudige lengte-modifiers](enkelvoudige-lengte-modifier@)
(ELMs) met dezelfde vermenigvuldiging t.o.v. standaardduur als VSA §5.10.
`duration-model` (default `default`) bepaalt de MusicXML-mapping (standaard =
kwartnoot).

## Reciteertoon

`role: recite` markeert een [reciteertoon](@): één akkoord voor N≥1 syllaben.
De ELM is de duur **per syllabe** (meestal `~`). De breve/“box” op het blad is
geen aparte ELM, maar die rol.

## Vormen

### Cycle-form (`cycle` + `final`)

Legacy shorthand voor het standaardpatroon `||: … :|| final`. Equivalent:

```yaml
text_mapping:
  - repeat: ["1", "2"]   # ids uit cycle
    until: final
  - phrase: laatste      # id uit final
```

Semantiek:

1. Tekstregels worden **cyclisch** over de ids in `cycle` gezet.
2. De **laatste** regel gebruikt altijd `final`.
3. Er is **geen** eis dat het aantal regels vóór `final` een veelvoud van
   `len(cycle)` is.
4. Bibliotheekfrasen (in `phrases` maar niet in `cycle`/`final`), zoals `"1a"`,
   via `text_mapping`, `mapping_plans`, of expliciete variant.

Zie [Mapping — text_mapping](mapping-vsa.md) voor prefix, embedded cycle en
meerdere plannen.

### Sequence-form (`sequence`)

Vaste toewijzing: één tekstregel per id in volgorde. Equivalent:

```yaml
text_mapping:
  - sequence: ["1", "3", "1", "2"]
```

### `text_mapping` / `mapping_plans`

Algemene vorm voor bladen met prefix, embedded `||: … :||`, of meerdere
cycle-varianten. Zie [mapping-vsa.md](mapping-vsa.md).

### Alias-form (`same_as`)

Het document erft melodische inhoud van een ander [vsa-template](@)-id (bijv.
tropaar = stichier op het blad).

## Roles

| Role       | Betekenis                                         |
| ---------- | ------------------------------------------------- |
| `open`     | Vaste openingsstap (vaak zelfde graad als recite) |
| `recite`   | [Reciteertoon](@); N syllaben × `duration`        |
| `cadence`  | Vaste cadens-/slotstap                            |
| `link`     | Verbinding; vaak `optional: true`                 |

## Optional

Als `optional: true`: mag bij mapping worden overgeslagen als er geen syllabe
voor is.

## Frase-ankers

| Anchor   | Bedoeling (werkhypothese)                              |
| -------- | ------------------------------------------------------ |
| `e.st.`  | Eerste streek / inzet                                  |
| `l.st.`  | Laatste streek op deze cadensnoot                      |
| `vl.st.` | Voorlaatste streek                                     |
| `l.lgr.` | Start van het slotmelisma: deze noot **en alle noten erna** in de frase op de laatste lettergreep |

Zie [frase-anker](@). Mapping naar syllaben: [mapping-vsa.md](mapping-vsa.md)
(experimenteel).

## Chromatische laddergraden

Prefix `#` / `b` op een [laddergraad](@) = chromatische wijziging t.o.v. de
laddertoon.

## Wat semantiek niet claimt

- Automatische gelijkheid VSA-hoogtecontour ↔ template-sopraan.
- Stem-autonome ritmes.
