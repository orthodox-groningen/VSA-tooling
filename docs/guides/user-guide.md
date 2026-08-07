# VSA Tool gebruikershandleiding

Deze handleiding is bedoeld voor iemand die de VSA-tool wil gebruiken zonder de code te hoeven begrijpen.

De voorbeelden zijn geschreven voor Windows 11 en CMD.exe.

## 1. Wat doet de VSA-tool?

De VSA-tool helpt bij het werken met [VSA-notatie](@bron): je schrijft
[VSA-tekst](@) in een [vsa-bestand](@bron) of in een [VSA-blok](@) in Markdown.

De tool kan:

| Taak                                                        | Commando             |
| ----------------------------------------------------------- | -------------------- |
| Controleren op [geldige VSA-notatie](@)                     | `vsa validate`       |
| Een [vsa-bestand](@bron) omzetten naar SVG                  | `vsa svg`            |
| [VSA-blokken](@) in Markdown vinden                         | `vsa blocks`         |
| Markdownbestanden verwerken naar SVG-bestanden              | `vsa process`        |
| Markdown voor Hugo genereren                                | `vsa build-markdown` |
| De interne structuur bekijken ([ast](@))                    | `vsa parse --ast`    |

Globaal:

```text
VSA-notatie
  ↓
controle
  ↓
SVG
  ↓
Markdown/Hugo-site
```

## 2. Welke taak wil ik uitvoeren?

Gebruik deze keuzetabel.

