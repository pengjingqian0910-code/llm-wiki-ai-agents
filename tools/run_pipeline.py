#!/usr/bin/env python3
"""把整條流程跑一遍，任何一關失敗就停下，並告訴你要回到哪個節點修。

節點順序：L（檢查 Wiki）→ I（更新索引）→ O（檢查大綱）→ G（產生簡報）→ H（檢查成品）
"""
import subprocess
import sys
from pathlib import Path

T = Path(__file__).resolve().parent
STEPS = [
    ("L 檢查 Wiki", [sys.executable, str(T / "lint_wiki.py")], "回到「ingest／整理概念頁」：補原文、改引文或陳述"),
    ("I 更新索引", [sys.executable, str(T / "build_index.py")], "檢查 wiki/ 的檔案格式"),
    ("O 檢查大綱", [sys.executable, str(T / "check_slides.py"), "--outline"], "回到「寫簡報大綱」：改 slides/slides.json"),
    ("G 產生簡報", [sys.executable, str(T / "build_slides.py")], "檢查 tools/build_slides.py"),
    ("H 檢查成品", [sys.executable, str(T / "check_slides.py")], "回到「寫大綱」或「產生簡報」：版面、顯示、操作問題"),
]
for name, cmd, back in STEPS:
    print(f"\n=== {name} ===")
    r = subprocess.run(cmd)
    if r.returncode != 0:
        print(f"\n✗ 停在「{name}」。→ {back}")
        sys.exit(1)
print("\n✓ 全部節點通過")
