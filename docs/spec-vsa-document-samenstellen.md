# VSA Document Samenstellen — specificatie

## Doel

Een auteur schrijft bronbestanden in Markdown met VSA-uitbreidingen.
Uit die bronbestanden wordt gegenereerd:

- **een HTML-pagina** die normaal in een browser werkt
- **hetzelfde HTML-bestand**, maar met A4-opmaak actief bij afdrukken (`@media print`)

Er is geen aparte print-pipeline; één HTML-bestand dient beide doelen.

---

## Invoerformaat

Basis: Markdown met GFM-extensies (tabellen, doorhalen), en uitgebreid met de volgende directives.

### 1. VSA-blok (bestaand)

    ::: vsa-notatie
    [VSA-inhoud]
    :::

Wordt door `vsa build-markdown` omgezet naar SVG en ingevoegd als shortcode of `<img>`.

### 2. Paginabreuk

    :::pagebreak:::

- In HTML: `<div class="pagebreak"></div>`
- In browser: onzichtbaar
- Bij afdrukken: CSS zorgt voor een harde A4-paginabreuk

### 3. Transclusion (include)

    :::include pad/naar/bestand.ext:::

Het pad is **relatief aan het includerende bestand** (niet aan de projectroot).

Ondersteunde bestandstypen:

| Extensie | Behandeling |
|----------|-------------|
| `.md`, `.markdown` | Inhoud wordt als Markdown ingevoegd; eigen includes worden recursief opgelost |
| `.vsa` | Wordt behandeld als een `:::vsa-notatie:::` blok en omgezet naar SVG |
| `.svg` | Wordt ingevoegd als `<img src="...">` |
| `.jpg`, `.jpeg`, `.png`, `.webp`, `.gif` | Wordt ingevoegd als `<img src="...">` |

### 3b. Coria-oefenlink

    :::coria "pad/naar/melodie.vsa" [label="…"] [mode="auto|html|mxl"]:::

Pad relatief aan het includerende bestand, zoals bij `:::include`.

- Als `{stem}.coria.html` naast de `.vsa` staat: link naar Coria-export-HTML
  (partij al gekozen). Build kopieert naar `static/coria/…`.
- Anders: link naar gegenereerde `.mxl` via Coria `play_from_url`.

Wordt bij `build-markdown` omgezet naar Hugo-shortcode `coria-html` of `coria`.

### 4. Conditionele inhoud

    :::web-only:::
    [inhoud die alleen op de website verschijnt]
    :::end-web-only:::

    :::print-only:::
    [inhoud die alleen bij afdrukken verschijnt]
    :::end-print-only:::

- `web-only` — verborgen bij afdrukken, zichtbaar in browser
- `print-only` — verborgen in browser, zichtbaar bij afdrukken

### 5. Samen op één pagina

    :::keep-together:::
    [inhoud die bij afdrukken bij elkaar gehouden wordt]
    :::end-keep-together:::

    :::keep-together scale="70%":::
    [inhoud met verkleinde SVGs]
    :::end-keep-together:::

- In browser: geen zichtbaar effect
- Bij afdrukken: CSS voorkomt een paginabreuk binnen het blok
  (`break-inside: avoid`)
- Als de inhoud groter is dan één pagina, verplaatst de browser het hele blok
  naar de volgende pagina; past het dan nog steeds niet, dan wordt de
  `avoid`-instructie genegeerd
- De optionele parameter `scale="<waarde>"` schaalt alle VSA-notaties binnen
  het blok naar de opgegeven breedte (bijv. `"70%"`); de hoogte schaalt
  proportioneel mee omdat de SVGs een `viewBox` hebben. Gebruik dit wanneer
  twee of meer SVGs samen op één pagina moeten passen.

---

## Sluitingstags

Elk blok-directive eindigt met een **directief-specifieke sluitingstag**:

| Opening | Sluiting |
|---------|----------|
| `:::web-only:::` | `:::end-web-only:::` |
| `:::print-only:::` | `:::end-print-only:::` |
| `:::keep-together:::` | `:::end-keep-together:::` |

Een verkeerde of ontbrekende sluitingstag geeft een foutmelding met de naam
van het openingsblok.

Nesting (een blok-directive binnen een ander blok-directive) is niet
toegestaan en levert een foutmelding op.

---

## Recursieve transclusion

Een included bestand mag zelf ook includes bevatten.
De verwerker lost dit van buiten naar binnen op.

**Regels:**

- Kringverwijzingen (A → B → A) worden gedetecteerd via een include-stack
  en afgebroken met een foutmelding die de kring toont
- Hetzelfde bestand mag meerdere keren worden included (geen kring);
  elk gebruik levert een zelfstandige kopie van de inhoud op
- Een `:::pagebreak:::` in een included bestand werkt identiek
  aan een paginabreuk in het hoofdbestand
- Blok-directives (`web-only`, `print-only`, `keep-together`) in included
  bestanden werken identiek aan die in het hoofdbestand
- VSA-blokken in included bestanden worden verwerkt als onderdeel
  van het uiteindelijke document; elk blok krijgt een unieke SVG-bestandsnaam

**Voorbeeld:**

````
boek.md :::include hoofdstuk-1.md::: :::include hoofdstuk-2.md:::

hoofdstuk-1.md (in submap hoofdstuk-1/) :::pagebreak::: :::include "melodie.vsa"::: :::include noot.md:::
````

Verwerking: `boek.md` → `hoofdstuk-1.md` → `melodie.vsa` + `noot.md`
                        → `hoofdstuk-2.md`

---

## Uitvoer

De verwerking loopt via de bestaande `vsa build-markdown`-stap, uitgebreid met:

1. **Include-resolutie** — recursief, vóór alle andere verwerking
2. **Paginabreuk-omzetting** — `:::pagebreak:::` → HTML-markering
3. **Blok-directives** — omgezet naar Hugo shortcodes
4. **VSA-rendering** — ongewijzigd; VSA-blokken (ook uit included `.vsa`-bestanden)
   worden omgezet naar SVG

Hugo verwerkt daarna het gegenereerde Markdown-bestand tot HTML.

---

## CSS voor afdrukken

```css
@media print {
    @page {
        size: A4;
        margin: 2cm;
    }

    /* Paginabreuk */
    .pagebreak {
        page-break-before: always;
    }

    /* Website-chrome verbergen */
    .site-header,
    .site-nav,
    .nav-buttons,
    footer {
        display: none;
    }

    /* Conditionele inhoud */
    .web-only { display: none; }

    /* Samen op één pagina */
    .keep-together {
        break-inside: avoid;
        page-break-inside: avoid;
    }

    /* Schaling van SVGs binnen keep-together (via scale-parameter) */
    .keep-together .vsa-notation {
        width: var(--vsa-scale, auto);
    }
}

/* print-only standaard verborgen in browser */
.print-only { display: none; }

@media print {
    .print-only { display: block; }
}
```
