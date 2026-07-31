# Deploy — 15 minutes, zero cost

Static site. No server, no database, no build step.

---

## Recommended: Cloudflare Pages + Access

Chosen because it is the only free option that lets the site stay **private**.
Your index names employers and states which exams you have not sat — that should
not be indexable.

### 1. Put the files in GitHub  (5 min)

1. github.com → **New repository** → name `knowledge-base` → **Private** → Create
2. On the repo page → **uploading an existing file**
3. Drag in everything from this folder, keeping the structure
4. Commit

Private is fine. Cloudflare Pages deploys from private repos on the free plan.

### 2. Connect Cloudflare Pages  (5 min)

1. dash.cloudflare.com → sign up (free, no card)
2. **Workers & Pages** → **Create** → **Pages** → **Connect to Git**
3. Authorise GitHub, pick `knowledge-base`
4. Build settings — leave everything empty:
   - Framework preset: **None**
   - Build command: *(blank)*
   - Build output directory: **/**
5. **Save and Deploy**

Live in ~40 seconds at `knowledge-base.pages.dev`. That subdomain is free forever.

### 3. Lock it down  (5 min)

1. Cloudflare dash → **Zero Trust** → set a team name
2. **Access** → **Applications** → **Add an application** → **Self-hosted**
3. Domain: your `.pages.dev` hostname
4. Policy: **Allow** → include → **Emails** → your Gmail
5. Save

Now visiting the site sends a one-time code to your email. Free up to 50 users.

---

## Free tier — what you actually get

| | Cloudflare Pages free |
|---|---|
| Bandwidth | unlimited |
| Sites | unlimited |
| Builds | 500 / month |
| Files per site | 20,000 |
| **Max file size** | **25 MiB** |
| Custom domains | 100 per project |
| SSL | automatic |
| Access (login wall) | free to 50 users |

Current site: 4 files, ~450 KB. You have room for roughly 19,996 more.

---

## About the domain

**Free domain registrars are a dead end.** Freenom — the `.tk` / `.ml` / `.ga`
provider everyone used — stopped new registrations in 2023 after ICANN action.
Anything still advertising free domains is either reselling Freenom stock or
worse. Do not put your CV behind one.

Your realistic options:

1. **`knowledge-base.pages.dev`** — free, permanent, HTTPS, no registrar.
   This is what I would use.
2. **A real domain** — `.xyz` or `.site` run about $1–3 for the first year,
   $10–15 after. Namecheap and Porkbun both work from Saudi Arabia and accept
   international cards. Add it in Pages → Custom domains; SSL is automatic.

There is no free option that gives you a real top-level domain. Anyone claiming
otherwise is selling something.

---

## Storage for certificates and CVs

- **Under 25 MB** → commit to `/files/` and add a row on the landing page
- **Over 25 MB** → Cloudflare R2 (10 GB free) or Google Drive, then link it

Scanned certificates are usually 1–5 MB. You will not hit the ceiling.

---

## Updating

The viewers are **generated**, never hand-edited. To change content:

1. Edit the markdown in `/docs/`
2. Regenerate the HTML
3. Push — Cloudflare redeploys automatically

Editing the HTML directly means your next regeneration silently discards it.

---

## Alternatives, honestly

| Host | Free | Private without paying | Notes |
|---|---|---|---|
| **Cloudflare Pages** | yes | **yes** — Access | best fit; PoPs in the Gulf |
| GitHub Pages | yes | no — needs Pro for private | simplest, but public |
| Netlify | yes | password needs paid tier | 100 GB/mo bandwidth cap |
| Vercel | yes | password needs Pro | aimed at app frameworks |

If the privacy concern goes away, GitHub Pages is one click fewer. It does not
go away — that is why Cloudflare is the recommendation.

---

## Making changes later

There are three ways, in increasing order of effort.

### A. Edit markdown on your phone  — no tooling at all

1. Open the repo on github.com (works fine in mobile Safari/Chrome)
2. Navigate to `docs/master-knowledge-index.md` → pencil icon
3. Edit, commit
4. The GitHub Action reruns `build/build.py`, commits the regenerated HTML,
   and Cloudflare redeploys

About 90 seconds end to end. This is the intended route for adding a topic,
fixing a typo, or setting a status. No laptop, no Python, no Claude.

### B. Claude Code  — for structural work

Clone the repo, open Claude Code in the folder. It reads `CLAUDE.md`
automatically, so it already knows the four axes, the numbering scheme, the
"never hand-edit the HTML" rule, and the accuracy commitments.

Good for: adding a whole course, restructuring an area, changing the design,
moving source tags to topic level.

It can create the repo, commit and push on its own once you have run
`gh auth login` once.

### C. This chat

Claude regenerates the files, you download and re-upload. Works, but it is
manual every time. Use A or B instead.

---

## What Claude Code can and cannot do here

| Task | Claude Code |
|---|---|
| Create the GitHub repo, commit, push | yes, after `gh auth login` |
| Edit markdown, regenerate HTML, verify counts | yes |
| Write and fix the GitHub Action | yes |
| Create your Cloudflare account | **no** — you do this |
| Connect Pages to the repo | **no** — dashboard, one time, ~2 min |
| Write the Access policy | **no** — dashboard, one time, ~2 min |

The Cloudflare steps are one-time. After the initial connect, every push
redeploys automatically and nothing touches Cloudflare again.

---

## The build

```bash
python3 build/build.py
```

Pure standard library — no `pip install`, no `node_modules`. It prints counts
and **exits non-zero if the parse comes back short**, which is how you find out
a markdown format got broken rather than discovering it as a silently missing
topic later.

Expected output:

```
knowledge  areas=10  categories=77  topics=741  subtopics=562  refs=132
courses    courses=13  modules=69  topics=445  subtopics=951
Build OK.
```

If those numbers drop, something in `docs/` no longer matches the format
documented in `CLAUDE.md`. That is a feature — an index that silently loses
entries is worse than one that refuses to build.
