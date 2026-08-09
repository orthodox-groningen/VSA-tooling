---
slug: severity
term: severity
termType: concept
glossaryTerm: Severity
glossaryText: "een waarde die aan een [diagnostic](@) / [diagnostische melding](@) is gekoppeld en aangeeft of de vastgestelde afwijking als blokkerende fout of als waarschuwing moet worden behandeld."
glossaryAlias: Ernstniveau
formPhrases:
  - severity
  - severities
  - severity level
  - severity levels
  - ernstniveau
  - ernstniveaus
---

# Severity

Severity / [ernstniveau](@) maakt onderscheid tussen blokkerende fouten en
waarschuwingen. De gekozen severity bepaalt de [publicatie](@)- of
validatie-uitkomst, maar verandert de onderliggende invoer niet.

Goede/valide voorbeelden van Severity zijn:
- `error` / `warning` op een [diagnostic](@)
- Stuurt exitcode / publicatiebeslissing

Geen goede/niet valide voorbeelden van Severity zijn:
- Een losse tekstlabel zonder diagnostic
- Wijzigt de [VSA](@)-bron of [AST](@)
