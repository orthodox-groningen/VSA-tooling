# Technische specificatie: `bron`-repository

Status: ontwerpdocument, groeit mee met de praktijk. Versie per 27 juni
2026.

## 1. Doel en scope

De `bron`-repository is de centrale, enige bron van waarheid voor de
muzikale inhoud (zangstukken) die binnen `orthodox-groningen` wordt gebruikt.
Parochie-sites (bijv. Hugo-installaties voor Hemelum, Groningen) consumeren
deze repository als databron; ze bewerken hem niet rechtstreeks.

De repository bevat **bronnen** (zie §3.1) en de bijbehorende metadata. Hij
bevat **geen** afgeleide bestanden (SVG, MusicXML gegenereerd uit VSA,
audio), en **geen** informatie over welke parochie welk materiaal gebruikt.

## 2. Mapstructuur (top-level)

```
bron/
├── README.md
├── LICENSE-CONTENT          # CC BY-SA 4.0 — inhoud/notatie/metadata
├── LICENSE-CODE             # MIT — eventuele scripts/tools
├── .gitignore
├── docs/
│   ├── specs/
│   │   └── terminologie.md       # vier niveaus, aliassen (canoniek in bron)
│   ├── zangstuk-formaat.md       # specificatie van zangstuk.yaml en .vsa
│   └── bron-repo-specificatie.md # dit document
├── zangstukken/
│   └── <zangstuk-id>/
│       ├── zangstuk.yaml
│       └── sources/
│           ├── vsa/<bron-id>.vsa
│           ├── scan/<bestandsnaam>.<pdf|png|jpg>
│           └── musicxml/<bron-id>.musicxml      # alleen als zelfstandige bron
└── composities/                                  # nog niet uitgewerkt, zie §7
    └── <compositie-id>.yaml
```

`derived/` (of vergelijkbaar) bestaat hier bewust **niet** als
git-getrackt onderdeel: afgeleide bestanden (SVG, gegenereerde MusicXML,
audio) worden gebouwd op het moment dat ze nodig zijn (lokaal of via CI) en
horen niet in deze repository te staan.

## 3. Het zangstuk

### 3.1 Definitie
Een **zangstuk** is de eenheid waarvoor één of meer bronnen bestaan. Een
bestand is een **bron** als er geen geautomatiseerd, herhaalbaar pad bestaat
om het uit een ander bestand in deze repository te genereren (zie ook
§3.1.1). Elk zangstuk staat in een eigen map onder `zangstukken/`, met als
mapnaam de zangstuk-`id`.

### 3.1.1 Bron versus afgeleid
- **Bron**: scans, VSA-bestanden, MusicXML/andere bestanden die
  rechtstreeks uit een muziekprogramma komen (niet afgeleid van VSA in deze
  repository).
- **Afgeleid**: alles dat geautomatiseerd uit een bronbestand in deze
  repository gegenereerd kan worden (bijv. SVG of MusicXML, gegenereerd door
  de vsa-tool uit een `.vsa`-bestand). Wordt niet opgeslagen in de
  repository.

### 3.2 Naamgeving van de zangstuk-`id`
- Map- en bestandsnamen: lowercase, woorden gescheiden door een koppelteken
  (`-`), geen diakritische tekens, geen spaties.
- **Specifieke gelegenheid** (heiligenfeest, vaste kalenderdatum):
  `<type>-<gelegenheid-slug>` — bijv. `troparion-nicolaas-van-myra`.
- **Zondagscyclus** (afhankelijk van de toon van de week, geen vaste datum):
  `<type>-zondag-toon-<n>` — bijv. `troparion-zondag-toon-1`.
- **Geen gelegenheid/cyclus van toepassing**: de algemene naam van het
  zangstuk is voldoende — bijv. `trisagion`, `eengeboren-zoon`.
- De `id` is **stabiel**: eenmaal toegekend, niet meer wijzigen zodra er
  ergens naar verwezen wordt (composities, toekomstige parochie-sites).
  Hernoemen mag alleen in een vroege/experimentele fase, zoals nu.

