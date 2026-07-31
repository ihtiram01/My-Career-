#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Renderer for the card-shaped pages: exam tracker and field experience.

Markdown shape:

    # PAGE TITLE
    ## Group heading | meta | meta
    key: value                 <- optional, applies to the group
    ### Card title | meta | meta
    - key: value               <- becomes a labelled row
    - plain bullet             <- becomes a list item

Imported by build.py; not run directly.
"""
import re, json

STATUS_COLOUR = {
    'certified': '#0B7D55', 'passed': '#0B7D55',
    'coursework': '#C55A0C', 'record conflict': '#C42A36',
    'not started': '#1B57C4', 'gap': '#6E35C9',
    'unverified': '#C42A36', 'course completed': '#C55A0C',
}
GROUP_TONE = {  # index into the fiber palette
    'PASSED': 2, 'COURSEWORK ONLY': 1, 'NEXT': 4, 'NOT CERTIFICATIONS': 5,
}
PAL = [('#8494AB', '#56697F'), ('#FF7A1A', '#C55A0C'), ('#34D399', '#0B7D55'),
       ('#22D3EE', '#0C7F99'), ('#4C8DFF', '#1B57C4'), ('#A97BFF', '#6E35C9'),
       ('#FF5A5F', '#C42A36'), ('#FF7AC6', '#B8367F'), ('#F5C542', '#8A6800'),
       ('#C98B5E', '#7E5129')]


def parse_cards(path):
    lines = path.read_text(encoding='utf-8').split('\n')
    title, groups, grp, card = '', [], None, None
    in_fm = False

    for raw in lines:
        ln = raw.rstrip()
        if ln.strip() == '---':
            in_fm = not in_fm
            continue
        if in_fm:
            if ln.startswith('title:'):
                title = ln.split(':', 1)[1].strip()
            continue
        if not ln.strip():
            continue

        if ln.startswith('# '):
            title = title or ln[2:].strip()
            continue

        if ln.startswith('## '):
            parts = [p.strip() for p in ln[3:].split('|')]
            grp = {'title': parts[0], 'meta': parts[1:], 'info': {}, 'cards': []}
            groups.append(grp)
            card = None
            continue

        if ln.startswith('### ') and grp is not None:
            parts = [p.strip() for p in ln[4:].split('|')]
            card = {'title': parts[0], 'meta': parts[1:], 'rows': [], 'bullets': [], 'links': []}
            grp['cards'].append(card)
            continue

        m = re.match(r'^-\s+(.+)$', ln)
        if m and card is not None:
            body = m.group(1).strip()
            km = re.match(r'^(status|priority|cost|deadline|note|action|blueprint|gap|process|master)\s*:\s*(.+)$',
                          body, re.I)
            if km:
                key, val = km.group(1).lower(), km.group(2).strip()
                if key == 'master':
                    card['links'] = [x.strip() for x in val.split(',') if x.strip()]
                else:
                    card['rows'].append({'k': key, 'v': val})
            else:
                card['bullets'].append(body)
            continue

        km = re.match(r'^(role|tag|summary)\s*:\s*(.+)$', ln, re.I)
        if km and grp is not None and card is None:
            grp['info'][km.group(1).lower()] = km.group(2).strip()
            continue

    for gi, g in enumerate(groups):
        key = g['title'].split('·')[0].strip().upper()
        g['tone'] = GROUP_TONE.get(key, gi % len(PAL))
        for c in g['cards']:
            st = next((r['v'] for r in c['rows'] if r['k'] == 'status'), '')
            c['tone'] = next((v for k, v in STATUS_COLOUR.items()
                              if k in st.lower()), None)

    meta = {'title': title,
            'groups': len(groups),
            'cards': sum(len(g['cards']) for g in groups),
            'items': sum(len(c['bullets']) + len(c['rows'])
                         for g in groups for c in g['cards'])}
    return {'meta': meta, 'groups': groups}


BODY = r'''
<div class="wrap">
<header class="hero">
  <div class="tbar"><a class="btn" href="../index.html">&larr; Home</a><button class="btn" id="themeBtn">Paper</button></div>
  <div class="eyebrow"><span class="dot"></span> __KICKER__</div>
  <h1>__TITLE__<span class="thin">Ihtiram Ullah — Network &amp; IT Infrastructure Engineer</span></h1>
  <p class="lede">__LEDE__</p>
  <div class="figs">__FIGS__</div>
</header>
<div class="bar">
  <div class="searchrow">
    <label class="search">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
      <input id="q" type="search" placeholder="__PH__" autocomplete="off" spellcheck="false">
    </label>
  </div>
  <div class="chips" id="grpChips"><span class="chiplabel">Section</span></div>
  <div class="stats"><span class="stat"><b id="sShown">0</b> shown</span></div>
</div>
<main id="root"></main>
<div class="empty hide" id="empty"><h3>Nothing matches</h3><p>Clear the search or turn a section back on.</p></div>
<footer>__FOOT__</footer>
</div>
'''

EXTRA_CSS = r'''
.tbar{display:flex;justify-content:space-between;gap:8px;margin-bottom:20px}
.tbar .btn{text-decoration:none;display:inline-block}
.grp{margin-top:44px;opacity:0;transform:translateY(14px);animation:rise .55s var(--ease) forwards}
.grph{display:flex;align-items:baseline;gap:12px;padding-bottom:12px;border-bottom:1px solid var(--line);flex-wrap:wrap}
.grph h2{font-family:var(--disp);font-weight:600;font-size:clamp(16px,3vw,21px);margin:0;letter-spacing:-.015em}
.grph .gm{font-family:var(--mono);font-size:10px;color:var(--faint)}
.grph .n{font-family:var(--mono);font-size:10px;color:var(--faint);margin-left:auto}
.ginfo{font-size:13.5px;color:var(--dim);margin:11px 0 0;padding:10px 13px;border-radius:8px;
  background:var(--panel);border-left:3px solid var(--c)}
.ginfo b{color:var(--ink)}
.cardgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:13px;margin-top:15px}
.kc{background:var(--panel);border:1px solid var(--line);border-radius:11px;padding:16px 17px;
  box-shadow:var(--shadow);position:relative;overflow:hidden;transition:transform .24s var(--ease),border-color .2s}
.kc::before{content:'';position:absolute;inset:0 0 auto 0;height:3px;background:var(--kc,var(--c))}
.kc:hover{transform:translateY(-3px);border-color:var(--kc,var(--c))}
.kc h3{font-family:var(--disp);font-weight:600;font-size:15.5px;margin:5px 0 4px;letter-spacing:-.01em}
.kc .cm{font-family:var(--mono);font-size:9.5px;color:var(--faint);letter-spacing:.04em;margin-bottom:10px}
.kc .rows2{display:flex;flex-direction:column;gap:5px;margin:10px 0}
.kc .r2{display:flex;gap:9px;font-size:13px;align-items:baseline}
.kc .r2 .k{font-family:var(--mono);font-size:9px;letter-spacing:.11em;text-transform:uppercase;
  color:var(--faint);flex:none;width:64px;padding-top:2px}
.kc .r2 .v{flex:1;color:var(--dim)}
.kc .r2.status .v{color:var(--kc,var(--ink));font-weight:600}
.kc .r2.action .v,.kc .r2.deadline .v{color:#C42A36;font-weight:500}
[data-theme="ink"] .kc .r2.action .v,[data-theme="ink"] .kc .r2.deadline .v{color:#FF7B7B}
.kc ul{margin:9px 0 0;padding-left:17px}
.kc li{font-size:13.2px;color:var(--dim);margin-bottom:4px;line-height:1.5}
.kc li::marker{color:var(--kc,var(--c))}
.kc .lnk{display:flex;gap:4px;flex-wrap:wrap;margin-top:11px;padding-top:10px;border-top:1px solid var(--line)}
.kc .lnk a{font-family:var(--mono);font-size:9px;padding:2px 6px;border-radius:4px;text-decoration:none;
  border:1px solid var(--line2);background:var(--panel2);color:var(--dim);transition:all .16s}
.kc .lnk a:hover{background:var(--kc,var(--c));color:#fff;border-color:var(--kc,var(--c))}
@media(max-width:640px){.cardgrid{grid-template-columns:1fr}.kc .r2 .k{width:56px}}
'''


HOME_CSS = r"""
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:15px;margin-top:32px}
.card{display:block;text-decoration:none;color:inherit;background:var(--panel);border:1px solid var(--line);
  border-radius:12px;padding:21px;box-shadow:var(--shadow);position:relative;overflow:hidden;
  transition:transform .28s var(--ease),border-color .22s,box-shadow .28s}