| Ik wil...                                                | Gebruik                                                    |
| -------------------------------------------------------- | ---------------------------------------------------------- |
| weten of mijn notatie [geldige VSA-notatie](@) is        | `vsa validate`                                             |
| één [vsa-bestand](@bron) bekijken als afbeelding         | `vsa svg`                                                  |
| zien welke [VSA-blokken](@) in een Markdownbestand staan | `vsa blocks`                                               |
| alleen SVG's genereren uit Markdownbestanden             | `vsa process`                                              |
| Hugo-content maken uit bron-Markdown                     | `vsa build-markdown`                                       |
| debuggen hoe de [parser](@) de tekst begrijpt            | `vsa parse --ast`                                          |
| de hele toolketen lokaal controleren                     | `scripts\ci.cmd`                                           |
| docs lokaal bekijken                                     | `scripts\docs-serve.cmd`                                   |
| Hugo-preview (voorbeeldconsumer)                         | [VSA-demo](https://github.com/orthodox-groningen/VSA-demo) |

## 3. Vanuit welke map werk je?

De meeste commando's hieronder ga je uitvoeren vanuit de repo-root:

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
```

Als je daar staat, is dit pad:

```text
examples\consumer-minimal\content-source
```

eigenlijk:

```text
C:\Git\orthodox-groningen\VSA-tooling\examples\consumer-minimal\content-source
```

## 4. Basisinstallatie

Voer uit:

```cmd
scripts\bootstrap.cmd
```

Dit doet:

| Stap                 | Wat gebeurt er?                          |
| -------------------- | ---------------------------------------- |
| `.venv` maken        | Python krijgt een lokale projectomgeving |
| VSA-tool installeren | Het commando `vsa` wordt beschikbaar     |
| pytest installeren   | Tests kunnen worden gedraaid             |

Controle:

```cmd
vsa --version
```

Voorbeeld:

```text
vsa 0.1.0
```

## 5. Eerst controleren: `vsa validate`

### Waarvoor gebruik je dit?

Gebruik `vsa validate` om te controleren of je VSA-invoer bruikbaar is.

Voorbeelden:

```cmd
vsa validate examples\minimal\050_svg_demo.vsa
```

```cmd
vsa validate examples\consumer-minimal\content-source
```

### Wat wordt gecontroleerd?

De tool controleert op dit moment onder andere:

| Controle                                                 | Voorbeeld van fout          |
| -------------------------------------------------------- | --------------------------- |
| scope is goed afgesloten                                 | `{tekst`                    |
| scope is niet leeg                                       | `{}`                        |
| geen whitespace binnen scope                             | `{te kst}`                  |
| geen losse sluitaccolade                                 | `tekst}`                    |
| pitch-marker is goed afgesloten                          | `[//:`                      |
| pitch-marker heeft dubbele punt                          | `[//]`                      |
| parser kan de VSA lezen                                  | ongeldige modifierstructuur |
| hoogte- en lengte-modifiers passen semantisch bij elkaar | `{/&\tekst_}`               |

Voorbeeld van een semantische fout:

```text
{/&\tekst_}
```

Hier zijn er twee hoogteposities:

```text
/ en \
```

maar maar één lengtepositie:

```text
_
```

Dan meldt de tool:

```text
VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH
```

### Wat is de output bij succes?

```text
OK
```

Exitcode:

```text
0
```

Dit betekent: de tool heeft geen fouten gevonden.

### Wat is de output bij fouten?

Voorbeeld:

```text
examples\site-demo-invalid\invalid-1.md:blok-1:1:1: VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH: Hoogte- en lengte-modifier bevatten niet hetzelfde aantal muzikale posities.
```

Uitleg:

| Deel                                      | Betekenis                                   |
| ----------------------------------------- | ------------------------------------------- |
| `examples\site-demo-invalid\invalid-1.md` | bestand waarin de fout zit                  |
| `blok-1`                                  | eerste [VSA-blok](@) in dat Markdownbestand |
| `1:1`                                     | regel en kolom binnen dat [VSA-blok](@)     |
| `VSA-...`                                 | foutcode                                    |
| tekst erna                                | Nederlandse uitleg                          |

Exitcode:

```text
1
```

Dit betekent: er zijn fouten gevonden.

### Wat doe je na een fout?

Gebruik deze aanpak:

| Stap   | Actie                                             |
| ------ | ------------------------------------------------- |
| 1      | Kijk naar het bestand vóór de eerste dubbele punt |
| 2      | Kijk welk `blok-N` genoemd wordt                  |
| 3      | Zoek dat [VSA-blok](@) in het Markdownbestand     |
| 4      | Kijk naar de foutcode                             |
| 5      | Corrigeer de VSA-notatie                          |
| 6      | Draai `vsa validate` opnieuw                      |

Voorbeeld:

```cmd
vsa validate examples\site-demo-invalid
```

Als er meerdere fouten zijn, toont de tool ze zoveel mogelijk allemaal.

Dat is bewust zo, zodat je niet telkens één fout hoeft te herstellen en opnieuw te draaien.

## 6. Eén SVG maken: `vsa svg`

### Waarvoor gebruik je dit?

Gebruik dit als je één los VSA-bestand snel als afbeelding wilt bekijken.

Voorbeeld:

```cmd
vsa svg examples\minimal\050_svg_demo.vsa output.svg
start output.svg
```

### Parameters

| Parameter      | Verplicht   | Betekenis                                        |
| -------------- | ----------- | ------------------------------------------------ |
| `svg`          | ja          | Subcommando: maak SVG                            |
| `<input.vsa>`  | ja          | VSA-bestand dat gelezen wordt                    |
| `<output.svg>` | ja          | SVG-bestand dat wordt aangemaakt of overschreven |

### Opties

| Optie                      | Default   | Betekenis                                               |
| -------------------------- | --------- | ------------------------------------------------------- |
| `--max-line-width <getal>` | `800`     | maximale breedte van een regel voordat wordt afgebroken |

Voorbeeld:

```cmd
vsa svg examples\minimal\100_multiline_demo.vsa output.svg --max-line-width 400
```

### Wat wordt gegenereerd?

Een SVG-bestand, bijvoorbeeld:

```text
output.svg
```

Als dat bestand al bestaat, wordt het overschreven.

### Wat kan er fout gaan?

| Fout                  | Mogelijke oorzaak               | Wat doen?                          |
| --------------------- | ------------------------------- | ---------------------------------- |
| bestand niet gevonden | pad is onjuist                  | controleer met `dir`               |
| parsefout             | geen [geldige VSA-notatie](@)   | draai eerst `vsa validate`         |
| SVG ziet er raar uit  | renderer is nog in ontwikkeling | bewaar voorbeeld als regressiecase |

Aanbevolen:

```cmd
vsa validate examples\minimal\100_multiline_demo.vsa
vsa svg examples\minimal\100_multiline_demo.vsa output.svg
```

## 7. [VSA-blokken](@) inspecteren: `vsa blocks`

### Waarvoor gebruik je dit?

Gebruik dit om te zien welke [VSA-blokken](@) in een Markdownbestand staan.

Voorbeeld:

```cmd
vsa blocks examples\minimal\031_markdown_block_metadata.md
```

Output zonder `--json`:

```text
1 VSA-blok(ken) gevonden
```

Met JSON:

```cmd
vsa blocks examples\minimal\031_markdown_block_metadata.md --json
```

Dan krijg je onder andere:

| Veld         | Betekenis                                |
| ------------ | ---------------------------------------- |
| `start_line` | regel waar het blok begint               |
| `end_line`   | regel waar het blok eindigt              |
| `metadata`   | instellingen zoals `do`, `mode`, `tempo` |
| `body`       | de VSA-inhoud                            |
| `ast`        | interne parserstructuur                  |

### Wanneer gebruik je `--json`?

Gebruik `--json` als je wilt debuggen.

Bij normaal dagelijks gebruik heb je dit meestal niet nodig.

## 8. Parser debuggen: `vsa parse --ast`

### Waarvoor gebruik je dit?

Gebruik dit alleen als je wilt zien hoe de tool een VSA-bestand intern begrijpt.

Voorbeeld:

```cmd
vsa parse examples\minimal\050_svg_demo.vsa --ast
```

### Wat is AST?

AST betekent:

```text
Abstract Syntax Tree
```

Dat is een technische naam voor de interne structuur van de invoer.

Voorbeeld:

```text
[:] {/Hei_}{/lig_} is de Heer. [:]
```

kan intern bestaan uit:

| Node              | Betekenis       |
| ----------------- | --------------- |
| `PitchMarkerNode` | `[:]`           |
| `ScopeNode`       | `{/Hei_}`       |
| `ScopeNode`       | `{/lig_}`       |
| `TextNode`        | ` is de Heer. ` |
| `PitchMarkerNode` | `[:]`           |

### Output

Met `--ast` krijg je JSON.

Zonder `--ast` krijg je alleen:

```text
OK
```

als de parser het bestand kan lezen.

### Wanneer heb je dit nodig?

| Situatie                       | Nodig?      |
| ------------------------------ | ----------- |
| gewone gebruiker               | meestal nee |
| fout zoeken in parser          | ja          |
| regressietests maken           | ja          |
| controleren of tekst verdwijnt | ja          |

## 9. SVG's genereren uit Markdown: `vsa process`

### Waarvoor gebruik je dit?

Gebruik `vsa process` als je Markdownbestanden hebt met [VSA-blokken](@) en alleen de SVG-bestanden wilt genereren.

Voorbeeld:

```cmd
vsa process examples\site-demo generated\vsa
```

### Parameters

| Parameter          | Verplicht   | Betekenis                                    |
| ------------------ | ----------- | -------------------------------------------- |
| `<bestand-of-map>` | ja          | Markdownbestand of map met Markdownbestanden |
| `<output-dir>`     | ja          | Map waarin SVG-bestanden worden geschreven   |

### Wat moet aanwezig zijn?

| Item                       | Moet bestaan?   | Uitleg                       |
| -------------------------- | --------------- | ---------------------------- |
| invoerbestand of invoermap | ja              | Hier staan Markdownbestanden |
| uitvoermap                 | nee             | Wordt automatisch aangemaakt |

### Wat wordt gegenereerd?

Voorbeeld:

```text
generated\vsa\zondag-toon-1-block-1.svg
```

Naamopbouw:

| Deel            | Betekenis                           |
| --------------- | ----------------------------------- |
| `zondag-toon-1` | afgeleid van bronpad/bestandsnaam   |
| `block-1`       | eerste [VSA-blok](@) in dat bestand |
| `.svg`          | gegenereerde SVG                    |

### Opties

| Optie                      | Default             | Betekenis            |
| -------------------------- | ------------------- | -------------------- |
| `--no-validate`            | uit                 | sla validatie over   |
| `--max-line-width <getal>` | `vsa.toml` of `800` | regelbreedte van SVG |

Gebruik `--no-validate` alleen tijdelijk bij debuggen.

Normaal wil je validatie juist aan laten staan.

## 10. Hugo-content bouwen: `vsa build-markdown`

### Waarvoor gebruik je dit?

Dit is het belangrijkste commando voor Hugo.

Het maakt:

1. gegenereerde Markdown;
2. gegenereerde SVG-bestanden.

Voorbeeld:

```cmd
vsa build-markdown examples\consumer-minimal\content-source generated\content generated\static\vsa
```

### Parameters

| Parameter      | Verplicht   | Betekenis                             |
| -------------- | ----------- | ------------------------------------- |
| `<input-dir>`  | ja          | map met handmatig geschreven Markdown |
| `<output-dir>` | ja          | map waar gegenereerde Markdown komt   |
| `<assets-dir>` | ja          | map waar gegenereerde SVG's komen     |

### Wat is `<input-dir>`?

Dit is waar jij schrijft.

Voorbeeld:

```text
examples\consumer-minimal\content-source
```

Daarin staat bijvoorbeeld:

```text
smoke.md
```

### Wat is `<output-dir>`?

Dit is waar de tool nieuwe Markdown schrijft.

Voorbeeld:

```text
generated\content
```

De mapstructuur blijft behouden:

```text
input:
examples\consumer-minimal\content-source\smoke.md

output:
generated\content\smoke.md
```

### Wat is `<assets-dir>`?

Dit is de fysieke map waar SVG-bestanden worden geschreven.

Voorbeeld:

```text
generated\static\vsa
```

Deze map hoeft nog niet te bestaan.

De tool maakt hem aan.

### Wat staat er in `<assets-dir>`?

Bijvoorbeeld:

```text
generated\static\vsa\zondag-toon-1-block-1.svg
```

Per [VSA-blok](@) komt er één SVG-bestand.

### Wat verandert er in de Markdown?

Bron-Markdown:

```markdown
::: vsa-notatie
[:] {/Hei_}{/lig_} is de Heer. [:]
:::
```

Gegenereerde Markdown met `img`:

```html
<img class="vsa-notation" src="/vsa/zondag-toon-1-block-1.svg" alt="VSA notatie">
```

Gegenereerde Markdown met `shortcode`:

```go-html-template
{{< vsa src="/vsa/zondag-toon-1-block-1.svg" >}}
```

### Opties

| Optie                          | Default                  | Betekenis                    |
| ------------------------------ | ------------------------ | ---------------------------- |
| `--assets-url-prefix <prefix>` | uit `vsa.toml` of `/vsa` | URL-pad dat in Markdown komt |
| `--max-line-width <getal>`     | uit `vsa.toml` of `800`  | SVG-regelbreedte             |
| `--output-mode img`            | uit `vsa.toml` of `img`  | gewone `<img>` tags          |
| `--output-mode shortcode`      | uit `vsa.toml` of `img`  | Hugo-shortcodes              |

### Bestandspad versus URL-pad

Dit is belangrijk.

`<assets-dir>` is een bestandspad:

```text
generated\static\vsa
```

`--assets-url-prefix` is een URL-pad:

```text
/vsa
```

Voorbeeld:

| Soort       | Waarde                 | Betekenis                              |
| ----------- | ---------------------- | -------------------------------------- |
| bestandspad | `generated\static\vsa` | waar SVG's op schijf worden opgeslagen |
| URL-pad     | `/vsa`                 | wat in HTML/Markdown wordt gezet       |

Als Hugo later `static\vsa` publiceert, wordt dat op de site bereikbaar als:

```text
/vsa/naam.svg
```

### Wat kan er fout gaan?

| Fout                              | Mogelijke oorzaak                                 | Oplossing                              |
| --------------------------------- | ------------------------------------------------- | -------------------------------------- |
| validatiefout                     | [VSA-blok](@) bevat fout                          | draai `vsa validate <input-dir>`       |
| geen SVG's                        | geen [VSA-blokken](@) gevonden                    | controleer `::: vsa-notatie`           |
| afbeelding niet zichtbaar in Hugo | `assets-url-prefix` past niet bij Hugo static-map | controleer outputpad en URL            |
| shortcode zichtbaar als tekst     | shortcode layout ontbreekt                        | voeg `layouts\shortcodes\vsa.html` toe |
| output overschreven               | doelmap was al gebruikt                           | gebruik aparte `generated\...` map     |

## 11. `vsa.toml`

Voorbeeld:

```toml
[rendering]
max-line-width = 800

[hugo]
assets-url-prefix = "/vsa"
output-mode = "img"

# Alternatief:
# output-mode = "shortcode"
```

### Betekenis

| Instelling          | Default   | Betekenis                           |
| ------------------- | --------- | ----------------------------------- |
| `max-line-width`    | `800`     | maximale SVG-regelbreedte           |
| `assets-url-prefix` | `/vsa`    | URL-prefix in gegenereerde Markdown |
| `output-mode`       | `img`     | `img` of `shortcode`                |

### Wat heeft voorrang?

```text
CLI-optie
  ↓
vsa.toml
  ↓
interne default
```

Voorbeeld:

Als in `vsa.toml` staat:

```toml
max-line-width = 800
```

maar je voert uit:

```cmd
vsa svg input.vsa output.svg --max-line-width 400
```

dan wint `400`.

## 12. Lokale scripts

| Script                   | Doel                        |
| ------------------------ | --------------------------- |
| `scripts\bootstrap.cmd`  | lokale omgeving klaarmaken  |
| `scripts\test.cmd`       | tests draaien               |
| `scripts\ci.cmd`         | volledige lokale CI         |
| `scripts\docs-serve.cmd` | MkDocs docs lokaal serveren |

## 13. Aanbevolen werkwijze

Tijdens ontwikkeling:

```cmd
scripts\test.cmd
```

Voor commit:

```cmd
scripts\ci.cmd
```

Daarna:

```cmd
git add .
git commit -m "Beschrijving"
git push
```

Op GitHub controleer je daarna:

```text
Actions
```

## 14. Als iets fout gaat

### Stap 1: valideer eerst

```cmd
vsa validate <bestand-of-map>
```

### Stap 2: test los SVG

```cmd
vsa svg <bestand.vsa> output.svg
start output.svg
```

### Stap 3: bouw Markdown opnieuw

```cmd
vsa build-markdown <input-dir> <output-dir> <assets-dir>
```

### Stap 4: bekijk gegenereerde bestanden

```cmd
dir /s generated
```

### Stap 5: draai tests

```cmd
scripts\test.cmd
```

## 15. Wanneer gebruik je welk commando?

| Situatie                           | Commando             |
| ---------------------------------- | -------------------- |
| ik schrijf VSA en wil controleren  | `vsa validate`       |
| ik wil één afbeelding bekijken     | `vsa svg`            |
| ik wil Markdownblokken inspecteren | `vsa blocks --json`  |
| ik wil SVG's uit Markdown halen    | `vsa process`        |
| ik wil Hugo-content maken          | `vsa build-markdown` |
| ik wil parserproblemen debuggen    | `vsa parse --ast`    |
| ik wil alles lokaal controleren    | `scripts\ci.cmd`     |

## Warnings en errors

Vanaf stap 37 kent de validator twee niveaus.

| Severity   | Betekenis                             |
| ---------- | ------------------------------------- |
| `error`    | validatie faalt; exitcode wordt fout  |
| `warning`  | aandachtspunt; validatie mag doorgaan |

Syntaxproblemen blijven `error`.

Semantische aandachtspunten kunnen via configuratie als `warning` worden behandeld, bijvoorbeeld:

```text
VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH
```

De oude foutcodes `VSA-SEMANTIC-MISSING-FINAL-PITCH-MARKER` en `VSA-SEMANTIC-EMPTY-FINAL-PITCH-MARKER` zijn obsolete. Een ontbrekende eindmarkering is toegestaan. Een eindmarkering `[:]` is geldig en betekent neutrale hoogte, equivalent aan `[-:]` c.q. `[~:]`.

Praktisch betekent dit:

- `vsa validate` kan waarschuwingen tonen zonder de build te laten falen;
- CI kan later via configuratie strenger worden gemaakt;
- bestaande foutcodes blijven bruikbaar.
