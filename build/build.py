#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build every page from the markdown in docs/.

    python3 build/build.py

HOW TO ADD A NEW PAGE
---------------------
1. Copy docs/_TEMPLATE.md to docs/whatever.md
2. Fill in the frontmatter and your content
3. Run this script

A page appears at whatever/index.html and a card appears on the home page.
No code change. Nothing else to edit.

Markdown is the source. The HTML is disposable output — never edit it by hand,
because the next build silently discards your changes.

Pure standard library. Python 3.8+.
"""
import re, json, sys, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cards

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
BUILD = Path(__file__).resolve().parent
FILES = ROOT / "files"

# The two tree-shaped pages have bespoke renderers. Everything else in docs/
# is auto-discovered and rendered as a card page.
TREE_PAGES = {
    "master-knowledge-index.md": dict(
        page="knowledge", tpl="knowledge.tpl", kind="knowledge",
        kicker="Section 06 · by layer", colour="#1B57C4",
        title="Knowledge by Layer",
        summary="Ten layers, copper up to CCTV. One home per concept, cross-referenced.",
        order=6),
    "course-syllabus-index.md": dict(
        page="courses", tpl="courses.tpl", kind="courses",
        kicker="Section 04 · by course", colour="#C55A0C",
        title="Course Content",
        summary="What each syllabus covered, merged from 21 documents. Links back to the knowledge index.",
        order=4),
}

NAMED_COLOURS = {
    "blue": "#1B57C4", "orange": "#C55A0C", "green": "#0B7D55", "aqua": "#0C7F99",
    "violet": "#6E35C9", "red": "#C42A36", "rose": "#B8367F", "yellow": "#8A6800",
    "bronze": "#7E5129", "slate": "#56697F",
}
PALETTE = {
    "00": ("#8494AB", "#56697F", "Slate"), "10": ("#FF7A1A", "#C55A0C", "Orange"),
    "20": ("#34D399", "#0B7D55", "Green"),  "30": ("#22D3EE", "#0C7F99", "Aqua"),
    "40": ("#4C8DFF", "#1B57C4", "Blue"),   "50": ("#A97BFF", "#6E35C9", "Violet"),
    "60": ("#FF5A5F", "#C42A36", "Red"),    "70": ("#FF7AC6", "#B8367F", "Rose"),
    "80": ("#F5C542", "#8A6800", "Yellow"), "90": ("#C98B5E", "#7E5129", "Bronze"),
}
SHORT = {"00": "Index", "10": "Physical", "20": "Systems", "30": "IP Core",
         "40": "Switch/Route", "50": "Wireless", "60": "Security",
         "70": "Virt/Cloud", "80": "Ops", "90": "CCTV"}


def read_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    fm = {}
    for ln in text[3:end].split("\n"):
        if ":" in ln:
            k, v = ln.split(":", 1)
            fm[k.strip().lower()] = v.strip()
    return fm


# ── knowledge index ─────────────────────────────────────────────────────
def parse_knowledge(path):
    lines = path.read_text(encoding="utf-8").split("\n")
    re_area = re.compile(r"^#\s+(\d{2})[–-](\d{2})\s+·\s+(.+)$")
    re_cat = re.compile(r"^###\s+(\d{2})\s+·\s+(.+?)\s*$")
    re_top = re.compile(r"^-\s+\*\*`(\d{2}\.\d{2})`\*\*\s+(.+?)\s+`([CXTR])`\s+`L:([^`]*)`(.*)$")
    re_sub = re.compile(r"^\s{2,}-\s+`(\d{2}\.\d{2}\.\d+)`\s+(.+)$")
    areas, area, cat, top = [], None, None, None
    for raw in lines:
        ln = raw.rstrip()
        m = re_area.match(ln)
        if m:
            code = m.group(1)
            if code not in PALETTE:
                area = None
                continue
            d, l, s = PALETTE[code]
            area = {"from": code, "to": m.group(2), "title": m.group(3).strip(),
                    "dark": d, "light": l, "strand": s, "short": SHORT[code], "cats": []}
            areas.append(area)
            cat = top = None
            continue
        if ln.startswith("# ") and not re_area.match(ln):
            area = None
            continue
        if area is None:
            continue
        m = re_cat.match(ln)
        if m:
            title = m.group(2)
            tags = re.findall(r"\[([^\]]+)\]", title)
            title = re.sub(r"\s*`\[[^\]]+\]`", "", title).strip()
            cat = {"id": m.group(1), "title": title, "tags": tags, "topics": []}
            area["cats"].append(cat)
            top = None
            continue
        m = re_top.match(ln)
        if m and cat is not None:
            refs = re.findall(r"`(\d{2}(?:\.\d{2})?)`", m.group(5) or "")
            top = {"id": m.group(1), "name": m.group(2).strip(), "type": m.group(3),
                   "subs": [], "refs": refs}
            cat["topics"].append(top)
            continue
        m = re_sub.match(ln)
        if m and top is not None:
            top["subs"].append({"id": m.group(1), "name": m.group(2).strip()})
    idx = {}
    for a in areas:
        for c in a["cats"]:
            idx[c["id"]] = {"kind": "cat", "title": c["title"], "area": a["from"]}
            for t in c["topics"]:
                idx[t["id"]] = {"kind": "topic", "title": t["name"], "area": a["from"],
                                "cat": c["id"], "catTitle": c["title"]}
    meta = {"areas": len(areas),
            "cats": sum(len(a["cats"]) for a in areas),
            "topics": sum(len(c["topics"]) for a in areas for c in a["cats"]),
            "subs": sum(len(t["subs"]) for a in areas for c in a["cats"] for t in c["topics"]),
            "refs": sum(len(t["refs"]) for a in areas for c in a["cats"] for t in c["topics"]),
            "generated": datetime.date.today().isoformat()}
    return {"meta": meta, "areas": areas, "index": idx}


# ── course index ────────────────────────────────────────────────────────
STATUS_FROM_LABEL = {
    "CERTIFIED": "certified", "CERTIFIED — OLDER VERSION": "certified-old",
    "COURSEWORK ONLY": "coursework", "PLANNED": "planned", "NOT TAKEN": "not-taken",
    "SELF-STUDY": "self-study", "REFERENCE": "reference",
    "BELOW LEVEL": "below-level", "⚠ RECORD CONFLICT": "conflict",
}
COURSE_COLOUR = {"ccst": 6, "ccna": 4, "encor": 4, "enarsi": 4, "scor": 6, "sncf": 6,
                 "aplus": 1, "netplus": 3, "linuxplus": 2, "itf": 0, "az104": 7,
                 "mcse": 2, "lpic1": 2}


def slug(name, code):
    s = (name + " " + code).lower()
    for key, pat in [("ccst", "support technician"), ("ccna", "ccna"), ("encor", "encor"),
                     ("enarsi", "enarsi"), ("scor", "scor"), ("sncf", "sncf"),
                     ("aplus", "comptia a+"), ("netplus", "network+"),
                     ("linuxplus", "linux+"), ("itf", "itf+"), ("az104", "az-104"),
                     ("mcse", "mcse"), ("lpic1", "lpic-1")]:
        if pat in s:
            return key
    return re.sub(r"[^a-z0-9]+", "-", s)[:24].strip("-")


def parse_courses(path):
    lines = path.read_text(encoding="utf-8").split("\n")
    re_course = re.compile(r"^#\s+(?!COURSE SYLLABUS|Merge report|Where|What)(.+)$")
    re_head = re.compile(r"^`([^`]+)`\s*·\s*([^·]+)·\s*\*\*(.+?)\*\*\s*$")
    re_mod = re.compile(r"^###\s+(\S+)\s+·\s+(.+)$")
    re_top = re.compile(r"^-\s+\*\*`([^`]+)`\*\*\s+(.+)$")
    re_sub = re.compile(r"^\s{2,}-\s+(.+)$")
    courses, c, mod, top = [], None, None, None
    for raw in lines:
        ln = raw.rstrip()
        m = re_course.match(ln)
        if m and not ln.startswith("##"):
            c = {"name": m.group(1).strip(), "code": "", "vendor": "",
                 "status": "not-taken", "note": "", "sources": [], "modules": []}
            courses.append(c)
            mod = top = None
            continue
        if c is None:
            continue
        m = re_head.match(ln)
        if m:
            c["code"] = m.group(1).strip()
            c["vendor"] = m.group(2).strip()
            c["status"] = STATUS_FROM_LABEL.get(m.group(3).strip(), "not-taken")
            continue
        if ln.startswith("> "):
            c["note"] = ln[2:].strip()
            continue
        if ln.startswith("<sub>Sources merged:"):
            body = ln[len("<sub>Sources merged:"):].replace("</sub>", "")
            c["sources"] = [s.strip() for s in body.split("·") if s.strip()]
            continue
        m = re_mod.match(ln)
        if m:
            mod = {"num": m.group(1), "title": m.group(2).strip(), "topics": []}
            c["modules"].append(mod)
            top = None
            continue
        m = re_top.match(ln)
        if m and mod is not None:
            rest = m.group(2)
            links = re.findall(r"→\s*(.+)$", rest)
            link_ids = re.findall(r"`(\d{2})`", links[0]) if links else []
            title = re.sub(r"\s*→.*$", "", rest)
            src = "merged" if "(merged)" in title else "primary"
            title = re.sub(r"\s*<sub>\*\(merged\)\*</sub>", "", title).strip()
            top = {"num": m.group(1), "title": title, "subs": [],
                   "links": link_ids, "src": src}
            mod["topics"].append(top)
            continue
        m = re_sub.match(ln)
        if m and top is not None:
            top["subs"].append(m.group(1).strip())
    for c in courses:
        c["key"] = slug(c["name"], c["code"])
        c["colour"] = COURSE_COLOUR.get(c["key"], 4)
        c["counts"] = {"modules": len(c["modules"]),
                       "topics": sum(len(m["topics"]) for m in c["modules"]),
                       "subs": sum(len(t["subs"]) for m in c["modules"] for t in m["topics"])}
    meta = {"courses": len(courses),
            "modules": sum(c["counts"]["modules"] for c in courses),
            "topics": sum(c["counts"]["topics"] for c in courses),
            "subs": sum(c["counts"]["subs"] for c in courses),
            "generated": datetime.date.today().isoformat()}
    return {"meta": meta, "courses": courses}


# ── shell ───────────────────────────────────────────────────────────────
def shell():
    tpl = (BUILD / "knowledge.tpl").read_text(encoding="utf-8")
    css = tpl[tpl.index("<style>") + 7: tpl.index("</style>")]
    head = (tpl[:tpl.index("<style>")].replace(
        re.search(r"<title>.*?</title>", tpl).group(0), "<title>__TITLETAG__</title>")
        + "<style>__CSS__</style>\n</head>\n<body>\n")
    return css, head


def render_tree(tpl_name, data, out):
    html = (BUILD / tpl_name).read_text(encoding="utf-8").replace(
        "__PAYLOAD__", json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    return len(html.encode()) / 1024


def render_card_page(md_path, cfg, css, head):
    data = cards.parse_cards(md_path)
    m = data["meta"]
    figs = "".join(f'<div class="fig"><b>{m[k]}</b><span>{lbl}</span></div>'
                   for k, lbl in [("groups", cfg.get("unit_group", "sections")),
                                  ("cards", cfg.get("unit_card", "items")),
                                  ("items", "details")])
    body = (cards.BODY.replace("__KICKER__", cfg["kicker"])
                      .replace("__TITLE__", cfg["title"])
                      .replace("__LEDE__", cfg["summary"])
                      .replace("__PH__", cfg.get("placeholder", "Search this page…"))
                      .replace("__FOOT__", cfg.get("footer", ""))
                      .replace("__FIGS__", figs))
    js = cards.CARD_JS.replace("__PAYLOAD__",
                               json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    html = (head.replace("__CSS__", css + cards.EXTRA_CSS)
                .replace("__TITLETAG__", cfg["title"] + " — Ihtiram Ullah")
            + body + "<script>" + js + "</script>\n</body></html>")
    out = ROOT / cfg["page"] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    return m, len(html.encode()) / 1024


# ── discovery ───────────────────────────────────────────────────────────
def discover():
    pages = []
    for md in sorted(DOCS.glob("*.md")):
        if md.name.startswith("_"):
            continue
        fm = read_frontmatter(md)
        if md.name in TREE_PAGES:
            cfg = dict(TREE_PAGES[md.name])
            cfg["src"] = md
        else:
            page = fm.get("page") or re.sub(r"[^a-z0-9]+", "-", md.stem.lower()).strip("-")
            colour = fm.get("colour", "").strip().lower()
            colour = NAMED_COLOURS.get(colour, colour if colour.startswith("#") else "#0B7D55")
            cfg = dict(src=md, kind="cards", page=page,
                       title=fm.get("title") or md.stem.replace("-", " ").title(),
                       kicker=fm.get("kicker", "Page"),
                       summary=fm.get("summary", ""),
                       placeholder=fm.get("placeholder", "Search this page…"),
                       footer=fm.get("footer", ""),
                       unit_group=fm.get("unit_group", "sections"),
                       unit_card=fm.get("unit_card", "items"),
                       colour=colour,
                       order=int(fm.get("order", 99)))
        cfg["order"] = int(cfg.get("order", 99))
        cfg.setdefault("unit_group", "sections")
        cfg.setdefault("unit_card", "items")
        pages.append(cfg)
    pages.sort(key=lambda p: (p["order"], p["title"]))
    return pages


def list_files():
    if not FILES.exists():
        return []
    out = []
    for f in sorted(FILES.iterdir()):
        if f.name.startswith(".") or not f.is_file():
            continue
        kb = f.stat().st_size / 1024
        size = f"{kb / 1024:.1f} MB" if kb >= 1024 else f"{kb:.0f} KB"
        out.append({"name": f.name, "size": size,
                    "ext": (f.suffix.lstrip(".").upper()[:4] or "FILE"),
                    "big": kb > 25 * 1024})
    return out


# ── home ────────────────────────────────────────────────────────────────
def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


# Order here is the order the buttons appear in.
CONTACT_FIELDS = ("whatsapp", "linkedin", "tiktok", "youtube", "email", "phone")
LABELS = {"whatsapp": "WhatsApp", "linkedin": "LinkedIn", "tiktok": "TikTok",
          "youtube": "YouTube", "email": "Email", "phone": "Phone"}

# Inline SVG only — the site has to work with no network, so no icon font
# and no remote images. 24x24 viewBox, single filled path each.
ICONS = {
    "whatsapp": "M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z",
    "linkedin": "M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z",
    "tiktok": "M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z",
    "youtube": "M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z",
    "email": "M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4-8 5-8-5V6l8 5 8-5v2z",
    "phone": "M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z",
}
BRAND = {"whatsapp": "#25D366", "linkedin": "#0A66C2", "tiktok": "#EE1D52",
         "youtube": "#FF0000", "email": "#C5221F", "phone": "#0B7D55"}


def home_config():
    """Landing-page details, from docs/_home.md. Underscore keeps it off the site."""
    path = DOCS / "_home.md"
    fm = read_frontmatter(path) if path.exists() else {}
    keys = ("name", "role", "location", "tagline", "about") + CONTACT_FIELDS
    return {k: fm.get(k, "").strip() for k in keys}


def contact_link(kind, value):
    """Build the href from whatever form was typed.

    Full URL, url-without-scheme, bare handle, @handle or a raw phone number
    all resolve — because in practice you paste whatever the app gave you.
    """
    v = value.strip()
    if kind == "email":
        return f"mailto:{v}", v
    if kind in ("whatsapp", "phone"):
        digits = re.sub(r"\D", "", v)
        # "00" is the international dialling prefix; wa.me and tel: both want
        # the bare country code, so 00966… must become 966….
        digits = re.sub(r"^00", "", digits)
        if not digits:
            return None, None
        return (f"https://wa.me/{digits}" if kind == "whatsapp" else f"tel:+{digits}"), v

    # Strip scheme, www. and the site's own domain, leaving just the handle/path.
    bare = re.sub(r"^https?://", "", v, flags=re.I)
    bare = re.sub(r"^(www|m|[a-z]{2})\.", "", bare, flags=re.I)
    domain = {"linkedin": r"linkedin\.com/", "tiktok": r"tiktok\.com/",
              "youtube": r"(youtube\.com/|youtu\.be/)"}[kind]
    bare = re.sub(rf"^{domain}", "", bare, flags=re.I).strip("/")
    if not bare:
        return None, None

    if kind == "linkedin":
        path = bare if bare.startswith(("in/", "company/")) else "in/" + bare.lstrip("@")
        return f"https://www.linkedin.com/{path}", f"linkedin.com/{path}"
    if kind == "tiktok":
        return (f"https://www.tiktok.com/@{bare.lstrip('@')}",
                f"tiktok.com/@{bare.lstrip('@')}")
    path = bare if bare.startswith(("@", "c/", "channel/", "user/")) else "@" + bare
    return f"https://www.youtube.com/{path}", f"youtube.com/{path}"


def contact_block(cfg):
    """One button per contact field that was actually filled in.

    A blank field produces nothing at all — no dead button, no placeholder.
    """
    btns = ""
    for kind in CONTACT_FIELDS:
        if not cfg.get(kind):
            continue
        href, label = contact_link(kind, cfg[kind])
        if not href:
            continue
        btns += (
            f'<a class="cbtn" href="{esc(href)}" style="--b:{BRAND[kind]}" '
            f'rel="noopener" aria-label="{LABELS[kind]}: {esc(label)}">'
            f'<svg viewBox="0 0 24 24" width="17" height="17" fill="currentColor" '
            f'aria-hidden="true"><path d="{ICONS[kind]}"/></svg>'
            f'<span>{LABELS[kind]}</span></a>')
    if not btns:
        return ""
    where = (f'<div class="cwhere">{esc(cfg["location"])}</div>'
             if cfg.get("location") else "")
    return f'<div class="ct"><div class="cbtns">{btns}</div>{where}</div>'


def build_home(css, head, tiles, docs_list, files_list):
    cfg = home_config()

    rows_html = ""
    for i, t in enumerate(tiles, 1):
        stat = " &middot; ".join(f'{v} {l}' for v, l in t["nums"][:2])
        rows_html += (
            f'<a class="ir" href="./{t["page"]}/index.html" style="--c:{t["colour"]}">'
            f'<span class="n">{i:02d}</span>'
            f'<span class="b"><h3>{esc(t["title"])}</h3><p>{esc(t["summary"])}</p></span>'
            f'<span class="st">{stat}</span>'
            '<svg class="go" width="19" height="19" viewBox="0 0 24 24" fill="none" '
            'stroke="currentColor" stroke-width="2.4" stroke-linecap="round" '
            'stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>')

    # Documents only when there is something to show — an empty box is clutter.
    docs_section = ""
    if files_list:
        file_rows = "".join(
            f'<a class="row" href="./files/{f["name"]}"><span class="ic ic-f">{f["ext"]}</span>'
            f'<span class="t"><b>{f["name"]}</b>'
            f'<span>{"TOO LARGE FOR PAGES — over 25 MB" if f["big"] else "document"}</span>'
            f'</span><span class="sz">{f["size"]}</span></a>' for f in files_list)
        docs_section = (
            '<section class="sec"><div class="sech"><h2>Documents</h2>'
            '<span>certificates · CV · PDFs</span></div>' + file_rows + '</section>')

    # Headline figures, taken straight from the parsed pages so they cannot
    # drift. (page slug, which of that page's figures) — missing pages are skipped.
    by_page = {t["page"]: t for t in tiles}
    hl = ""
    for page, i in (("experience", 0), ("experience", 1), ("courses", 0), ("knowledge", 1)):
        t = by_page.get(page)
        if t and len(t["nums"]) > i:
            v, l = t["nums"][i]
            hl += f'<div><b>{v}</b><span>{esc(l)}</span></div>'
    hl = f'<div class="hl">{hl}</div>' if hl else ""

    about = f'<p class="ab">{esc(cfg["about"])}</p>' if cfg["about"] else ""
    contact = contact_block(cfg)
    profile = f'<section class="prof">{about}{contact}</section>' if about or contact else ""

    body = f'''<div class="wrap">
<header class="hero">
  <div class="tbar"><button class="btn" id="themeBtn">Paper</button></div>
  <div class="eyebrow"><span class="dot"></span> {esc(cfg["role"] or "Personal knowledge base")} <span style="opacity:.4">/</span> {esc(cfg["location"])}</div>
  <h1>{esc(cfg["name"] or "Knowledge Base")}<span class="thin">{esc(cfg["tagline"])}</span></h1>
</header>
{hl}
{profile}
<section class="sec idxsec">
  <div class="sech"><h2>Contents</h2><span>{len(tiles)} sections</span></div>
  <nav class="idx">{rows_html}</nav>
</section>
{docs_section}
<footer>
  <b>Edit</b> &nbsp; every page is generated from the markdown in <code>docs/</code>. Change the markdown, never the HTML.<br>
  <b>Note</b> &nbsp; marked noindex. It names employers and states which exams are unsat.
</footer>
</div>
<script>
const T={{paper:{{l:'Paper',tc:'#2F6FD0',tx:'#0E7A54',tt:'#C2660C',tr:'#7040C4',a:'#1B57C4'}},
         ink:{{l:'Ink',tc:'#7FA8E8',tx:'#5FD6A4',tt:'#FFAE5C',tr:'#B79BE8',a:'#4C8DFF'}}}};
let th='paper';
function ap(t){{th=t;document.documentElement.dataset.theme=t;const v=T[t],r=document.documentElement.style;
  r.setProperty('--tc',v.tc);r.setProperty('--tx',v.tx);r.setProperty('--tt',v.tt);
  r.setProperty('--tr',v.tr);r.setProperty('--a40',v.a);
  document.getElementById('themeBtn').textContent=v.l;
  try{{window.storage.set('kb-theme',t);}}catch(e){{}}}}
document.getElementById('themeBtn').onclick=()=>ap(th==='paper'?'ink':'paper');
(async()=>{{try{{const r=await window.storage.get('kb-theme');if(r&&r.value)th=r.value;}}catch(e){{}}ap(th);}})();
</script>
</body></html>'''
    title = cfg["name"] or "Knowledge Base"
    html = (head.replace("__CSS__", css + cards.HOME_CSS)
                .replace("__TITLETAG__", f'{title} — {cfg["role"]}' if cfg["role"] else title)
            + body)
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    return len(html.encode()) / 1024


def main():
    fail = False
    css, head = shell()
    pages = discover()
    tiles, docs_list = [], []

    print(f"discovered {len(pages)} page(s) in docs/\n")
    for cfg in pages:
        md = cfg["src"]
        docs_list.append({"name": md.name, "title": cfg["title"],
                          "size": f"{md.stat().st_size / 1024:.0f} KB"})

        if cfg["kind"] == "knowledge":
            d = parse_knowledge(md)
            m = d["meta"]
            size = render_tree(cfg["tpl"], d, ROOT / cfg["page"] / "index.html")
            print(f"  {cfg['page']:<12} {m['cats']} categories · {m['topics']} topics · "
                  f"{m['subs']} subtopics · {m['refs']} refs   {size:.0f} KB")
            if m["areas"] != 10 or m["topics"] < 500:
                print("    ! parsed short")
                fail = True
            tiles.append({**cfg, "nums": [(m["cats"], "categories"), (m["topics"], "topics"),
                                          (m["subs"], "subtopics"), (m["refs"], "cross-refs")]})

        elif cfg["kind"] == "courses":
            d = parse_courses(md)
            m = d["meta"]
            size = render_tree(cfg["tpl"], d, ROOT / cfg["page"] / "index.html")
            print(f"  {cfg['page']:<12} {m['courses']} courses · {m['modules']} modules · "
                  f"{m['topics']} topics · {m['subs']} subtopics   {size:.0f} KB")
            if m["courses"] < 5 or m["topics"] < 200:
                print("    ! parsed short")
                fail = True
            tiles.append({**cfg, "nums": [(m["courses"], "courses"), (m["modules"], "modules"),
                                          (m["topics"], "topics"), (m["subs"], "subtopics")]})

        else:
            m, size = render_card_page(md, cfg, css, head)
            print(f"  {cfg['page']:<12} {m['groups']} {cfg['unit_group']} · "
                  f"{m['cards']} {cfg['unit_card']} · {m['items']} details   {size:.0f} KB")
            if m["cards"] < 1:
                print("    ! no cards found — check the markdown format")
                fail = True
            tiles.append({**cfg, "nums": [(m["groups"], cfg["unit_group"]),
                                          (m["cards"], cfg["unit_card"]),
                                          (m["items"], "details")]})

    files_list = list_files()
    hb = build_home(css, head, tiles, docs_list, files_list)
    print(f"\n  {'index.html':<12} home · {len(tiles)} cards · {len(files_list)} file(s)"
          f"   {hb:.0f} KB")

    if fail:
        print("\nBUILD FAILED — output written but something parsed short.")
        sys.exit(1)
    print("\nBuild OK.")


if __name__ == "__main__":
    main()
