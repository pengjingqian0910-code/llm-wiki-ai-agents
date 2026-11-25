# CLAUDE.md：AI Agents LLM Wiki 與教學簡報

AI 在這個專案做任何事之前，請先讀完。

## 目的
用 6 篇公開來源建立「AI Agents」的 LLM Wiki，再用 Wiki 當唯一知識來源，產生給零基礎同學看的教學 HTML 簡報。

## 結構
```
raw/              原文引文集（原樣保存，不改）。檔名 S<編號>-<名稱>.md，檔頭有 id/title/url/fetched
wiki/sources/     每篇來源一頁：摘要與「讀的時候要注意」
wiki/concepts/    概念頁：每個主張固定四行（見下）
wiki/index.md     索引，由 tools/build_index.py 產生，不手改
wiki/log.md       操作紀錄，只新增、不改寫舊紀錄
slides/slides.json  簡報大綱（只引用主張編號）
slides/index.html   成品，由 tools/build_slides.py 產生，不手改
tools/            lint_wiki.py、build_index.py、check_slides.py、build_slides.py、run_pipeline.py
```

## 主張的固定格式（概念頁）
```
### AGENT-1
陳述：中文陳述，只說引文支持的內容。
來源：S3
引文：「原文逐字句子」
```

## 規則
1. 沒有原文引文的內容，不可以進 Wiki，也不可以進簡報。
2. 引文必須逐字出現在對應 `raw/S?-*.md` 的原文裡，不可以改字、不可以含 `...`（被截斷的句子只引用完整出現的那一段）。
3. 抽取工具「用自己的話」的概述不是原文，不可以當引文。
4. 陳述裡的數字、數量，必須是引文裡有的；自己數出來的數量要在引文裡找得到依據。
5. 新增來源：存 `raw/`、寫 `wiki/sources/`、整理進概念頁、在 `wiki/log.md` 加一行。
6. 簡報的要點與原文由程式從 Wiki 填入。大綱裡只有 lead、plain（白話補充）、label 可以自己寫，而且：不可以出現沒有依據的數字，不可以寫成來源說的話；白話補充在畫面上標明「不是來源」。
7. 簡報只能用 Wiki 的主張；每頁至少綁一個主張（標題頁、來源頁除外）。
8. 簡報要放進 1280×720 不捲動，手機寬度（390px）不橫向溢出；除了 Google Fonts，不載入外部資源。
9. 核心主張（卡片、欄位、步驟）不可以只藏在折疊區。

## 流程與完成的定義
修改後執行 `python tools/run_pipeline.py`，五關（L、I、O、G、H）全部通過才算完成；再用瀏覽器看一眼截圖。任何一關失敗，依訊息回到對應節點修，不要略過檢查。

## 不要做的事
- 不要手改 `wiki/index.md`、`slides/index.html`。
- 不要改 `raw/` 的內容。
- 不要編造來源、引文、數字或網址。
- 不要在簡報裡加入 Wiki 沒有的新知識；需要的話，先走「新增來源」流程。
