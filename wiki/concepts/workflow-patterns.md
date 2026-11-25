# 五種常見的 Workflow 模式

> Anthropic 整理的五種把 LLM 串起來的做法。

<!-- 每個主張固定格式：### ID／陳述／來源／引文。tools/lint_wiki.py 會檢查引文是否真的出現在 raw/ 的原文裡。 -->

### PAT-1
陳述：提示鏈（prompt chaining）：把任務拆成一串步驟，每次 LLM 呼叫處理前一次的輸出。
來源：S1
引文：「Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one.」

### PAT-2
陳述：路由（routing）：先分類輸入，再導向專門的後續任務。
來源：S1
引文：「Routing classifies an input and directs it to a specialized followup task.」

### PAT-3
陳述：平行化（parallelization）：LLM 可以同時處理一個任務，再用程式彙整輸出。
來源：S1
引文：「LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically.」

### PAT-4
陳述：協調者—工作者（orchestrator-workers）：由一個中心 LLM 動態拆解任務、分派給工作者 LLM。
來源：S1
引文：「a central LLM dynamically breaks down tasks, delegates them to worker LLMs」

### PAT-5
陳述：評估者—優化者（evaluator-optimizer）：一個 LLM 產生回應，另一個在迴圈中給出評估與回饋。
來源：S1
引文：「In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.」
