# Doel en scope

## Doel

Een **vsa-template** legt een formulematige liturgische melodie machineleesbaar
vast, zodat:

1. frasen, herhalingsstructuur en muzikale rollen eenduidig zijn;
2. latere tooling tekst (bijv. VSA) op die formule kan mappen;
3. afgeleide uitvoer (bijv. MusicXML SATB) reproduceerbaar kan worden.

## Niet-doelen (deze draft)

- Vervanging van VSA-tekstnotatie;
- volledige transcriptie van alle toonboekpagina’s;
- layout/engraving-regels voor drukwerk;
- canonieke pitches uit AI- of OMR-lezing van scans.

## Bronregel voor pitches

PDF’s en plaatjes leveren **feature-eisen** (wat de taal moet kunnen uitdrukken).
Normatieve toonhoogtes in voorbeelden komen alleen uit **menselijk gecontroleerde**
invoer. Onzekere octaven of akkoorden horen in [`open-points.md`](open-points.md)
of als `pitches_status: provisional` in metadata.

## Do-context

Templates gebruiken dezelfde **do-context** als VSA (`do` + `mode`). Event-pitches
zijn laddergraden, geen losse scientific pitches. Duur gebruikt VSA-ELMs.

## Architectuurdefault

Het template beschrijft de **volledige SATB-formule** (zoals op het blad).
Koppeling met VSA-tekst is een aparte laag ([`mapping-vsa.md`](mapping-vsa.md)).
Alternatief “VSA = S, template = alleen harmony” blijft een open punt.

## Werknaam

| Term             | Betekenis                                                   |
| ---------------- | ----------------------------------------------------------- |
| **vsa-template** | YAML-document volgens deze specificatie                     |
| frase            | Genoemde melodische eenheid met id (`1`, `2`, `laatste`, …) |
| event            | Eén muzikale stap in een frase (recite, cadensnoot, …)      |
| anker            | Label zoals `e.st.`, `l.st.`, `vl.st.` op een event         |

Org-brede termen (`zangstuk-id`, `variant-id`, …): zie
[bron terminologie](https://github.com/orthodox-groningen/bron/blob/main/docs/specs/terminologie.md).
Nieuwe glossarytermen alleen via PR op **bron** (zie open punten).
