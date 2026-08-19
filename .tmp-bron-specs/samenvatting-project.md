# Samenvatting: Orthodoxe kerkmuziek-repository project

Status per 27 juni 2026. Bedoeld als startpunt voor een vervolggesprek met
Claude als het huidige gesprek de sessielimiet bereikt.

## Doel van het project

Een systeem voor orthodoxe kerkmuziek (Slavische traditie) waarmee parochies
zangmateriaal kunnen beheren, delen en gebruiken voor de liturgie en voor het
instuderen van stemmen door koorleden. Het geheel wordt opgezet binnen de
GitHub-organisatie `github.com/orthodox-ronl`, ontsloten via
GitHub Pages (`*.github.io`).

## Huidig experiment

We bouwen een **bron-repository** (`bron`) met daarin de zangstukken, en
zijn van plan om die te gaan testen via een kale **Hugo-installatie** voor de
parochie Hemelum (en later Groningen) die zangstukken uit `bron` ophaalt en
toont. Doel van dat experiment: erachter komen welke ontwerpbeslissingen de
bron-repo nodig heeft door 'm echt te proberen *gebruiken*, niet om nu al een
kant-en-klare site te bouwen.

**Stand van zaken: alleen de bron-repo is uitgewerkt. De Hugo-kant is nog
niet gestart.** Dat is de logische volgende stap. Daarnaast bestaat er,
buiten dit gesprek, een **vsa-tool** die `.vsa`-bestanden naar SVG omzet
(en in de toekomst naar MusicXML), waar de bron-repo van afhankelijk is voor
het genereren van afgeleide weergaven.

## Architectuur — overwogen scenario's (besloten)

Drie scenario's zijn overwogen voor hoe parochies en de bron-repo zich tot
elkaar verhouden:

- **A. Monoliet bron + dunne parochie-sites** — alles centraal, parochies
  consumeren alleen.
- **B. Federatief** — elke parochie een eigen volwaardige repo, bron-repo
  alleen gedeelde basis.
- **C. Hybride** — bron-repo blijft centraal, met een laagdrempelig
  contributieproces voor parochies.

**Besluit**: voorlopig **scenario C in lichte vorm**. Met 2-3 parochies
(Hemelum, Groningen, mogelijk later Leeuwarden en Zwolle) en jij (de
opdrachtgever) als enige technische beheerder — de koorleider/priester
beoordeelt inhoudelijk maar werkt niet zelf met git — voegt een federatieve
opzet (B) alleen overhead toe zonder voordeel. Eén bron-repo dus, met
lichte, aparte presentatie-repo's per parochie (eigen "gezicht", gedeelde
content).

## Bron-repo: kernconcepten

### Terminologie
- **Zangstuk**: de eenheid waarvoor een bron (VSA, scan, MusicXML, ...)
  bestaat. Vervangt de eerder gebruikte, te generieke term "item".
- **Source / bron-variant**: een specifieke versie van een zangstuk, met
  eigen herkomst (auteur/componist/arrangeur, referentie).
