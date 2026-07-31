<!DOCTYPE html>
<html lang="en" data-theme="paper">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Master Knowledge Index — Ihtiram Ullah</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box}
:root{
  --mono:'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,monospace;
  --disp:'Space Grotesk',system-ui,sans-serif;
  --body:'IBM Plex Sans',system-ui,-apple-system,sans-serif;
  --rail:26px; --ease:cubic-bezier(.22,1,.36,1);
}
/* ── drafting paper (default) ── */
[data-theme="paper"]{
  --bg:#EDF1F7; --bg2:#E3EAF3; --panel:#FFFFFF; --panel2:#F4F8FC;
  --ink:#16222F; --dim:#4E617A; --faint:#8496AB;
  --line:rgba(28,58,98,.13); --line2:rgba(28,58,98,.22);
  --grid:rgba(40,90,160,.07); --shadow:0 1px 2px rgba(20,45,80,.06),0 6px 18px rgba(20,45,80,.05);
  --mark:#FFE08A; --markink:#3D2C00;
}
/* ── ink navy (alternate) ── */
[data-theme="ink"]{
  --bg:#0F1B2B; --bg2:#132234; --panel:#17273B; --panel2:#1D3049;
  --ink:#E7EFF9; --dim:#9DB0C6; --faint:#7A8DA6;
  --line:rgba(140,180,230,.13); --line2:rgba(140,180,230,.24);
  --grid:rgba(120,170,235,.06); --shadow:0 1px 2px rgba(0,0,0,.25);
  --mark:rgba(255,214,102,.32); --markink:#FFEDB8;
}
html,body{margin:0;padding:0}
body{background:var(--bg); color:var(--ink); font-family:var(--body); font-size:15px;
  line-height:1.55; -webkit-font-smoothing:antialiased; overflow-x:hidden;
  transition:background .35s var(--ease), color .35s var(--ease)}
