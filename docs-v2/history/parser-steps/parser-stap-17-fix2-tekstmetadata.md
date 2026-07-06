# Stap 17 fix 2 - tekstmetadata in SVG

Door tekstwrapping wordt een gewone tekstnode gesplitst in woorden.

Dat is goed voor layout, maar lastig voor regressietests en debugging.

Daarom schrijft de SVG-renderer de originele tekstnode ook als commentaar:

```xml
<!-- plain-text: is de Heer. -->
```

Dit verandert de zichtbare output niet, maar maakt het makkelijker om te controleren dat gewone tekst behouden blijft.