.card::before{content:'';position:absolute;inset:0 0 auto 0;height:4px;background:var(--c)}
.card:hover{transform:translateY(-4px);border-color:var(--c);
  box-shadow:0 10px 30px color-mix(in srgb,var(--c) 18%,transparent)}
.card h3{font-family:var(--disp);font-weight:600;font-size:18px;margin:6px 0 6px;letter-spacing:-.015em}
.card p{color:var(--dim);font-size:13.3px;margin:0 0 15px;line-height:1.55}
.card .kicker{font-family:var(--mono);font-size:9.5px;letter-spacing:.15em;text-transform:uppercase;color:var(--c)}
.card .nums{display:flex;gap:15px;flex-wrap:wrap;font-family:var(--mono);border-top:1px solid var(--line);padding-top:12px}
.card .nums div b{display:block;font-size:16px;font-weight:700;color:var(--ink);line-height:1.2}
.card .nums div span{font-size:8.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--faint)}
.card .go{position:absolute;right:19px;bottom:19px;color:var(--c);opacity:0;transform:translateX(-6px);transition:all .28s var(--ease)}
.card:hover .go{opacity:1;transform:none}
.tbar{display:flex;justify-content:flex-end;margin-bottom:16px}
.sec{margin-top:48px}
.sech{display:flex;align-items:baseline;gap:12px;padding-bottom:12px;border-bottom:1px solid var(--line);flex-wrap:wrap}
.sech h2{font-family:var(--disp);font-weight:600;font-size:18px;margin:0;letter-spacing:-.015em}
.sech span{font-family:var(--mono);font-size:10px;color:var(--faint);margin-left:auto}
.row{display:flex;align-items:center;gap:12px;padding:12px 10px;border-bottom:1px solid var(--line);
  text-decoration:none;color:inherit;transition:padding-left .2s var(--ease),background .16s;border-radius:7px}
