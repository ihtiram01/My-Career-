<!DOCTYPE html>
<html lang="en" data-theme="paper">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Course Syllabus Index — Ihtiram Ullah</title>
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

/* course-specific */
.pill{font-family:var(--mono);font-size:9px;letter-spacing:.07em;text-transform:uppercase;
  padding:3px 8px;border-radius:20px;border:1px solid;white-space:nowrap}
.st-certified{color:#0E8A5F;border-color:#0E8A5F88;background:#0E8A5F14}
.st-certified-old{color:#B08900;border-color:#B0890088;background:#B0890014}
.st-coursework{color:#C55A0C;border-color:#C55A0C88;background:#C55A0C14}
.st-planned{color:#1B57C4;border-color:#1B57C488;background:#1B57C414}
.st-not-taken{color:var(--faint);border-color:var(--line2)}
.st-self-study{color:#6E35C9;border-color:#6E35C988;background:#6E35C914}
.st-reference{color:var(--faint);border-color:var(--line2)}
.st-below-level{color:var(--faint);border-color:var(--line2)}
.st-conflict{color:#C42A36;border-color:#C42A36;background:#C42A3618;font-weight:700}
[data-theme="ink"] .st-certified{color:#4ADFA6}[data-theme="ink"] .st-certified-old{color:#F0CE5A}
[data-theme="ink"] .st-coursework{color:#FF9F58}[data-theme="ink"] .st-planned{color:#7FA8E8}
[data-theme="ink"] .st-self-study{color:#B79BE8}[data-theme="ink"] .st-conflict{color:#FF7B7B}
.note{font-size:13px;color:var(--dim);margin:9px 0 0;padding:9px 12px;border-radius:7px;
  background:var(--panel);border-left:3px solid var(--c)}
.note.warn{border-left-color:#C42A36;background:color-mix(in srgb,#C42A36 7%,var(--panel))}
.srcs{font-family:var(--mono);font-size:9px;color:var(--faint);margin-top:7px;line-height:1.7}
.vendor{font-family:var(--mono);font-size:10px;color:var(--faint)}
.mlink{font-family:var(--mono);font-size:9px;padding:2px 6px;border-radius:4px;cursor:default;
  border:1px solid var(--line2);background:var(--panel2);color:var(--dim)}
.mlink b{color:var(--c)}
.mergedtag{font-family:var(--mono);font-size:8.5px;padding:1.5px 5px;border-radius:3px;
  border:1px dashed var(--line2);color:var(--faint)}
.course{margin-top:46px;opacity:0;transform:translateY(14px);animation:rise .55s var(--ease) forwards}
.chead2{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;padding-bottom:12px;
  border-bottom:1px solid var(--line)}
.ccode{font-family:var(--mono);font-weight:700;font-size:12.5px;color:var(--c);padding:3px 8px;
  border:1px solid var(--c);border-radius:5px;background:color-mix(in srgb,var(--c) 10%,transparent)}
.cname{font-family:var(--disp);font-weight:600;font-size:clamp(16px,3vw,21px);letter-spacing:-.015em;margin:0}
.ccount{font-family:var(--mono);font-size:10.5px;color:var(--faint);margin-left:auto}
@media(max-width:640px){.ccount{width:100%;margin-left:0}.srcs{display:none}}
</style>
</head>
<body>
<div class="wrap">
<header class="hero">
  <div class="eyebrow"><span class="dot"></span> Course syllabus index <span style="opacity:.4">/</span> v1.0 <span style="opacity:.4">/</span> 2026-07-30</div>
  <h1>Course Syllabus Index<span class="thin">What each course actually covered — merged from 21 source documents</span></h1>
  <p class="lede">Four levels: <b>course → module → topic → subtopic</b>. Search returns every course a term appears in, with its full path — so “IP” surfaces in CCNA, ENCOR, Network+, AZ-104 and A+ at once. <b>→ 44</b> markers link back to the Master Knowledge Index.</p>
  <div class="figs">
    <div class="fig"><b>13</b><span>courses</span></div>
    <div class="fig"><b>69</b><span>modules</span></div>
    <div class="fig"><b>445</b><span>topics</span></div>
    <div class="fig"><b>951</b><span>subtopics</span></div>
  </div>
  <div class="strands" id="strands"></div>
</header>
<div class="bar">
  <div class="searchrow">
    <label class="search">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
      <input id="q" type="search" placeholder="Search every syllabus — ip, ospf, dhcp, raid, python…" autocomplete="off" spellcheck="false">
    </label>
    <button class="btn" id="themeBtn">Paper</button>
    <button class="btn" id="toggleAll">Expand</button>
  </div>
  <div class="chips" id="vendorChips"><span class="chiplabel">Vendor</span></div>
  <div class="chips" id="statusChips"><span class="chiplabel">Status</span></div>
  <div class="stats">
    <span class="stat"><b id="sShown">445</b> shown</span>
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
  <b>Status</b> &nbsp; certified &nbsp;·&nbsp; coursework only (exam not sat) &nbsp;·&nbsp; planned &nbsp;·&nbsp; not taken &nbsp;·&nbsp; record conflict<br>
  <b>Level</b> &nbsp; 0 heard of it &nbsp;·&nbsp; 1 can explain &nbsp;·&nbsp; 2 studied / labbed &nbsp;·&nbsp; 3 production &nbsp;·&nbsp; 4 own it<br>
  <b>→ 44</b> &nbsp; maps to that category in the Master Knowledge Index
</footer>
</div>
<script>
const D = __PAYLOAD__;
const CS = D.courses, META = D.meta;
const ESC={'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'};
const esc = s => String(s).replace(/[&<>"]/g, m => ESC[m]);
const PAL=[['#8494AB','#56697F'],['#FF7A1A','#C55A0C'],['#34D399','#0B7D55'],['#22D3EE','#0C7F99'],
           ['#4C8DFF','#1B57C4'],['#A97BFF','#6E35C9'],['#FF5A5F','#C42A36'],['#FF7AC6','#B8367F'],
           ['#F5C542','#8A6800'],['#C98B5E','#7E5129']];
const SLBL={certified:'Certified','certified-old':'Certified · older version',coursework:'Coursework only',
  planned:'Planned','not-taken':'Not taken','self-study':'Self-study',reference:'Reference',
  'below-level':'Below level',conflict:'Record conflict'};
const THEMES={paper:{label:'Paper',tc:'#2F6FD0',tx:'#0E7A54',tt:'#C2660C',tr:'#7040C4'},
              ink:{label:'Ink',tc:'#7FA8E8',tx:'#5FD6A4',tt:'#FFAE5C',tr:'#B79BE8'}};
let theme='paper', allOpen=false, levels={}; const mem={};
function applyTheme(t){
  theme=t; document.documentElement.dataset.theme=t;
  const v=THEMES[t], r=document.documentElement.style;
  r.setProperty('--tc',v.tc);r.setProperty('--tx',v.tx);r.setProperty('--tt',v.tt);r.setProperty('--tr',v.tr);
  r.setProperty('--a40', t==='paper'?'#1B57C4':'#4C8DFF');
  document.getElementById('themeBtn').textContent=v.label;
  document.querySelectorAll('[data-ci]').forEach(el=>{
    el.style.setProperty('--c', PAL[CS[+el.dataset.ci].colour][t==='paper'?1:0]);});
  try{window.storage.set('csi-theme',t);}catch(e){}
}
async function loadState(){
  try{const r=await window.storage.get('csi-levels'); if(r&&r.value) levels=JSON.parse(r.value);}catch(e){levels=mem.l||{};}
  try{const r=await window.storage.get('csi-theme'); if(r&&r.value) theme=r.value;}catch(e){}
}
async function save(){mem.l=levels; try{await window.storage.set('csi-levels',JSON.stringify(levels));}catch(e){}}

const root=document.getElementById('root'), strandsEl=document.getElementById('strands');
const vendors=new Set(), statuses=new Set();
CS.forEach((c,ci)=>{
  vendors.add(c.vendor); statuses.add(c.status);
  const s=document.createElement('button');
  s.className='strand'; s.dataset.ci=ci; s.dataset.key=c.key;
  s.innerHTML=`<em>${esc(c.code.split(/[ /]/)[0])}</em><span>${esc(c.vendor)}</span>`;
  s.title=`${esc(c.name)} — ${SLBL[c.status]}`;
  s.onclick=()=>{clearSearch();document.getElementById('c-'+c.key).scrollIntoView({behavior:'smooth',block:'start'});};
  strandsEl.appendChild(s);

  const sec=document.createElement('section');
  sec.className='course'; sec.id='c-'+c.key; sec.dataset.ci=ci;
  sec.dataset.vendor=c.vendor; sec.dataset.status=c.status;
  sec.style.animationDelay=(ci*45)+'ms';
  let h=`<div class="chead2"><span class="ccode">${esc(c.code)}</span>
    <h2 class="cname">${esc(c.name)}</h2>
    <span class="pill st-${c.status}">${SLBL[c.status]}</span>
    <span class="ccount">${c.counts.modules} modules · ${c.counts.topics} topics · ${c.counts.subs} subtopics</span></div>
    <p class="note${c.status==='conflict'?' warn':''}">${esc(c.note)}</p>
    <div class="srcs">Merged from: ${c.sources.map(esc).join(' &nbsp;·&nbsp; ')}</div>
    <div class="cats">`;
  c.modules.forEach(m=>{
    const topics=m.topics.map(t=>{
      const has=t.subs.length>0;
      const subs=t.subs.map((s,i)=>`<div class="sub" data-id="${c.key}:${t.num}.${i+1}"><span class="sid">${t.num}.${i+1}</span><span class="sname">${esc(s)}</span></div>`).join('');
      const links=(t.links||[]).map(x=>`<span class="mlink" title="Master Knowledge Index category ${x}">→<b>${x}</b></span>`).join('');
      const merged=(t.src&&t.src!=='primary')?`<span class="mergedtag">${esc(t.src)}</span>`:'';
      return `<div class="topic" id="t-${c.key}-${t.num}" data-id="${c.key}:${t.num}">
        <div class="trow">
          <svg class="tcaret${has?'':' ghost'}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="m9 6 6 6-6 6"/></svg>
          <span class="tid">${t.num}</span><span class="tname">${esc(t.title)}</span>
          ${has?`<span class="sn">${t.subs.length}</span>`:''}${merged}
          ${links?`<span class="refs">${links}</span>`:''}
          <button class="lv" data-id="${c.key}:${t.num}">L·</button>
        </div>
        ${has?`<div class="subs"><div class="subsin"><div class="sublist">${subs}</div></div></div>`:''}
      </div>`;}).join('');
    h+=`<div class="cat" id="m-${c.key}-${m.num}">
      <div class="chead" role="button" tabindex="0">
        <svg class="caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="m9 6 6 6-6 6"/></svg>
        <span class="cnum">${esc(m.num)}</span><span class="ctitle">${esc(m.title)}</span>
        <span class="cn">${m.topics.length}</span></div>
      <div class="body"><div class="bodyin"><div class="topics">${topics}</div></div></div></div>`;
  });
  sec.innerHTML=h+'</div>'; root.appendChild(sec);
});

function mkchips(id, vals, attr){
  const el=document.getElementById(id);
  [...vals].sort().forEach(v=>{
    const b=document.createElement('button'); b.className='chip'; b.dataset[attr]=v;
    b.textContent=(attr==='status'?SLBL[v]:v);
    b.onclick=()=>{b.classList.toggle('on');apply();}; el.appendChild(b);});
}
mkchips('vendorChips',vendors,'vendor'); mkchips('statusChips',statuses,'status');

document.addEventListener('click',e=>{
  const hit=e.target.closest('.hit'); if(hit){jump(hit.dataset.goto);return;}
  const lv=e.target.closest('.lv');
  if(lv){let v=lv.dataset.v===undefined?-1:+lv.dataset.v; v++;
    if(v>4){delete lv.dataset.v;lv.classList.remove('set');lv.textContent='L·';delete levels[lv.dataset.id];}
    else{lv.dataset.v=v;lv.classList.add('set');lv.textContent='L'+v;levels[lv.dataset.id]=v;}
    lv.classList.remove('bumped');void lv.offsetWidth;lv.classList.add('bumped');save();stats();return;}
  const tc=e.target.closest('.tcaret:not(.ghost)');
  if(tc){tc.closest('.topic').classList.toggle('open');return;}
  const tr=e.target.closest('.trow');
  if(tr){const tp=tr.closest('.topic'); if(tp.querySelector('.subs'))tp.classList.toggle('open');return;}
  const ch=e.target.closest('.chead'); if(ch){ch.parentElement.classList.toggle('open');return;}
});
document.addEventListener('keydown',e=>{
  if((e.key==='Enter'||e.key===' ')&&e.target.closest('.chead')){e.preventDefault();e.target.closest('.chead').parentElement.classList.toggle('open');}
  if(e.key==='/'&&document.activeElement.id!=='q'){e.preventDefault();document.getElementById('q').focus();}
  if(e.key==='Escape')clearSearch();
});
function jump(id){
  if(!id)return;
  const [key,num]=id.split(':'); const base=num.split('.').slice(0,2).join('.');
  clearSearch();
  const t=document.getElementById('t-'+key+'-'+base) || document.getElementById('t-'+key+'-'+num);
  const cat=t?t.closest('.cat'):null; if(cat)cat.classList.add('open');
  if(!t)return;
  if(num.split('.').length>base.split('.').length) t.classList.add('open');
  setTimeout(()=>{t.scrollIntoView({behavior:'smooth',block:'center'});
    t.classList.remove('flash');void t.offsetWidth;t.classList.add('flash');},90);
}
const q=document.getElementById('q'), resEl=document.getElementById('results');
let timer; q.addEventListener('input',()=>{clearTimeout(timer);timer=setTimeout(apply,120);});
function clearSearch(){q.value='';apply();}
function hl(text,term){
  if(!term)return esc(text);
  const i=text.toLowerCase().indexOf(term);
  if(i<0)return esc(text);
  return esc(text.slice(0,i))+'<mark>'+esc(text.slice(i,i+term.length))+'</mark>'+esc(text.slice(i+term.length));
}
function apply(){
  const term=q.value.trim().toLowerCase();
  const vs=[...document.querySelectorAll('#vendorChips .chip.on')].map(c=>c.dataset.vendor);
  const ss=[...document.querySelectorAll('#statusChips .chip.on')].map(c=>c.dataset.status);
  if(term){renderResults(term,vs,ss);return;}
  resEl.classList.remove('on');resEl.innerHTML='';root.style.display='';
  let shown=0,any=false;
  CS.forEach(c=>{
    const sec=document.getElementById('c-'+c.key);
    const ok=(!vs.length||vs.includes(c.vendor))&&(!ss.length||ss.includes(c.status));
    sec.classList.toggle('hide',!ok);
    if(ok){any=true;shown+=c.counts.topics;
      sec.querySelectorAll('.cat').forEach(cat=>{if(!allOpen&&!vs.length&&!ss.length)cat.classList.remove('open');});}
  });
  document.getElementById('empty').classList.toggle('hide',any);
  document.getElementById('sShown').textContent=shown;
}
function renderResults(term,vs,ss){
  root.style.display='none';document.getElementById('empty').classList.add('hide');
  let total=0,html='';
  CS.forEach((c,ci)=>{
    if(vs.length&&!vs.includes(c.vendor))return;
    if(ss.length&&!ss.includes(c.status))return;
    const col=PAL[c.colour][theme==='paper'?1:0];
    let g='',n=0;
    c.modules.forEach(m=>{
      m.topics.forEach(t=>{
        if(t.title.toLowerCase().includes(term)||m.title.toLowerCase().includes(term)){
          n++;g+=`<div class="hit" data-goto="${c.key}:${t.num}" style="--c:${col}">
            <div class="mid"><div class="crumb">${esc(c.code)} <b>›</b> ${esc(m.num)} ${esc(m.title)}</div>
            <div class="txt"><span style="font-family:var(--mono);font-size:11px;opacity:.6">${t.num}</span> ${hl(t.title,term)}</div></div>
            <span class="kind">topic</span></div>`;}
        t.subs.forEach((s,i)=>{
          if(!s.toLowerCase().includes(term))return;
          n++;g+=`<div class="hit" data-goto="${c.key}:${t.num}.${i+1}" style="--c:${col}">
            <div class="mid"><div class="crumb">${esc(c.code)} <b>›</b> ${esc(m.title)} <b>›</b> ${t.num} ${esc(t.title)}</div>
            <div class="txt"><span style="font-family:var(--mono);font-size:11px;opacity:.6">${t.num}.${i+1}</span> ${hl(s,term)}</div></div>
            <span class="kind">subtopic</span></div>`;});
      });});
    if(n){total+=n;
      html+=`<div class="rgroup" style="--c:${col}"><div class="rgtitle">
        <span class="anum">${esc(c.code)}</span><h3>${esc(c.name.split('—')[0].trim())}</h3>
        <span class="pill st-${c.status}">${SLBL[c.status]}</span><span class="n">${n}</span></div>${g}</div>`;}
  });
  resEl.innerHTML = total
    ? `<div class="rhead">${total} match${total===1?'':'es'} for &ldquo;${esc(term)}&rdquo; across ${resEl.dataset.n=html.split('rgroup').length-1} course${(html.split('rgroup').length-1)===1?'':'s'}</div>`+html
    : `<div class="empty"><h3>Nothing matches &ldquo;${esc(term)}&rdquo;</h3><p>Try a shorter term, or clear the filters.</p></div>`;
  resEl.classList.add('on');
  document.getElementById('sShown').textContent=total;
}
const COLS={paper:['#D64545','#D97A1F','#B08900','#12855C','#0C7C93'],
            ink:['#FF7B7B','#FFB067','#F0CE5A','#4ADFA6','#3FD9F0']};
function stats(){
  const v=Object.values(levels);
  document.getElementById('sRated').textContent=v.length;
  document.getElementById('sProd').textContent=v.filter(x=>x>=3).length;
  const bar=document.getElementById('lvbar');bar.innerHTML='';
  for(let i=0;i<5;i++){const c=v.filter(x=>x===i).length;if(!c)continue;
    const el=document.createElement('i');el.style.width=(c/META.topics*100)+'%';
    el.style.background=COLS[theme][i];el.title='L'+i+': '+c;bar.appendChild(el);}
}
document.getElementById('toggleAll').onclick=function(){
  allOpen=!allOpen;
  document.querySelectorAll('.cat').forEach(c=>c.classList.toggle('open',allOpen));
  this.textContent=allOpen?'Collapse':'Expand';};
document.getElementById('themeBtn').onclick=()=>applyTheme(theme==='paper'?'ink':'paper');
document.getElementById('exportBtn').onclick=()=>{
  let out='# Levels — Course Syllabus Index\n# course  id  level  topic\n\n';
  CS.forEach(c=>c.modules.forEach(m=>m.topics.forEach(t=>{
    const k=c.key+':'+t.num;
    if(levels[k]!==undefined)out+=`${c.code}  ${t.num}  L${levels[k]}  ${t.title}\n`;})));
  if(!Object.keys(levels).length)out+='(nothing rated yet)\n';
  const b=new Blob([out],{type:'text/plain'}),u=URL.createObjectURL(b);
  const a=document.createElement('a');a.href=u;a.download='course-levels.txt';a.click();URL.revokeObjectURL(u);};
document.querySelectorAll('.course').forEach(sec=>{
  new IntersectionObserver(es=>es.forEach(e=>{
    if(e.isIntersecting){const ci=e.target.dataset.ci;
      document.querySelectorAll('.strand').forEach(s=>s.classList.toggle('on',s.dataset.ci===ci));}
  }),{rootMargin:'-12% 0px -74% 0px'}).observe(sec);});
loadState().then(()=>{
  applyTheme(theme);
  document.querySelectorAll('.lv').forEach(lv=>{const v=levels[lv.dataset.id];
    if(v!==undefined){lv.dataset.v=v;lv.classList.add('set');lv.textContent='L'+v;}});
  stats();});
</script>
</body></html>