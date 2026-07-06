# Parser stap 7 - SVG rendering

Deze stap introduceert:

```text
MusicalPosition[]
  ↓
SVGRenderer
  ↓
SVG
```

De renderer gebruikt voorlopig:

- eenvoudige cirkels;
- vaste horizontale spacing;
- verticale offset op basis van EHM;
- gewone tekstlabels.

Doel:

- rendering-pipeline stabiliseren;
- Hugo-integratie voorbereiden;
- regressietests voor SVG mogelijk maken.
