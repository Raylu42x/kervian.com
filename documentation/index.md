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
src/              # Source templates, layouts, and content
src/banner.md     # Announcement banner — edit to show/hide sitewide notices
src/_data/        # Eleventy global data files
src/_includes/    # Layout and component templates
docs/             # Built site output (Cloudflare Pages deployment target)
.eleventy.js      # Eleventy configuration
```

> `docs/` is the static site output directory — it's excluded from the documentation site via `.no-docs`. Markdown docs live in `documentation/` instead.

## Guides

- [Content Guide](./content-guide.md) — adding projects, tutorials, and featured projects (with full frontmatter reference)
- [Admin Panel](./admin.md) — using the `/admin/` web UI to create posts without touching code

## Banner

To show a sitewide announcement, edit `src/banner.md`:

```markdown
---
active: true
permalink: false
---
Your announcement text here (markdown supported)
```

Set `active: false` to hide the banner. The banner is always visible on the homepage and dismissible (via a close button) on all other pages.
