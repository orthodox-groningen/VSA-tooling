# Semantiek

## Do-context en modus

Zoals in VSA:

- `do` — absolute scientific pitch van de grondtoon;
- `mode` — intervalstructuur van de ladder (`major`, `minor`, …).

Alle `pitches` in events zijn **laddergraden** binnen die context, geen
losse absolute noten. Export naar MusicXML (later) resolvet graad → pitch via
dezelfde ladderlogica als VSA.

Optionele `key_signature` op het blad is afleidbaar uit `do`+`mode` en is in
templates geen primaire bron van waarheid.

## Duration

ELMs hebben dezelfde vermenigvuldiging t.o.v. standaardduur als VSA §5.10.
`duration-model` (default `default`) bepaalt de MusicXML-mapping van die
standaardduur (standaard = kwartnoot).

## Recite

`role: recite` betekent: één akkoord (vaste graden) voor N≥1 syllaben.
De duur-ELM is de duur **per syllabe** (meestal `~`), niet een “breve-ELM”.

## Vormen (cycle / sequence / alias)

Ongewijzigd t.o.v. eerdere draft: zie cycle-form, sequence-form, alias-form in
[`syntax.md`](syntax.md).

### Cycle-form

Tekstfrasen → herhaalde `cycle`, laatste tekstfrase → `final`.
Bibliotheekfrasen (`1a`, …) alleen via mapping/variant.

### Sequence-form

Vaste lijst phrase-ids; lengte moet (na mapping) bij de tekst passen.

### Alias-form

`same_as` erft melodische inhoud van een ander template-id.

## Roles

| Role       | Betekenis                                            |
| ---------- | ---------------------------------------------------- |
| `open`     | Vaste openingsstap (vaak zelfde graad als recite)    |
| `recite`   | Reciteertoon; N syllaben × `duration`                |
| `cadence`  | Vaste cadens-/slotstap                               |
| `link`     | Verbinding; vaak `optional: true`                    |

## Optional / anchors

Ongewijzigd: optional mag worden overgeslagen; ankers registreren bladlabels
`e.st.` / `l.st.` / `vl.st.`.

## Chromatische graden

Prefix `#` / `b` op een graad = chromatische wijziging t.o.v. de laddertoon
(vergelijkbaar met VSA halftoon-prefix op EHM, maar hier op een **absolute
graadpositie** in het template).

## Wat semantiek niet claimt

- Automatische gelijkheid VSA-EHM-contour ↔ template-S.
- Stem-autonome ritmes.
