# VSA stap 31 - voorbeeldvalidatie en CLI-demo pagina's

Deze stap doet twee dingen.

## 1. Voorbeelden valideren

Alle voorbeelden die goed moeten zijn worden automatisch gevalideerd.

Voorbeelden die fout moeten zijn worden automatisch gecontroleerd op falen.

Daarmee voorkomen we dat de demo-site of voorbeelden per ongeluk ongeldige VSA bevatten.

## 2. CLI-demo pagina's

De Hugo-demo krijgt per belangrijk `vsa`-commando een eigen pagina:

- `vsa validate`
- `vsa svg`
- `vsa blocks`
- `vsa parse`
- `vsa process`
- `vsa build-markdown`
- `vsa --version`

Elke pagina laat zien:

- doel;
- input;
- commando;
- verwachte output;
- wat er fout kan gaan;
- wat je daarna moet doen.
