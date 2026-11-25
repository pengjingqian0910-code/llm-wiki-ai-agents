#!/usr/bin/env python3
"""節點 G：依 slides/slides.json（大綱）和 wiki 主張，產生單一檔案的 slides/index.html。

簡報裡的「要點」和「原文引文」一律從 Wiki 讀出來，不手打，所以不可能和 Wiki 不一致。
大綱裡只有 lead / plain / label 這些導讀文字是人寫的，由 check_slides.py 另外檢查。
"""
import html
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wikilib import ROOT, load_claims, load_sources  # noqa: E402

E = html.escape
CLAIMS = load_claims()
SOURCES = load_sources()


def claim_li(cid, with_label=None):
    c = CLAIMS[cid]
    label = f'<strong class="lbl">{E(with_label)}</strong>' if with_label else ""
    return (
        f'<div class="claim" data-claim="{cid}">{label}'
        f'<p class="stmt">{E(c["stmt"])} <span class="src">{c["src"]}</span></p>'
        f'<details><summary>原文</summary><blockquote data-quote-of="{cid}">{E(c["quote"])}</blockquote></details></div>'
    )


def footer_refs(ids):
    seen = []
    for i in ids:
        if i not in seen:
            seen.append(i)
    return "Wiki：" + "、".join(f"{CLAIMS[i]['page']}#{i}" for i in seen)


def all_ids(s):
    ids = []
    for c in s.get("cards", []):
        ids.append(c["claim"])
    for col in s.get("cols", []):
        ids += col["claims"]
    for st in s.get("steps", []):
        if st.get("claim"):
            ids.append(st["claim"])
    ids += s.get("guards", []) + s.get("claims_extra", [])
    for it in s.get("items", []):
        ids += it["claims"]
    return ids


def render_slide(s, n, total):
    ids = all_ids(s)
    lay = s["layout"]
    body = ""
    head = f'<h2>{E(s["title"])}</h2>' + (f'<p class="lead">{E(s["lead"])}</p>' if s.get("lead") else "")

    if lay == "title":
        return (
            f'<section class="slide title-slide" id="{s["id"]}" data-layout="title"><div class="inner">'
            f'<p class="kicker">LLM Wiki × 教學簡報</p><h1>{E(s["title"])}</h1>'
            f'<p class="sub">{E(s["subtitle"])}</p><p class="meta">{E(s["meta"])}</p></div></section>'
        )

    if lay == "cards":
        cards = "".join(f'<div class="card">{claim_li(c["claim"], c["label"])}</div>' for c in s["cards"])
        body = f'<div class="cards n{len(s["cards"])}">{cards}</div>'
    elif lay == "twocol":
        cols = ""
        for col in s["cols"]:
            cols += f'<div class="col"><h3>{E(col["heading"])}</h3>' + "".join(claim_li(c) for c in col["claims"]) + "</div>"
        body = f'<div class="twocol">{cols}</div>'
    elif lay == "loop":
        nodes = []
        for i, st in enumerate(s["steps"]):
            nodes.append(f'<div class="node"><span class="no">{i + 1}</span>{E(st["label"])}</div>')
            if i < len(s["steps"]) - 1:
                nodes.append('<div class="arrow" aria-hidden="true">→</div>')
        back = '<div class="back" aria-hidden="true">↺ 根據回饋，再回到「推理」，直到結束</div>'
        guards = "".join(claim_li(g) for g in s["guards"])
        step_claims, shown = "", []
        for st in s["steps"]:                       # 每個步驟的依據直接顯示（同一主張只顯示一次）
            if st.get("claim") and st["claim"] not in shown:
                shown.append(st["claim"])
                step_claims += claim_li(st["claim"])
        body = (
            f'<div class="loopbox"><div class="flow" role="img" aria-label="推理、行動、環境回饋的迴圈">{"".join(nodes)}</div>{back}</div>'
            f'<div class="twocol"><div class="col"><h3>迴圈在做什麼</h3>{step_claims}</div>'
            f'<div class="col"><h3>迴圈的出口</h3>{guards}</div></div>'
        )
    elif lay == "quiz":
        items = ""
        for it in s["items"]:
            ans = "".join(claim_li(c) for c in it["claims"])
            items += f'<details class="q"><summary>{E(it["q"])}</summary><div class="ans">{ans}</div></details>'
        body = f'<div class="quiz">{items}</div>'
    elif lay == "sources":
        rows = ""
        for sid, m in SOURCES.items():
            rows += (
                f'<li><span class="sid">{sid}</span><div><a href="{E(m["url"])}" target="_blank" rel="noopener noreferrer">{E(m["title"])}</a>'
                f'<span class="pub">{E(m["publisher"])}</span></div></li>'
            )
        body = f'<ol class="sources">{rows}</ol><p class="note">每個來源都存了原文引文集（raw/），簡報中的每個要點都能對回 Wiki 的主張編號。</p>'

    extra = ""
    if s.get("claims_extra"):
        extra = '<details class="more"><summary>補充主張</summary>' + "".join(claim_li(c) for c in s["claims_extra"]) + "</details>"
    plain = f'<p class="plain"><span>白話補充（我的話，不是來源）</span>{E(s["plain"])}</p>' if s.get("plain") else ""
    foot = f'<footer class="refs">{E(footer_refs(ids))}</footer>' if ids else ""
    return (
        f'<section class="slide" id="{s["id"]}" data-layout="{lay}" data-claims="{" ".join(ids)}"><div class="inner">'
        f'{head}{body}{extra}{plain}</div>{foot}</section>'
    )


