---
title: Glossary
---

# Terminologie

<!-- Deze glossary wordt gegenereerd uit de TEv2 machine-readable glossary van de docs-scope. -->

### [@include-vsa](/VSA-tooling/terminologie/include-vsa)

een substring is een `@include-vsa`-directive als en slechts als zij met `@include-vsa` begint, exact een ondersteunde resolverparameter bevat (`zoek=`, `id=` of `lokaal=`) en tijdens verwerking door de body van het doelbestand wordt vervangen.

### [Abstract Syntax Tree](/VSA-tooling/terminologie/ast)

een gegevensstructuur is de AST als en slechts als zij de expliciete nodeboom is die de parser uit VSA-invoer produceert en die validator en renderer zonder semantische herinterpretatie kunnen lezen.

### [Bracket-directive](/VSA-tooling/terminologie/bracket-directive)

een tekstfragment is een bracket-directive als en slechts als het als een afzonderlijk VSA-token tussen `[` en `]` voorkomt en door bracket-dispatch wordt geclassificeerd voordat de inhoudelijke parsing verdergaat.

### [Control-token](/VSA-tooling/terminologie/control-token)

een bracket-directive is een control-token als en slechts als de tokenwaarde een ondersteunde control-tokenvorm is, zoals `[*]`, `[/]`, `[*?]` of `[/?]`, en niet als pitch-marker wordt geparseerd.

### [Diagnostic](/VSA-tooling/terminologie/diagnostic)

een melding is een diagnostic als en slechts als zij door parser of validator wordt geproduceerd en ten minste een foutcode, severity, bronlocatie en uitleg of context bij een vastgestelde afwijking bevat.

### [Enkelvoudige hoogte-modifier](/VSA-tooling/terminologie/enkelvoudige-hoogte-modifier)

een hoogte-modifier is een enkelvoudige hoogte-modifier als en slechts als hij uit precies een geldige EHM bestaat: een basis-hoogtebeweging, eventueel voorafgegaan door een halftoon-prefix.

### [Enkelvoudige lengte-modifier](/VSA-tooling/terminologie/enkelvoudige-lengte-modifier)

een lengte-modifier is een enkelvoudige lengte-modifier als en slechts als hij uit precies een geldige ELM bestaat en daarmee precies een duurpositie representeert.

### [Hoogte-modifier](/VSA-tooling/terminologie/hoogte-modifier)

een modifier is een hoogte-modifier als en slechts als hij voor het zangelement in een VSA-scope staat en bestaat uit een geldige EHM of uit meerdere geldige EHM's gescheiden door `&`.

### [Hugo-output](/VSA-tooling/terminologie/hugo-output)

een artifactset is Hugo-output als en slechts als zij door een VSA-buildstap gegenereerde Hugo-compatibele Markdown en de daarbij verwezen assets bevat.

### [Lengte-modifier](/VSA-tooling/terminologie/lengte-modifier)

een modifier is een lengte-modifier als en slechts als hij na het zangelement in een VSA-scope staat en bestaat uit een geldige ELM of uit meerdere geldige ELM's gescheiden door `&`.

### [Metadata](/VSA-tooling/terminologie/metadata)

gegevens zijn metadata als en slechts als zij als gestructureerde blokparameters of YAML-frontmatter bij VSA-bronmateriaal staan, verwerking of identificatie sturen en zelf niet tot de zichtbare VSA-notatie behoren.

### [Modifier](/VSA-tooling/terminologie/modifier)

een tekenreeks is een modifier als en slechts als zij binnen een VSA-scope als hoogte-modifier voor het zangelement of als lengte-modifier na het zangelement wordt geparseerd.

### [Parser](/VSA-tooling/terminologie/parser)

een component is een parser als en slechts als hij VSA-brontekst of tokens volgens de grammatica omzet naar expliciete AST-nodes, bronlocaties behoudt en geen semantische reparaties of renderlogica uitvoert.

### [Pitch-marker](/VSA-tooling/terminologie/pitch-marker)

een bracket-directive is een pitch-marker als en slechts als zij de vorm `[<EHM>:]` heeft, waarbij `<EHM>` leeg is of een geldige enkelvoudige hoogte-modifier bevat.

### [Publicatie](/VSA-tooling/terminologie/publicatie)

een proces is publicatie als en slechts als het gegenereerde demo-, preview- of productie-output bouwt, controleert en beschikbaar maakt voor GitHub Pages of hergebruik.

### [Renderer](/VSA-tooling/terminologie/renderer)

een component is een renderer als en slechts als hij een gevalideerde AST of daarvan afgeleid layoutmodel omzet naar concrete uitvoer, zoals SVG, JSON, Markdown, Hugo-output of MusicXML, zonder de AST semantisch te wijzigen.

### [Samengestelde hoogte-modifier](/VSA-tooling/terminologie/samengestelde-hoogte-modifier)

een hoogte-modifier is een samengestelde hoogte-modifier als en slechts als hij uit twee of meer geldige EHM's bestaat die onderling door `&` zijn gescheiden.

### [Samengestelde lengte-modifier](/VSA-tooling/terminologie/samengestelde-lengte-modifier)

een lengte-modifier is een samengestelde lengte-modifier als en slechts als hij uit twee of meer geldige ELM's bestaat die onderling door `&` zijn gescheiden.

### [Severity](/VSA-tooling/terminologie/severity)

een waarde is een severity als en slechts als zij aan een diagnostic is gekoppeld en aangeeft of de vastgestelde afwijking als blokkerende fout of als waarschuwing moet worden behandeld.

### [Validator](/VSA-tooling/terminologie/validator)

een component is een validator als en slechts als hij een geparseerde AST of VSA-invoer toetst aan semantische en normatieve regels en overtredingen als diagnostics rapporteert zonder ze stilzwijgend te repareren.

### [Vereenvoudigde Slavische Accentnotatie](/VSA-tooling/terminologie/vsa)

een notatie- of toolingketen valt onder VSA als en slechts als zij VSA-brontekst met scopes, modifiers en bracket-directives gebruikt om liturgische zangteksten te valideren, renderen of publiceren.

### [VSA-scope](/VSA-tooling/terminologie/vsa-scope)

een tekstfragment is een VSA-scope als en slechts als het met `{` begint, met `}` eindigt, geen whitespace binnen de accolades bevat en door de parser kan worden opgesplitst in optionele hoogte-modifier, verplicht zangelement en optionele lengte-modifier.

### [vsa.toml](/VSA-tooling/terminologie/vsa-toml)

een bestand is `vsa.toml` als en slechts als het het projectconfiguratiebestand met die naam is en herkende VSA-toolinginstellingen bevat voor rendering, output of validatie.

### [Zangstuk](/VSA-tooling/terminologie/zangstuk)

een inhoudelijke eenheid is een zangstuk als en slechts als zij een afgebakend gezang of muzikale tekst vormt die zelfstandig kan worden geidentificeerd, vastgelegd, verwerkt of gepubliceerd.


