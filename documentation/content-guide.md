# Content Guide

How to add projects, tutorials, and featured projects to kervian.com.

All content lives in `src/`. Eleventy reads markdown frontmatter to decide where a page shows up. The `tags` field controls collection membership, which controls which index pages list it.

---

## Add a Project

1. Create a new file in `src/projects/`, e.g. `src/projects/my-thing.md`.
2. Use this frontmatter:

   ```yaml
   ---
   layout: base.njk
   title: My Thing
   tags: [project, portfolio]
   bodyClass: glow-purple
   excerpt: One-sentence summary that shows up on the card.
   ---
   ```

3. Write the body in markdown below the frontmatter.

The file's URL will be `/projects/my-thing/`. It will automatically appear on `/projects/` because of the `project` tag.

### Where it shows up
| Tag included        | Appears on            |
| ------------------- | --------------------- |
| `project`           | `/projects/`          |
| `portfolio`         | `/portfolio/`         |
| `project, portfolio`| both                  |

---

## Add a Featured Project

Featured projects appear in the horizontal "Featured Projects" rail on the homepage (`/`).

To mark a project as featured, add `featured: true` to its frontmatter:

```yaml
---
layout: base.njk
title: Bird Study
tags: [project, portfolio]
featured: true
excerpt: I studied a book about birds for a second.
---
```

Rules:

- Any number of projects can be featured — they all show.
- If **no** project has `featured: true`, the homepage falls back to showing the first 3 projects automatically.
- To un-feature, remove the line or set `featured: false`.

The rail scrolls left/right and uses the same 300px card width as every other card on the site.

---

## Add a Tutorial

1. Create a new file in `src/tutorials/`, e.g. `src/tutorials/solder-a-wire.md`.
2. Use this frontmatter:

   ```yaml
   ---
   layout: base.njk
   title: How to Solder a Wire
   tags: build
   bodyClass: glow-orange
   excerpt: Short summary of what the tutorial teaches.
   ---
   ```

3. Write the tutorial body in markdown.

Tutorials use the `build` tag (not `tutorial`) because Eleventy's tutorials collection is defined as everything tagged `build`. The page automatically appears on `/tutorials/`.

---

## Frontmatter Reference

### Projects (`src/projects/*.md`)

| Field        | Required | Example                              | Notes |
| ------------ | -------- | ------------------------------------ | ----- |
| `layout`     | yes      | `base.njk`                           | Always `base.njk`. |
| `title`      | yes      | `Bird Study`                         | Shown in `<title>`, card heading, and page H1. |
| `tags`       | yes      | `[project, portfolio]`               | Must include `project` to appear on `/projects/`. Add `portfolio` to also list on `/portfolio/`. |
| `excerpt`    | yes      | `Short one-liner.`                   | Used as the card description on index pages. |
| `bodyClass`  | no       | `glow-purple`                        | Sets the neon accent color for this page. See color list below. |
| `featured`   | no       | `true`                               | If `true`, appears in the homepage Featured Projects rail. |
| `portfolioImage` | no   | `https://…/image.jpg`                | Image shown on the portfolio card variant. |

### Tutorials (`src/tutorials/*.md`)

| Field        | Required | Example                              | Notes |
| ------------ | -------- | ------------------------------------ | ----- |
| `layout`     | yes      | `base.njk`                           | Always `base.njk`. |
| `title`      | yes      | `How to Build a LED Light`           | Shown in `<title>`, card heading, and page H1. |
| `tags`       | yes      | `build`                              | Must be `build` (not `tutorial`) to appear on `/tutorials/`. |
| `excerpt`    | yes      | `Short summary.`                     | Used as the card description. |
| `bodyClass`  | no       | `glow-orange`                        | Neon accent color. |

### Glow colors (`bodyClass`)

Pick the one that fits the page's vibe. Defined in `src/css/main.css`:

- `glow-green` (default)
- `glow-blue`
- `glow-pink`
- `glow-purple`
- `glow-orange`
- `glow-red`
- `glow-yellow`
- `glow-teal`
- `glow-lightblue`
- `glow-white`

---

## How Collections Work

Defined in `.eleventy.js`:

- **`collections.projects`** — every page tagged `project`. Powers `/projects/` and the homepage Featured rail.
- **`collections.tutorials`** — every page tagged `build`. Powers `/tutorials/`.
- **`collections.games`** — every `index.html` inside `src/games/` (excluding the games hub itself). Powers `/games/`.

To add a new collection, edit `.eleventy.js` and add another `addCollection` call.

---

## Quick Recipes

**"I built a cool thing — show it on the homepage."**
Create `src/projects/cool-thing.md` with `tags: [project, portfolio]` and `featured: true`.

**"Take this off the homepage rail but keep it on the projects page."**
Remove `featured: true` from its frontmatter.

**"Write a how-to."**
Create `src/tutorials/how-to-thing.md` with `tags: build`.

**"Hide a project entirely."**
Delete the file, or remove `project` from its `tags`.
