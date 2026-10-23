# Knowledge Base — project instructions

Personal knowledge base for **Ihtiram Ullah (Mickey)**, Network & IT Infrastructure
Engineer, Riyadh. Two indexes over the same body of knowledge: one organised by
technology, one by course.

Read this before changing anything.

---

## The one rule that matters

**Markdown is the source. HTML is disposable output.**

```
docs/*.md  ──[ build/build.py ]──>  index.html          (landing page)
                                    knowledge/index.html
                                    courses/index.html
                                    exams/  experience/
                                    labs/   coursework/
```

Never hand-edit **any** `index.html`, the landing page included. The next build
overwrites them without warning. If you find yourself editing HTML to change
content, stop — the change belongs in `docs/`.

Editing the **template** (`build/*.tpl`) is correct when changing design or
behaviour. Editing the generated file is not.

After any change to `docs/`:

```bash
python3 build/build.py
```

No dependencies. Python 3.8+. It prints counts and exits non-zero if the parse
comes back short, which is the signal that a markdown format got broken.

---

## Layout

```
index.html              GENERATED — landing page, built by build_home()
*/index.html            GENERATED — every section page. Do not edit any of them.

The landing page is a numbered index of seven sections. The number is the
page's `order:`; the heading is its `title:`. Both live in frontmatter, so
resequencing is a frontmatter edit, never a code edit.

  01 experience/   Career & Projects     docs/field-experience.md
  02 exams/        Certifications        docs/exam-tracker.md
  03 roadmap/      Roadmap               docs/roadmap.md
  04 courses/      Course Content        docs/course-syllabus-index.md
  05 coursework/   My Class Notes        docs/my-coursework.md
  06 knowledge/    Knowledge by Layer    docs/master-knowledge-index.md
  07 labs/         Labs & Practice       docs/lab-log.md

Slugs are frozen — they are what published links point at. Rename the
`title:`, never the `page:`.

02 and 03 are deliberately separate: what is held versus what is next.
04, 05 and 06 are three different things and must not be renamed into each
other — 04 is the vendor's official syllabus, 05 is his own class notes,
06 is the technology reference organised by layer, not by course.

docs/
  _home.md                     landing-page config: name, role, tagline,
                               about paragraph, contact fields. Leading
                               underscore keeps it from becoming a page.
                               Blank contact fields are simply not rendered.
  master-knowledge-index.md    source of truth, technology index
  course-syllabus-index.md     source of truth, course index
build/
  build.py              the only build step
  knowledge.tpl         HTML shell + CSS + JS, payload replaced at build
  courses.tpl           same, for the course index
files/                  certificates, CVs, PDFs (25 MB ceiling on Pages)
_headers                noindex + security headers
robots.txt              disallow all
```

---

## Career & Certifications pages (portfolio)

`docs/field-experience.md` and `docs/exam-tracker.md` render as a dashboard of
numbered cards, each opening its own detail page with previous / next links.

- **Order is the order in the file**, newest first. The 01, 02 … numbers are
  added by the build. Re-sequence by moving a `##` block.
- `slug:` on each `##` role freezes its address (`experience/wemart/`). Set it
  once, never change it. Certifications use the title alone (`exams/ccna-200-301/`)
  — never put status words in a slug, or passing an exam breaks the link.
- `type:` (Employment · Contract · Freelance · Independent) sets the stripe
  colour on experience. Certification colour comes from `status:`.
