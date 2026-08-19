# Doel en scope

[VSA](@) ([Vereenvoudigde Slavische Accentnotatie](vsa@)) is een tekstgebaseerde
domeinspecifieke taal (DSL) voor Slavische accentnotatie. De taal definieert
een eenduidige, machineleesbare en menselijk leesbare notatie waarmee
[zangstukken](@bron) kunnen worden vastgelegd, gevalideerd en verder verwerkt
([conversiemechanisme](@bron)
naar o.a. SVG/MusicXML; [exportmechanisme](@bron)
in een [samenstelling](@bron) via `:::include`).

Deze specificatie beschrijft de **taal en haar semantiek** (plus toolcontracts
in de overige specificatiepagina’s). Org-brede begrippen zoals
[zangstuk](@bron) en [afgeleide](@bron) staan in de
[bron-terminologie](https://orthodox-ronl.github.io/bron/specs/terminologie/);
tool-termen in de [glossary](../glossary.md).

## Status

Dit document consolideert algemene specificatie-informatie uit de bestaande
VSA-documentatie (betekenis behouden, structuur opgeschoond).

## Inleiding

<!-- ter herinnering: http://www.ivanmoody.co.uk/orthodoxliturgylinks.htm bevat allerlei links over orthodoxe liturgie -->

De Slavisch‑orthodoxe zangtraditie kent een lange geschiedenis van
**staffloze neumen­notatie**, waarvan de bekendste vorm de klassieke
**Znamenny‑notatie** is. Deze notatie gebruikt ideografische tekens
(*kriuki* of *znamëna*) om melodische beweging, formules en expressie vast te
leggen zonder exacte toonhoogtes. Een toegankelijke introductie is te vinden
op [Znamenny chant](https://en.wikipedia.org/wiki/Znamenny_chant), en een
overzicht van historische notatievormen op
[Znamenny musical notation](https://en.wikipedia.org/wiki/Znamenny_notation).

Hoewel deze officiële systemen rijk en complex zijn, ontstonden er in
parochies ook **vereenvoudigde, mondeling overgeleverde markeersystemen**.
Deze systemen — vaak bestaande uit gestapelde streepjes boven de tekst en
horizontale lijnen onder syllaben — dienden als praktische hulpmiddelen om
**richting**, **accent** en **duur** van de zang aan te geven. Ze zijn echter
**niet gestandaardiseerd**, **niet officieel gedocumenteerd**, en verschillen
per regio, koorleider of lokale traditie. Historische uitleg uit het
Nederlandse Liturgikon: [Liturgikon-notatie](../guides/liturgikon-notatie.md).

Dit document introduceert een formele codificatie van deze praktijkgerichte
notatie: de **[Vereenvoudigde Slavische Accentnotatie](vsa@) ([VSA-notatie](@bron))**. [VSA](@) is
geen vervanging van historische kriuki- of znamenny-notatie, maar een lichte,
consistente en reproduceerbare manier om Slavisch‑orthodoxe congregatiezang
digitaal te noteren.

Het doel is een notatie die:

- eenvoudig te leren is voor zangers zonder gespecialiseerde opleiding;
- aansluit bij bestaande parochiële praktijk;
- formeel definieerbaar is in een grammatica;
- betrouwbaar te parseren, valideren en renderen is;
- bruikbaar is in tekstgebaseerde workflows, statische websites en
  automatische [renderers](@) of weergavecomponenten;
- voldoende semantische informatie bevat voor conversie naar symbolische
  muziekformaten zoals MusicXML.

[VSA](@) beschrijft melodische beweging binnen een modaal toonstelsel waarin
stapgrootten niet uniform zijn en afhankelijk zijn van de gekozen grondtoon:
de `do` van de toonladder.

## Terminologie

**Geen parallelle glossary hier.** Definities:

| Bron                                                                                 | Inhoud                                              |
| ------------------------------------------------------------------------------------ | --------------------------------------------------- |
| [Glossary (deze site)](../glossary.md)                                               | Tool-termen + geselecteerde bron-termen (na TEv2)   |
| [bron — terminologie](https://orthodox-ronl.github.io/bron/specs/terminologie/) | Org-brede canonieke begrippen                       |
| Curated texts                                                                        | `docs/terminologie/` (lokaal) en bron `docs/terms/` |

Gebruik TermRefs in specificatietekst (`[parser](@)`, `[zangstuk](@bron)`, …)
in plaats van een tweede termtabel bij te houden.
