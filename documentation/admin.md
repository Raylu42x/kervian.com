# Admin Panel

A web-based admin lives at [/admin/](https://kervian.com/admin/). It runs [Sveltia CMS](https://github.com/sveltia/sveltia-cms) — a Git-based CMS that commits new project and tutorial files (and uploaded images) directly to this repo. GitHub Actions then rebuilds the site automatically.

You sign in with GitHub. Only accounts with write access to `Raylu42x/kervian.com` can save anything — there is no way around it.

---

## What you can do

- **Edit site pages** — Home, About, Portfolio, Projects index, Tutorials index, and the sitewide banner. Listed under **Site Pages** in the sidebar.
- **Create / edit / delete projects** — full form for every frontmatter field (title, excerpt, tags, featured toggle, portfolio image upload, body).
- **Create / edit / delete tutorials** — same idea; `tags: build` is set automatically.
- **Upload images** — saved to `src/uploads/` and referenced via `/uploads/...`.
- **Work from any device** — phone, laptop, tablet.

### Warning: every field is editable

All frontmatter fields (including `layout`, `tags`, `bodyClass`, `permalink`) are shown as editable text — nothing is hidden. That means you have full control, but also means you can break a page by changing `layout` to something invalid or wiping the `tags` field on a project.

Safe defaults if you're unsure:
- `layout`: always `base.njk`
- `bodyClass`: a `glow-*` value (see content guide)
- Projects `tags`: must include `project` to show on `/projects/`
- Tutorials `tags`: must be `build`

Bodies use a **plain-text** editor (not WYSIWYG) so Nunjucks template tags like `{% for project in collections.projects %}` are preserved exactly. If a card grid disappears after editing the homepage or an index page, you probably deleted a `{% for %}` / `{% endfor %}` pair.

Everything is just markdown in the repo. The CMS is a UI on top of the same files you can still edit by hand in VS Code.

---

## Logging in

Sveltia does not run a public OAuth proxy, so there are two ways to log in. The simple way (PAT) needs zero setup. The polished way (OAuth) needs about 10 minutes of one-time setup.

### Option 1 — Personal Access Token (recommended to start)

No OAuth App, no Worker, no extra service. You generate a GitHub token once and paste it into the admin login screen. The browser stores it; you won't be asked again unless you sign out or clear the site's data.

1. Go to **GitHub → Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**.
2. Settings:
   - **Token name**: `Kervian Admin`
   - **Expiration**: whatever you want (90 days, 1 year, no expiration).
   - **Repository access**: *Only select repositories* → pick `Raylu42x/kervian.com`.
   - **Permissions → Repository permissions**:
     - Contents: **Read and write**
     - Metadata: **Read-only** (auto-selected)
3. Click **Generate token** and copy it (you only see it once).
4. At `https://kervian.com/admin/`, click **Sign In with Token**, paste the token, done.

If the token ever leaks, revoke it on GitHub and generate a new one — no other cleanup needed.

### Option 2 — Real "Log in with GitHub" button (optional upgrade)

Polished button instead of pasting a token. Requires deploying [sveltia-cms-auth](https://github.com/sveltia/sveltia-cms-auth), a tiny Cloudflare Worker, via `wrangler` (free tier).

1. Follow the [sveltia-cms-auth README](https://github.com/sveltia/sveltia-cms-auth#readme) to deploy the Worker. It will give you a URL like `https://sveltia-cms-auth.<sub>.workers.dev`.
2. Create a GitHub OAuth App (Settings → Developer settings → OAuth Apps → New OAuth App):
   - **Homepage**: `https://kervian.com`
   - **Authorization callback URL**: `https://sveltia-cms-auth.<sub>.workers.dev/callback`
3. Put the Client ID + secret into the Worker's environment variables (per its README).
4. In `src/admin/config.yml`, uncomment and set `base_url:` to your Worker URL.

After that, the admin login becomes a single GitHub button.

---

## Using the admin

1. Visit `https://kervian.com/admin/`.
2. Sign in (paste your PAT, or click "Log in with GitHub" if you set up the Worker).
3. Pick **Projects** or **Tutorials** from the sidebar.
4. Click **New Project** (or **New Tutorial**).
5. Fill out the form:
   - **Title** — page title.
   - **Show on** — checkboxes for `/projects/` and `/portfolio/`. Leave both checked unless you want to hide it from one.
   - **Featured on homepage?** — toggle to show in the homepage Featured rail.
   - **Excerpt** — the one-liner shown on the card.
   - **Glow color** — neon accent for this page.
   - **Portfolio image** — upload an image (lives at `/uploads/...`).
   - **Body** — rich markdown editor.
6. Click **Save** (draft) and then **Publish**.

Behind the scenes: clicking Publish creates a commit on `main` → GH Actions runs the Eleventy build → GH Pages serves it. The new page is live in about 1 minute.

---

## Where things go

| In the admin              | In the repo                  | On the site                |
| ------------------------- | ---------------------------- | -------------------------- |
| New Project "Birds Two"   | `src/projects/birds-two.md`  | `/projects/birds-two/`     |
| New Tutorial "Solder"     | `src/tutorials/solder.md`    | `/tutorials/solder/`       |
| Uploaded image `bird.jpg` | `src/uploads/bird.jpg`       | `/uploads/bird.jpg`        |

---

## Editing the form itself

The form fields, options, and validation are defined in [`src/admin/config.yml`](../src/admin/config.yml). To add a new frontmatter field (e.g. a `subtitle`), add it under the matching collection's `fields` list. See the [Sveltia / Decap widget reference](https://decapcms.org/docs/widgets/) for available field types.

---

## Future: migrate to a VPS

Once a VPS is available, the plan is to retire this Git-based CMS and build a proper self-hosted admin system. Rough sketch of what that would look like:

- **Host the site itself on the VPS** instead of GitHub Pages. Eleventy still builds the static `docs/`, but it's served by nginx/Caddy on your own server (or kept on GH Pages and only the admin moves — both options stay on the table).
- **Real backend** — a small Node/Go/Python service running on the VPS that exposes:
  - A login endpoint (simple password / session cookie, no GitHub OAuth dance).
  - Endpoints to create, edit, delete projects and tutorials.
  - An image upload endpoint that writes to disk.
- **Database optional** — content can stay as markdown files (so the Eleventy build still works the same way), or move to a small SQLite/Postgres DB with a build step that materializes markdown.
- **Drop Sveltia + the PAT/Worker flow entirely.** The `/admin/` route becomes a custom UI talking to your own API.
- **Deploy pipeline** — git push still triggers builds, OR the backend writes files and runs `npm run build` itself after each save.

What to think about before doing it:
- Whether the VPS will host *just* the admin/API (with the public site staying on GH Pages) or the whole site. Hosting both is simpler conceptually but means you own uptime.
- Auth: shared password is fine for solo use; if more people get involved, switch to per-user accounts.
- Backups: once content is on the VPS, you're responsible for backing it up. Keeping the markdown in git remains the easiest backup.
- TLS / domain: point `kervian.com` (or `admin.kervian.com`) at the VPS, run Caddy for automatic Let's Encrypt certs.

This is a "someday" item — the current setup works fine for solo content editing. Revisit when (a) the VPS exists, (b) the PAT flow starts feeling annoying, or (c) you want features the Git-based CMS can't do (e.g. drafts with a non-public preview URL, scheduled publishing, comments).

---

## Troubleshooting

- **"Failed to load config.yml"** — check that `.eleventy.js` still has the `addPassthroughCopy({"src/admin": "admin"})` line and that `npm run build` produced `docs/admin/config.yml`.
- **"Sign In with Token" rejects the token** — the PAT is missing `Contents: Read and write` on the `Raylu42x/kervian.com` repo, or it has expired. Generate a new one with the right permissions.
- **Save button does nothing** — the token (or signed-in account) does not have write access to `Raylu42x/kervian.com`. Re-check repo access on the PAT or add the GitHub user as a collaborator.
- **New post not appearing on the live site** — check the [Actions tab](https://github.com/Raylu42x/kervian.com/actions) on GitHub; the build may have failed.
