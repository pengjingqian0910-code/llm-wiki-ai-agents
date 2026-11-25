# Agent 的運作迴圈

> 想、做、看結果、再調整：ReAct 與環境回饋。

<!-- 每個主張固定格式：### ID／陳述／來源／引文。tools/lint_wiki.py 會檢查引文是否真的出現在 raw/ 的原文裡。 -->

### LOOP-1
陳述：ReAct 讓語言模型交錯地產生語言推理過程與文字動作。
來源：S5
引文：「ReAct enables language models to generate both verbal reasoning traces and text actions in an interleaved manner.」

### LOOP-2
陳述：在 ReAct 之前，方法通常只讓模型做其中一件事：推理，或執行任務動作。
來源：S5
引文：「Previous methods prompt language models (LM) to either generate self-conditioned reasoning traces or task-specific actions.」

### LOOP-3
陳述：ReAct 的表現優於只產生動作的模型，並和思維鏈（CoT）推理的表現相當。
來源：S5
引文：「ReAct outperforms vanilla action generation models while being competitive with chain of thought reasoning (CoT) performance.」

### LOOP-4
陳述：ReAct 論文探索讓 LLM 同時產生推理過程與任務動作。
來源：S4
引文：「In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions」

### LOOP-5
陳述：在問答與事實查核任務上，ReAct 克服了幻覺的問題。
來源：S4
引文：「Concretely, on question answering (HotpotQA) and fact verification (Fever), ReAct overcomes issues of hallucination」

### LOOP-6
陳述：Agent 在每一步都要從環境取得「真實回饋」（ground truth），用來判斷進度。
來源：S1
引文：「gain "ground truth" from the environment at each step」

### LOOP-7
陳述：Agent 可以在檢查點或遇到阻礙時暫停，等待人類回饋。
來源：S1
引文：「Agents can then pause for human feedback at checkpoints or when encountering blockers.」

### LOOP-8
陳述：迴圈裡通常也會設定停止條件。
來源：S1
引文：「it's also common to include stopping conditions」

### LOOP-9
陳述：自我反思對現實任務很重要，因為試誤不可避免。
來源：S2
引文：「It plays a crucial role in real-world tasks where trial and error are inevitable.」