CSS = r"""
:root{--bg:#EEF2EF;--paper:#FAFBFA;--ink:#1B2A24;--muted:#55655D;--line:#D3DBD6;--pine:#24493E;--amber:#D99A2B;--deep:#16302A;
--sans:"Noto Sans TC","PingFang TC","Microsoft JhengHei",sans-serif;--serif:"Noto Serif TC","Songti TC","PMingLiU",serif}
*{box-sizing:border-box}html,body{height:100%;margin:0}
body{background:var(--bg);color:var(--ink);font-family:var(--sans);line-height:1.6;overflow:hidden}
a{color:var(--pine);text-underline-offset:3px}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:3px solid var(--amber);outline-offset:2px}
.deck{position:fixed;inset:0 0 56px 0}
.slide{position:absolute;inset:0;display:none;flex-direction:column;overflow-y:auto;overflow-x:hidden;padding:0}
.slide.on{display:flex}
.inner{width:min(1100px,100%);margin:0 auto;padding:clamp(20px,4vh,44px) clamp(20px,4vw,48px) 12px;flex:1}
h1,h2,h3{font-family:var(--serif);margin:0;line-height:1.25}
h2{font-size:clamp(26px,4.2vw,40px);color:var(--pine)}
h3{font-size:19px;margin:0 0 8px;color:var(--pine)}
.lead{font-size:clamp(16px,2vw,20px);color:var(--muted);margin:8px 0 18px;max-width:46em}
.title-slide{background:var(--deep);color:#fff}
.title-slide .inner{display:flex;flex-direction:column;justify-content:center}
.title-slide h1{font-size:clamp(40px,8vw,84px);color:#fff}
.kicker{letter-spacing:.2em;color:var(--amber);font-weight:700;margin:0 0 12px}
.sub{font-size:clamp(18px,2.6vw,26px);margin:16px 0 0;max-width:34em}
.meta{margin-top:28px;color:#B9CBC3;font-size:15px}
.cards{display:grid;gap:14px;grid-template-columns:1fr}
@media(min-width:820px){.cards.n2,.cards.n4{grid-template-columns:1fr 1fr}.cards.n3{grid-template-columns:repeat(3,1fr)}.cards.n5{grid-template-columns:repeat(3,1fr)}}
.card,.col,.guards{background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:14px 16px}
.twocol{display:grid;gap:14px;grid-template-columns:1fr}@media(min-width:820px){.twocol{grid-template-columns:1fr 1fr}}
.lbl{display:block;font-family:var(--serif);color:var(--pine);font-size:18px;margin-bottom:2px}
.claim{margin:0 0 10px}.claim:last-child{margin-bottom:0}
.stmt{margin:0;font-size:16px}
.src{display:inline-block;font-size:12px;font-weight:700;background:var(--pine);color:#fff;border-radius:4px;padding:0 6px;vertical-align:1px}
details summary{cursor:pointer;color:var(--muted);font-size:14px;margin-top:2px}
blockquote{margin:6px 0 0;padding:6px 12px;border-left:4px solid var(--amber);background:#F7EBD2;font-size:14px;font-style:italic;word-break:break-word}
.more{margin-top:14px}.more .claim{margin-top:8px}
.plain{margin:16px 0 0;padding:10px 14px;border-radius:8px;background:#E6EFE8;border-left:6px solid var(--pine);font-size:16px}
.plain span{display:block;font-size:12px;color:var(--muted);font-weight:700}
.loopbox{background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:18px;margin-bottom:14px}
.flow{display:flex;flex-wrap:wrap;align-items:center;gap:10px;justify-content:center}
.node{background:var(--pine);color:#fff;border-radius:10px;padding:10px 20px;font-weight:700;font-size:20px}
.node .no{display:inline-block;width:24px;height:24px;line-height:24px;text-align:center;border-radius:50%;background:var(--amber);color:var(--ink);font-size:14px;margin-right:8px}
.arrow{font-size:26px;color:var(--pine)}
.back{text-align:center;margin-top:12px;color:var(--muted);font-size:15px}.basis{margin-top:14px;padding-top:12px;border-top:1px solid var(--line)}
.quiz details.q{background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:12px 16px;margin-bottom:10px}
.quiz summary{font-size:18px;font-weight:700;color:var(--ink)}
.ans{margin-top:10px}
.sources{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.sources li{display:flex;gap:12px;background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:10px 14px}
.sid{font-weight:800;color:#fff;background:var(--pine);border-radius:6px;padding:0 8px;height:fit-content}
.pub{display:block;color:var(--muted);font-size:14px}.note{color:var(--muted);font-size:14px;margin-top:12px}
.refs{padding:6px clamp(20px,4vw,48px) 10px;font-size:12px;color:var(--muted);width:min(1100px,100%);margin:0 auto;word-break:break-all}
.bar{position:fixed;left:0;right:0;bottom:0;height:56px;display:flex;align-items:center;gap:12px;padding:0 16px;background:var(--paper);border-top:1px solid var(--line)}
.bar button{font:inherit;border:1px solid var(--pine);background:transparent;color:var(--pine);border-radius:8px;padding:6px 14px;cursor:pointer}
.bar button:hover:not(:disabled){background:var(--pine);color:#fff}.bar button:disabled{opacity:.35;cursor:default}
.track{flex:1;height:6px;background:var(--line);border-radius:3px;overflow:hidden}.fill{height:100%;width:0;background:var(--pine);transition:width .25s}
.count{font-size:14px;color:var(--muted);min-width:4.5em;text-align:right}
@media(prefers-reduced-motion:reduce){.fill{transition:none}}
@media print{body{overflow:visible}.deck{position:static}.slide{display:flex!important;position:static;min-height:100vh;page-break-after:always}.bar{display:none}details>*{display:block!important}}
"""

