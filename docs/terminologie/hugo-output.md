---
slug: hugo-output
term: hugo-output
termType: concept
glossaryTerm: Hugo-output
glossaryText: "een artifactset die door een [VSA](@)-buildstap gegenereerde Hugo-compatibele Markdown en de daarbij verwezen assets bevat."
glossaryAlias: Hugo-content
formPhrases:
  - hugo-output
  - hugo-outputs
  - hugo-content
  - hugo-contentsets
---

# Hugo-output

Hugo-output / [hugo-content](@) is het resultaat van buildstappen die
bron-Markdown en [VSA](@)-assets voorbereiden voor Hugo. Losse bronbestanden
die nog niet door die buildstap zijn gegenereerd, zijn geen Hugo-output.

Goede/valide voorbeelden van Hugo-output zijn:
- Gegenereerde Markdown + verwezen assets
- Output van de [renderer](@)/buildstap

Geen goede/niet valide voorbeelden van Hugo-output zijn:
- Ruwe content-source vóór `build-markdown`
- Handmatige kopie zonder buildstap