### 3.3 `zangstuk.yaml` — verplichte en optionele velden

```yaml
id: <string>                  # verplicht, gelijk aan de mapnaam
title: <string>                # verplicht

# Liturgische metadata (optioneel, naar behoefte toevoegen)
occasion: <string>             # bijv. "H. Nicolaas van Myra"
occasion_date: <"MM-DD">       # vaste kalenderdatum, indien van toepassing
occasion_type: vast-feest | zondag-cyclus
tone: <integer>                # liturgische toon, los van de identiteit/id
koormap_nummer: <string>       # bestaand Nederlands nummeringssysteem,
                                # bijv. "8a" — NIET de bestandsnaam-sorteer-
                                # prefix (010-, 020-, ...), die is uitsluitend
                                # sorteervolgorde van scans

sources:                       # verplicht, minstens één entry
  - id: <string>               # verplicht, uniek binnen dit zangstuk
    # --- precies één van de volgende drie statussen ---
    file: <relatief pad>           # bestand staat in deze repository
    access:                        # bestand NIET opgenomen (copyright)
      note: <string>
      contact: <string>            # en/of:
      url: <string>
    status: nog-niet-getranscribeerd  # bron bekend, nog niet als bestand aanwezig
    # --- einde statusveld ---

    based_on: <source-id>      # optioneel: deze source is een bewerking van
                                # een andere source binnen hetzelfde zangstuk
    author: <string>            # gebruik author/composer/arranger naar wat
    composer: <string>          # van toepassing is; ook "Anoniem"/"Anoniem-2"
    arranger: <string>          # zijn toegestane waarden
    reference: <string>         # bijv. "Liturgikon, pp. 174-175"
    description: <string>       # vrije toelichting op de variant
    language: <string>          # bij meerdere taalversies van dezelfde
                                  # compositie, bijv. "nederlands"
    copyright_status: vrij | copyrighted | onbekend
    note: <string>               # vrije aantekening
```

Regels:
- Exact één van `file:` / `access:` / `status: nog-niet-getranscribeerd` per
  source-entry.
- `based_on` verwijst naar een `id` van een andere source **binnen
  hetzelfde zangstuk**.
- Een scan die door meerdere zangstukken wordt gedeeld (zie §4) wordt
  gerefereerd met een relatief pad dat buiten de eigen zangstuk-map wijst,
  bijv. `file: ../ander-zangstuk-id/sources/scan/bestand.pdf`.

## 4. Eén bronbestand, meerdere zangstukken

- **Tekst/VSA-bronbestanden** (bijv. een markdown-bestand met meerdere
  `::: vsa-notatie ::: `-blokken) die meerdere zangstukken bevatten: **bij
  opname in deze repository altijd splitsen** in losse `.vsa`-bestanden,
  één per zangstuk, elk in de map van het bijbehorende zangstuk.
- **Scans/PDF's** met meerdere zangstukken op één blad: **niet** splitsen.
  Het bestand blijft fysiek bij één zangstuk; andere zangstukken die
  hetzelfde bestand delen, verwijzen ernaar met een relatief pad (zie §3.3).
  Bij herhaaldelijk voorkomen van dit patroon: een gedeelde `/scans/`-map op
  het hoogste niveau overwegen in plaats van kruisverwijzingen.

## 5. VSA-bestanden

### 5.1 Platte VSA (zonder frontmatter)
Een `.vsa`-bestand zonder `---`-kop is platte VSA-notatietekst zonder
metadata. Dit blijft volledig ondersteund.

### 5.2 VSA met YAML-frontmatter
Optioneel kan een `.vsa`-bestand een YAML-frontmatter hebben:

```yaml
---
muziek:
  do: <notenaam+octaaf, bijv. F4>
  mode: major | minor
  tempo: <integer, BPM>
  meter: <string, bijv. "4/4">      # optioneel
identificatie:
  title: <string>
  subtitle: <string>                 # optioneel
  composer: <string>
  lyricist: <string>                 # optioneel
  rights: <string>                    # optioneel, vrije weergave-tekst
  language: <taalcode, bijv. nl>
  tone: <integer>
---
```

