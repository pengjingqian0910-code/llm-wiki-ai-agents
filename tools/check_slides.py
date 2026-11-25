#!/usr/bin/env python3
"""簡報檢查。分兩關：
  1. 大綱檢查（節點 O）：產生 HTML 之前，先檢查 slides.json 有沒有對上 Wiki。
  2. 成品檢查（節點 H）：用瀏覽器實際打開 slides/index.html 檢查。

用法：
  python tools/check_slides.py          # 兩關都跑
  python tools/check_slides.py --outline  # 只跑第 1 關（不需要先產生 HTML）
有錯誤時結束碼為 1。
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wikilib import ROOT, CONCEPTS, load_claims  # noqa: E402

CLAIMS = load_claims()
errors = []
KNOWN_LAYOUTS = {"title", "cards", "twocol", "loop", "quiz", "sources"}
ZH_NUM = {"二": 2, "兩": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9, "十": 10}
EN_NUM = {2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}


def err(where, msg):
    errors.append(f"{where}: {msg}")


def slide_ids(s):
    ids = [c["claim"] for c in s.get("cards", [])]
    for col in s.get("cols", []):
        ids += col["claims"]
    ids += [st["claim"] for st in s.get("steps", []) if st.get("claim")]
    ids += s.get("guards", []) + s.get("claims_extra", [])
    for it in s.get("items", []):
        ids += it["claims"]
    return ids


def group_count(s):
    """這一頁「並列的項目」有幾個：卡片數、欄數、步驟數。數量詞可以對到它。"""
    return {len(s.get("cards", [])), len(s.get("cols", [])), len(s.get("steps", [])), len(s.get("guards", []))} - {0}


def outline_check(spec):
    slides = spec["slides"]
    if not 8 <= len(slides) <= 14:
        err("大綱", f"共 {len(slides)} 頁，應在 8 到 14 頁之間")
    seen_ids = set()
    used_pages = set()
    for s in slides:
        sid = s.get("id", "?")
        if sid in seen_ids:
            err(sid, "頁面 id 重複")
        seen_ids.add(sid)
        if s.get("layout") not in KNOWN_LAYOUTS:
            err(sid, f"未知的 layout：{s.get('layout')}")
        ids = slide_ids(s)
        for c in ids:
            if c not in CLAIMS:
                err(sid, f"引用了不存在的主張 {c}")
        if s.get("layout") not in ("title", "sources") and not ids:
            err(sid, "內容頁沒有綁定任何 Wiki 主張")
        used_pages |= {CLAIMS[c]["page"] for c in ids if c in CLAIMS}

        # 導讀文字（標題、lead、plain、問題、標籤）裡的數量詞，必須有依據
        texts = [s.get("title", ""), s.get("lead", ""), s.get("plain", "")]
        texts += [c["label"] for c in s.get("cards", [])] + [i["q"] for i in s.get("items", [])]
        texts += [c["heading"] for c in s.get("cols", [])]
        text = " ".join(texts)
        text = re.sub(r"[（(][一二三四五六七八九十]+[）)]", "", text)      # 「（一）」「（二）」是編號
        text = re.sub(r"第[一二三四五六七八九十\d]+", "", text)             # 序數
        text = re.sub(r"[一二三四五六七八九十]+位|[\d]+ 分鐘", "", text) if s.get("layout") == "title" else text
        evidence = " ".join(CLAIMS[c]["stmt"] + " " + CLAIMS[c]["quote"] for c in ids if c in CLAIMS).lower()
        nums = [int(n) for n in re.findall(r"\d+", text)] + [ZH_NUM[c] for c in text if c in ZH_NUM and c != "十"]
        for n in nums:
            in_claims = str(n) in evidence or EN_NUM.get(n, "~") in evidence
            if not in_claims and n not in group_count(s):
                err(sid, f"導讀文字出現數量「{n}」，但本頁的主張裡沒有，也不等於本頁並列的項目數 {sorted(group_count(s))}")

    all_pages = {p.stem for p in CONCEPTS.glob("*.md")}
    for p in sorted(all_pages - used_pages):
        err("大綱", f"Wiki 概念頁 {p} 沒有出現在任何一頁簡報")


def html_check():
    from playwright.sync_api import sync_playwright

    path = ROOT / "slides" / "index.html"
    if not path.exists():
        err("HTML", "slides/index.html 不存在，請先跑 build_slides.py")
        return
    spec = json.loads((ROOT / "slides" / "slides.json").read_text(encoding="utf-8"))
    n = len(spec["slides"])
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": 1280, "height": 720})
        page = ctx.new_page()
        js_errors, bad_requests = [], []
        page.on("pageerror", lambda e: js_errors.append(str(e)))
        page.on("request", lambda r: bad_requests.append(r.url) if not re.match(r"^(file:|data:|https://fonts\.(googleapis|gstatic)\.com)", r.url) else None)
        page.goto(path.as_uri())
        page.wait_for_selector(".slide.on")
        if js_errors:
            err("HTML", f"JS 錯誤：{js_errors}")
        if bad_requests:
            err("HTML", f"載入了不允許的外部資源：{bad_requests}")
        if page.locator(".slide").count() != n:
            err("HTML", f"頁數 {page.locator('.slide').count()} 不等於大綱的 {n}")

        # 引文與主張內容必須和 Wiki 一模一樣
        for el in page.locator("[data-quote-of]").all():
            cid = el.get_attribute("data-quote-of")
            if el.text_content().strip() != CLAIMS[cid]["quote"]:
                err("HTML", f"{cid} 的原文引文和 Wiki 不一致")
        for el in page.locator("[data-claim]").all():
            cid = el.get_attribute("data-claim")
            if CLAIMS[cid]["stmt"] not in el.locator(".stmt").text_content():
                err("HTML", f"{cid} 的陳述和 Wiki 不一致")

        # 核心主張必須「直接看得到」：卡片、欄位、步驟、出口裡的主張，不可以只出現在「補充主張」折疊區
        for s in spec["slides"]:
            core = [c["claim"] for c in s.get("cards", [])] + [c for col in s.get("cols", []) for c in col["claims"]]
            core += [st["claim"] for st in s.get("steps", []) if st.get("claim")] + s.get("guards", [])
            for cid in dict.fromkeys(core):
                visible = page.locator(f"#{s['id']} .claim[data-claim='{cid}']:not(details.more .claim)").count()
                if visible == 0:
                    err(s["id"], f"核心主張 {cid} 沒有直接顯示（只藏在折疊區或根本沒畫出來）")

        # 鍵盤操作：往右走到最後一頁、再往左回到第一頁
        page.keyboard.press("Home")
        for _ in range(n - 1):
            page.keyboard.press("ArrowRight")
        if page.locator("#count").text_content().strip() != f"{n} / {n}":
            err("HTML", f"按 {n - 1} 次 → 後沒有停在最後一頁：{page.locator('#count').text_content()}")
        for _ in range(n - 1):
            page.keyboard.press("ArrowLeft")
        if page.locator("#count").text_content().strip() != f"1 / {n}":
            err("HTML", "按 ← 沒有回到第一頁")

        # 桌面尺寸：每一頁都要在不捲動的情況下放得進畫面（原文收合時）
        for i in range(n):
            page.keyboard.press("Home")
            for _ in range(i):
                page.keyboard.press("ArrowRight")
            m = page.evaluate("""() => { const s = document.querySelector('.slide.on');
                return {id: s.id, sh: s.scrollHeight, ch: s.clientHeight, sw: s.scrollWidth, cw: s.clientWidth}; }""")
            if m["sh"] > m["ch"] + 1:
                err(m["id"], f"1280×720 放不下：內容高 {m['sh']}px，可視高 {m['ch']}px（超出 {m['sh'] - m['ch']}px）")
            if m["sw"] > m["cw"] + 1:
                err(m["id"], "1280×720 出現橫向溢出")

        # 手機尺寸：不可以橫向溢出（允許垂直捲動）
        mp = b.new_context(viewport={"width": 390, "height": 800}).new_page()
        mp.goto(path.as_uri())
        mp.wait_for_selector(".slide.on")
        for i in range(n):
            mp.keyboard.press("Home")
            for _ in range(i):
                mp.keyboard.press("ArrowRight")
            m = mp.evaluate("""() => { const s = document.querySelector('.slide.on');
                return {id: s.id, sw: s.scrollWidth, cw: s.clientWidth}; }""")
            if m["sw"] > m["cw"] + 1:
                err(m["id"], f"390px 手機寬度橫向溢出（{m['sw']} > {m['cw']}）")
        b.close()


def main():
    spec = json.loads((ROOT / "slides" / "slides.json").read_text(encoding="utf-8"))
    outline_check(spec)
    stage = "大綱"
    if "--outline" not in sys.argv and not errors:
        html_check()
        stage = "大綱＋成品"
    if errors:
        print(f"發現 {len(errors)} 個問題（{stage}檢查）：")
        for e in errors:
            print("  -", e)
        return 1
    print(f"OK：{stage}檢查全部通過")
    return 0


if __name__ == "__main__":
    sys.exit(main())
