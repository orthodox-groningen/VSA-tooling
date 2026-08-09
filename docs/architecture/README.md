# Architectuur

Deze map beschrijft de actuele technische opbouw van de [VSA-tooling](@bron).

| Document               | Onderwerp                                                                                                |
| ---------------------- | -------------------------------------------------------------------------------------------------------- |
| `overview.md`          | Hoofdlijn van de verwerking                                                                              |
| `design-principles.md` | Fundamentele ontwerpprincipes en architectuurfilosofie van [VSA](@)                                      |
| `parser.md`            | Lexer, [parser](@) en [AST](@) / [syntactische boom](@)-opbouw                                           |
| `ast.md`               | Belangrijkste [AST](@)-concepten                                                                         |
| `directives.md`        | [Bracket-directives](@) / [bracket-tokens](@) en dispatch                                                |
| `validation.md`        | Semantische validatie en [diagnostics](@) / [diagnostische meldingen](@)                                 |
| `rendering.md`         | SVG- en markdown-rendering ([renderer](@), [glyphs](@), [hugo-output](@))                                |
| `publication.md`       | Hugo, preview, productie en [publicatie](@)-checks                                                       |
| `ci.md`                | Tests, CI en betrouwbaarheid                                                                             |
| `source-trace.md`      | Herkomst van de geconsolideerde architectuur                                                             |

Historische stapdocumenten blijven bronmateriaal en horen uiteindelijk onder `history/`.
