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
        kicker="Index 01 · by technology", colour="#1B57C4",
        title="Master Knowledge Index",
        summary="Ten layers, copper up to CCTV. One home per concept, cross-referenced.",
        order=1),
    "course-syllabus-index.md": dict(
        page="courses", tpl="courses.tpl", kind="courses",
        kicker="Index 02 · by course", colour="#C55A0C",
        title="Course Syllabus Index",
        summary="What each syllabus covered, merged from 21 documents. Links back to index 01.",
        order=2),
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
def build_home(css, head, tiles, docs_list, files_list):
    cards_html = ""
    for t in tiles:
        nums = "".join(f'<div><b>{v}</b><span>{l}</span></div>' for v, l in t["nums"])
        cards_html += (
            f'<a class="card" href="./{t["page"]}/index.html" style="--c:{t["colour"]}">'
            f'<div class="kicker">{t["kicker"]}</div><h3>{t["title"]}</h3>'
            f'<p>{t["summary"]}</p><div class="nums">{nums}</div>'
            '<svg class="go" width="20" height="20" viewBox="0 0 24 24" fill="none" '
            'stroke="currentColor" stroke-width="2.4" stroke-linecap="round" '
            'stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>')

    doc_rows = "".join(
        f'<a class="row" href="./docs/{d["name"]}"><span class="ic">MD</span>'
        f'<span class="t"><b>{d["name"]}</b><span>{d["title"]}</span></span>'
        f'<span class="sz">{d["size"]}</span></a>' for d in docs_list)

    if files_list:
        file_rows = "".join(
            f'<a class="row" href="./files/{f["name"]}"><span class="ic ic-f">{f["ext"]}</span>'
            f'<span class="t"><b>{f["name"]}</b>'
            f'<span>{"TOO LARGE FOR PAGES — over 25 MB" if f["big"] else "document"}</span>'
            f'</span><span class="sz">{f["size"]}</span></a>' for f in files_list)
    else:
        file_rows = ('<div class="empt">Drop PDFs, certificates or your CV into the '
                     '<code>files/</code> folder and rebuild — they appear here '
                     'automatically.<br>Anything over <b>25 MB</b> will not deploy '
                     'to Cloudflare Pages.</div>')

    body = f'''<div class="wrap">
<header class="hero">
  <div class="tbar"><button class="btn" id="themeBtn">Paper</button></div>
  <div class="eyebrow"><span class="dot"></span> Personal knowledge base <span style="opacity:.4">/</span> Riyadh, KSA</div>
  <h1>Knowledge Base<span class="thin">Ihtiram Ullah — Network &amp; IT Infrastructure Engineer</span></h1>
  <p class="lede">Everything studied and everything built. Each index is searchable and works offline once loaded.</p>
</header>
<div class="cards">{cards_html}</div>
<section class="sec">
  <div class="sech"><h2>Source files</h2><span>markdown · edit these, not the pages</span></div>
  {doc_rows}
</section>
<section class="sec">
  <div class="sech"><h2>Documents</h2><span>certificates · CV · PDFs</span></div>
  {file_rows}
</section>
<footer>
  <b>Add a page</b> &nbsp; copy <code>docs/_TEMPLATE.md</code>, write it, run <code>python3 build/build.py</code>. A card appears here on its own.<br>
  <b>Private</b> &nbsp; marked noindex. It names employers and states which exams are unsat — not for search engines.
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
    html = (head.replace("__CSS__", css + cards.HOME_CSS)
                .replace("__TITLETAG__", "Knowledge Base — Ihtiram Ullah") + body)
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