- **Compositie** (nog niet uitgewerkt): een verzameling zangstukken in een
  bepaalde volgorde voor een gebruikscontext (bijv. "Antifonen - weekdagen,
  Hemelum"). Bedoeld om duplicatie van VSA-inhoud over meerdere
  markdown-bestanden te voorkomen. Vorm (YAML vs. leesbaar document) nog
  niet bepaald — bewust opengelaten, prioriteit lager dan de bron-repo zelf.

### Bron versus afgeleid: een principiële regel
Een bestand is een **bron** als er geen geautomatiseerd, herhaalbaar pad
bestaat om het uit een ander bestand in de repository te genereren. Dit
geldt voor scans, VSA-bestanden, en MusicXML/andere bestanden die
rechtstreeks uit een muziekprogramma komen (niet afgeleid van VSA). Een SVG
of MusicXML die door de vsa-tool automatisch uit een `.vsa`-bestand is
gegenereerd is **afgeleid** en wordt niet in de repository opgenomen — wordt
gegenereerd op het moment dat het nodig is (build-stap, nog niet
geïmplementeerd).

### Drie statussen voor een source-entry
1. **`file:`** — het bronbestand staat daadwerkelijk in de repository.
2. **`access:`** — het bestand wordt *niet* opgenomen omdat er copyright op
   rust; in plaats daarvan een contactpunt of URL.
3. **`status: nog-niet-getranscribeerd`** — de bron is bekend (en vaak vrij
   van rechten), maar nog niet als bestand aanwezig. Geen `file:`, geen
   `access:`.

### Eén bronbestand met meerdere zangstukken — een algemene regel
- **Tekst/VSA-bronbestanden** met meerdere zangstukken → **meteen
  splitsen** in losse `.vsa`-bestanden, één per zangstuk.
- **Scans/PDF's** met meerdere zangstukken op één blad → **niet** splitsen.
  Het bestand blijft bij één zangstuk; het andere zangstuk verwijst ermee
  naar het bestand via een relatief pad
  (`file: ../ander-zangstuk/sources/scan/bestand.pdf`). Bij herhaling van
  dit patroon: gedeelde `/scans/`-map op het hoogste niveau overwegen.

### Auteurschap / copyright
- Velden: `author`, `composer`, `arranger`. `copyright_status`: `vrij`,
  `copyrighted`, of `onbekend`.
- Copyright-gevoelig materiaal: geen apart private repo, metadata blijft
  publiek, bestand ontbreekt (`access:`-blok met contactpunt/URL).

### Liturgische metadata
- `occasion`, `occasion_date`, `occasion_type` (`vast-feest` /
  `zondag-cyclus`), `tone`, `koormap_nummer` (bestaand Nederlands
  liturgie-nummeringssysteem, bijv. "8a"/"15c" — **niet** te verwarren met
  de bestandsnaam-sorteerprefixes `010-`/`020-`/`034-`, die puur
  sorteervolgorde van scans zijn), `language` (voor zangstukken met
  meerdere taalversies van dezelfde compositie).
- **Bewust nog niet vastgelegd**: schriftlezingen (epistel/evangelie) —
  horen bij de viering als geheel, niet bij het zangstuk; te behandelen
  zodra het liturgisch-kalender-subsysteem aan de orde is.

### Naamgevingsconventie voor zangstuk-id's
- Specifieke gelegenheid (heiligenfeest op vaste datum):
  `<type>-<gelegenheid-slug>`, bijv. `troparion-nicolaas-van-myra`.
- Zondagscyclus (afhankelijk van de toon van de week):
  `<type>-zondag-toon-<n>`, bijv. `troparion-zondag-toon-1`.
- Geen vaste regel voor zangstukken zonder gelegenheid/cyclus (bijv.
  `trisagion`).

## VSA-bestanden: YAML-frontmatter (nieuw besluit)

`.vsa`-bestanden kunnen een optionele YAML-frontmatter krijgen
(`---`-afgebakend), gebruikt door de (externe) vsa-tool om naar MusicXML te
kunnen converteren. Bestanden zonder `---`-kop blijven gewoon platte
VSA-tekst zonder metadata — geen breaking change.

```yaml
---
muziek:
  do: F4
  mode: major
  tempo: 80
  meter: 4/4          # optioneel
identificatie:
  title: Tropaar van de zondag, toon 1
  composer: Traditioneel
  language: nl
  tone: 1
  subtitle: ...
  lyricist: ...
  rights: ...
---
```

### Verhouding tot `zangstuk.yaml` (belangrijke afspraak)
De `muziek`-sectie (do, mode, tempo, meter) overlapt niet met
`zangstuk.yaml` en hoort logisch bij het `.vsa`-bestand — geen probleem.

De `identificatie`-sectie overlapt wél met velden die al in `zangstuk.yaml`
staan (`title`, `composer`/`author`, `language`, `tone`, `rights`/
`copyright_status`). Om te voorkomen dat deze twee plekken uit elkaar gaan
lopen, geldt de volgende **voorrangsregel**:

> **Binnen de bron-repo is `zangstuk.yaml` de uiteindelijke bron van
> waarheid.** De `identificatie`-sectie in de VSA-frontmatter is vooral
> bedoeld voor het geval het `.vsa`-bestand **los van de bron-repo**
> gebruikt wordt (bijv. losstaand met de vsa-tool, of gedeeld met derden).
> Een toekomstige validatiestap zou kunnen controleren dat frontmatter en
> `zangstuk.yaml` niet tegenstrijdig zijn, in plaats van blind beide te
> vertrouwen.

`rights` in de frontmatter is een vrije weergave-tekst (komt op de
gegenereerde MusicXML/bladmuziek te staan), **geen vervanging** van het
gestructureerde `copyright_status`/`access:`-mechanisme in `zangstuk.yaml` —
dat blijft de plek waar bepaald wordt of een bestand wel/niet gepubliceerd
mag worden.

### Overige aanbevelingen (nog niet doorgevoerd, ter overweging)
- Optioneel `source_id:`-veld in de frontmatter, corresponderend met de
  `id:` van de bijbehorende source-entry in `zangstuk.yaml`, voor latere
  geautomatiseerde validatie dat bestand en metadata bij elkaar horen.
- Mogelijke toekomstige uitbreiding van `muziek` met per-sectie overrides
  (bijv. een refrein in een andere modus dan de coupletten) — nu niet nodig.
- Striktheid in datatypen (bijv. `tempo` als getal, niet als string) door
  de vsa-tool zelf af te dwingen, niet aan de gebruiker over te laten.

## Licenties
- **`LICENSE-CONTENT`**: CC BY-SA 4.0, voor de zangstukken/notatie/metadata.
- **`LICENSE-CODE`**: MIT, voor eventuele scripts/tools.

## Openstaande vragen / nog te beslissen

1. **Compositie-laag**: vorm nog niet gekozen. Lage prioriteit.
2. **Vierde zangstuk uit het Hemelum-bestand** ("Rest van de kleine
   intocht") — bewust nog niet uitgewerkt op verzoek van de opdrachtgever.
3. **Gedeelde `/scans/`-map**: nu opgelost met cross-reference. Bij
   herhaling herzien.
4. **Kastorski copyright**: status `onbekend`, bewust niet uitgezocht.
5. **`docs/zangstuk-formaat.md`**: nog te schrijven (zie het apart
   gedeelde document `bron-repo-specificatie.md` voor een eerste aanzet
   richting een technische specificatie van de hele repo).
6. **Hugo-opzet**: nog te beginnen. Eerste concrete stap: kale Hugo-site
   voor Hemelum, met als doel één pagina die één zangstuk toont. Open vraag:
   git submodule, build-time fetch via CI, of Hugo Modules? Voorlopige
   voorkeur: build-time fetch.
7. **VSA-validatie/voorrangsregel**: de afspraak hierboven (zangstuk.yaml
   is leidend) is nu alleen vastgelegd als regel, nog niet als
   geautomatiseerde controle.

## Technische randvoorwaarden van de werkomgeving (voor Claude zelf)
- Geen directe toegang tot de computer van de opdrachtgever: alleen
  bestanden die expliciet zijn geüpload, zijn leesbaar; alleen bestanden die
  expliciet via `present_files` worden aangeboden, zijn voor de
  opdrachtgever downloadbaar.
- Werk gebeurt in een tijdelijke containeromgeving die niet persisteert
  tussen gesprekken.

## Volledige boomstructuur van de bron-repo tot nu toe

```yaml
bron/                                    # root van de bron-repository
  README.md
  LICENSE-CONTENT                        # CC BY-SA 4.0
  LICENSE-CODE                           # MIT
  .gitignore
  docs/
    zangstuk-formaat.md                  # NOG TE SCHRIJVEN
    bron-repo-specificatie.md            # technische specificatie (zie apart document)

  zangstukken/

    antifoon-1-weekdagen/
      zangstuk.yaml
      # id: antifoon-1-weekdagen
      # title: "1e Antifoon (weekdagen)"
      # sources:
      #   - id: liturgikon
      #     author: "Liturgikon"
      #     reference: "Liturgikon, pp. 174-175, 270-271"
      #     copyright_status: vrij
      #     status: nog-niet-getranscribeerd
      #   - id: groningen
      #     file: sources/vsa/groningen.vsa
      #     based_on: liturgikon
      #     author: "Parochie Groningen"
      #     description: "Refreintekst 'Door de gebeden van de heilige
      #                    Moeder Gods, o Heiland, red ons'"
      #     copyright_status: vrij
      sources/
        vsa/
          groningen.vsa

    antifoon-2-weekdagen/
      zangstuk.yaml
      # id: antifoon-2-weekdagen
      # title: "2e Antifoon (weekdagen)"
      # sources:
      #   - id: liturgikon
      #     author: "Liturgikon"
      #     reference: "Liturgikon, pp. 174-175, 270-271"
      #     copyright_status: vrij
      #     status: nog-niet-getranscribeerd
      #   - id: groningen
      #     file: sources/vsa/groningen.vsa
      #     based_on: liturgikon
      #     author: "Parochie Groningen"
      #     description: "Refreintekst 'Verlos ons Zoon van God...'"
      #     copyright_status: vrij
      sources/
        vsa/
          groningen.vsa

    eengeboren-zoon/
      zangstuk.yaml
      # id: eengeboren-zoon
      # title: "Eengeboren Zoon (weekdagen)"
      # sources:
      #   - id: liturgikon
      #     file: sources/vsa/liturgikon.vsa
      #     author: "Liturgikon"
      #     copyright_status: vrij
      sources/
        vsa/
          liturgikon.vsa

    # NOG NIET UITGEWERKT (op verzoek opdrachtgever):
    # troparia-kleine-intocht-weekdagen/   ("Rest van de kleine intocht")

    troparion-zondag-toon-1/
      zangstuk.yaml
      # id: troparion-zondag-toon-1
      # title: "Troparion - Zondag, toon 1"
      # occasion: "Zondag (opstandingscyclus)"
      # occasion_type: zondag-cyclus
      # tone: 1
      # sources:
      #   - id: scan-koormap-010
      #     file: sources/scan/010-troparion-kondakion-toon-1.pdf
      #     author: "Liturgikon"
      #     copyright_status: vrij
      #   - id: groningen
      #     file: sources/vsa/groningen.vsa
      #     based_on: scan-koormap-010
      #     author: "Parochie Groningen"
      #     copyright_status: vrij
      sources/
        scan/
          010-troparion-kondakion-toon-1.pdf
        vsa/
          groningen.vsa

    kondakion-zondag-toon-1/
      zangstuk.yaml
      # id: kondakion-zondag-toon-1
      # title: "Kondakion - Zondag, toon 1"
      # occasion: "Zondag (opstandingscyclus)"
      # occasion_type: zondag-cyclus
      # tone: 1
      # sources:
      #   - id: scan-koormap-010
      #     file: ../troparion-zondag-toon-1/sources/scan/010-troparion-kondakion-toon-1.pdf
      #     author: "Liturgikon"
      #     copyright_status: vrij
      #   - id: groningen
      #     file: sources/vsa/groningen.vsa
      #     based_on: scan-koormap-010
      #     author: "Parochie Groningen"
      #     copyright_status: vrij
      sources/
        vsa/
          groningen.vsa

    trisagion/
      zangstuk.yaml
      # id: trisagion
      # title: "Trisagion"
      # koormap_nummer: "8a"
      # sources:
      #   - id: scan-koormap-020
      #     file: sources/scan/020-_8a__trisagion.pdf
      #     author: onbekend
      #     copyright_status: onbekend
      sources/
        scan/
          020-_8a__trisagion.pdf

    cherubijnenhymne-kastorski/
      zangstuk.yaml
      # id: cherubijnenhymne-kastorski
      # title: "Cherubijnenhymne (Kastorski)"
      # koormap_nummer: "15c"
      # sources:
      #   - id: scan-koormap-034-ru
      #     file: sources/scan/034-_15c__cherubijnen_hymne__kastorski_-_ru_.pdf
      #     composer: "A. Kastorski"
      #     language: kerkslavisch-getranslitereerd
      #     copyright_status: onbekend
      #   - id: scan-koormap-034-nl
      #     file: sources/scan/034-_15c__cherubijnen_hymne__kastorski_-_nl_.pdf
      #     composer: "A. Kastorski"
      #     language: nederlands
      #     copyright_status: onbekend
      sources/
        scan/
          034-_15c__cherubijnen_hymne__kastorski_-_ru_.pdf
          034-_15c__cherubijnen_hymne__kastorski_-_nl_.pdf

    cherubijnenhymne-onbekend/
      zangstuk.yaml
      # id: cherubijnenhymne-onbekend
      # title: "Cherubijnenhymne (vooralsnog ongeïdentificeerd)"
      # sources:
      #   - id: scan-koormap-groningen-2019
      #     file: sources/scan/koormap-groningen-2019.pdf
      #     author: onbekend
      #     copyright_status: onbekend
      #     note: "PLACEHOLDER-bestand, geen echte scan-inhoud."
      sources/
        scan/
          koormap-groningen-2019.pdf      # placeholder, nog te vervangen

    troparion-nicolaas-van-myra/
      zangstuk.yaml
      # id: troparion-nicolaas-van-myra
      # occasion: "H. Nicolaas van Myra"
      # occasion_date: "12-06"
      # occasion_type: vast-feest
      # tone: 4
      # sources: [{ id: liturgikon, file: sources/vsa/liturgikon.vsa,
      #             author: "Liturgikon", copyright_status: vrij }]
      sources/vsa/liturgikon.vsa

    kondakion-nicolaas-van-myra/
      zangstuk.yaml
      # id: kondakion-nicolaas-van-myra
      # occasion: "H. Nicolaas van Myra"
      # occasion_date: "12-06"
      # occasion_type: vast-feest
      # tone: 3
      # sources: [{ id: liturgikon, file: sources/vsa/liturgikon.vsa,
      #             author: "Liturgikon", copyright_status: vrij }]
      sources/vsa/liturgikon.vsa

    troparion-apostel-andreas/
      zangstuk.yaml
      # id: troparion-apostel-andreas
      # occasion: "Apostel Andreas, de Eerstgeroepene"
      # occasion_date: "11-30"
      # occasion_type: vast-feest
      # tone: 4
      # sources: [{ id: liturgikon, file: sources/vsa/liturgikon.vsa,
      #             author: "Liturgikon", copyright_status: vrij }]
      sources/vsa/liturgikon.vsa

    kondakion-apostel-andreas/
      zangstuk.yaml
      # id: kondakion-apostel-andreas
      # occasion: "Apostel Andreas, de Eerstgeroepene"
      # occasion_date: "11-30"
      # occasion_type: vast-feest
      # tone: 2
      # sources: [{ id: liturgikon, file: sources/vsa/liturgikon.vsa,
      #             author: "Liturgikon", copyright_status: vrij }]
      sources/vsa/liturgikon.vsa

    troparion-tempelgang-moeder-gods/
      zangstuk.yaml
      # id: troparion-tempelgang-moeder-gods
      # occasion: "Tempelgang van de Moeder Gods"
      # occasion_date: "11-21"
      # occasion_type: vast-feest
      # tone: 4
      # sources: [{ id: liturgikon, file: sources/vsa/liturgikon.vsa,
      #             author: "Liturgikon", copyright_status: vrij }]
      sources/vsa/liturgikon.vsa

    kondakion-tempelgang-moeder-gods/
      zangstuk.yaml
      # id: kondakion-tempelgang-moeder-gods
      # occasion: "Tempelgang van de Moeder Gods"
      # occasion_date: "11-21"
      # occasion_type: vast-feest
      # tone: 4
      # sources: [{ id: liturgikon, file: sources/vsa/liturgikon.vsa,
      #             author: "Liturgikon", copyright_status: vrij }]
      sources/vsa/liturgikon.vsa
```

## Hoe verder te gaan in een nieuw gesprek

Plak dit document als eerste bericht, en voeg toe wat je daarna wilt doen.
Zie ook het apart gedeelde `bron-repo-specificatie.md` voor de technische
specificatie en workflows.
