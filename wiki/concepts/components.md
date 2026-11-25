# Agent 的組成元件

> 兩種常見的拆法：OpenAI 的三元件，以及 Weng 的規劃、記憶、工具。

<!-- 每個主張固定格式：### ID／陳述／來源／引文。tools/lint_wiki.py 會檢查引文是否真的出現在 raw/ 的原文裡。 -->

### COMP-1
陳述：OpenAI 指出，最基本的 Agent 由三個核心元件組成。
來源：S3
引文：「In its most fundamental form, an agent consists of three core components:」

### COMP-2
陳述：第一個元件是模型：負責 Agent 的推理與決策。
來源：S3
引文：「The LLM powering the agent’s reasoning and decision-making」

### COMP-3
陳述：第二個元件是工具：Agent 用來採取行動的外部函式或 API。
來源：S3
引文：「External functions or APIs the agent can use to take action」

### COMP-4
陳述：第三個元件是指令：明確規範 Agent 行為的準則與護欄。
來源：S3
引文：「Explicit guidelines and guardrails defining how the agent behaves」

### COMP-5
陳述：Anthropic 的基本積木是「加強版 LLM」：LLM 加上檢索、工具與記憶。
來源：S1
引文：「The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory.」

### COMP-6
陳述：規劃：Agent 把大任務拆成較小、可處理的子目標。
來源：S2
引文：「The agent breaks down large tasks into smaller, manageable subgoals, enabling efficient handling of complex tasks.」

### COMP-7
陳述：短期記憶很短而且有限，因為受到 Transformer 上下文視窗長度的限制。
來源：S2
引文：「It is short and finite, as it is restricted by the finite context window length of Transformer.」

### COMP-8
陳述：長期記憶是 Agent 查詢時可以取用的外部向量資料庫，能快速檢索。
來源：S2
引文：「Long-term memory as the external vector store that the agent can attend to at query time, accessible via fast retrieval.」

### COMP-9
陳述：替 LLM 配上外部工具，可以大幅擴充模型的能力。
來源：S2
引文：「Equipping LLMs with external tools can significantly extend the model capabilities.」

### COMP-10
陳述：每個 Agent 都要定義自己的角色、說話風格，並附上指令與可用工具的描述。
來源：S6
引文：「Every agent defines its role, personality, and communication style, including specific instructions and descriptions of available tools.」
