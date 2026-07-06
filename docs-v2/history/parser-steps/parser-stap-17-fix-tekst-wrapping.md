# Stap 17 fix - tekstwrapping

De eerste multiline-renderer behandelde gewone tekstnodes als ondeelbaar.

Voorbeeld:

```text
TextNode(" is de Heer, en heilig is Zijn Naam. ")
```

Dat gaf onnodige witruimte wanneer daarna een scope kwam.

Deze patch splitst tekstnodes in woordsegmenten:

```text
"is "
"de "
"Heer, "
"en "
...
```

Scopes blijven wel ondeelbaar, zodat VSA-markeringen niet losraken van hun zangelement.
