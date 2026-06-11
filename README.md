# VSA stap 35 - URL policy fix

Deze patch trekt alle URL-generatie recht voor:

- lokale Hugo-server;
- lokale preview-build;
- GitHub Pages deploy;
- branch-aware artifacts.

## Probleem

Er waren twee soorten fouten:

1. SVG's werden soms geladen vanaf domein-root:

```text
https://orthodox-groningen.github.io/vsa/...
```

2. GitHub Pages kreeg soms een verkeerde baseURL:

```text
https://orthodox-groningen.github.io/orthodox-groningen/VSA-tooling/...
```

## Beleid

| Context | baseURL |
|---------|---------|
| lokaal serveren | `/` |
| lokale build | `/` |
| GitHub Pages | `https://<owner>.github.io/<repo>/` |
| artifact build | `/` |

## Belangrijke regel

Voor GitHub Pages gebruiken we niet:

```text
github.server_url/github.repository
```

want dat is voor GitHub zelf, niet voor GitHub Pages.

Wel:

```text
https://${{ github.repository_owner }}.github.io/${{ github.event.repository.name }}/
```
