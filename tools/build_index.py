#!/usr/bin/env python3
"""節點 I：依 wiki/ 的實際內容重新產生 wiki/index.md（索引由程式產生，不手改）。"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wikilib import ROOT, load_claims, load_sources  # noqa: E402

claims, sources = load_claims(), load_sources()
lines = ["# Wiki 索引：AI Agents", "", "> 這個檔案由 tools/build_index.py 產生，請不要手動修改。", "", "## 來源（raw → wiki/sources）", ""]
for sid, m in sources.items():
    n = sum(1 for c in claims.values() if c["src"] == sid)
    lines.append(f"- [{sid}](sources/{sid}.md)　{m['title']}（{m['publisher']}）— 被 {n} 個主張引用")
lines += ["", "## 概念頁（wiki/concepts）", ""]
for page in sorted((ROOT / "wiki" / "concepts").glob("*.md")):
    first = page.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip()
    ids = [k for k, c in claims.items() if c["page"] == page.stem]
    srcs = sorted({claims[k]["src"] for k in ids})
    lines.append(f"- [{first}](concepts/{page.name})　{len(ids)} 個主張，來源 {'、'.join(srcs)}")
lines += ["", f"合計：{len(sources)} 篇來源、{len(claims)} 個主張。", "", "操作歷史見 [log.md](log.md)。", ""]
(ROOT / "wiki" / "index.md").write_text("\n".join(lines), encoding="utf-8")
print(f"已更新 wiki/index.md（{len(sources)} 篇來源、{len(claims)} 個主張）")
