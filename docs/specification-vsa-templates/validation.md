# Validatie

Validatie van een [vsa-template](@) gebeurt in twee lagen.

## 1. Structureel (schema)

Controleer tegen
[`schema/vsa-template.schema.json`](schema/vsa-template.schema.json):

- verplichte topvelden;
- enums (`genre`, `role`, `duration`, `anchor`, …);
- pitchpatroon;
- `pitches` altijd S/A/T/B.

Automatische toets: `tests/test_vsa_template_schema.py`.

## 2. Semantisch (documentregels)

Naast het schema MUST een conforme validator:

| Code                          | Regel                                              |
| ----------------------------- | -------------------------------------------------- |
| `TEMPLATE-FORM`               | Precies cycle+final, sequence, of same_as          |
| `TEMPLATE-PHRASE-ID-UNIQUE`   | Frase-ids uniek                                    |
| `TEMPLATE-CYCLE-REF`          | Elke id in `cycle` bestaat in `phrases`            |
| `TEMPLATE-FINAL-REF`          | `final` bestaat in `phrases`                       |
| `TEMPLATE-FINAL-NOT-IN-CYCLE` | `final` komt niet voor in `cycle`                  |
| `TEMPLATE-CYCLE-NONEMPTY`     | `cycle` heeft ≥1 element                           |
| `TEMPLATE-SEQUENCE-REF`       | Elke id in `sequence` bestaat in `phrases`         |
| `TEMPLATE-MAPPING`            | `text_mapping` / `mapping_plans` semantisch geldig |
| `TEMPLATE-SAME-AS` / `-REF`   | Alias geldig; doel-id bestaat in de suite          |
| `TEMPLATE-PHRASE-EVENTS`      | Elke frase heeft ≥1 event                          |

Draft-v0 DOET NOG GEEN:

- toonladdervalidatie;
- controle dat ankers “muzikaal kloppen”;
- pitch-verificatie tegen PDF.

## Ernst

| Severity | Gebruik                                          |
| -------- | ------------------------------------------------ |
| error    | Schema- of documentregelfout                     |
| warning  | bijv. `pitches_status: provisional` (toekomstig) |

## Toekomstige CLI

```text
vsa template validate pad\naar\template.yaml
```

Nog niet geïmplementeerd; de pytest-suite dekt de structurele + documentregels.