.row:hover{padding-left:15px;background:var(--panel)}
.row .ic{width:30px;height:30px;flex:none;display:grid;place-items:center;border-radius:7px;
  font-family:var(--mono);font-size:9px;font-weight:700;border:1px solid;
  color:#0E7A54;border-color:#0E7A5455;background:#0E7A5412}
.row .ic-f{color:#1B57C4;border-color:#1B57C455;background:#1B57C412}
.row .t{flex:1;min-width:0}
.row .t b{display:block;font-weight:500;font-size:14.3px}
.row .t span{font-family:var(--mono);font-size:10px;color:var(--faint)}
.row .sz{font-family:var(--mono);font-size:10px;color:var(--faint);flex:none}
.empt{padding:24px 14px;color:var(--faint);font-size:13.3px;border:1px dashed var(--line2);
  border-radius:9px;margin-top:12px;text-align:center;line-height:1.7}
.empt code{font-family:var(--mono);font-size:12px;color:var(--dim);background:var(--panel2);
  padding:2px 6px;border-radius:4px}
"""


CARD_JS = r'''
const D = __PAYLOAD__;
const G = D.groups;
const ESC={'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'};
const esc=s=>String(s).replace(/[&<>"]/g,m=>ESC[m]);
const PAL=[['#8494AB','#56697F'],['#FF7A1A','#C55A0C'],['#34D399','#0B7D55'],['#22D3EE','#0C7F99'],
           ['#4C8DFF','#1B57C4'],['#A97BFF','#6E35C9'],['#FF5A5F','#C42A36'],['#FF7AC6','#B8367F'],
           ['#F5C542','#8A6800'],['#C98B5E','#7E5129']];
const T={paper:{l:'Paper',tc:'#2F6FD0',tx:'#0E7A54',tt:'#C2660C',tr:'#7040C4',a:'#1B57C4'},
         ink:{l:'Ink',tc:'#7FA8E8',tx:'#5FD6A4',tt:'#FFAE5C',tr:'#B79BE8',a:'#4C8DFF'}};
let th='paper';
function ap(t){th=t;document.documentElement.dataset.theme=t;const v=T[t],r=document.documentElement.style;
  r.setProperty('--tc',v.tc);r.setProperty('--tx',v.tx);r.setProperty('--tt',v.tt);
  r.setProperty('--tr',v.tr);r.setProperty('--a40',v.a);
  document.getElementById('themeBtn').textContent=v.l;
  document.querySelectorAll('[data-tone]').forEach(el=>el.style.setProperty('--c',PAL[+el.dataset.tone][t==='paper'?1:0]));
  try{window.storage.set('kb-theme',t);}catch(e){}}
document.getElementById('themeBtn').onclick=()=>ap(th==='paper'?'ink':'paper');

const root=document.getElementById('root');
G.forEach((g,gi)=>{
  const sec=document.createElement('section');
  sec.className='grp'; sec.dataset.tone=g.tone; sec.dataset.g=gi;
  sec.style.animationDelay=(gi*55)+'ms';
  const info=g.info&&Object.keys(g.info).length
    ? `<div class="ginfo">${g.info.role?`<b>${esc(g.info.role)}</b><br>`:''}${esc(g.info.summary||'')}</div>` : '';
  const cardsHtml=g.cards.map(c=>{
    const rows=c.rows.map(r=>`<div class="r2 ${esc(r.k)}"><span class="k">${esc(r.k)}</span><span class="v">${esc(r.v)}</span></div>`).join('');
    const bl=c.bullets.length?`<ul>${c.bullets.map(b=>`<li>${esc(b)}</li>`).join('')}</ul>`:'';
    const lk=c.links.length?`<div class="lnk">${c.links.map(x=>`<a href="../knowledge/index.html" title="Master Knowledge Index category ${esc(x)}">&rarr; ${esc(x)}</a>`).join('')}</div>`:'';
    const meta=c.meta.length?`<div class="cm">${c.meta.map(esc).join(' &nbsp;&middot;&nbsp; ')}</div>`:'';
    const tone=c.tone?`style="--kc:${c.tone}"`:'';
    const hay=esc((c.title+' '+c.meta.join(' ')+' '+c.rows.map(r=>r.k+' '+r.v).join(' ')+' '+c.bullets.join(' ')).toLowerCase());
    return `<article class="kc" ${tone} data-s="${hay}"><h3>${esc(c.title)}</h3>${meta}
      <div class="rows2">${rows}</div>${bl}${lk}</article>`;}).join('');
  sec.innerHTML=`<div class="grph"><h2>${esc(g.title)}</h2>
    ${g.meta.map(x=>`<span class="gm">${esc(x)}</span>`).join('')}
    <span class="n">${g.cards.length}</span></div>${info}
    <div class="cardgrid">${cardsHtml}</div>`;
  root.appendChild(sec);
});

const chips=document.getElementById('grpChips');
G.forEach((g,gi)=>{const b=document.createElement('button');b.className='chip';b.dataset.g=gi;
  b.textContent=g.title.length>26?g.title.slice(0,24)+'\u2026':g.title;
  b.onclick=()=>{b.classList.toggle('on');apply();};chips.appendChild(b);});

const q=document.getElementById('q');
let tm;q.addEventListener('input',()=>{clearTimeout(tm);tm=setTimeout(apply,110);});
document.addEventListener('keydown',e=>{if(e.key==='Escape'){q.value='';apply();}
  if(e.key==='/'&&document.activeElement.id!=='q'){e.preventDefault();q.focus();}});
function apply(){
  const term=q.value.trim().toLowerCase();
  const on=[...document.querySelectorAll('#grpChips .chip.on')].map(c=>c.dataset.g);
  let shown=0,any=false;
  document.querySelectorAll('.grp').forEach(sec=>{
    if(on.length&&!on.includes(sec.dataset.g)){sec.classList.add('hide');return;}
    let has=false;
    sec.querySelectorAll('.kc').forEach(c=>{
      const ok=!term||c.dataset.s.includes(term);
      c.classList.toggle('hide',!ok); if(ok){has=true;shown++;}});
    sec.classList.toggle('hide',!has); if(has)any=true;});
  document.getElementById('empty').classList.toggle('hide',any);
  document.getElementById('sShown').textContent=shown;
}
(async()=>{try{const r=await window.storage.get('kb-theme');if(r&&r.value)th=r.value;}catch(e){}ap(th);apply();})();
'''
