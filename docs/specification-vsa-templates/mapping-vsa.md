# Mapping VSA ↔ vsa-template (experimenteel)

Status: **hypotheses**, geen normatieve VSA 1.0-wijziging.

## Doel

Beschrijven hoe een [VSA](@)-tekstblok op [template-events](template-event@) van
een [vsa-template](@) kan landen, zonder lyrics in de template-syntax te
stoppen.

## Feiten

1. `*` in VSA markeert vaak een frasegrens; dat correspondeert met de volgende
   toewijzing in `cycle` / `final` of `sequence`.
2. Templates hebben [reciteertoon](@)-events voor variabel syllabe-aantal.
3. Bladen markeren [frase-ankers](frase-anker@) (`e.st.`, `l.st.`, `vl.st.`) op
   vaste events.

## Hypotheses

| #   | Hypothese                                                                    |
| -   | ---------                                                                    |
| H1  | Ongemarkeerde VSA-syllaben vóór cadens-scopes vallen op recite.              |
| H2  | Cadens-scopes corresponderen met `cadence`-events, vaak bij `l.st.` of erna. |
| H3  | `{/…}` direct na `*` kan `e.st.` van de volgende [template-frase](@) zijn.   |
| H4  | `optional: true` events worden overgeslagen zonder syllabe (H4).             |
| H5  | Split/merge van duren gebeurt in VSA of in een latere mappingstap.           |

## Architectuurkeuzes (open)

| Pad                       | Melodie-S                                 | Overige stemmen        |
| ------------------------- | ----------------------------------------- | ---------------------- |
| A (default in deze draft) | uit template-[laddergraden](laddergraad@) | uit template           |
| B                         | uit VSA + [do-context](@)                 | uit template (harmony) |

Walkthrough: [`examples/walkthroughs/elia-tropaar-toon-4.md`](examples/walkthroughs/elia-tropaar-toon-4.md).

## Wat deze laag niet doet

- Geen nieuwe VSA-syntax voor SATB.
- Geen garantie dat VSA-EHM’s gelijk zijn aan Δ(template-S).
