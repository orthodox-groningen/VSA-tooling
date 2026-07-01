# Hugo demo-site structuur

## Hoofdindeling

```text
content-source/
├── kerkmuziek-tradities/   # tradities, luisterlinks, partituren (oriëntatie)
├── liturgikon-notatie/     # Liturgikon-notatie uitleg (1968)
├── voorbeelden/
└── praktijk/
```

## `voorbeelden/`

Doel:

- tooluitleg;
- demo's;
- CLI-documentatie;
- renderingdiagnostiek;
- voorbeelden die primair de werking van VSA-tooling demonstreren.

## `praktijk/`

Doel:

- echte liturgische praktijkvoorbeelden;
- materiaal dat inhoudelijk als zangvoorbeeld gebruikt kan worden.

Huidige hoofdsecties:

```text
praktijk/
├── feesteigen/
├── weekdagen/
└── zondagen/
```

## `praktijk/zondagen/`

Alle zondagsvoorbeelden horen hier, dus niet los onder `praktijk/` en niet onder top-level `zondag/`.

## Top-level `zondag/`

Als deze map nog bestaat, is dat historisch/demomateriaal.

Die sectie hoort niet in de normale navigatie te verschijnen. Gebruik daarvoor:

```yaml
vsa_nav_exclude: true
```

Later kan dit materiaal worden verplaatst naar bijvoorbeeld:

```text
voorbeelden/bronnen/zondag/
```

als het nog nodig is voor tooldemo's zoals "Markdown en Hugo".

## Obsolete prototype

Deze map is verouderd en kan weg:

```text
examples/examples/
```
