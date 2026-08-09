---
slug: fixture
term: fixture
termType: concept
glossaryTerm: Fixture
glossaryText: "een vastgelegd voorbeeld of testset (meestal onder `examples/`) waarmee [VSA](@)-gedrag van [parser](@), [validator](@), [renderer](@) of CLI reproduceerbaar wordt gecontroleerd; vaak met vaste verwachte uitvoer."
formPhrases:
  - fixture
  - fixtures
  - Fixture
  - Fixtures
  - fixture-bestand
  - fixture-bestanden
  - fixture-map
  - fixture-mappen
  - fixture-pad
  - fixture-paden
  - fixture-catalogus
  - fixtures-catalogus
  - fixture-indeling
  - fixture-voorbeeld
  - fail-fixture
  - docs-fixture
---

# Fixture

Een fixture is een gecontroleerde invoerset voor tests, regressie of
docs-walkthroughs. De canonieke bestanden staan onder `examples/`; docs
**citeren** die paden en vervangen golden files niet.

Goede/valide voorbeelden van Fixture zijn:
- `examples/regression/*/input.vsa` met verwachte AST/validatie/SVG
- Walkthrough-`.vsa` onder `examples/docs-walkthroughs/`
- Bewust ongeldige cases onder `examples/expected-fail/`

Geen goede/niet valide voorbeelden van Fixture zijn:
- Productie-[zangstukken](@bron) in de [bron-repository](@bron)
- Gegenereerde output onder `generated/`
- Een losse notitie zonder reproduceerbare invoer
