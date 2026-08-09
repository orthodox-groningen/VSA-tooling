# Walkthrough: Tropaar Profeet Elia (toon 4) ↔ template `tropaar-toon-4`

Niet-normatief onderzoeksdossier. Hypotheses: H1–H5 in
[`../../mapping-vsa.md`](../../mapping-vsa.md).

## VSA-bron

```text
[//:] Gij waart een {En_}gel {/in} het {\vlees_} *
{/de} grondslag der pro{fe_}{\ten_} *
en de tweede Voorloper van {Chris_}{/tus_} {\komst_}, *
{/roem}rijke E{li_}{\a} *
Gij hebt uit den hoge uw geest gezonden op E{-&/li_&_}{\sa_} *
{/gij} verjaagt ziekten en reinigt me{laat_}{\sen_}: *
en doet zo ook genezing opwellen voor allen die u ver{-&\e_&_}{/ren_} [//:]
```

## Frase-toewijzing (cycle)

Template: `cycle: [1, 2]`, `final: laatste` → 7 regels:

| Regel | Tekst (kort)                         | Frase     |
| ----- | ------------------------------------ | --------- |
| 1     | Gij waart een Engel in het vlees     | `1`       |
| 2     | de grondslag der profeten            | `2`       |
| 3     | en de tweede Voorloper … komst       | `1`       |
| 4     | roemrijke Elia                       | `2`       |
| 5     | Gij hebt … Elisa                     | `1`       |
| 6     | gij verjaagt … melatsen              | `2`       |
| 7     | en doet zo ook … vereren             | `laatste` |

## Regel 1 ↔ frase `1` (hypothese)

| Syllaben (groepen)     | Event-role (template)       | Anker   | Opmerking                       |
| ---------------------- | --------------------------- | ------- | ------------------------------- |
| Gij waart een          | recite                      | —       | H1                              |
| En_ gel                | cadence (pre) / recite-rand | —       | VSA markeert duur               |
| in                     | cadence                     | `l.st.` | H2; VSA `{/in}`                 |
| het vlees              | cadence (na l.st.)          | —       | Contour kan afwijken van blad-S |

**Spanning:** VSA eindcontour vs template-S na `l.st.` is niet 1:1 bewezen
(zie chatonderzoek). Onder pad A winnen template-pitches; onder pad B VSA-S.

## Regel 2 ↔ frase `2` (hypothese)

| Syllaben          | Event-role | Anker          | Opmerking                                                          |
| ----------------- | ---------- | -------------- | ------------------------------------------------------------------ |
| *(geen)*          | link       | —              | `optional: true` overgeslagen (H4)                                 |
| de                | cadence    | `e.st.`        | VSA `{/de}` — H3                                                   |
| grondslag der pro | recite     | —              | H1                                                                 |
| fe / ten          | cadence    | `l.st.` + slot | VSA heeft 2 scopes; template 3 cadensnoten → split/merge-open (H5) |

## Architectuurnotitie

Deze walkthrough falsifieert nog niet pad A vs B. Volgende audit: menselijke
pitchcontrole van `tropaar-toon-4.yaml` + één regel volledig uitsplitsen in
MusicXML-handvoorbeeld.
