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
src/              # Source templates and content
src/banner.md     # Announcement banner — set active: true/false to show/hide
src/_data/        # Eleventy global data files
src/_includes/    # Layout and component templates
docs/             # Output directory (GitHub Pages / deployment target)
.eleventy.js      # Eleventy config
```

> `docs/` is the static site output and is excluded from the documentation site via `.no-docs`.

## Banner

To show a sitewide announcement, edit `src/banner.md`:

```markdown
---
active: true
permalink: false
---
Your announcement text here (markdown supported)
```

Set `active: false` to hide the banner. The banner is always visible on the homepage and dismissible on all other pages.
