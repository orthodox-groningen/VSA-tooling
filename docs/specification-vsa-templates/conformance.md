# Conformiteit

## Conforming template-document

Een YAML-bestand is een **conform [vsa-template](@) (draft-v0)** indien:

1. het voldoet aan het JSON Schema;
2. het alle semantische documentregels uit [`validation.md`](validation.md) haalt;
3. `spec_version` gelijk is aan `draft-v0`.

`pitches_status: provisional` mag: structureel conform.
Normatieve [laddergraad](@)-claims vereisen `verified` én menselijke audit.

## Conforming validator

Een tool is een conforme draft-v0-validator indien zij:

- elk `library/*/template.yaml` accepteert;
- elk bestand onder `examples/invalid/` weigert;
- fouten rapporteert met stabiele codes uit `validation.md` (waar van toepassing).

Referentiegedrag: `tests/test_vsa_template_schema.py`.

## Conforming future exporter (niet in draft-v0)

Een toekomstige MusicXML-exporter is pas conform wanneer die specificatie
apart is vastgelegd. Draft-v0 eist **geen** exportgedrag.