- `private:` on a role, or `- private:` inside a project, is a note for Mickey.
  It stays in the markdown and is **never rendered**. Coaching notes ("be precise
  in interviews", earnings, "do not claim day 3") belong there, not in `summary:`.
- Photos: `- photo: img/experience/<slug>/01.jpg | caption` inside a project.
  Optional `cover:` on the role sets the dashboard picture; otherwise the first
  photo is used. A path that does not exist **fails the build**. Over 1.5 MB
  warns; over 25 MB fails (Cloudflare limit).
- Before adding any photo: blur badges, faces, rack labels, serial numbers,
  hostnames and IPs. Client data halls (center3) and the Diriyah estate are
  confidential sites.
- `<!-- … -->` blocks are skipped by the parser — use them for editing notes.

---

## The four axes (technology index)

Every topic carries all four. Breaking one breaks the filters.

| Axis | Meaning | Example |
|---|---|---|
| **Layer** | the folder — one home per concept | `44` OSPF, inside area `40–49` |
| **Type** | `C` concept · `X` config · `T` troubleshoot · `R` reference | `44.04` is `C` |
| **Source** | course tags and field tags, on the *category* | `[CCNA][ENCOR][MetroL3]` |
| **Level** | `L:_` until rated, then `L0`–`L4` | set in the browser, not the file |

Numbering is Johnny.Decimal: `AREA.CATEGORY.TOPIC.SUBTOPIC` →
`40–49` › `44` › `44.04` › `44.04.3`.

### Structural rules — do not violate

1. **One concept, one home.** OSPF lives at `44` and nowhere else. It is tagged
   `[CCNA][ENCOR][ENARSI]`, not duplicated into three places.
2. **Courses are tags, not folders.** That is what the course index is for.
3. **Cloud and vendor platforms are implementations, not new topics.** Azure
   Private DNS is a subtopic under `33 DNS`, not a new category.
4. **Multi-vendor configs live in one note** with Cisco / Huawei / ZTE / Extreme
   as columns, not four separate topics.
5. **Cross-references are bidirectional.** Adding `→ 47.01` to `44.04` means
   `47.01` should also list `44.04`.

---

## Markdown formats the parser expects

Break these and the build fails loudly, which is the intent.

**Technology index** — `docs/master-knowledge-index.md`

```markdown
# 40–49 · SWITCHING & ROUTING

### 44 · OSPF  `[CCNA]` `[ENCOR]` `[ENARSI]` `[MetroL3]`

- **`44.04`** Area types  `C`  `L:_`  →  `44.05`, `47.01`
  - `44.04.1` Backbone area 0 — all areas must touch it
  - `44.04.2` Standard area
```

Area headings must use an en dash (`40–49`) and the `·` separator. Only the ten
numbered areas `00`–`90` are parsed; anything after them (the "Where to extend"
and "What I could not know" sections) is ignored by design.

**Course index** — `docs/course-syllabus-index.md`

```markdown
# CCNP ENCOR — Implementing Cisco Enterprise Network Core Technologies

`350-401 v1.1` · Cisco · **COURSEWORK ONLY**

> Coursework complete. Exam NOT sat. Highest-priority gap on your roadmap.

<sub>Sources merged: Cisco blueprint v1.1 · NetAcad breakdown</sub>

### 1 · Architecture (15%)

- **`1.1`** Explain enterprise design principles  →  `40`, `42`, `48`
  - High-level designs: 2-tier, 3-tier, fabric, cloud
```

Status labels are a fixed set: `CERTIFIED`, `CERTIFIED — OLDER VERSION`,
`COURSEWORK ONLY`, `PLANNED`, `NOT TAKEN`, `SELF-STUDY`, `REFERENCE`,
`BELOW LEVEL`, `⚠ RECORD CONFLICT`. Anything else falls back to "not taken".

---

## Design language

Layer colours are the **TIA-598 fiber optic colour code** — a real standard from
Mickey's own field, not an arbitrary palette. Blue, orange, green, aqua, slate,
violet, red, rose, yellow, bronze. White and black are in the real code but do
not read on screen, so those two positions were substituted. Keep this if you
touch the palette; it is the reason the design feels like it belongs to him.

Two themes: `paper` (pale blue-grey drafting sheet, the default) and `ink` (deep
navy). **No black backgrounds** — he asked for that explicitly.

Fonts: Space Grotesk (display), IBM Plex Sans (body), JetBrains Mono (data).

Constraints that came from real bugs, not preference:

- **No `localStorage` or `sessionStorage`.** Use `window.storage` with a
  try/catch fallback to an in-memory object.
- **Do not reuse the class name `hit`** for anything other than search-result
  rows. It collided with a level-chip animation once and silently broke rating.
- Mobile: `.trow` and `.searchrow` must stay `flex-wrap: wrap`, or reference
  chips push the type and level controls off-screen.
- Respect `prefers-reduced-motion`.

---

## Accuracy commitments

This file exists partly to stop a future edit from quietly undoing honesty work.

1. **MCSE is a record conflict.** The syllabus is Windows Server **2012**
   (70-410 → 70-414); Microsoft retired those exams in January 2021. There is no
   credential called "MCSE Server 2022". The status stays `⚠ RECORD CONFLICT`
   until Mickey decides how to describe it. Do not quietly relabel it.
2. **CCNP ENCOR and ENARSI are coursework, not passes.** Status stays
   `COURSEWORK ONLY` until he sits the exams.
3. **ITIL is unverified.** Category `85` is tagged `[CV — unverified]`.
4. **Only `L3+` belongs on a CV.** `L1`–`L2` is "familiar with, not in production".
5. **AlmavivA is thin** in the knowledge index — two categories tagged. The
   career page entry is filled from his own CV (Oct 2026). Do not invent coverage
   beyond what he has stated.
6. **center3 was two days of a three-day booking.** Day 3 scope is not his.

---

## Known gaps

- Source tags sit on the **category**, not the topic. So `[AlmavivA]` + type `X`
  returns "config topics in categories where AlmavivA appears", not "configs he
  personally did there". Moving tags to topic level is the fix; it is 741
  decisions, so do it one category at a time when he needs it.
- 43 of 77 categories have no subtopics yet. Listed under "Where to extend".
- Master-index links in the course file are keyword-derived. Roughly 388 of 445
  topics are linked and some are loose. Navigation aid, not ground truth.
- No syllabus supplied for AZ-900, VMware ESXi/vCenter, or CCTV Operator.

---

## Deployment

Cloudflare Pages, git-connected to this repo, behind Cloudflare Access. Every
push to `main` redeploys. See `DEPLOY.md`.

The GitHub Action in `.github/workflows/build.yml` runs `build/build.py` on any
push touching `docs/` or `build/`, and commits the regenerated HTML. That means
Mickey can edit markdown from GitHub's mobile web editor and the site rebuilds
itself — no laptop needed.

If you change the build script, check the Action still passes before pushing.
