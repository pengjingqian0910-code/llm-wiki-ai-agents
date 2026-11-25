# Wiki 操作紀錄

只新增、不改寫舊紀錄。格式：日期｜動作｜內容。

2026-11-25｜討論｜主題定為「AI Agents」；簡報對象是完全沒接觸過的同學，約 10 頁。決定用「先抓原文、再寫來源頁、再寫概念頁」的順序，每個主張都要附原文引文。
2026-11-25｜ingest｜S1 Anthropic《Building effective AI agents》：抓取 2 次，存入 raw/S1。
2026-11-25｜ingest｜S2 Lilian Weng《LLM Powered Autonomous Agents》：抓取 2 次，存入 raw/S2。
2026-11-25｜ingest｜S3 OpenAI《A practical guide to building agents》：抓取 1 次，存入 raw/S3。
2026-11-25｜ingest｜S4 ReAct 論文摘要（arXiv）：抓取 1 次，存入 raw/S4。工具只回傳句首。
2026-11-25｜ingest｜S5 Google Research ReAct 部落格：抓取 1 次，存入 raw/S5。
2026-11-25｜ingest｜S6 Google Cloud《What are AI agents?》：抓取 1 次，存入 raw/S6。
2026-11-25｜整理｜建立 8 個概念頁：ai-agent、workflow-vs-agent、components、agent-loop、workflow-patterns、multi-agent、when-to-use、risks-guardrails。
2026-11-25｜lint｜第一次檢查發現 3 個錯誤：WA-3 的「兩」沒有依據（改寫）；COMP-3、COMP-4 的「二」「三」是序數（改 lint 規則與用字）。
2026-11-25｜大綱｜檢查發現 s04 的「三個」「兩種」沒有依據，並移除一句沒有來源的推論。
2026-11-25｜簡報｜看截圖發現核心主張被藏在折疊區；改為直接顯示後，s05 超出 86px，改成兩欄；新增「核心主張可見」檢查。
2026-11-25｜完成｜run_pipeline.py 全部通過：6 篇來源、53 個主張、11 頁簡報。
