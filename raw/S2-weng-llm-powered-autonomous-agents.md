---
id: S2
title: LLM Powered Autonomous Agents
publisher: Lil'Log
authors: Lilian Weng
published: 2023-06-23
url: https://lilianweng.github.io/posts/2023-06-23-agent/
fetched: 2026-11-25
how: WebFetch，兩次抽取。
note: 工具抽出的逐字引文集，不是整頁備份；每句最多約 125 字元。第 2 次抽取中，工具對超長句改用自己的話概述，這些概述不是原文，已標示。
---

## 第 1 次抽取（原樣保存）

- Introduction: "Building agents with LLM (large language model) as its core controller is a cool concept."
- Agent system design: "In a LLM-powered autonomous agent system, LLM functions as the agent’s brain, complemented by several key components:"
- Planning: "A complicated task usually involves many steps."
- Task decomposition: "The agent breaks down large tasks into smaller, manageable subgoals, enabling efficient handling of complex tasks."
- Tree of Thoughts (chain of thought extension): "extends CoT by exploring multiple reasoning possibilities at each step."
- Self-reflection: "It plays a crucial role in real-world tasks where trial and error are inevitable."
- Reflexion: "is a framework to equip agents with dynamic memory and self-reflection capabilities to improve reasoning skills."
- Memory: "Memory can be defined as the processes used to acquire, store, retain, and later retrieve information."
- Short-term memory: "It is short and finite, as it is restricted by the finite context window length of Transformer."
- Long-term memory: "Long-term memory as the external vector store that the agent can attend to at query time, accessible via fast retrieval."
- Tool use: "Tool use is a remarkable and distinguishing characteristic of human beings."
- Tool use (capabilities): "Equipping LLMs with external tools can significantly extend the model capabilities."
- Challenges (planning): "Planning over a lengthy history and effectively exploring the solution space remain challenging."
- Challenges (reliability): "Consequently, much of the agent demo code focuses on parsing model output."

（抽取工具附註：Tree of Thoughts 與 Reflexion 是句子片段，因為原句開頭是模型或框架名稱。）

## 第 2 次抽取（原樣保存）

(a) "In a LLM-powered autonomous agent system, LLM functions as the agent's brain, complemented by several key components:" The post describes planning, memory, and tool use as these components. Planning is quoted: "The agent breaks down large tasks into smaller, manageable subgoals, enabling efficient handling of complex tasks." Memory and tool use are paraphrased because their exact sentences exceed 125 characters. Memory lets the agent retain and recall information over long periods, often through an external vector store. Tool use lets the agent call external APIs for information the model lacks.

(b) CoT is paraphrased because the exact sentence exceeds 125 characters. The post says CoT has become a standard prompting technique for improving model performance on complex tasks by having the model "think step by step."

(c) ReAct is paraphrased because the exact sentence exceeds 125 characters. The post says ReAct combines reasoning and acting in an LLM by expanding the action space to include both task-specific actions and language.

(d) NOT FOUND as an exact sentence within the limit. The exact text, "Finite context length: The restricted context capacity limits the inclusion of historical information, detailed instructions, API call context, and responses," exceeds 125 characters. The post identifies finite context length as a challenge because the restricted context capacity limits how much history, instructions, and API context the model can include.

(e) "Consequently, much of the agent demo code focuses on parsing model output." The preceding sentence in the post, which is longer than 125 characters, says that LLM output reliability is questionable because of formatting errors and refusals to follow instructions. I've paraphrased that point.
