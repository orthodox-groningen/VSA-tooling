---
slug: terminologie
term: terminologie
termType: concept
excludeFromMRG: yes
---

# Terminologie

Deze pagina bevat de gegenereerde glossary voor de TEv2-documentatiescope.

| [@include-vsa](terms/include-vsa.md) | een substring die met `@include-vsa` begint, exact een ondersteunde resolverparameter bevat (`zoek=`, `id=` of `lokaal=`) en tijdens verwerking door de body van het doelbestand wordt vervangen. |
| [AST](terms/ast.md) | Afkorting van [Abstract Syntax Tree](terms/ast.md). |
| [Abstract Syntax Tree](terms/ast.md) | een expliciete nodeboom die door de parser uit VSA-invoer wordt geproduceerd en die validator en renderer zonder semantische herinterpretatie kunnen lezen. |
| [Bracket-directive](terms/bracket-directive.md) | een tekstfragment dat als afzonderlijk VSA-token tussen `[` en `]` voorkomt en door bracket-dispatch wordt geclassificeerd voordat de inhoudelijke parsing verdergaat. |
| [Control-token](terms/control-token.md) | een bracket-directive waarvan de tokenwaarde een ondersteunde control-tokenvorm is, zoals `[*]`, `[/]`, `[*?]` of `[/?]`, en die niet als pitch-marker wordt geparseerd. |
| [Diagnostic](terms/diagnostic.md) | een melding die door parser of validator wordt geproduceerd en ten minste een foutcode, severity, bronlocatie en uitleg of context bij een vastgestelde afwijking bevat. |
| [EHM](terms/enkelvoudige-hoogte-modifier.md) | Afkorting van [Enkelvoudige hoogte-modifier](terms/enkelvoudige-hoogte-modifier.md). |
| [Enkelvoudige hoogte-modifier](terms/enkelvoudige-hoogte-modifier.md) | een hoogte-modifier die uit precies een geldige EHM bestaat: een basis-hoogtebeweging, eventueel voorafgegaan door een halftoon-prefix. |
| [ELM](terms/enkelvoudige-lengte-modifier.md) | Afkorting van [Enkelvoudige lengte-modifier](terms/enkelvoudige-lengte-modifier.md). |
| [Enkelvoudige lengte-modifier](terms/enkelvoudige-lengte-modifier.md) | een lengte-modifier die uit precies een geldige ELM bestaat en daarmee precies een duurpositie representeert. |
| [Hoogte-modifier](terms/hoogte-modifier.md) | een modifier die voor het zangelement in een VSA-scope staat en bestaat uit een geldige EHM of uit meerdere geldige EHM's gescheiden door `&`. |
| [Hugo-output](terms/hugo-output.md) | een artifactset die door een VSA-buildstap gegenereerde Hugo-compatibele Markdown en de daarbij verwezen assets bevat. |
| [Lengte-modifier](terms/lengte-modifier.md) | een modifier die na het zangelement in een VSA-scope staat en bestaat uit een geldige ELM of uit meerdere geldige ELM's gescheiden door `&`. |
| [Metadata](terms/metadata.md) | gegevens die als gestructureerde blokparameters of YAML-frontmatter bij VSA-bronmateriaal staan, verwerking of identificatie sturen en zelf niet tot de zichtbare VSA-notatie behoren. |
| [Modifier](terms/modifier.md) | een tekenreeks die binnen een VSA-scope als hoogte-modifier voor het zangelement of als lengte-modifier na het zangelement wordt geparseerd. |
| [Parser](terms/parser.md) | een component die VSA-brontekst of tokens volgens de grammatica omzet naar expliciete AST-nodes, bronlocaties behoudt en geen semantische reparaties of renderlogica uitvoert. |
| [Pitch-marker](terms/pitch-marker.md) | een bracket-directive met de vorm `[<EHM>:]`, waarbij `<EHM>` leeg is of een geldige enkelvoudige hoogte-modifier bevat. |
| [Publicatie](terms/publicatie.md) | een proces dat gegenereerde demo-, preview- of productie-output bouwt, controleert en beschikbaar maakt voor GitHub Pages of hergebruik. |
| [Renderer](terms/renderer.md) | een component die een gevalideerde AST of daarvan afgeleid layoutmodel omzet naar concrete uitvoer, zoals SVG, JSON, Markdown, Hugo-output of MusicXML, zonder de AST semantisch te wijzigen. |
| [Samengestelde hoogte-modifier](terms/samengestelde-hoogte-modifier.md) | een hoogte-modifier die uit twee of meer geldige EHM's bestaat die onderling door `&` zijn gescheiden. |
| [Samengestelde lengte-modifier](terms/samengestelde-lengte-modifier.md) | een lengte-modifier die uit twee of meer geldige ELM's bestaat die onderling door `&` zijn gescheiden. |
| [Severity](terms/severity.md) | een waarde die aan een diagnostic is gekoppeld en aangeeft of de vastgestelde afwijking als blokkerende fout of als waarschuwing moet worden behandeld. |
| [Validator](terms/validator.md) | een component die een geparseerde AST of VSA-invoer toetst aan semantische en normatieve regels en overtredingen als diagnostics rapporteert zonder ze stilzwijgend te repareren. |
| [VSA](terms/vsa.md) | Afkorting van [Vereenvoudigde Slavische Accentnotatie](terms/vsa.md). |
| [Vereenvoudigde Slavische Accentnotatie](terms/vsa.md) | een notatie- of toolingketen die VSA-brontekst met scopes, modifiers en bracket-directives gebruikt om liturgische zangteksten te valideren, renderen of publiceren. |
| [VSA-scope](terms/vsa-scope.md) | een tekstfragment dat met `{` begint, met `}` eindigt, geen whitespace binnen de accolades bevat en door de parser kan worden opgesplitst in optionele hoogte-modifier, verplicht zangelement en optionele lengte-modifier. |
| [vsa.toml](terms/vsa-toml.md) | een projectconfiguratiebestand met de naam `vsa.toml` dat herkende VSA-toolinginstellingen bevat voor rendering, output of validatie. |
| [Zangstuk](terms/zangstuk.md) | een inhoudelijke eenheid die een afgebakend gezang of muzikale tekst vormt en zelfstandig kan worden geidentificeerd, vastgelegd, verwerkt of gepubliceerd. |

