# Pages enable fix

## Symptoom

De ingebouwde workflow **pages build and deployment** faalt op **Deploy to GitHub Pages**
(kort na een geslaagde peaceiris-push naar `gh-pages`). De preview/productie-URL werkt vaak
wel; de rode run is een configuratieconflict, geen ontbrekende site-inhoud.

## Oorzaak

Pages staat op **GitHub Actions** als bron, terwijl `peaceiris/actions-gh-pages` direct naar
de branch `gh-pages` pusht. GitHub start dan een tweede deploy-mechanisme dat faalt.

## Oplossing (canoniek)

```text
Settings → Pages → Build and deployment → Source → Deploy from a branch
Branch: gh-pages
Folder: /
```

**Niet** "GitHub Actions" gebruiken naast peaceiris. Zie ook
[CI-architectuur](ci-reliability.md) en [reuse-vsa-tooling.md](../reuse-vsa-tooling.md).

## Automatisch herstellen

Niet mogelijk met de standaard `GITHUB_TOKEN` (vereist repo-admin). Eenmalig handmatig:

```text
Settings → Pages → Build and deployment → Source → Deploy from a branch
Branch: gh-pages
Folder: /
```

Daarna verdwijnt de rode run **pages build and deployment**; peaceiris-deploys blijven werken.

## Verouderd (niet meer gebruiken)

`actions/configure-pages` + `actions/deploy-pages` was een eerdere poging. Dat mechanisme
conflicteert met peaceiris + gedeelde `gh-pages` (preview in `/preview/`, productie in `/`).
