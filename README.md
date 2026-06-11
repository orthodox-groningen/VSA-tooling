# VSA stap 34 - shortcode voorbeeld escape fix

Deze patch lost het probleem op dat een shortcodevoorbeeld in een Markdown-codeblok toch door Hugo werd uitgevoerd.

Probleem:

```go-html-template
{{< vsa src="/vsa/demo-block-1.svg" >}}
```

werd in de demo-site uitgevoerd, waardoor je een plaatje-placeholder zag in plaats van de tekst van de shortcode.

Fix:

```go-html-template
{{</* vsa src="/vsa/demo-block-1.svg" */>}}
```

Hugo toont dit als shortcodevoorbeeld, maar voert het niet uit.
