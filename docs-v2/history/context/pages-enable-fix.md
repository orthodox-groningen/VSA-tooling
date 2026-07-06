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
[CI-architectuur](../../architecture/ci.md).

## Automatisch herstellen

`pages-deploy-reusable.yml` zet vóór elke deploy via de GitHub API de legacy-bron. Handmatig:
**Actions → Configure GitHub Pages (legacy gh-pages) → Run workflow**.

## Verouderd (niet meer gebruiken)

`actions/configure-pages` + `actions/deploy-pages` — conflicteert met peaceiris en gedeelde
`gh-pages` (preview `/preview/`, productie `/`).
