---
id: S5
title: "ReAct: Synergizing Reasoning and Acting in Language Models"
publisher: Google Research（部落格）
published: 2022-11-08
url: https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/
fetched: 2026-11-25
how: WebFetch，一次抽取。
note: 工具抽出的逐字引文集；最後一段是工具自己的概述，不是原文。
---

## 抽取結果（原樣保存）

"Previous methods prompt language models (LM) to either generate self-conditioned reasoning traces or task-specific actions."

"We present ReAct, a simple yet effective method for synergizing reasoning and acting in language models."

"ReAct enables language models to generate both verbal reasoning traces and text actions in an interleaved manner."

"ReAct outperforms vanilla action generation models while being competitive with chain of thought reasoning (CoT) performance."

"ReAct consistently achieves best fine-tuning performances."

（以下是抽取工具自己的概述，不是原文，不可當引文使用：）
In my own words, not quoted: ReAct has a model alternate between reasoning steps and actions that get feedback from an external environment, with reasoning updating the model's own working context. Reasoning-only prompting lacks grounding in the outside world, and acting-only approaches lack abstract goal planning and working memory. The page reports that combining the two performed better than either alone on the tested question-answering and decision-making tasks.
