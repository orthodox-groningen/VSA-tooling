# Stap 34 - shortcode voorbeeld escape fix

Hugo voert shortcodes uit, ook als ze in documentatie als voorbeeld bedoeld zijn.

Daarom is dit fout in documentatie:

```go-html-template
{{< vsa src="/vsa/demo-block-1.svg" >}}
```

Gebruik in documentatie:

```go-html-template
{{</* vsa src="/vsa/demo-block-1.svg" */>}}
```

Dan toont Hugo het voorbeeld zonder de shortcode uit te voeren.
