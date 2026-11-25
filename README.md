# AI Agents：LLM Wiki 與教學 HTML 簡報

用 6 篇公開來源建立「AI Agents」LLM Wiki（53 個附原文引文的主張），再用 Wiki 產生一份給零基礎同學看的教學簡報（11 頁）。

- 簡報：`slides/index.html`（部署後：`https://<帳號>.github.io/<repository>/slides/`）
- Wiki 索引：[wiki/index.md](wiki/index.md)　操作紀錄：[wiki/log.md](wiki/log.md)
- 流程設計、執行紀錄與反思：[WORKFLOW.md](WORKFLOW.md)
- 給 AI 的專案規則：[CLAUDE.md](CLAUDE.md)

## 本機操作

```bash
python tools/run_pipeline.py    # 檢查 Wiki → 更新索引 → 檢查大綱 → 產生簡報 → 檢查成品
```

簡報檢查需要 Python 版 Playwright（`pip install playwright && playwright install chromium`）。簡報操作：← → 換頁，每個要點可以點「原文」展開引文。

## 部署到 GitHub Pages
1. 整個資料夾上傳到 GitHub repository。
2. Settings → Pages → Source 選 `main`、`/ (root)`，存檔。
3. 簡報網址是 `https://<帳號>.github.io/<repository>/slides/`。