**Voorrangsregel** (zie ook samenvattingsdocument): binnen deze repository
is `zangstuk.yaml` de uiteindelijke bron van waarheid voor velden die
overlappen met `identificatie` (title, auteurschap, taal, toon,
rechten/copyright-status). De `identificatie`-sectie in de frontmatter is
primair bedoeld voor gebruik van het `.vsa`-bestand **los van** deze
repository (bijv. zelfstandig met de vsa-tool, of gedeeld met derden).
`rights` is een vrije weergave-tekst voor gegenereerde output, geen
vervanging van `copyright_status`/`access:`.

## 6. Vereiste bestanden voor het functioneren van de repository

| Bestand | Verplicht | Functie |
|---|---|---|
| `README.md` | ja | Eerste uitleg, korte structuurbeschrijving |
| `LICENSE-CONTENT` | ja | Licentie voor inhoud (CC BY-SA 4.0) |
| `LICENSE-CODE` | ja, zodra er scripts zijn | Licentie voor code (MIT) |
| `.gitignore` | ja | Voorkomt dat afgeleide/tijdelijke bestanden worden getrackt |
| `docs/zangstuk-formaat.md` | aanbevolen | Volledige specificatie van het zangstuk-formaat |
| `zangstukken/<id>/zangstuk.yaml` | ja, per zangstuk | Metadata en sources |
| `zangstukken/<id>/sources/...` | ja, tenzij alle sources `access:`/`status:` zijn | Daadwerkelijke bronbestanden |

Er is op dit moment **geen build-configuratiebestand** (bijv. voor het
genereren van afgeleide bestanden of een gepubliceerde index) — dat is een
nog te ontwerpen onderdeel, zie §8.

## 7. Composities (nog niet uitgewerkt)

Een **compositie** beschrijft welke zangstukken (en welke source-variant
daarvan) in welke volgorde gebruikt worden voor een gebruikscontext (bijv.
"Antifonen - weekdagen, Hemelum"). Dit voorkomt duplicatie van VSA-inhoud
over meerdere documenten.

Voorlopig voorstel (niet definitief):

```yaml
title: <string>
parish: <parochie-slug>           # optioneel
items:
  - { zangstuk: <zangstuk-id>, source: <source-id> }
  - ...
```

Open vragen: exacte locatie (`composities/` op het hoogste niveau, zoals nu
aangenomen, of ergens anders), bestandsformaat (kale YAML versus een
leesbaarder documentformaat), en of dit uiteindelijk in deze repository
hoort of beter bij de parochie-repo's past (een compositie is in feite al
een eerste stap richting "gebruik door een specifieke parochie").

## 8. Nog te ontwerpen: publicatie/build

Nog niet uitgewerkt, maar relevant voor het vervolg:
- Een build-stap die uit `.vsa`-bestanden afgeleide bestanden genereert
  (SVG nu, MusicXML in de toekomst) met de vsa-tool.
- Een gepubliceerde index (bijv. JSON, via GitHub Pages) die parochie-sites
  tijdens hun eigen build kunnen raadplegen, zodat zij niet rechtstreeks in
  de structuur van deze repository moeten graven.
- Een manier om bij build-time `file:`-sources wél en `access:`-sources
  niet mee te nemen in wat er gepubliceerd wordt.

## 9. Workflows

Onderstaande workflows beschrijven het beheer van de repository in de
huidige fase: één beheerder (de opdrachtgever), geen self-service door
parochies. Koorleider/priester geven inhoudelijk akkoord buiten git om
(mondeling, e-mail, etc.); de beheerder verwerkt dat in commits.

### 9.1 Nieuw zangstuk toevoegen (vanaf een nieuwe bron)
1. Bepaal de zangstuk-`id` volgens de naamgevingsconventie (§3.2).
2. Maak de map `zangstukken/<id>/` aan met een lege `sources/`-structuur.
3. Plaats het bronbestand in de juiste submap (`sources/vsa/`,
   `sources/scan/`, ...).
