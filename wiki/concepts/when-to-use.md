# 什麼時候該用 Agent

> Agent 不是預設答案：先確認需要，再決定要不要做。

<!-- 每個主張固定格式：### ID／陳述／來源／引文。tools/lint_wiki.py 會檢查引文是否真的出現在 raw/ 的原文裡。 -->

### USE-1
陳述：很多應用只要把單次 LLM 呼叫搭配檢索與範例調好，通常就夠了。
來源：S1
引文：「For many applications, however, optimizing single LLM calls with retrieval and in-context examples is usually enough.」

### USE-2
陳述：Anthropic 提醒：最合適的方案，有時就是完全不做 agentic system。
來源：S1
引文：「This might mean not building agentic systems at all.」

### USE-3
陳述：OpenAI 建議：決定做 Agent 之前，先確認你的使用情境清楚符合條件。
來源：S3
引文：「Before committing to building an agent, validate that your use case can meet these criteria clearly.」

### USE-4
陳述：如果不符合條件，確定性的（寫死規則的）方案可能就足夠了。
來源：S3
引文：「Otherwise, a deterministic solution may suffice.」

### USE-5
陳述：Agent 的自主性，使它適合在可信任的環境中擴大處理任務的規模。
來源：S1
引文：「Agents' autonomy makes them ideal for scaling tasks in trusted environments.」
