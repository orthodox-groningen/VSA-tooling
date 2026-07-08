---
slug: terminologie
term: terminologie
termType: concept
excludeFromMRG: yes
---

# Terminologie

Deze pagina bevat de gegenereerde glossary voor de TEv2-documentatiescope.

### [@include-vsa](/VSA-tooling/terminologie/include-vsa)

een substring die met `@include-vsa` begint, exact een ondersteunde resolverparameter bevat (`zoek=`, `id=` of `lokaal=`) en tijdens verwerking door de body van het doelbestand wordt vervangen.

### [Abstract Syntax Tree](/VSA-tooling/terminologie/ast)

een expliciete nodeboom die door de parser uit VSA-invoer wordt geproduceerd en die validator en renderer zonder semantische herinterpretatie kunnen lezen.

### [Bracket-directive](/VSA-tooling/terminologie/bracket-directive)

een tekstfragment dat als afzonderlijk VSA-token tussen `[` en `]` voorkomt en door bracket-dispatch wordt geclassificeerd voordat de inhoudelijke parsing verdergaat.

### [Control-token](/VSA-tooling/terminologie/control-token)

een bracket-directive waarvan de tokenwaarde een ondersteunde control-tokenvorm is, zoals `[*]`, `[/]`, `[*?]` of `[/?]`, en die niet als pitch-marker wordt geparseerd.

### [Diagnostic](/VSA-tooling/terminologie/diagnostic)

een melding die door parser of validator wordt geproduceerd en ten minste een foutcode, severity, bronlocatie en uitleg of context bij een vastgestelde afwijking bevat.

### [Enkelvoudige hoogte-modifier](/VSA-tooling/terminologie/enkelvoudige-hoogte-modifier)

een hoogte-modifier die uit precies een geldige EHM bestaat: een basis-hoogtebeweging, eventueel voorafgegaan door een halftoon-prefix.

### [Enkelvoudige lengte-modifier](/VSA-tooling/terminologie/enkelvoudige-lengte-modifier)

een lengte-modifier die uit precies een geldige ELM bestaat en daarmee precies een duurpositie representeert.

### [Hoogte-modifier](/VSA-tooling/terminologie/hoogte-modifier)

een modifier die voor het zangelement in een VSA-scope staat en bestaat uit een geldige EHM of uit meerdere geldige EHM's gescheiden door `&`.

### [Hugo-output](/VSA-tooling/terminologie/hugo-output)

een artifactset die door een VSA-buildstap gegenereerde Hugo-compatibele Markdown en de daarbij verwezen assets bevat.

### [Lengte-modifier](/VSA-tooling/terminologie/lengte-modifier)

een modifier die na het zangelement in een VSA-scope staat en bestaat uit een geldige ELM of uit meerdere geldige ELM's gescheiden door `&`.

### [Metadata](/VSA-tooling/terminologie/metadata)

gegevens die als gestructureerde blokparameters of YAML-frontmatter bij VSA-bronmateriaal staan, verwerking of identificatie sturen en zelf niet tot de zichtbare VSA-notatie behoren.

### [Modifier](/VSA-tooling/terminologie/modifier)

een tekenreeks die binnen een VSA-scope als hoogte-modifier voor het zangelement of als lengte-modifier na het zangelement wordt geparseerd.

### [Parser](/VSA-tooling/terminologie/parser)

een component die VSA-brontekst of tokens volgens de grammatica omzet naar expliciete AST-nodes, bronlocaties behoudt en geen semantische reparaties of renderlogica uitvoert.

### [Pitch-marker](/VSA-tooling/terminologie/pitch-marker)

een bracket-directive met de vorm `[<EHM>:]`, waarbij `<EHM>` leeg is of een geldige enkelvoudige hoogte-modifier bevat.

### [Publicatie](/VSA-tooling/terminologie/publicatie)

een proces dat gegenereerde demo-, preview- of productie-output bouwt, controleert en beschikbaar maakt voor GitHub Pages of hergebruik.

### [Renderer](/VSA-tooling/terminologie/renderer)

een component die een gevalideerde AST of daarvan afgeleid layoutmodel omzet naar concrete uitvoer, zoals SVG, JSON, Markdown, Hugo-output of MusicXML, zonder de AST semantisch te wijzigen.

### [Samengestelde hoogte-modifier](/VSA-tooling/terminologie/samengestelde-hoogte-modifier)

een hoogte-modifier die uit twee of meer geldige EHM's bestaat die onderling door `&` zijn gescheiden.

### [Samengestelde lengte-modifier](/VSA-tooling/terminologie/samengestelde-lengte-modifier)

een lengte-modifier die uit twee of meer geldige ELM's bestaat die onderling door `&` zijn gescheiden.

### [Severity](/VSA-tooling/terminologie/severity)

een waarde die aan een diagnostic is gekoppeld en aangeeft of de vastgestelde afwijking als blokkerende fout of als waarschuwing moet worden behandeld.

### [Validator](/VSA-tooling/terminologie/validator)

een component die een geparseerde AST of VSA-invoer toetst aan semantische en normatieve regels en overtredingen als diagnostics rapporteert zonder ze stilzwijgend te repareren.

### [Vereenvoudigde Slavische Accentnotatie](/VSA-tooling/terminologie/vsa)

een notatie- of toolingketen die VSA-brontekst met scopes, modifiers en bracket-directives gebruikt om liturgische zangteksten te valideren, renderen of publiceren.

### [VSA-scope](/VSA-tooling/terminologie/vsa-scope)

een tekstfragment dat met `{` begint, met `}` eindigt, geen whitespace binnen de accolades bevat en door de parser kan worden opgesplitst in optionele hoogte-modifier, verplicht zangelement en optionele lengte-modifier.

### [vsa.toml](/VSA-tooling/terminologie/vsa-toml)

een projectconfiguratiebestand met de naam `vsa.toml` dat herkende VSA-toolinginstellingen bevat voor rendering, output of validatie.

### [Zangstuk](/VSA-tooling/terminologie/zangstuk)

een inhoudelijke eenheid die een afgebakend gezang of muzikale tekst vormt en zelfstandig kan worden geidentificeerd, vastgelegd, verwerkt of gepubliceerd.