4. Schrijf `zangstuk.yaml`: minimaal `id`, `title`, en één source-entry met
   `file:`, `access:`, of `status: nog-niet-getranscribeerd`.
5. Vul liturgische metadata in indien van toepassing (`occasion`, `tone`,
   `koormap_nummer`, ...).
6. Commit en push.

### 9.2 Nieuwe bronvariant toevoegen aan een bestaand zangstuk
1. Controleer of het inderdaad een variant van een bestaand zangstuk is
   (inhoudelijke vergelijking), niet een nieuw zangstuk.
2. Plaats het nieuwe bronbestand in `sources/<formaat>/` van het bestaande
   zangstuk.
3. Voeg een nieuwe source-entry toe aan `zangstuk.yaml`, met `based_on` naar
   de oorspronkelijke source indien van toepassing.
4. Commit en push.

### 9.3 Eén bronbestand met meerdere zangstukken verwerken
1. Bepaal of het bestand splitsbaar is (tekst/VSA) of niet (scan/PDF).
2. **Splitsbaar**: splits in losse bestanden, volg daarna workflow 9.1 of
   9.2 per zangstuk.
3. **Niet-splitsbaar**: volg workflow 9.1 voor het eerste zangstuk (bestand
   komt daar fysiek te staan); volg workflow 9.1 voor het tweede zangstuk
   maar gebruik een relatieve `file:`-verwijzing naar het bestand bij het
   eerste zangstuk in plaats van een eigen kopie.

### 9.4 Bron vervangen door een definitievere versie (bijv. scan → VSA)
1. Voeg de nieuwe, definitievere bron toe als nieuwe source-entry (niet de
   oude verwijderen) — zie §3.1, `based_on` indien relevant.
2. Beoordeel of de oudere source (bijv. de scan) nog behouden moet blijven
   ter referentie, of kan worden gemarkeerd/verwijderd. Bij twijfel:
   behouden, met een `note:` die de status verduidelijkt.

### 9.5 Zangstuk of source markeren als copyright-gevoelig
1. Zet `copyright_status: copyrighted` (of `onbekend` als nog niet
   uitgezocht) op de source-entry.
2. Vervang `file:` door `access:` met `note:` en `contact:`/`url:`.
3. Verwijder het bronbestand zelf uit de repository (of neem het nooit op).

### 9.6 Een zangstuk-id hernoemen
Alleen toepassen in de huidige, vroege fase waarin nog niets extern naar
id's verwijst. Zodra composities, build-indexen of parochie-sites bestaan:
vermijden, of expliciet als breaking change behandelen.
1. Hernoem de map.
2. Werk `id:` in `zangstuk.yaml` bij.
3. Werk alle relatieve cross-references die naar deze map verwijzen bij
   (zie §4, gedeelde scans) — controleer alle andere `zangstuk.yaml`'s op
   het oude pad.
4. Werk eventuele `note:`-teksten bij die het oude id noemen.

### 9.7 Afgeleide bestanden genereren (nog niet geautomatiseerd)
Op dit moment handmatig, met de vsa-tool, buiten de repository om. Niet
committen. Zodra een build-stap bestaat (zie §8), dit vervangen door een
geautomatiseerde workflow.

### 9.8 Validatie (nog niet geautomatiseerd, aanbevolen voor de toekomst)
Mogelijke toekomstige controles, nu nog handmatig te doen:
- Elke source-entry heeft precies één van `file:`/`access:`/`status:`.
- Elk `file:`-pad verwijst naar een bestaand bestand.
- Elke `based_on`-waarde verwijst naar een bestaande source-id binnen
  hetzelfde zangstuk.
- VSA-frontmatter (indien aanwezig) is geldige YAML en bevat geen
  tegenstrijdigheden met `zangstuk.yaml` (zie §5.2).
