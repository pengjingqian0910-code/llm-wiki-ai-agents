#!/usr/bin/env python3
"""Wiki 檢查（節點 L）：每個主張都要有出處，而且引文要真的出現在原文裡。

用法：python tools/lint_wiki.py
有錯誤時結束碼為 1。警告不影響結束碼，但要看。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
CONCEPTS = ROOT / "wiki" / "concepts"
SOURCES = ROOT / "wiki" / "sources"

# 抽取工具自己的概述不是原文，這些標記之後的文字不能當引文來源
NOT_QUOTE_MARKERS = ["（以下是抽取工具自己的概述"]

NUM_WORDS = {"2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
ZH_NUM = {"二": "2", "兩": "2", "三": "3", "四": "4", "五": "5", "六": "6", "七": "7", "八": "8", "九": "9"}

errors, warnings = [], []


def norm(s: str) -> str:
    s = (s.replace("’", "'").replace("‘", "'")
          .replace("“", '"').replace("”", '"'))
    return re.sub(r"\s+", " ", s).strip()


def load_raw():
    raws = {}
    for p in sorted(RAW.glob("S*.md")):
        text = p.read_text(encoding="utf-8")
        m = re.match(r"S\d+", p.name)
        sid = m.group(0)
        for mk in NOT_QUOTE_MARKERS:
            if mk in text:
                text = text.split(mk)[0]
        # 去掉 front matter，只比對正文
        body = text.split("---", 2)[-1] if text.startswith("---") else text
        raws[sid] = norm(body)
    return raws


def parse_claims(path):
    text = path.read_text(encoding="utf-8")
    claims = []
    for block in re.split(r"(?m)^### ", text)[1:]:
        lines = block.strip().splitlines()
        cid = lines[0].strip()
        fields = {}
        for ln in lines[1:]:
            m = re.match(r"(陳述|來源|引文)：(.*)", ln)
            if m:
                fields[m.group(1)] = m.group(2).strip()
        claims.append((cid, fields, path.name))
    return claims


def main():
    raws = load_raw()
    if len(raws) < 5:
        errors.append(f"raw/ 只有 {len(raws)} 篇來源，作業要求至少 5 篇")

    seen, cited = {}, {}
    page_sources = {}
    for page in sorted(CONCEPTS.glob("*.md")):
        for cid, f, fname in parse_claims(page):
            where = f"{fname} {cid}"
            if cid in seen:
                errors.append(f"{where}: ID 重複（也出現在 {seen[cid]}）")
            seen[cid] = fname
            for k in ("陳述", "來源", "引文"):
                if k not in f or not f[k]:
                    errors.append(f"{where}: 缺少「{k}」")
            if not all(k in f for k in ("陳述", "來源", "引文")):
                continue
            sid = f["來源"]
            if sid not in raws:
                errors.append(f"{where}: 來源 {sid} 沒有對應的 raw 檔")
                continue
            cited.setdefault(sid, []).append(cid)
            page_sources.setdefault(fname, set()).add(sid)

            m = re.fullmatch(r"「(.+)」", f["引文"])
            if not m:
                errors.append(f"{where}: 引文要用「」包住")
                continue
            quote = m.group(1)
            if "..." in quote or "…" in quote:
                errors.append(f"{where}: 引文含省略號，代表是被截斷的，請只引用完整出現的片段")
            if norm(quote) not in raws[sid]:
                errors.append(f"{where}: 引文沒有出現在 {sid} 的原文裡 → {quote[:60]}")
            if len(quote.split()) < 4:
                warnings.append(f"{where}: 引文太短（{len(quote.split())} 字），容易脫離上下文")

            # 陳述裡的數字，必須在引文裡找得到（避免憑空出現數字）
            stmt = re.sub(r"第[一二三四五六七八九十\d]+", "", f["陳述"])   # 「第二個」是序數，不是數量
            stmt_nums = set(re.findall(r"\d+", stmt)) | {ZH_NUM[c] for c in stmt if c in ZH_NUM}
            q = norm(quote).lower()
            for n in stmt_nums:
                if n not in q and NUM_WORDS.get(n, "~~") not in q:
                    errors.append(f"{where}: 陳述出現數字 {n}，但引文裡沒有")

    for sid in raws:
        if sid not in cited:
            warnings.append(f"{sid} 沒有被任何主張引用")
    for page, srcs in page_sources.items():
        if len(srcs) < 2:
            warnings.append(f"{page} 只有一個來源（{sorted(srcs)}），沒有交叉驗證")

    for sp in SOURCES.glob("S*.md"):
        if not re.match(r"S\d+", sp.name) or sp.stem not in raws:
            errors.append(f"wiki/sources/{sp.name} 沒有對應的 raw 檔")

    log = ROOT / "wiki" / "log.md"
    if not log.exists():
        errors.append("缺少 wiki/log.md")

    for w in warnings:
        print("警告：", w)
    if errors:
        print(f"\n發現 {len(errors)} 個錯誤：")
        for e in errors:
            print("  -", e)
        return 1
    print(f"OK：{len(raws)} 篇來源、{len(seen)} 個主張，引文全部在原文中找到。（警告 {len(warnings)} 個）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
