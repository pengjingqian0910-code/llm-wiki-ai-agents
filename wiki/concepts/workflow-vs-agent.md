# Workflow 與 Agent 的差別

> Anthropic 對「預先寫好流程」和「讓模型自己決定流程」的區分。

<!-- 每個主張固定格式：### ID／陳述／來源／引文。tools/lint_wiki.py 會檢查引文是否真的出現在 raw/ 的原文裡。 -->

### WA-1
陳述：Workflow 是用預先寫好的程式路徑，把 LLM 和工具串起來的系統。
來源：S1
引文：「Workflows are systems where LLMs and tools are orchestrated through predefined code paths.」

### WA-2
陳述：Agent 則是由 LLM 動態決定自己的流程與工具使用方式的系統。
來源：S1
引文：「Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage」

### WA-3
陳述：Anthropic 把這些不同的做法統稱為 agentic systems。
來源：S1
引文：「we categorize all these variations as agentic systems」

### WA-4
陳述：Agent 通常只是 LLM 在迴圈裡，根據環境回饋來使用工具。
來源：S1
引文：「They are typically just LLMs using tools based on environmental feedback in a loop.」

### WA-5
陳述：Agent 從使用者的指令或互動討論開始工作。
來源：S1
引文：「Agents begin their work with either a command from, or interactive discussion with, the human user.」
