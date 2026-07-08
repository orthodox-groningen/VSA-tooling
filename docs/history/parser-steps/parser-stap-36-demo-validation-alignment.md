# Stap 36 - demo/validator alignment

Stap 36 introduceerde een nieuwe semantische regel:

```text
[:] ... [:]
```

is ongeldig na gezongen materiaal.

Daarom zijn:

- Hugo demo voorbeelden;
- markdown builder tests;
- markdown processor tests;

aangepast naar:

```text
[:] ... [\\:]
```