JS = r"""
(function(){
  var slides=[].slice.call(document.querySelectorAll('.slide')),i=0;
  var prev=document.getElementById('prev'),next=document.getElementById('next'),fill=document.getElementById('fill'),count=document.getElementById('count');
  function go(n){
    i=Math.max(0,Math.min(slides.length-1,n));
    slides.forEach(function(s,k){s.classList.toggle('on',k===i);});
    slides[i].scrollTop=0;
    prev.disabled=i===0;next.disabled=i===slides.length-1;
    fill.style.width=((i+1)/slides.length*100)+'%';count.textContent=(i+1)+' / '+slides.length;
    try{history.replaceState(null,'','#'+(i+1));}catch(e){}
  }
  prev.addEventListener('click',function(){go(i-1);});next.addEventListener('click',function(){go(i+1);});
  document.addEventListener('keydown',function(e){
    if(e.target.closest&&e.target.closest('summary')&&(e.key===' '||e.key==='Enter'))return;
    if(e.key==='ArrowRight'||e.key==='PageDown'||e.key===' '){e.preventDefault();go(i+1);}
    else if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();go(i-1);}
    else if(e.key==='Home'){go(0);}else if(e.key==='End'){go(slides.length-1);}
  });
  var h=parseInt((location.hash||'').slice(1),10);go(isNaN(h)?0:h-1);
})();
"""


def main():
    spec = json.loads((ROOT / "slides" / "slides.json").read_text(encoding="utf-8"))
    total = len(spec["slides"])
    secs = "\n".join(render_slide(s, n + 1, total) for n, s in enumerate(spec["slides"]))
    page = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(spec["title"])}｜教學簡報</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&family=Noto+Serif+TC:wght@600;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<main class="deck" aria-label="簡報">
{secs}
</main>
<nav class="bar" aria-label="簡報控制">
<button id="prev" type="button" aria-label="上一頁">← 上一頁</button>
<div class="track" aria-hidden="true"><div class="fill" id="fill"></div></div>
<span class="count" id="count" aria-live="polite"></span>
<button id="next" type="button" aria-label="下一頁">下一頁 →</button>
</nav>
<script>{JS}</script>
</body>
</html>
"""
    out = ROOT / "slides" / "index.html"
    out.write_text(page, encoding="utf-8")
    print(f"已產生 {out.relative_to(ROOT)}：{total} 頁")


if __name__ == "__main__":
    main()
