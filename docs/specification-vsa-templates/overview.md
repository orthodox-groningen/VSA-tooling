# Doel en scope

## Het idee in het kort

In de liturgische praktijk bestaan **formulemelodieën**: vaste melodische
patronen (tropaar, stichier, vers, …) waarop telkens **andere teksten** worden
gezongen. Op het toonboekblad staan die formules vaak **zonder lyrics**, met
herhaalstructuur (`||: 1, 2 :|| laatste`), [reciteertonen](reciteertoon@) en
klemtoonlabels (`e. st.`, `l. st.`, …).

Een [vsa-template](@) is de **machineleesbare vastlegging** van zo’n formule:

1. welke [template-frasen](template-frase@) er zijn;
2. hoe ze herhaald of vast geordend worden;
3. welke SATB-[laddergraden](laddergraad@) en duren ([ELM](enkelvoudige-lengte-modifier@))
   elk [template-event](@) heeft;
4. binnen welke [do-context](@) (`do` + `mode`) die graden klinken.

De **tekst** van een concreet [zangstuk](@bron) blijft in [VSA](@). Later kan
tooling tekst + template combineren tot bijvoorbeeld MusicXML. Zo scheid je
**herbruikbare melodie** van **unieke tekst**.

```text
toonboekblad (formule)  →  vsa-template (YAML)
VSA-tekst (lyrics+relatieve melodie)  →  mapping (experimenteel)
                                         ↓
                              afgeleide (bijv. MusicXML SATB)
```

## Doel

- Formules eenduidig en diffbaar in git vastleggen.
- Zelfde formule hergebruiken voor veel teksten.
- Aansluiten op VSA-begrippen: [do-context](@), [ELM](enkelvoudige-lengte-modifier@),
  relatieve/[laddergraad](@)-denken.
- Pad openhouden naar reproduceerbare [afgeleiden](@bron) (SVG/MusicXML) zonder
  OMR als bron van waarheid.

## Niet-doelen (deze draft)

- Vervanging van [VSA](@)-tekstnotatie.
- Volledige transcriptie van alle toonboekpagina’s in één keer.
- Layout-/drukwerkregels.
- Canonieke toonhoogtes uit AI- of OMR-lezing van scans.

## Bronregel voor toonhoogtes

PDF’s en plaatjes leveren **feature-eisen** (wat de taal moet kunnen uitdrukken).
Normatieve graden in voorbeelden komen alleen uit **menselijk gecontroleerde**
invoer. Onzekerheden: [`open-points.md`](open-points.md) of
`pitches_status: provisional`.

## Architectuur (VSA→template-instance)

Het [vsa-template](@) beschrijft de **volledige SATB-formule** zoals op het
blad (inclusief optionele noten). Runtime-melodie voor **S** komt uit [VSA](@);
**A/T/B** komen uit de template en volgen dezelfde optional-/split-beslissingen
als S. Zie [Mapping VSA](mapping-vsa.md).

## Begrippen (TermRefs)

Geen parallelle termtabel bijhouden: definities staan in curated texts /
[glossary](../glossary.md). In deze specificatie:

| Begrip                    | TermRef                                                             |
| ------------------------- | ------------------------------------------------------------------- |
| Document / formule        | [vsa-template](@)                                                   |
| Melodisch blok            | [template-frase](@)                                                 |
| Één stap/akkoord          | [template-event](@)                                                 |
| Klemtoonlabel op noot     | [frase-anker](@)                                                    |
| Id van een template-frase | [frase-id](@)                                                       |
| Staff-text op de formule  | [formulelabel](@) ([frase-id](@) of [frase-anker](@))               |
| Variabel syllabe-akkoord  | [reciteertoon](@)                                                   |
| Graad t.o.v. do           | [laddergraad](@)                                                    |
| Grondtoon + modus         | [do-context](@)                                                     |
| Duursymbool               | [enkelvoudige lengte-modifier](enkelvoudige-lengte-modifier@) (ELM) |
| Org: werk                 | [zangstuk](@bron)                                                   |

Genre-labels op het blad (`tropaar`, `stichier`, `vers`) en toonnummers (1–8)
zijn metadata in het YAML; nog geen aparte glossarytermen.

## Status

Draft **v0**: syntax/semantiek/validatie + voorbeelden + schematests. Nog geen
export-CLI. Zie [README](README.md) voor documentenlijst en v0-criteria.
