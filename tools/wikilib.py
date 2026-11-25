"""讀取 Wiki 的共用函式：主張（claims）與來源（sources）。"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONCEPTS = ROOT / "wiki" / "concepts"
RAW = ROOT / "raw"


def load_claims():
    """回傳 {claim_id: {stmt, src, quote, page}}，順序依頁面與出現順序。"""
    claims = {}
    for page in sorted(CONCEPTS.glob("*.md")):
        text = page.read_text(encoding="utf-8")
        for block in re.split(r"(?m)^### ", text)[1:]:
            lines = block.strip().splitlines()
            cid = lines[0].strip()
            f = {}
            for ln in lines[1:]:
                m = re.match(r"(陳述|來源|引文)：(.*)", ln)
                if m:
                    f[m.group(1)] = m.group(2).strip()
            quote = re.sub(r"^「|」$", "", f.get("引文", ""))
            claims[cid] = {"stmt": f.get("陳述", ""), "src": f.get("來源", ""), "quote": quote, "page": page.stem}
    return claims


def load_sources():
    """回傳 {S1: {title, publisher, url}}，來自 raw/ 檔頭。"""
    out = {}
    for p in sorted(RAW.glob("S*.md")):
        head = p.read_text(encoding="utf-8").split("---")[1]
        meta = {}
        for ln in head.splitlines():
            m = re.match(r"(\w+):\s*(.*)", ln)
            if m:
                meta[m.group(1)] = m.group(2).strip().strip('"')
        out[meta["id"]] = meta
    return out
