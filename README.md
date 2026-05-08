# kervian.com

Personal website for Bennett Kervian, built with [Eleventy](https://www.11ty.dev/) and hosted at [kervian.com](https://kervian.com).

## Stack

- **Generator**: Eleventy (11ty) v2
- **Hosting**: Cloudflare Pages
- **DNS**: Cloudflare

## Development

```bash
npm install
npm run dev      # local dev server
npm run build    # production build
```

## Structure

```
src/         # Source templates and content
docs/        # Output directory (GitHub Pages / deployment target)
.eleventy.js # Eleventy config
```

> `docs/` is the static site output and is excluded from the documentation site via `.no-docs`.
