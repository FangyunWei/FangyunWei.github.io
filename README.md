# Fangyun Wei Personal Homepage

Static academic homepage deployed to [https://fangyunwei.github.io](https://fangyunwei.github.io) with GitHub Pages.

## Contents

- `index.html`, `styles.css`, `favicon.svg`: homepage and styling
- `images/fangyun-wei.jpg`: profile photo
- `data/publications.json`: publication records and direct links
- `data/provided-publications.json`: source list of publications
- `scripts/render-news.py`: renders the publication list into `index.html`
- `.github/workflows/pages.yml`: deploys the repository to GitHub Pages on pushes to `main`

## Update publications

Edit `data/publications.json` and run `python3 scripts/render-news.py` from this directory. Then commit and push the changes to `main`.
