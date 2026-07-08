# Stap 35 - URL policy fix

Deze stap legt het URL-beleid vast.

## Lokaal

Voor lokaal gebruik:

```text
baseURL = /
```

## GitHub Pages

Voor deploy naar GitHub Pages:

```text
https://<owner>.github.io/<repo>/
```

In GitHub Actions:

```yaml
--baseURL "https://${{ github.repository_owner }}.github.io/${{ github.event.repository.name }}/"
```

Gebruik niet:

```yaml
github.server_url/github.repository
```

want dat verwijst naar GitHub zelf, niet naar GitHub Pages.

## Assets

`vsa build-markdown` mag nog steeds `/vsa/...` genereren.

De Hugo shortcode normaliseert dit:

```go-html-template
{{ $src = replaceRE "^/" "" $src }}
{{ $src | relURL }}
```

Daardoor wordt op GitHub Pages:

```text
/vsa/x.svg
```

correct:

```text
/VSA-tooling/vsa/x.svg
```
