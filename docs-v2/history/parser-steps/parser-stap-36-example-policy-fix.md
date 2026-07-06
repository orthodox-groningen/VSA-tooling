# Stap 36 - example policy fix

De test `test_all_good_examples_validate` valideerde eerst de volledige map:

```text
examples/minimal
```

Dat is te grof.

Die map bevat ook kleine feature- en randvoorbeelden.
Onder strengere semantiek kunnen sommige daarvan bewust of historisch ongeldig zijn.

Nieuw beleid:

```text
curated good examples      → moeten valideren
examples/expected-fail/*.vsa → moeten falen
```

De demo-site blijft volledig gevalideerd:

```text
examples/hugo-demo/content-source
```
