# kervian.com

Personal website for Bennett Kervian, built with [Eleventy](https://www.11ty.dev/) and hosted at [kervian.com](https://kervian.com).

## Stack

- **Generator**: Eleventy (11ty) v2
- **Hosting**: Cloudflare Pages
- **DNS**: Cloudflare

## Development

```bash
npm install
npm run dev      # local dev server with live reload
npm run build    # production build → docs/
```

## Structure

```
src/         # Source templates, layouts, and content
docs/        # Built site output (Cloudflare Pages deployment target)
.eleventy.js # Eleventy configuration
```

> `docs/` is the static site output directory — it's excluded from the documentation site via `.no-docs`. Markdown docs live in `documentation/` instead.
