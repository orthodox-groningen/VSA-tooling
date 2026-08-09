# Mapping VSA ↔ vsa-template (experimenteel)

Status: **hypotheses**, geen normatieve VSA 1.0-wijziging.

## Doel

Beschrijven hoe een VSA-tekstblok op frase-events van een template kan landen,
zonder de template-syntax te vermengen met lyrics.

## Feiten (uit praktijk / bladen)

1. `*` in VSA markeert vrijwel altijd een frasegrens; dat correspondeert met de volgende
   toewijzing in `cycle` / `final`.
2. Templates hebben `recite`-events voor variabel syllabe-aantal.
3. Bladen markeren ankers (`e.st.`, `l.st.`, `vl.st.`) op vaste events.

## Hypotheses

| #   | Hypothese                                                                                                           |
| -   | ---------                                                                                                           |
| H1  | Ongemarkeerde VSA-syllaben vóór cadens-scopes vallen op `recite`.                                                   |
| H2  | Scopes rond cadens (`{/…}`, `{\…}`, `{…_}`) corresponderen met `cadence`-events, vaak bij `anchor: l.st.` of erna.  |
| H3  | `{/…}` direct na `*` kan `e.st.` van de volgende frase zijn.                                                        |
| H4  | `optional: true` events worden overgeslagen als er geen syllabe voor is.                                            |
| H5  | Split/merge van duren gebeurt in de **auteurlijke VSA** of in een latere mappingstap — niet door het template zelf. |

## Architectuurkeuzes (open)

| Pad                       | Melodie-S               | Overige stemmen        |
| ------------------------- | ----------------------- | ---------------------- |
| A (default in deze draft) | uit template-pitches    | uit template           |
| B                         | uit VSA (relatief + do) | uit template (harmony) |

Beslissing: nog open — zie [`open-points.md`](open-points.md). Walkthroughs
moeten beide paden kunnen documenteren.

## Walkthrough

Zie [`examples/walkthroughs/elia-tropaar-toon-4.md`](examples/walkthroughs/elia-tropaar-toon-4.md).

## Wat deze laag niet doet

- Geen nieuwe VSA-syntax voor SATB.
- Geen garantie dat VSA-EHM’s gelijk zijn aan Δ(template-S).