body::before{content:''; position:fixed; inset:0; pointer-events:none; z-index:0;
  background-image:linear-gradient(var(--grid) 1px,transparent 1px),
                   linear-gradient(90deg,var(--grid) 1px,transparent 1px);
  background-size:44px 44px;
  mask-image:radial-gradient(ellipse 130% 90% at 50% 0%,#000 15%,transparent 80%);
  -webkit-mask-image:radial-gradient(ellipse 130% 90% at 50% 0%,#000 15%,transparent 80%)}
.wrap{position:relative; z-index:1; max-width:1180px; margin:0 auto; padding:0 18px 120px}

/* HERO */
header.hero{padding:50px 0 26px}
.eyebrow{font-family:var(--mono); font-size:10.5px; letter-spacing:.2em; text-transform:uppercase;
  color:var(--faint); margin-bottom:15px; display:flex; align-items:center; gap:9px; flex-wrap:wrap}
.eyebrow .dot{width:5px;height:5px;border-radius:50%;background:currentColor;
  color:var(--a40); box-shadow:0 0 9px currentColor; animation:pulse 2.6s ease-in-out infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
h1{font-family:var(--disp); font-weight:700; font-size:clamp(32px,6.8vw,58px); line-height:1;
  letter-spacing:-.032em; margin:0 0 12px}
h1 .thin{display:block; font-weight:400; color:var(--dim); font-size:clamp(16px,3vw,24px);
  letter-spacing:-.01em; margin-top:10px}
.lede{color:var(--dim); max-width:62ch; font-size:14.5px; margin:0 0 8px}
.lede b{color:var(--ink); font-weight:600}
.figs{display:flex; gap:22px; flex-wrap:wrap; margin:22px 0 4px; font-family:var(--mono)}
.fig b{display:block; font-size:21px; font-weight:700; color:var(--ink); line-height:1.15}
.fig span{font-size:9.5px; letter-spacing:.15em; text-transform:uppercase; color:var(--faint)}

/* STRANDS */
.strands{display:flex; gap:3px; height:50px; margin:24px 0 6px; border-radius:6px;
  overflow:hidden; border:1px solid var(--line); background:var(--panel); box-shadow:var(--shadow)}
.strand{flex:1; position:relative; cursor:pointer; background:transparent; border:0;
  transition:flex .45s var(--ease); overflow:hidden; padding:0}
.strand::before{content:''; position:absolute; inset:0 0 auto 0; height:4px; background:var(--c)}
.strand::after{content:''; position:absolute; left:0;right:0;top:4px;bottom:0;
  background:linear-gradient(to bottom,var(--c),transparent); opacity:.12; transition:opacity .25s}
.strand:hover::after,.strand.on::after{opacity:.3}
.strand:hover,.strand.on{flex:1.7}
.strand em{position:absolute; top:12px; left:0; right:0; text-align:center; font-family:var(--mono);
  font-size:10.5px; font-style:normal; font-weight:700; color:var(--c)}
.strand span{position:absolute; bottom:6px; left:0; right:0; text-align:center; font-family:var(--mono);
  font-size:9px; color:var(--dim); opacity:0; transition:opacity .3s; white-space:nowrap}
.strand:hover span,.strand.on span{opacity:1}

/* TOOLBAR */
.bar{position:sticky; top:0; z-index:40; margin:20px -18px 0; padding:11px 18px;
  background:color-mix(in srgb,var(--bg) 88%,transparent); backdrop-filter:blur(14px);
  border-bottom:1px solid var(--line)}
.searchrow{display:flex; gap:8px; align-items:center}
.search{flex:1; display:flex; align-items:center; gap:9px; background:var(--panel);
  border:1px solid var(--line2); border-radius:9px; padding:9px 13px; transition:border-color .2s,box-shadow .2s}
.search:focus-within{border-color:var(--a40); box-shadow:0 0 0 3px color-mix(in srgb,var(--a40) 18%,transparent)}
.search svg{flex:none; opacity:.5}
.search input{flex:1; background:none; border:0; outline:none; color:var(--ink);
  font-family:var(--body); font-size:15px; min-width:0}
.search input::placeholder{color:var(--faint)}
.btn{font-family:var(--mono); font-size:10.5px; letter-spacing:.07em; text-transform:uppercase;
  background:var(--panel); color:var(--dim); border:1px solid var(--line2); padding:10px 12px;
  border-radius:8px; cursor:pointer; white-space:nowrap; transition:all .18s}
.btn:hover{color:var(--ink); background:var(--panel2)}
.chips{display:flex; gap:6px; flex-wrap:wrap; margin-top:9px; align-items:center}
.chiplabel{font-family:var(--mono); font-size:9.5px; letter-spacing:.13em; text-transform:uppercase;
  color:var(--faint); margin-right:2px}
.chip{font-family:var(--mono); font-size:10.5px; padding:5px 10px; border-radius:20px;
  border:1px solid var(--line2); background:var(--panel); color:var(--dim); cursor:pointer;
  transition:all .18s; white-space:nowrap}
.chip:hover{color:var(--ink)}
.chip.on{background:var(--ink); color:var(--bg); border-color:var(--ink); font-weight:700}
.chip.t-C.on{background:var(--tc);border-color:var(--tc);color:#fff}
.chip.t-X.on{background:var(--tx);border-color:var(--tx);color:#fff}
.chip.t-T.on{background:var(--tt);border-color:var(--tt);color:#fff}
.chip.t-R.on{background:var(--tr);border-color:var(--tr);color:#fff}
.stats{display:flex; gap:15px; flex-wrap:wrap; margin-top:10px; padding-top:10px; border-top:1px solid var(--line)}
.stat{font-family:var(--mono); font-size:10.5px; color:var(--faint); letter-spacing:.03em}
.stat b{color:var(--ink); font-weight:700; font-size:12.5px}
.lvbar{display:flex; height:5px; flex:1; min-width:120px; border-radius:3px; overflow:hidden;
  background:var(--panel); align-self:center; border:1px solid var(--line)}
.lvbar i{display:block; height:100%; transition:width .5s var(--ease)}

/* AREAS */
.area{margin-top:42px; opacity:0; transform:translateY(14px); animation:rise .55s var(--ease) forwards}
@keyframes rise{to{opacity:1;transform:none}}
.ahead{display:flex; align-items:baseline; gap:12px; padding-bottom:12px;
  border-bottom:1px solid var(--line); margin-bottom:4px; flex-wrap:wrap}
.anum{font-family:var(--mono); font-weight:700; font-size:13px; color:var(--c); letter-spacing:.04em;
  padding:3px 8px; border:1px solid var(--c); border-radius:5px;
  background:color-mix(in srgb,var(--c) 10%,transparent)}
.atitle{font-family:var(--disp); font-weight:600; font-size:clamp(17px,3.2vw,22px);
  letter-spacing:-.015em; margin:0}
.acount{font-family:var(--mono); font-size:10.5px; color:var(--faint); margin-left:auto}
.cats{position:relative; padding-left:var(--rail)}
.cats::before{content:''; position:absolute; left:9px; top:0; bottom:0; width:2px;
  background:linear-gradient(to bottom,var(--c),color-mix(in srgb,var(--c) 20%,transparent));
  border-radius:2px; transform-origin:top; animation:draw .8s var(--ease) forwards}
@keyframes draw{from{transform:scaleY(0)}to{transform:scaleY(1)}}
.cat{position:relative; border-bottom:1px solid var(--line)}
.cat::before{content:''; position:absolute; left:calc(-1*var(--rail) + 11px); top:23px;
  width:13px; height:2px; background:var(--c); opacity:.45}
.cat::after{content:''; position:absolute; left:calc(-1*var(--rail) + 6px); top:20px; width:8px;
  height:8px; border-radius:50%; background:var(--bg); border:2px solid var(--c);
  transition:box-shadow .25s,background .25s}
.cat.open::after{background:var(--c); box-shadow:0 0 10px var(--c)}
.chead{display:flex; align-items:center; gap:10px; padding:13px 4px; cursor:pointer;
  user-select:none; transition:padding-left .22s var(--ease)}
.chead:hover{padding-left:8px}
.cnum{font-family:var(--mono); font-size:12px; font-weight:700; color:var(--c); flex:none}
.ctitle{font-family:var(--disp); font-weight:500; font-size:15.5px}
.cn{font-family:var(--mono); font-size:10px; color:var(--faint); flex:none}
.ctags{display:flex; gap:4px; flex-wrap:wrap; margin-left:auto; align-items:center}
.ctag{font-family:var(--mono); font-size:9px; padding:2.5px 6px; border-radius:4px;
  background:var(--panel2); color:var(--faint); border:1px solid var(--line); white-space:nowrap}
.ctag.field{color:var(--c); border-color:color-mix(in srgb,var(--c) 40%,transparent);
  background:color-mix(in srgb,var(--c) 9%,transparent); font-weight:700}
.caret{flex:none; width:15px; height:15px; color:var(--faint); transition:transform .32s var(--ease)}
.cat.open>.chead .caret{transform:rotate(90deg); color:var(--c)}
.body{display:grid; grid-template-rows:0fr; transition:grid-template-rows .4s var(--ease)}
.cat.open>.body{grid-template-rows:1fr}
.bodyin{overflow:hidden; min-height:0}
.topics{padding:2px 0 14px}

/* TOPIC */
.topic{border-radius:8px; transition:background .16s}
.topic:hover{background:var(--panel)}
.topic.flash{animation:flash 1.7s var(--ease)}
@keyframes flash{0%,60%{background:color-mix(in srgb,var(--c) 22%,transparent)}100%{background:transparent}}
.trow{display:flex; align-items:center; gap:9px; padding:7px 10px 7px 8px}
.tcaret{flex:none; width:14px; height:14px; color:var(--faint); transition:transform .3s var(--ease); cursor:pointer}
.topic.open .tcaret{transform:rotate(90deg); color:var(--c)}
.tcaret.ghost{opacity:0; pointer-events:none}
.tid{font-family:var(--mono); font-size:10.5px; color:var(--faint); flex:none; width:44px}
.tname{flex:1; font-size:14px; min-width:0}
.ty{font-family:var(--mono); font-size:9.5px; font-weight:700; width:18px; height:18px;
  display:grid; place-items:center; border-radius:4px; flex:none; border:1px solid}
.ty-C{color:var(--tc);border-color:color-mix(in srgb,var(--tc) 42%,transparent);background:color-mix(in srgb,var(--tc) 10%,transparent)}
.ty-X{color:var(--tx);border-color:color-mix(in srgb,var(--tx) 42%,transparent);background:color-mix(in srgb,var(--tx) 10%,transparent)}
.ty-T{color:var(--tt);border-color:color-mix(in srgb,var(--tt) 42%,transparent);background:color-mix(in srgb,var(--tt) 10%,transparent)}
.ty-R{color:var(--tr);border-color:color-mix(in srgb,var(--tr) 42%,transparent);background:color-mix(in srgb,var(--tr) 10%,transparent)}
.sn{font-family:var(--mono); font-size:9px; color:var(--faint); flex:none;
  padding:1.5px 5px; border-radius:9px; background:var(--panel2); border:1px solid var(--line)}
.lv{font-family:var(--mono); font-size:9.5px; font-weight:700; flex:none; min-width:31px; height:20px;
  display:grid; place-items:center; border-radius:5px; cursor:pointer; border:1px dashed var(--line2);
  color:var(--faint); background:transparent; transition:all .2s}
.lv:hover{border-color:var(--dim); color:var(--dim)}
.lv.set{border-style:solid}
.lv[data-v="0"]{color:#D64545;border-color:#D6454588;background:#D6454518}
.lv[data-v="1"]{color:#D97A1F;border-color:#D97A1F88;background:#D97A1F18}
.lv[data-v="2"]{color:#B08900;border-color:#B0890088;background:#B0890018}
.lv[data-v="3"]{color:#12855C;border-color:#12855C88;background:#12855C18}
.lv[data-v="4"]{color:#0C7C93;border-color:#0C7C93;background:#0C7C9322;
  box-shadow:0 0 8px color-mix(in srgb,#0C7C93 35%,transparent)}
[data-theme="ink"] .lv[data-v="0"]{color:#FF7B7B;border-color:#FF7B7B88;background:#FF7B7B1A}
[data-theme="ink"] .lv[data-v="1"]{color:#FFB067;border-color:#FFB06788;background:#FFB0671A}
[data-theme="ink"] .lv[data-v="2"]{color:#F0CE5A;border-color:#F0CE5A88;background:#F0CE5A1A}
[data-theme="ink"] .lv[data-v="3"]{color:#4ADFA6;border-color:#4ADFA688;background:#4ADFA61A}
[data-theme="ink"] .lv[data-v="4"]{color:#3FD9F0;border-color:#3FD9F0;background:#3FD9F026}
@keyframes bump{50%{transform:scale(1.2)}}
.lv.bumped{animation:bump .3s var(--ease)}
.refs{display:flex; gap:4px; flex-wrap:wrap; flex:none}
.ref{font-family:var(--mono); font-size:9px; padding:2px 6px; border-radius:4px; cursor:pointer;
  border:1px solid var(--line2); background:var(--panel2); color:var(--dim); transition:all .18s}
.ref:hover{background:var(--c); color:#fff; border-color:var(--c)}

/* SUBTOPICS */
.subs{display:grid; grid-template-rows:0fr; transition:grid-template-rows .34s var(--ease)}
.topic.open .subs{grid-template-rows:1fr}
.subsin{overflow:hidden; min-height:0}
.sublist{padding:2px 0 9px 62px; position:relative}
.sublist::before{content:''; position:absolute; left:50px; top:2px; bottom:11px; width:1px;
  background:color-mix(in srgb,var(--c) 32%,transparent)}
.sub{display:flex; align-items:baseline; gap:9px; padding:4px 8px; border-radius:6px; position:relative}
.sub::before{content:''; position:absolute; left:-12px; top:12px; width:9px; height:1px;
  background:color-mix(in srgb,var(--c) 32%,transparent)}
.sub:hover{background:var(--panel2)}
.sid{font-family:var(--mono); font-size:9.5px; color:var(--faint); flex:none; min-width:48px}
.sname{font-size:13.2px; color:var(--dim)}
.sub:hover .sname{color:var(--ink)}

/* SEARCH RESULTS */
#results{display:none; margin-top:26px}
#results.on{display:block}
.rhead{font-family:var(--mono); font-size:10.5px; letter-spacing:.13em; text-transform:uppercase;
  color:var(--faint); padding-bottom:9px; border-bottom:1px solid var(--line); margin-bottom:4px}
.rgroup{margin-top:20px}
.rgtitle{display:flex; align-items:center; gap:9px; margin-bottom:7px}
.rgtitle .anum{font-size:11px}
.rgtitle h3{font-family:var(--disp); font-weight:600; font-size:14.5px; margin:0}
.rgtitle .n{font-family:var(--mono); font-size:10px; color:var(--faint); margin-left:auto}
.hit{display:flex; align-items:flex-start; gap:10px; padding:9px 11px; border-radius:8px;
  cursor:pointer; border:1px solid transparent; transition:all .16s; background:var(--panel);
  margin-bottom:4px; box-shadow:var(--shadow)}
.hit:hover{border-color:var(--c); transform:translateX(3px)}
.hit .crumb{font-family:var(--mono); font-size:9.5px; color:var(--faint); margin-bottom:3px}
.hit .crumb b{color:var(--c); font-weight:700}
.hit .txt{font-size:14px; line-height:1.4}
.hit .mid{flex:1; min-width:0}
.hit .kind{font-family:var(--mono); font-size:8.5px; letter-spacing:.09em; text-transform:uppercase;
  padding:2px 6px; border-radius:4px; border:1px solid var(--line2); color:var(--faint); flex:none}
mark{background:var(--mark); color:var(--markink); border-radius:3px; padding:0 2px; font-weight:600}
.hide{display:none !important}
.empty{text-align:center; padding:70px 20px; color:var(--faint)}
.empty h3{font-family:var(--disp); color:var(--dim); font-weight:500; margin:0 0 7px; font-size:19px}
footer{margin-top:64px; padding-top:24px; border-top:1px solid var(--line);
  font-family:var(--mono); font-size:10.5px; color:var(--faint); line-height:2}
footer b{color:var(--dim)}
@media(max-width:640px){
  .wrap{padding:0 13px 100px}
  :root{--rail:20px}
  .bar{margin-left:-13px;margin-right:-13px;padding-left:13px;padding-right:13px}
  .strands{height:42px}
  .strand em{font-size:9px;top:9px}
  .strand span{display:none}
  .ctags{width:100%;margin-left:0;order:3;padding-left:23px}
  .chead{flex-wrap:wrap;gap:8px;padding:15px 4px}
  .acount{width:100%;margin-left:0}
  .tid{width:38px;font-size:10px}
  .tname{font-size:13.5px}
  .chip{padding:8px 12px;font-size:11px}
  .trow{padding:10px 8px}
  .lv{min-width:38px;height:28px;font-size:10.5px}
  .ty{width:22px;height:22px;font-size:10px}
  .btn{padding:12px 13px}
  .sublist{padding-left:44px}
  .sublist::before{left:33px}
  .sid{min-width:44px}
  /* let the toolbar buttons drop to their own row */
  .searchrow{flex-wrap:wrap}
  .search{flex:1 1 100%}
  .searchrow .btn{flex:1}
  /* reference chips get their own line instead of pushing type+level off-screen */
  .trow{flex-wrap:wrap}
  .tname{flex:1 1 45%}
  .refs{order:9; width:100%; padding-left:52px; margin-top:1px}
}
@media(prefers-reduced-motion:reduce){*{animation-duration:.01ms !important;transition-duration:.01ms !important}}
:focus-visible{outline:2px solid var(--a40); outline-offset:2px; border-radius:4px}
</style>
</head>
<body>
<div class="wrap">
<header class="hero">
  <div class="eyebrow"><span class="dot"></span> Personal knowledge map <span style="opacity:.4">/</span> v2.0 <span style="opacity:.4">/</span> July 2026</div>
  <h1>Master Knowledge Index<span class="thin">Ihtiram Ullah — Network &amp; IT Infrastructure Engineer</span></h1>
  <p class="lede">Four levels deep: <b>area → category → topic → subtopic</b>. Colours follow the <b>TIA-598 fiber code</b>, one strand per layer. Search returns every place a term appears, with its full path. Cross-references link topics that depend on each other.</p>
  <div class="figs">
    <div class="fig"><b>77</b><span>categories</span></div>
    <div class="fig"><b>741</b><span>topics</span></div>
    <div class="fig"><b>562</b><span>subtopics</span></div>
    <div class="fig"><b>132</b><span>cross-refs</span></div>
  </div>
  <div class="strands" id="strands"></div>
</header>

<div class="bar">
  <div class="searchrow">
    <label class="search">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
      <input id="q" type="search" placeholder="Search — ospf, poe, fiber, gpo, raid…" autocomplete="off" spellcheck="false">
    </label>
    <button class="btn" id="themeBtn" title="Switch theme">Paper</button>
    <button class="btn" id="toggleAll">Expand</button>
  </div>
  <div class="chips" id="typeChips"><span class="chiplabel">Type</span></div>
  <div class="chips" id="tagChips"><span class="chiplabel">Source</span></div>
  <div class="stats">
    <span class="stat"><b id="sShown">741</b> shown</span>
    <span class="stat"><b id="sRated">0</b> rated</span>
    <span class="stat"><b id="sProd">0</b> at L3+</span>
    <div class="lvbar" id="lvbar"></div>
    <button class="btn" id="exportBtn" style="padding:5px 10px">Export</button>
  </div>
</div>

<section id="results"></section>
<main id="root"></main>
<div class="empty hide" id="empty"><h3>Nothing matches</h3><p>Clear the search or turn off a filter.</p></div>

<footer>
  <b>Type</b> &nbsp; C concept &nbsp;·&nbsp; X config &nbsp;·&nbsp; T troubleshoot &nbsp;·&nbsp; R reference<br>
  <b>Level</b> &nbsp; 0 heard of it &nbsp;·&nbsp; 1 can explain &nbsp;·&nbsp; 2 studied / labbed &nbsp;·&nbsp; 3 production &nbsp;·&nbsp; 4 own it<br>
  <b>Claim rule</b> &nbsp; only L3+ belongs on a CV. L1–2 is “familiar with, not in production”.
</footer>
</div>
<script>
const D = __PAYLOAD__;
const AREAS = D.areas, IDX = D.index, META = D.meta;
const ESC={'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'};
const esc = s => String(s).replace(/[&<>"]/g, m => ESC[m]);
const FIELD = new Set(['Wemart','MetroL3','ZTE-RIY1','AlmavivA','Veevo','UCT','Field']);
const TYN = {C:'Concept',X:'Config',T:'Troubleshoot',R:'Reference'};

/* theme */
const THEMES = {
  paper:{label:'Paper', tc:'#2F6FD0', tx:'#0E7A54', tt:'#C2660C', tr:'#7040C4'},
  ink:  {label:'Ink',   tc:'#7FA8E8', tx:'#5FD6A4', tt:'#FFAE5C', tr:'#B79BE8'}
};
let theme='paper';
function applyTheme(t){
  theme=t; document.documentElement.dataset.theme=t;
  const v=THEMES[t], r=document.documentElement.style;
  r.setProperty('--tc',v.tc); r.setProperty('--tx',v.tx);
  r.setProperty('--tt',v.tt); r.setProperty('--tr',v.tr);
  AREAS.forEach(a=>r.setProperty('--a'+a.from, t==='paper'?a.light:a.dark));
  document.getElementById('themeBtn').textContent=v.label;
  document.querySelectorAll('[data-area]').forEach(el=>{
    const a=AREAS.find(x=>x.from===el.dataset.area);
    el.style.setProperty('--c', t==='paper'?a.light:a.dark);
  });
  try{ window.storage.set('mki-theme', t); }catch(e){}
}

/* storage */
let levels={}; const mem={};
async function loadState(){
  try{const r=await window.storage.get('mki-levels'); if(r&&r.value) levels=JSON.parse(r.value);}catch(e){levels=mem.l||{};}
  try{const r=await window.storage.get('mki-theme'); if(r&&r.value) theme=r.value;}catch(e){}
}
async function save(){ mem.l=levels; try{await window.storage.set('mki-levels',JSON.stringify(levels));}catch(e){} }

/* build */
const root=document.getElementById('root'), strandsEl=document.getElementById('strands');
let allTags=new Set();
AREAS.forEach((a,ai)=>{
  const s=document.createElement('button');
  s.className='strand'; s.dataset.area=a.from;
  s.innerHTML=`<em>${a.from}</em><span>${esc(a.short)}</span>`;
  s.title=`${a.from}–${a.to} ${esc(a.title)}`;
  s.onclick=()=>{ clearSearch(); document.getElementById('area-'+a.from).scrollIntoView({behavior:'smooth',block:'start'}); };
  strandsEl.appendChild(s);

  const sec=document.createElement('section');
  sec.className='area'; sec.id='area-'+a.from; sec.dataset.area=a.from;
  sec.style.animationDelay=(ai*50)+'ms';
  const nt=a.cats.reduce((t,c)=>t+c.topics.length,0);
  const ns=a.cats.reduce((t,c)=>t+c.topics.reduce((u,x)=>u+x.subs.length,0),0);
  let h=`<div class="ahead"><span class="anum">${a.from}–${a.to}</span>
    <h2 class="atitle">${esc(a.title)}</h2>
    <span class="acount">${a.cats.length} categories · ${nt} topics · ${ns} subtopics · ${esc(a.strand)} strand</span></div><div class="cats">`;
  a.cats.forEach(c=>{
    c.tags.forEach(t=>allTags.add(t));
    const tags=c.tags.map(t=>`<span class="ctag${FIELD.has(t)?' field':''}">${esc(t)}</span>`).join('');
    const topics=c.topics.map(t=>{
      const hasSubs=t.subs.length>0;
      const subs=t.subs.map(s=>`<div class="sub" data-id="${s.id}"><span class="sid">${s.id}</span><span class="sname">${esc(s.name)}</span></div>`).join('');
      const refs=t.refs.map(r=>`<button class="ref" data-goto="${r}" title="${esc((IDX[r]||{}).title||'')}">→${r}</button>`).join('');
      return `<div class="topic" id="t-${t.id}" data-id="${t.id}" data-type="${t.type}" data-tags="${esc(c.tags.join('|'))}">
        <div class="trow">
          <svg class="tcaret${hasSubs?'':' ghost'}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="m9 6 6 6-6 6"/></svg>
          <span class="tid">${t.id}</span>
          <span class="tname">${esc(t.name)}</span>
          ${hasSubs?`<span class="sn">${t.subs.length}</span>`:''}
          ${refs?`<span class="refs">${refs}</span>`:''}
          <span class="ty ty-${t.type}" title="${TYN[t.type]}">${t.type}</span>
          <button class="lv" data-id="${t.id}">L·</button>
        </div>
        ${hasSubs?`<div class="subs"><div class="subsin"><div class="sublist">${subs}</div></div></div>`:''}
      </div>`;
    }).join('');
    h+=`<div class="cat" id="c-${c.id}" data-cat="${c.id}">
      <div class="chead" role="button" tabindex="0">
        <svg class="caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="m9 6 6 6-6 6"/></svg>
        <span class="cnum">${c.id}</span><span class="ctitle">${esc(c.title)}</span>
        <span class="cn">${c.topics.length}</span><span class="ctags">${tags}</span></div>
      <div class="body"><div class="bodyin"><div class="topics">${topics}</div></div></div></div>`;
  });
  sec.innerHTML=h+'</div>'; root.appendChild(sec);
});

/* chips */
const tcEl=document.getElementById('typeChips');
[['C','Concept'],['X','Config'],['T','Troubleshoot'],['R','Reference']].forEach(([k,l])=>{
  const b=document.createElement('button'); b.className='chip t-'+k; b.dataset.type=k;
  b.textContent=k+' '+l; b.onclick=()=>{b.classList.toggle('on');apply();}; tcEl.appendChild(b);
});
const tgEl=document.getElementById('tagChips');
[...allTags].sort().forEach(t=>{
  const b=document.createElement('button'); b.className='chip'; b.dataset.tag=t;
  b.textContent=t; b.onclick=()=>{b.classList.toggle('on');apply();}; tgEl.appendChild(b);
});

/* interactions */
document.addEventListener('click',e=>{
  const g=e.target.closest('[data-goto]');
  if(g){ jump(g.dataset.goto); return; }
  const hit=e.target.closest('.hit');
  if(hit){ jump(hit.dataset.goto); return; }
  const lv=e.target.closest('.lv');
  if(lv){
    let v=lv.dataset.v===undefined?-1:+lv.dataset.v; v++;
    if(v>4){delete lv.dataset.v; lv.classList.remove('set'); lv.textContent='L·'; delete levels[lv.dataset.id];}
    else{lv.dataset.v=v; lv.classList.add('set'); lv.textContent='L'+v; levels[lv.dataset.id]=v;}
    lv.classList.remove('bumped'); void lv.offsetWidth; lv.classList.add('bumped'); save(); stats(); return;
  }
  const tc=e.target.closest('.tcaret:not(.ghost)');
  if(tc){ tc.closest('.topic').classList.toggle('open'); return; }
  const tr=e.target.closest('.trow');
  if(tr){ const tp=tr.closest('.topic');
    if(tp.querySelector('.subs')) tp.classList.toggle('open'); return; }
  const ch=e.target.closest('.chead');
  if(ch){ ch.parentElement.classList.toggle('open'); return; }
});
document.addEventListener('keydown',e=>{
  if((e.key==='Enter'||e.key===' ')&&e.target.closest('.chead')){
    e.preventDefault(); e.target.closest('.chead').parentElement.classList.toggle('open');
  }
  if(e.key==='/'&&document.activeElement.id!=='q'){e.preventDefault();document.getElementById('q').focus();}
  if(e.key==='Escape')clearSearch();
});

/* jump to a topic from a reference or search hit */
function jump(id){
  if(!id) return;
  const topicId = id.includes('.') ? id.split('.').slice(0,2).join('.') : null;
  clearSearch();
  const cat = document.getElementById('c-'+ (topicId? topicId.split('.')[0] : id));
  if(cat) cat.classList.add('open');
  const el = topicId ? document.getElementById('t-'+topicId) : cat;
  if(!el) return;
  if(topicId && id.split('.').length===3) el.classList.add('open');
  setTimeout(()=>{
    el.scrollIntoView({behavior:'smooth',block:'center'});
    el.classList.remove('flash'); void el.offsetWidth; el.classList.add('flash');
  },90);
}

/* search — every occurrence, with full path */
const q=document.getElementById('q'), resEl=document.getElementById('results');
let timer; q.addEventListener('input',()=>{clearTimeout(timer);timer=setTimeout(apply,120);});
function clearSearch(){ q.value=''; apply(); }

function hl(text,term){
  if(!term) return esc(text);
  const i=text.toLowerCase().indexOf(term);
  if(i<0) return esc(text);
  return esc(text.slice(0,i))+'<mark>'+esc(text.slice(i,i+term.length))+'</mark>'+esc(text.slice(i+term.length));
}

function apply(){
  const term=q.value.trim().toLowerCase();
  const types=[...document.querySelectorAll('#typeChips .chip.on')].map(c=>c.dataset.type);
  const tags=[...document.querySelectorAll('#tagChips .chip.on')].map(c=>c.dataset.tag);
  const filtering=types.length||tags.length;

  if(term){ renderResults(term,types,tags); return; }
  resEl.classList.remove('on'); resEl.innerHTML='';
  root.style.display='';

  let shown=0, any=false;
  AREAS.forEach(a=>{
    const areaEl=document.getElementById('area-'+a.from); let areaHas=false;
    a.cats.forEach(c=>{
      const catEl=document.getElementById('c-'+c.id); let catHas=false;
      c.topics.forEach(t=>{
        let ok=true;
        if(types.length && !types.includes(t.type)) ok=false;
        if(ok && tags.length && !tags.some(x=>c.tags.includes(x))) ok=false;
        const el=document.getElementById('t-'+t.id);
        el.classList.toggle('hide',!ok);
        if(ok){catHas=true;shown++;}
      });
      catEl.classList.toggle('hide',!catHas);
      if(catHas){ areaHas=true;
        if(filtering) catEl.classList.add('open');
        else if(!allOpen) catEl.classList.remove('open');
      }
    });
    areaEl.classList.toggle('hide',!areaHas);
    if(areaHas) any=true;
  });
  document.getElementById('empty').classList.toggle('hide',any);
  document.getElementById('sShown').textContent=shown;
}

function renderResults(term,types,tags){
  root.style.display='none';
  document.getElementById('empty').classList.add('hide');
  let total=0, html='';
  AREAS.forEach(a=>{
    let group='', n=0;
    a.cats.forEach(c=>{
      if(tags.length && !tags.some(x=>c.tags.includes(x))) return;
      c.topics.forEach(t=>{
        if(types.length && !types.includes(t.type)) return;
        const inT = t.name.toLowerCase().includes(term) || t.id.includes(term) || c.title.toLowerCase().includes(term);
        const subHits = t.subs.filter(s=>s.name.toLowerCase().includes(term));
        if(inT){
          n++; group+=`<div class="hit" data-goto="${t.id}" style="--c:${theme==='paper'?a.light:a.dark}">
            <div class="mid"><div class="crumb">${a.from}–${a.to} ${esc(a.title)} <b>›</b> ${c.id} ${esc(c.title)}</div>
            <div class="txt"><span style="font-family:var(--mono);font-size:11px;opacity:.6">${t.id}</span> ${hl(t.name,term)}</div></div>
            <span class="kind">topic</span><span class="ty ty-${t.type}">${t.type}</span></div>`;
        }
        subHits.forEach(s=>{
          n++; group+=`<div class="hit" data-goto="${s.id}" style="--c:${theme==='paper'?a.light:a.dark}">
            <div class="mid"><div class="crumb">${a.from}–${a.to} <b>›</b> ${c.id} ${esc(c.title)} <b>›</b> ${t.id} ${esc(t.name)}</div>
            <div class="txt"><span style="font-family:var(--mono);font-size:11px;opacity:.6">${s.id}</span> ${hl(s.name,term)}</div></div>
            <span class="kind">subtopic</span></div>`;
        });
      });
    });
    if(n){ total+=n;
      html+=`<div class="rgroup" data-area="${a.from}" style="--c:${theme==='paper'?a.light:a.dark}">
        <div class="rgtitle"><span class="anum">${a.from}–${a.to}</span><h3>${esc(a.title)}</h3><span class="n">${n}</span></div>
        ${group}</div>`;
    }
  });
  resEl.innerHTML = total
    ? `<div class="rhead">${total} match${total===1?'':'es'} for “${esc(term)}” across the index</div>`+html
    : `<div class="empty"><h3>Nothing matches “${esc(term)}”</h3><p>Try a shorter term, or clear the source filters.</p></div>`;
  resEl.classList.add('on');
  document.getElementById('sShown').textContent=total;
}

/* stats */
const COLS={paper:['#D64545','#D97A1F','#B08900','#12855C','#0C7C93'],
            ink:['#FF7B7B','#FFB067','#F0CE5A','#4ADFA6','#3FD9F0']};
function stats(){
  const v=Object.values(levels);
  document.getElementById('sRated').textContent=v.length;
  document.getElementById('sProd').textContent=v.filter(x=>x>=3).length;
  const bar=document.getElementById('lvbar'); bar.innerHTML='';
  for(let i=0;i<5;i++){
    const c=v.filter(x=>x===i).length; if(!c)continue;
    const el=document.createElement('i');
    el.style.width=(c/META.topics*100)+'%'; el.style.background=COLS[theme][i];
    el.title='L'+i+': '+c; bar.appendChild(el);
  }
}

/* expand all */
let allOpen=false;
document.getElementById('toggleAll').onclick=function(){
  allOpen=!allOpen;
  document.querySelectorAll('.cat').forEach(c=>c.classList.toggle('open',allOpen));
  this.textContent=allOpen?'Collapse':'Expand';
};
document.getElementById('themeBtn').onclick=()=>applyTheme(theme==='paper'?'ink':'paper');

/* export */
document.getElementById('exportBtn').onclick=()=>{
  let out='# Levels — Master Knowledge Index\n# id  level  topic\n\n';
  AREAS.forEach(a=>a.cats.forEach(c=>c.topics.forEach(t=>{
    if(levels[t.id]!==undefined) out+=`${t.id}  L${levels[t.id]}  ${t.name}\n`;
  })));
  if(!Object.keys(levels).length) out+='(nothing rated yet)\n';
  const b=new Blob([out],{type:'text/plain'}), u=URL.createObjectURL(b);
  const el=document.createElement('a'); el.href=u; el.download='knowledge-levels.txt'; el.click();
  URL.revokeObjectURL(u);
};

/* scrollspy */
document.querySelectorAll('.area').forEach(a=>{
  new IntersectionObserver(es=>es.forEach(e=>{
    if(e.isIntersecting){const id=e.target.dataset.area;
      document.querySelectorAll('.strand').forEach(s=>s.classList.toggle('on',s.dataset.area===id));}
  }),{rootMargin:'-12% 0px -74% 0px'}).observe(a);
});

loadState().then(()=>{
  applyTheme(theme);
  document.querySelectorAll('.lv').forEach(lv=>{
    const v=levels[lv.dataset.id];
    if(v!==undefined){lv.dataset.v=v;lv.classList.add('set');lv.textContent='L'+v;}
  });
  stats();
});
</script>
</body></html>