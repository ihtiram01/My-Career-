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
        title_ar="المعرفة حسب الطبقات", title_ur="پرتوں کے لحاظ سے علم",
        summary_ar="عشر طبقات، من الكابلات النحاسية إلى أنظمة المراقبة. مفهوم واحد في مكان واحد، مع إحالات مرجعية.",
        summary_ur="دس پرتیں، کاپر سے سی سی ٹی وی تک۔ ہر تصور کا ایک ہی مقام، باہمی حوالوں کے ساتھ۔",
        order=6),
    "course-syllabus-index.md": dict(
        page="courses", tpl="courses.tpl", kind="courses",
        kicker="Section 04 · by course", colour="#C55A0C",
        title="Course Content",
        summary="What each syllabus covered, merged from 21 documents. Links back to the knowledge index.",
        title_ar="محتوى الدورات", title_ur="کورس کا مواد",
        summary_ar="ما غطته كل دورة، مدمجاً من ٢١ وثيقة، مع روابط إلى فهرس المعرفة.",
        summary_ur="ہر کورس نے کیا احاطہ کیا، ۲۱ دستاویزات سے یکجا۔ نالج انڈیکس سے منسلک۔",
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
                       title_ar=fm.get("title_ar", ""), title_ur=fm.get("title_ur", ""),
                       summary_ar=fm.get("summary_ar", ""), summary_ur=fm.get("summary_ur", ""),
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

# ── languages ───────────────────────────────────────────────────────────
# Landing page only. The seven section pages are English; switching the
# language says so rather than pretending otherwise.
LANGS = [("en", "English", "ltr"), ("ar", "العربية", "rtl"), ("ur", "اردو", "rtl")]

UI = {
    "en": {"contents": "Contents", "sections": "sections", "based": "Based in",
           "note": "Section pages are in English for now.",
           "foot1": "Every page is generated from the markdown in docs/. Change the markdown, never the HTML.",
           "foot2": "Marked noindex. It names employers and states which exams are unsat."},
    "ar": {"contents": "المحتويات", "sections": "أقسام", "based": "المقر",
           "note": "صفحات الأقسام باللغة الإنجليزية حالياً.",
           "foot1": "كل صفحة يتم توليدها من ملفات markdown في مجلد docs/. عدّل الـ markdown، ولا تعدّل ملفات HTML.",
           "foot2": "الموقع غير مُفهرس في محركات البحث. يذكر جهات العمل والاختبارات التي لم تُجتَز بعد."},
    "ur": {"contents": "فہرست", "sections": "حصے", "based": "مقام",
           "note": "سیکشن کے صفحات فی الحال انگریزی میں ہیں۔",
           "foot1": "ہر صفحہ docs/ کے markdown سے بنتا ہے۔ markdown میں تبدیلی کریں، HTML میں کبھی نہیں۔",
           "foot2": "سرچ انجن سے محفوظ۔ اس میں آجروں کے نام اور غیر منعقدہ امتحانات درج ہیں۔"},
}

# Words used in the figure strips, so "8 roles" reads correctly in each language.
STAT_WORDS = {
    "roles":      {"ar": "أدوار",    "ur": "کردار"},
    "projects":   {"ar": "مشاريع",   "ur": "پروجیکٹس"},
    "companies":  {"ar": "شركات",    "ur": "کمپنیاں"},
    "courses":    {"ar": "دورات",    "ur": "کورسز"},
    "modules":    {"ar": "وحدات",    "ur": "ماڈیولز"},
    "topics":     {"ar": "مواضيع",   "ur": "موضوعات"},
    "categories": {"ar": "فئات",     "ur": "زمرے"},
    "sections":   {"ar": "أقسام",    "ur": "حصے"},
    "entries":    {"ar": "مدخلات",   "ur": "اندراجات"},
    "tracks":     {"ar": "مسارات",   "ur": "ٹریکس"},
    "actions":    {"ar": "إجراءات",  "ur": "اقدامات"},
    "areas":      {"ar": "مجالات",   "ur": "شعبے"},
    "labs":       {"ar": "مختبرات",  "ur": "لیبز"},
}


def home_config():
    """Landing-page details, from docs/_home.md. Underscore keeps it off the site."""
    path = DOCS / "_home.md"
    fm = read_frontmatter(path) if path.exists() else {}
    keys = (("name", "role", "location", "tagline") +
            tuple(f"{k}_{l}" for k in ("role", "location", "tagline")
                  for l, _, _ in LANGS if l != "en") + CONTACT_FIELDS)
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
        if not href:            continue
        btns += (
            f'<a class="cbtn" href="{esc(href)}" style="--b:{BRAND[kind]}" '
            f'rel="noopener" aria-label="{LABELS[kind]}: {esc(label)}">'
            f'<svg viewBox="0 0 24 24" width="17" height="17" fill="currentColor" '
            f'aria-hidden="true"><path d="{ICONS[kind]}"/></svg>'
            f'<span>{LABELS[kind]}</span></a>')
    if not btns:
        return ""
    where = (f'<div class="cwhere" id="cWhere">{esc(cfg["location"])}</div>'
             if cfg.get("location") else "")
    return f'<div class="ct"><div class="cbtns">{btns}</div>{where}</div>'


def build_home(css, head, tiles, docs_list, files_list):
    cfg = home_config()

    def row_data(lang):
        out = []
        for i, t in enumerate(tiles, 1):
            title = t.get(f"title_{lang}") or t["title"]
            summ = t.get(f"summary_{lang}") or t["summary"]
            # Arabic noun-number agreement changes with the count (dual, 3-10
            # plural, 11+ singular accusative). Rather than encode all of that,
            # use the noun-first form Arabic interfaces normally use, which is
            # correct whatever the number.
            stat = " · ".join(
                (f'{STAT_WORDS.get(l, {}).get(lang, l)}: {v}' if lang == "ar"
                 else f'{v} {STAT_WORDS.get(l, {}).get(lang, l)}')
                for v, l in t["nums"][:2])
            out.append({"n": f"{i:02d}", "href": f"./{t['page']}/index.html",
                        "c": t["colour"], "t": title, "s": summ, "st": stat})
        return out

    rows_html = "".join(
        f'<a class="ir" href="{r["href"]}" style="--c:{r["c"]};animation-delay:{i*70}ms">'
        f'<span class="n">{r["n"]}</span>'
        f'<span class="b"><h3>{esc(r["t"])}</h3><p>{esc(r["s"])}</p></span>'
        f'<span class="st">{esc(r["st"])}</span>'
        '<svg class="go" width="19" height="19" viewBox="0 0 24 24" fill="none" '
        'stroke="currentColor" stroke-width="2.4" stroke-linecap="round" '
        'stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>'
        for i, r in enumerate(row_data("en")))

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
    hl_pairs = []
    for page, i in (("experience", 0), ("experience", 1), ("courses", 0), ("knowledge", 1)):
        t = by_page.get(page)
        if t and len(t["nums"]) > i:
            hl_pairs.append(t["nums"][i])
    hl = "".join(f'<div><b>{v}</b><span>{esc(l)}</span></div>' for v, l in hl_pairs)
    hl = f'<div class="hl" id="hl">{hl}</div>' if hl else ""

    contact = contact_block(cfg)
    profile = f'<section class="prof">{contact}</section>' if contact else ""

    # Everything the language switcher swaps, for every language.
    i18n = {}
    for lang, _, _ in LANGS:
        u = dict(UI["en"], **UI.get(lang, {}))
        i18n[lang] = {
            "ui": u,
            "role": cfg.get(f"role_{lang}") or cfg["role"],
            "loc": cfg.get(f"location_{lang}") or cfg["location"],
            "tag": cfg.get(f"tagline_{lang}") or cfg["tagline"],
            "hl": [{"v": v, "l": STAT_WORDS.get(l, {}).get(lang, l)} for v, l in hl_pairs],
            "rows": row_data(lang),
        }
    langbtns = "".join(
        f'<button class="lbtn{" on" if code == "en" else ""}" data-lang="{code}" '
        f'lang="{code}" type="button">{name}</button>' for code, name, _ in LANGS)

    body = f'''<div class="wrap">
<header class="hero">
  <div class="tbar">
    <div class="langs" role="group" aria-label="Language">{langbtns}</div>
    <button class="btn" id="themeBtn">Paper</button>
  </div>
  <div class="eyebrow"><span class="dot"></span> <span id="hRole">{esc(cfg["role"] or "Personal knowledge base")}</span> <span style="opacity:.4">/</span> <span id="hLoc">{esc(cfg["location"])}</span></div>
  <h1><span class="nm">{esc(cfg["name"] or "Knowledge Base")}</span><span class="thin" id="hTag">{esc(cfg["tagline"])}</span></h1>
</header>
{hl}
{profile}
<section class="sec idxsec">
  <div class="sech"><h2 id="hContents">Contents</h2><span id="hCount">{len(tiles)} sections</span></div>
  <nav class="idx" id="idx">{rows_html}</nav>
</section>
{docs_section}
<footer>
  <span id="fNote" class="fnote hide"></span>
  <span id="fOne">Every page is generated from the markdown in <code>docs/</code>. Change the markdown, never the HTML.</span><br>
  <span id="fTwo">Marked noindex. It names employers and states which exams are unsat.</span>
</footer>
</div>
<script>
const I18N={json.dumps(i18n, ensure_ascii=False, separators=(",", ":"))};
const DIR={json.dumps({c: d for c, _, d in LANGS})};
let lang='en';
const REDUCED=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
function countUp(el,to){{
  to=Number(to)||0;
  if(REDUCED||to<=0){{el.textContent=to;return;}}
  const t0=performance.now(),dur=Math.min(1100,420+to);
  (function step(t){{
    const p=Math.min(1,(t-t0)/dur);
    el.textContent=Math.round(to*(1-Math.pow(1-p,3)));
    if(p<1)requestAnimationFrame(step);
  }})(t0);
}}
function figures(D){{
  const hl=document.getElementById('hl'); if(!hl)return;
  const src=(D||I18N[lang]||I18N.en).hl;
  hl.querySelectorAll('b').forEach((b,i)=>{{ if(src[i])countUp(b,src[i].v); }});
}}
function paint(l){{
  const D=I18N[l]||I18N.en; lang=l;
  const r=document.documentElement;
  r.lang=l; r.dir=DIR[l]||'ltr';
  document.getElementById('hRole').textContent=D.role;
  document.getElementById('hLoc').textContent=D.loc;
  document.getElementById('hTag').textContent=D.tag;
  document.getElementById('hContents').textContent=D.ui.contents;
  document.getElementById('hCount').textContent=D.rows.length+' '+D.ui.sections;
  const w=document.getElementById('cWhere'); if(w) w.textContent=D.loc;
  const hl=document.getElementById('hl');
  if(hl){{
    hl.innerHTML=D.hl.map(x=>'<div><b>'+x.v+'</b><span>'+x.l+'</span></div>').join('');
    figures(D);
  }}
  const esc=s=>String(s).replace(/[&<>"]/g,m=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[m]));
  document.getElementById('idx').innerHTML=D.rows.map((x,i)=>
    '<a class="ir" href="'+x.href+'" style="--c:'+x.c+';animation-delay:'+(i*70)+'ms">'+
    '<span class="n">'+x.n+'</span><span class="b"><h3>'+esc(x.t)+'</h3><p>'+esc(x.s)+'</p></span>'+
    '<span class="st">'+esc(x.st)+'</span>'+
    '<svg class="go" width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" '+
    'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'+
    '<path d="M5 12h14M13 6l6 6-6 6"/></svg></a>').join('');
  document.getElementById('fOne').textContent=D.ui.foot1;
  document.getElementById('fTwo').textContent=D.ui.foot2;
  const n=document.getElementById('fNote');
  n.textContent=D.ui.note; n.classList.toggle('hide', l==='en');
  document.querySelectorAll('.lbtn').forEach(b=>b.classList.toggle('on', b.dataset.lang===l));
  try{{window.storage.set('kb-lang',l);}}catch(e){{}}
}}
document.querySelectorAll('.lbtn').forEach(b=>b.onclick=()=>paint(b.dataset.lang));
(async()=>{{
  let l='en';
  try{{const r=await window.storage.get('kb-lang');if(r&&r.value&&I18N[r.value])l=r.value;}}catch(e){{}}
  // English is already in the HTML, so only the figures need starting.
  if(l!=='en')paint(l); else figures();
}})();
</script>
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




# ── hierarchical career portfolio ──────────────────────────────────────
# Experience and Certifications render as a dashboard of numbered cards, each
# opening its own detail page. Order on the page is the order in the markdown,
# so the sequence is edited by moving a `##` block, never by touching code.

PORTFOLIO_CSS = r"""
.port-wrap{max-width:1120px;margin:0 auto;padding:28px 18px 100px;position:relative;z-index:1}
.port-top{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-bottom:34px}
.port-top a,.port-top button{font:600 11px var(--mono);letter-spacing:.06em;text-transform:uppercase;
  color:var(--dim);background:var(--panel);border:1px solid var(--line2);border-radius:8px;padding:10px 13px;
  text-decoration:none;cursor:pointer}
.port-hero{padding:30px 0 28px;border-bottom:1px solid var(--line)}
.port-kicker{font:10px var(--mono);letter-spacing:.18em;text-transform:uppercase;color:var(--a40)}
.port-hero h1{font:700 clamp(32px,6vw,56px)/1.04 var(--disp);letter-spacing:-.04em;margin:12px 0}
.port-hero p{max-width:68ch;color:var(--dim);font-size:15px;line-height:1.7;margin:0}
.port-stats{display:flex;gap:12px;flex-wrap:wrap;margin:22px 0}
.port-stat{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:13px 16px;min-width:110px}
.port-stat b{display:block;font:700 23px var(--disp);color:var(--ink)}
.port-stat span{font:9px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--faint)}
.port-tools{margin:22px 0 18px}
.port-tools input{width:100%;min-width:0;padding:12px 14px;border-radius:9px;border:1px solid var(--line2);
  background:var(--panel);color:var(--ink);font:14px var(--body)}
.port-legend{display:flex;gap:14px;flex-wrap:wrap;margin:-4px 0 18px;font:10px var(--mono);color:var(--faint);
  letter-spacing:.06em;text-transform:uppercase}
.port-legend i{display:inline-block;width:10px;height:10px;border-radius:3px;margin-right:6px;vertical-align:-1px}
.port-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,310px),1fr));gap:15px}
.port-card{display:flex;flex-direction:column;gap:9px;padding:20px;background:var(--panel);border:1px solid var(--line);
  border-radius:13px;text-decoration:none;color:inherit;box-shadow:var(--shadow);position:relative;overflow:hidden;
  transition:transform .2s,border-color .2s}
.port-card:before{content:"";height:4px;position:absolute;inset:0 0 auto;background:var(--accent)}
.port-card:hover{transform:translateY(-3px);border-color:var(--accent)}
.port-card .cover{margin:-20px -20px 6px;aspect-ratio:16/9;background:var(--panel2);overflow:hidden}
.port-card .cover img{width:100%;height:100%;object-fit:cover;display:block}
.port-seq{font:700 12px var(--mono);color:var(--accent);letter-spacing:.06em}
.port-card h2{font:600 19px/1.25 var(--disp);margin:0;letter-spacing:-.02em}
.port-card p{color:var(--dim);font-size:13px;line-height:1.65;margin:0}
.port-meta{font:10px var(--mono);letter-spacing:.04em;color:var(--faint);text-transform:uppercase}
.port-pills{display:flex;gap:7px;flex-wrap:wrap;margin-top:auto;padding-top:8px}
.port-pill{font:10px var(--mono);padding:5px 8px;border-radius:20px;background:var(--panel2);border:1px solid var(--line);color:var(--dim)}
.port-pill.lead{color:var(--accent);border-color:color-mix(in srgb,var(--accent) 45%,transparent);font-weight:700}
.port-arrow{color:var(--accent);font:600 12px var(--mono);margin-top:4px}
.port-detail{max-width:900px;margin:0 auto}
.port-detail .intro{background:var(--panel);border:1px solid var(--line);border-left:4px solid var(--accent);
  border-radius:12px;padding:18px 20px;margin:22px 0}
.port-detail .intro h2{font:600 18px var(--disp);margin:0 0 10px}
.port-detail > h2{font:600 19px var(--disp);margin:30px 0 12px}
.port-detail h3{font:600 16px var(--disp);margin:0 0 8px}
.port-detail .detail-card{background:var(--panel);border:1px solid var(--line);border-radius:11px;padding:17px 19px;margin:12px 0}
.port-detail ul{padding-left:20px;margin:9px 0;color:var(--dim)}
.port-detail li{font-size:13.5px;line-height:1.7;margin:5px 0}
.port-detail .detail-row{display:grid;grid-template-columns:120px 1fr;gap:12px;padding:8px 0;border-bottom:1px solid var(--line)}
.port-detail .detail-row:last-child{border:0}
.port-detail .detail-row b{font:10px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--faint)}
.port-detail .detail-row span{font-size:13.5px;color:var(--dim)}
.port-detail .detail-row.status span{color:var(--accent);font-weight:600}
.port-detail .refs{display:flex;gap:7px;flex-wrap:wrap;margin-top:12px}
.port-detail .refs a{font:10px var(--mono);color:var(--a40);text-decoration:none;border:1px solid var(--line2);border-radius:6px;padding:5px 8px}
.gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,200px),1fr));gap:10px;margin:14px 0 4px}
.gallery figure{margin:0;background:var(--panel2);border:1px solid var(--line);border-radius:9px;overflow:hidden}
.gallery a{display:block;aspect-ratio:4/3;overflow:hidden}
.gallery img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .3s}
.gallery a:hover img{transform:scale(1.04)}
.gallery figcaption{font-size:12px;color:var(--dim);padding:7px 10px;line-height:1.45}
.port-pager{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:38px 0 0}
.port-pager a{display:block;padding:14px 16px;border:1px solid var(--line2);border-radius:10px;background:var(--panel);
  text-decoration:none;color:inherit}
.port-pager a:hover{border-color:var(--a40)}
.port-pager small{display:block;font:9.5px var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--faint);margin-bottom:4px}
.port-pager b{font:600 14px var(--disp)}
.port-pager .next{text-align:right;grid-column:2}
.port-empty{padding:24px;text-align:center;color:var(--faint);border:1px dashed var(--line2);border-radius:10px}
@media(max-width:600px){.port-wrap{padding:18px 14px 70px}.port-hero{padding-top:18px}
  .port-detail .detail-row{grid-template-columns:1fr;gap:3px}
  .port-pager{grid-template-columns:1fr}.port-pager .next{grid-column:1}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}}
"""

# Engagement type -> accent. Shown as a coloured stripe and a legend.
TYPE_COLOUR = [
    ("employment", "#1B57C4", "Employment"),
    ("contract",   "#6E35C9", "Contract"),
    ("freelance",  "#0B7D55", "Freelance"),
    ("project",    "#0C7F99", "Site project"),
    ("independent", "#7E5129", "Independent"),
]
# Credential status -> accent. Order matters: first match wins.
STATUS_ACCENT = [
    ("record conflict", "#C42A36", "Record conflict"),
    ("unconfirmed",     "#C55A0C", "Unconfirmed"),
    ("coursework",      "#C55A0C", "Coursework only"),
    ("course completed", "#8A6800", "Course completed"),
    ("passed",          "#0B7D55", "Passed"),
    ("certified",       "#0B7D55", "Passed"),
]

PHOTO_WARN_KB = 1500       # big photos slow phones down; still built
PHOTO_MAX_MB = 25          # Cloudflare Pages hard limit per file


def slugify(text, limit=60):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower().replace("&", " and ")).strip("-")
    return s[:limit].rstrip("-")


def unique_slug(base, used):
    s, n = base, 2
    while s in used:
        s, n = f"{base}-{n}", n + 1
    used.add(s)
    return s


def type_accent(kind):
    k = (kind or "").lower()
    for key, colour, label in TYPE_COLOUR:
        if key in k:
            return colour, label
    return "#1B57C4", (kind or "Employment")


def status_accent(status):
    st = (status or "").lower()
    for key, colour, label in STATUS_ACCENT:
        if key in st:
            return colour, label
    return "#56697F", status or "Record"


def check_photo(src, problems):
    """Photos are paths from the repo root. Missing ones fail the build."""
    f = ROOT / src
    if not f.is_file():
        problems.append(f"missing photo: {src}")
        return
    kb = f.stat().st_size / 1024
    if kb > PHOTO_MAX_MB * 1024:
        problems.append(f"photo over {PHOTO_MAX_MB} MB, Cloudflare will reject it: {src}")
    elif kb > PHOTO_WARN_KB:
        print(f"    · large photo ({kb / 1024:.1f} MB), consider resizing: {src}")


def portfolio_shell(title, css, head, body):
    script = """
<script>
(function(){
 const palettes={paper:{tc:'#2F6FD0',tx:'#0E7A54',tt:'#C2660C',tr:'#7040C4',a:'#1B57C4'},
                 ink:{tc:'#7FA8E8',tx:'#5FD6A4',tt:'#FFAE5C',tr:'#B79BE8',a:'#4C8DFF'}};
 let theme='paper';
 function apply(t){
   theme=t;document.documentElement.dataset.theme=t;
   const p=palettes[t],root=document.documentElement.style;
   root.setProperty('--tc',p.tc);root.setProperty('--tx',p.tx);
   root.setProperty('--tt',p.tt);root.setProperty('--tr',p.tr);root.setProperty('--a40',p.a);
   const btn=document.getElementById('themeBtn');if(btn)btn.textContent=t==='paper'?'Paper':'Ink';
 }
 const btn=document.getElementById('themeBtn');
 if(btn)btn.addEventListener('click',function(){
   apply(theme==='paper'?'ink':'paper');
   try{if(window.storage)window.storage.set('kb-theme',theme);}catch(e){}
 });
 (async function(){
   try{if(window.storage){const saved=await window.storage.get('kb-theme');if(saved&&saved.value==='ink')theme='ink';}}catch(e){}
   apply(theme);
 })();
})();
</script>
"""
    return (head.replace("__CSS__", css + PORTFOLIO_CSS)
                .replace("__TITLETAG__", esc(title) + " — Ihtiram Ullah")
            + body + script + "\n</body></html>")


def portfolio_header(title, kicker, summary, back_href, back_label="Back"):
    return f'''
<div class="port-wrap">
  <nav class="port-top" aria-label="Page navigation">
    <a href="{esc(back_href)}">&larr; {esc(back_label)}</a>
    <button id="themeBtn" type="button">Paper</button>
  </nav>
  <header class="port-hero">
    <div class="port-kicker">{esc(kicker)}</div>
    <h1>{esc(title)}</h1>
    {f"<p>{esc(summary)}</p>" if summary else ""}
  </header>
'''


def gallery_html(photos, prefix):
    if not photos:
        return ""
    figs = "".join(
        f'<figure><a href="{esc(prefix + ph["src"])}" target="_blank" rel="noopener">'
        f'<img src="{esc(prefix + ph["src"])}" alt="{esc(ph["cap"] or "Project photo")}" loading="lazy"></a>'
        + (f'<figcaption>{esc(ph["cap"])}</figcaption>' if ph["cap"] else "") + "</figure>"
        for ph in photos)
    return f'<div class="gallery">{figs}</div>'


def portfolio_card_content(card, knowledge_href, prefix):
    rows = "".join(
        f'<div class="detail-row {esc(r["k"])}"><b>{esc(r["k"])}</b><span>{esc(r["v"])}</span></div>'
        for r in card.get("rows", []))
    bullets = ("<ul>" + "".join(f"<li>{esc(x)}</li>" for x in card.get("bullets", [])) + "</ul>"
               if card.get("bullets") else "")
    refs = ""
    if card.get("links"):
        refs = '<div class="refs">' + "".join(
            f'<a href="{esc(knowledge_href)}">&rarr; Knowledge {esc(x)}</a>'
            for x in card["links"]) + "</div>"
    meta = " · ".join(card.get("meta", []))
    return (f'<article class="detail-card"><h3>{esc(card["title"])}</h3>'
            + (f'<div class="port-meta">{esc(meta)}</div>' if meta else "")
            + (f'<div>{rows}</div>' if rows else "") + bullets
            + gallery_html(card.get("photos", []), prefix) + refs + "</article>")


def pager_html(entries, i):
    """Previous / next links so the detail pages read as one sequence."""
    out = []
    if i > 0:
        p = entries[i - 1]
        out.append(f'<a class="prev" href="../{esc(p["slug"])}/index.html"><small>&larr; {esc(p["seq"])}</small><b>{esc(p["title"])}</b></a>')
    if i < len(entries) - 1:
        n = entries[i + 1]
        out.append(f'<a class="next" href="../{esc(n["slug"])}/index.html"><small>{esc(n["seq"])} &rarr;</small><b>{esc(n["title"])}</b></a>')
    return f'<nav class="port-pager" aria-label="Sequence">{"".join(out)}</nav>' if out else ""


def write_page(path, html):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")


# Career & Projects is split in two, the same way the CV is: employers on staff,
# and project / contract work. `type: Employment` lands in Company Experience,
# anything else in Project Experience; `section: company|projects` overrides.
EXPERIENCE_SECTIONS = [
    ("company",  "Company Experience", "Company",
     "Roles held on staff — the employers, in order."),
    ("projects", "Project Experience", "Project",
     "Contracts, freelance dispatches and site projects — each delivered as its own engagement."),
]

PORTFOLIO_SECTION_CSS = r"""
.port-jump{display:flex;gap:10px;flex-wrap:wrap;margin:0 0 6px}
.port-jump a{display:flex;align-items:center;gap:10px;padding:11px 15px;border:1px solid var(--line2);border-radius:10px;
  background:var(--panel);text-decoration:none;color:var(--ink);font:600 14px var(--disp)}
.port-jump a:hover{border-color:var(--a40)}
.port-jump b{font:700 11px var(--mono);color:var(--a40);padding:2px 7px;border-radius:20px;background:var(--panel2)}
.port-group{margin:34px 0 0;scroll-margin-top:16px}
.port-group-head{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;padding-bottom:10px;margin-bottom:16px;
  border-bottom:1px solid var(--line)}
.port-group-head h2{font:700 clamp(21px,3.4vw,27px) var(--disp);letter-spacing:-.025em;margin:0}
.port-group-head .n{font:11px var(--mono);color:var(--faint);letter-spacing:.08em;text-transform:uppercase}
.port-group-head p{flex-basis:100%;margin:2px 0 0;color:var(--dim);font-size:13.5px}
"""


def experience_section_key(info, kind):
    explicit = (info.get("section") or "").strip().lower()
    if explicit.startswith("comp") or explicit.startswith("employ"):
        return "company"
    if explicit.startswith("proj"):
        return "projects"
    return "company" if kind.lower() == "employment" else "projects"


def render_portfolio_page(md_path, cfg, css, head):
    data = cards.parse_cards(md_path)
    groups = data["groups"]
    is_experience = cfg["page"] == "experience"
    base_dir = ROOT / cfg["page"]
    problems, used, entries = [], set(), []
    total = 0

    # 1. One entry per detail page, in file order.
    if is_experience:
        for g in groups:
            info = g.get("info", {})
            colour, kind = type_accent(info.get("type"))
            photos = [ph for c in g["cards"] for ph in c.get("photos", [])]
            cover = info.get("cover") or (photos[0]["src"] if photos else "")
            entries.append(dict(
                title=g["title"], meta=g.get("meta", []), info=info, cards=g["cards"],
                summary=info.get("summary", ""), role=info.get("role", ""),
                accent=colour, kind=kind, cover=cover, n_photos=len(photos),
                section=experience_section_key(info, kind),
                slug=unique_slug(info.get("slug") or slugify(g["title"]), used)))
        sections = [dict(key=k, title=t, label=l, desc=d,
                         entries=[e for e in entries if e["section"] == k])
                    for k, t, l, d in EXPERIENCE_SECTIONS]
        sections = [s for s in sections if s["entries"]]
    else:
        for g in groups:
            for c in g["cards"]:
                status = next((r["v"] for r in c.get("rows", []) if r["k"] == "status"), g["title"])
                colour, label = status_accent(status)
                summary = next((r["v"] for r in c.get("rows", []) if r["k"] in ("note", "blueprint")), "")
                photos = c.get("photos", [])
                entries.append(dict(
                    title=c["title"], meta=c.get("meta", []), card=c, group=g["title"],
                    status=status, label=label, summary=summary, accent=colour,
                    cover=photos[0]["src"] if photos else "", n_photos=len(photos),
                    slug=unique_slug(slugify(c["title"]), used)))
        sections = [dict(key="all", title="", label="Credential", desc="", entries=entries)]

    # Numbering restarts in each section: Company 01–04, Project 01–07.
    for s in sections:
        width = max(2, len(str(len(s["entries"]))))
        for i, e in enumerate(s["entries"], 1):
            e["seq"] = str(i).zfill(width)

    # Remove detail folders from earlier builds that no longer match an entry.
    keep = {e["slug"] for e in entries}
    if base_dir.exists():
        for d in base_dir.iterdir():
            # only ever a folder this build made: exactly one generated index.html
            if d.is_dir() and d.name not in keep and [f.name for f in d.iterdir()] == ["index.html"]:
                (d / "index.html").unlink()
                d.rmdir()

    # 2. Detail pages. Previous / next stays inside the entry's own section.
    prefix = "../../"
    for s in sections:
        seq_list = s["entries"]
        last = seq_list[-1]["seq"]
        for i, e in enumerate(seq_list):
            style = f' style="--accent:{e["accent"]}"'
            if is_experience:
                total += len(e["cards"])
                for c in e["cards"]:
                    for ph in c.get("photos", []):
                        check_photo(ph["src"], problems)
                if e["info"].get("cover"):
                    check_photo(e["info"]["cover"], problems)
                kicker = f'{s["title"]} · {e["seq"]} of {last} · {e["kind"]}'
                body = portfolio_header(e["title"], kicker, e["summary"],
                                        f'../index.html#{s["key"]}', "All experience")
                pills = "".join(f'<span class="port-pill">{esc(x)}</span>' for x in e["meta"])
                body += f'<div class="port-detail"{style}><div class="intro">'
                body += f'<h2>{esc(e["role"])}</h2>' if e["role"] else ""
                body += f'<div class="port-pills"><span class="port-pill lead">{esc(e["kind"])}</span>{pills}</div></div>'
                body += "<h2>Work &amp; technical scope</h2>"
                body += "".join(portfolio_card_content(c, prefix + "knowledge/index.html", prefix)
                                for c in e["cards"])
            else:
                total += 1
                for ph in e["card"].get("photos", []):
                    check_photo(ph["src"], problems)
                kicker = f'Credential {e["seq"]} of {last} · {e["label"]}'
                body = portfolio_header(e["title"], kicker, e["summary"], "../index.html", "All credentials")
                body += f'<div class="port-detail"{style}><h2>Credential record</h2>'
                body += portfolio_card_content(e["card"], prefix + "knowledge/index.html", prefix)
            body += pager_html(seq_list, i) + "</div></div>"
            write_page(base_dir / e["slug"] / "index.html",
                       portfolio_shell(e["title"], css, head, body))

    # 3. Dashboard tiles.
    def tile(e):
        cover = (f'<div class="cover"><img src="../{esc(e["cover"])}" alt="" loading="lazy"></div>'
                 if e["cover"] else "")
        if is_experience:
            lead, sub, n = e["kind"], e["role"], len(e["cards"])
            extra = [f'{n} work area{"s" if n != 1 else ""}']
            arrow = "Open"
        else:
            lead, sub = e["label"], e["group"].split("·")[0].strip().title()
            extra, arrow = [], "Open credential"
        if e["n_photos"]:
            extra.append(f'{e["n_photos"]} photo{"s" if e["n_photos"] != 1 else ""}')
        pills = (f'<span class="port-pill lead">{esc(lead)}</span>'
                 + "".join(f'<span class="port-pill">{esc(x)}</span>' for x in e["meta"] + extra))
        hay = " ".join([e["title"], sub, e["summary"], lead, " ".join(e["meta"])]).lower()
        return (f'<a class="port-card" href="./{esc(e["slug"])}/index.html" style="--accent:{e["accent"]}" '
                f'data-search="{esc(hay)}">{cover}<span class="port-seq">{esc(e["seq"])}</span>'
                f'<div class="port-meta">{esc(sub)}</div><h2>{esc(e["title"])}</h2>'
                + (f'<p>{esc(e["summary"])}</p>' if e["summary"] else "")
                + f'<div class="port-pills">{pills}</div><span class="port-arrow">{arrow} &rarr;</span></a>')

    if is_experience:
        jump = '<nav class="port-jump" aria-label="Sections">' + "".join(
            f'<a href="#{s["key"]}">{esc(s["title"])} <b>{len(s["entries"])}</b></a>'
            for s in sections) + "</nav>"
        grid = "".join(
            f'<section class="port-group" id="{s["key"]}">'
            f'<div class="port-group-head"><h2>{esc(s["title"])}</h2>'
            f'<span class="n">{len(s["entries"])} {"role" if s["key"] == "company" else "engagement"}'
            f'{"s" if len(s["entries"]) != 1 else ""}</span><p>{esc(s["desc"])}</p></div>'
            f'<div class="port-grid">{"".join(tile(e) for e in s["entries"])}</div></section>'
            for s in sections)
        legend_src, title = TYPE_COLOUR, "Career & Projects"
        n_company = sum(len(s["entries"]) for s in sections if s["key"] == "company")
        n_projects = sum(len(s["entries"]) for s in sections if s["key"] == "projects")
        stats = [(n_company, "companies"), (n_projects, "projects"), (total, "work areas")]
    else:
        jump = ""
        grid = f'<div class="port-grid">{"".join(tile(e) for e in entries)}</div>'
        legend_src, title = STATUS_ACCENT, "Certifications & Training"
        stats = [(len(entries), "credentials"), (len(groups), "status groups")]

    seen, legend = set(), ""
    for _, colour, label in legend_src:
        if label not in seen:
            seen.add(label)
            legend += f'<span><i style="background:{colour}"></i>{esc(label)}</span>'

    stats_html = "".join(f'<div class="port-stat"><b>{n}</b><span>{esc(l)}</span></div>' for n, l in stats)
    body = portfolio_header(title, cfg["kicker"], cfg["summary"], "../index.html", "Home")
    body += f"""<div class="port-stats">{stats_html}</div>{jump}
      <div class="port-tools"><input id="portfolioSearch" type="search" placeholder="{esc(cfg.get("placeholder", "Search this section"))}" aria-label="Search this section"></div>
      <div class="port-legend">{legend}</div>
      <main id="portfolioGrid">{grid}</main>
      <p class="port-empty" id="portfolioEmpty" hidden>No matching entries. Try another search.</p>
      <footer style="margin-top:38px;color:var(--faint);font-size:12px">{cfg.get("footer", "")}</footer>
    </div>
    <script>
    (function(){{const q=document.getElementById('portfolioSearch'),items=[...document.querySelectorAll('.port-card')],
      groups=[...document.querySelectorAll('.port-group')],empty=document.getElementById('portfolioEmpty');
    q.addEventListener('input',function(){{const term=q.value.trim().toLowerCase();let count=0;
      items.forEach(x=>{{const ok=!term||x.dataset.search.includes(term);x.hidden=!ok;if(ok)count++;}});
      groups.forEach(g=>{{g.hidden=![...g.querySelectorAll('.port-card')].some(x=>!x.hidden);}});
      empty.hidden=count!==0;}});}})();
    </script>"""
    html = portfolio_shell(title, css + PORTFOLIO_SECTION_CSS, head, body)
    write_page(base_dir / "index.html", html)
    if is_experience:
        result = {"groups": n_company, "cards": n_projects, "areas": total}
    else:
        result = {"groups": len(groups), "cards": total, "areas": total}
    result.update(items=data["meta"]["items"], problems=problems)
    return result, len(html.encode()) / 1024



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

        elif cfg["page"] in ("experience", "exams"):
            m, size = render_portfolio_page(md, cfg, css, head)
            print(f"  {cfg['page']:<12} {m['groups']} {cfg['unit_group']} · "
                  f"{m['cards']} {cfg['unit_card']} · {m['items']} details   {size:.0f} KB")
            if m["cards"] < 1:
                print("    ! no portfolio entries found — check the markdown format")
                fail = True
            for prob in m["problems"]:
                print(f"    ! {prob}")
                fail = True
            # Same labels as the page's own frontmatter, so the home page says
            # "11 roles · 30 projects", never "30 employers".
            tiles.append({**cfg, "nums": [(m["groups"], cfg["unit_group"]),
                                          (m["cards"], cfg["unit_card"]),
                                          (m["items"], "details")]})

        else:
            m, size = render_card_page(md, cfg, css, head)
            print(f"  {cfg['page']:<12} {m['groups']} {cfg['unit_group']} · "
                  f"{m['cards']} {cfg['unit_card']} · {m['items']} details   {size:.0f} KB")
            if m["cards"] < 1:
                print("    ! no cards found — check the markdown format")
                fail = True
            tiles.append({**cfg, "nums": [(m["groups"], cfg["unit_group"]),                                          (m["cards"], cfg["unit_card"]),
                                          (m["items"], "details")]})

    files_list = list_files()
    hb = build_home(css, head, tiles, docs_list, files_list)
    print(f"\n  {'index.html':<12} home · {len(tiles)} cards · {len(files_list)} file(s)"
          f"   {hb:.0f} KB")

    if fail:
        print("\nBUILD FAILED — see the ! lines above. Output was written but is not safe to publish.")
        sys.exit(1)
    print("\nBuild OK.")


if __name__ == "__main__":
    main()