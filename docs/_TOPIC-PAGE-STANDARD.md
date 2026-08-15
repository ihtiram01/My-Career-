---
title: Topic Page Standard
description: How every topic page inside Knowledge by Layer is written.
---

# TOPIC PAGE STANDARD

How every topic inside **06 Knowledge by Layer** is written. Copy this shape for
every new topic. A topic is not "covered" until all thirteen blocks exist.

This file is a standard, not a page. The leading underscore keeps the build from
turning it into one.

---

## Naming and placement

```
docs/<topic-slug>.md          one file per topic, auto-discovered by build.py
img/<topic-slug>/*.png        screenshots and diagrams, displayed inline
files/*.pdf | *.mp4 | *.zip   downloads (never images — /files/* forces download)
```

---

## The thirteen blocks, in order

| # | Block | Rule |
|---|---|---|
| 01 | Header | ID, layer, type tag, source tags, level, date, one-line definition |
| 02 | What it is | Plain language. No jargon in the first sentence |
| 03 | Why it exists | The problem it solves. History and dates where they matter |
| 04 | Where it sits | Layer, port, protocol position, what talks to what |
| 05 | How it works | Step by step, in order, the way it actually happens on the wire |
| 06 | Subtopics | Every child concept, each with its own section. Nothing left as "etc" |
| 07 | Vendor CLI | Cisco, Huawei, Juniper, Linux, Windows. Every command explained line by line — never a bare code block |
| 08 | GUI equivalent | Where a GUI exists (Windows, PuTTY, vendor web UI), the click path |
| 09 | Troubleshooting | Symptom → cause → fix, as a table |
| 10 | Field notes | What actually happened on site. Real device models, real limitations |
| 11 | Assets | PDF, images, video, zip — linked, with size and page count |
| 12 | Cross-references | Sibling topics, by ID |
| 13 | Verification | Sources, what is confirmed, what is not |

---

## Non-negotiables

- **Never a bare command block.** Every command gets a line explaining what it
  does and why. A page of copied config teaches nothing.
- **Real syntax per vendor.** Cisco `crypto key generate rsa` and Huawei
  `rsa local-key-pair create` are not interchangeable. Verify before writing.
- **Flag what you have not tested.** A page that quietly presents untested config
  as fact is worse than a shorter page.
- **Field notes are the differentiator.** Anyone can copy a vendor guide. The
  paragraph about the S5735S missing its STelnet client is the part no one else
  has.
- **Screenshots live in `img/<topic>/`**, referenced with an absolute path
  `/img/<topic>/name.png`, and always carry alt text.

---

## Working rhythm

One topic at a time. A topic is finished when all thirteen blocks are filled and
it is filed in both **04 Course Content** and **06 Knowledge by Layer**.
Half-filled pages do not get committed — they get finished or they stay in draft.

---

## Pipeline

| Order | Topic | Layer | State |
|---|---|---|---|
| 1 | SSH — Secure Shell | 60–69 Security | Model page, complete — `63.14` |
| 2 | Single-mode vs multi-mode fibre | 10–19 Physical | Video done, page to write |
| 3 | Ethernet vs fibre | 10–19 Physical | Video done, page to write |
| 4 | Fibre patch cord identification | 10–19 Physical | Video done, page to write |
| 5 | Telnet | 60–69 Security | Pairs with SSH. Index entry exists at `37.07` (Telnet vs SSH) — decide whether the full page lives there or in 63 |
| 6 | AAA / TACACS+ / RADIUS | 60–69 Security | Follows device access. Index entries exist at `63.11` and `35.02` |
| 7 | VLANs | 40–49 Switching | Core switching entry |
| 8 | STP / RSTP / MSTP | 40–49 Switching | Follows VLANs |

---

## Open structural questions

Raised by the first topic page, to be settled before the pipeline runs far:

1. **Topic pages become landing-page rows.** `build.py` auto-discovers every
   non-underscore file in `docs/`, so each topic page adds a numbered row to the
   landing page beside Career & Projects and Roadmap. That is correct for seven
   sections and wrong for seventy topics. Topic pages need either an
   `index: false` frontmatter flag or a `docs/topics/` subfolder, and either one
   is a `build.py` change.

2. **Source tags sit on the category, not the topic.** The index format has no
   per-topic source field, so a topic sourced from `[Wemart]` inside a category
   tagged `[CCNA]` cannot record that without retagging all of its siblings. Same
   known gap already recorded in `CLAUDE.md`.
