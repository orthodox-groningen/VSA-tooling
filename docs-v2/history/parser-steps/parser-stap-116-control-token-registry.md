# Stap 116 - Control token registry

## Doel

Deze stap legt control tokens vast als een **registry**: een expliciete tabel met
gereserveerde tokens, abstracte betekenissen en renderer-specifieke interpretatie.

Deze stap activeert de tokens nog niet in de parser of bracket-token-stream.

## Registry

| Token | Abstracte betekenis | Hard/zacht | Renderer-onafhankelijk doel |
|---|---|---|---|
| `[*]` | `phrase_rest` | hard | rustpunt, adempunt of zichtbare tekstmarkering |
| `[/]` | `phrase_boundary` | hard | frasegrens, maatstreep of regelgrens |
| `[*?]` | `optional_phrase_rest` | zacht | optioneel rustpunt, optioneel adempunt of zachte hint |
| `[/?]` | `optional_phrase_boundary` | zacht | optionele frasegrens, optionele maatstreep of zachte hint |

## Rendererbeleid

De registry beschrijft alleen de abstracte betekenis.

Elke renderer of exporteur bepaalt via configuratie hoe een token wordt uitgewerkt.

### SVG

Mogelijke uitwerkingen:

- zichtbaar teken;
- harde regelbreuk;
- zachte regelbreuk;
- geen uitvoer.

### MusicXML

Mogelijke uitwerkingen:

- breath mark;
- barline;
- system break;
- geen uitvoer.

## Huidig parsercontract

Totdat de parser expliciet wordt aangepast, blijven deze tokens gewone tekst of
syntaxfouten volgens de bestaande regels.

Belangrijk bestaande contracten:

```text
[/] tekst
```

blijft voor de bracket-token-stream gewone tekst.

```text
Parser("[/]")
```

blijft ongeldig, omdat het geen hoogte-markering `[<EHM>:]` is.

## Latere activering

Wanneer deze tokens echt syntax worden, moeten tegelijk worden aangepast:

- `bracket_token_stream`;
- parser;
- semantische validatie;
- SVG-rendering;
- MusicXML-export;
- bestaande stap-96/97/105 regressietests.

Tot die migratiestap mag de registry niet impliciet het huidige parsercontract wijzigen.
