---
id: S1
title: Building effective AI agents
publisher: Anthropic (Engineering)
authors: Erik S., Barry Zhang
published: 2024-12-19
url: https://www.anthropic.com/engineering/building-effective-agents
fetched: 2026-11-25
how: WebFetch，兩次抽取（第 1 次：廣泛；第 2 次：補定義與模式句）。
note: 這個檔案是「工具抽出的逐字引文集」，不是整頁網頁備份。抽取工具每句最多回傳約 125 字元，較長的句子只會回傳前段或最長片段。
---

## 第 1 次抽取（原樣保存）

The page notes that much of the tooling described has changed since December 2024.

- Workflows vs. agents: "Workflows are systems where LLMs and tools are orchestrated through predefined code paths."
- Workflows vs. agents: "Agents begin their work with either a command from, or interactive discussion with, the human user."
- When to use (and not use) agents: "This might mean not building agentic systems at all."
- When to use (and not use) agents: "For many applications, however, optimizing single LLM calls with retrieval and in-context examples is usually enough."
- Augmented LLM: "The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory."
- Prompt chaining: "Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one."
- Routing: "Routing classifies an input and directs it to a specialized followup task."
- Parallelization: "LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically."
- Orchestrator-workers (excerpt): "a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results."
- Evaluator-optimizer: "This is analogous to the iterative writing process a human writer might go through when producing a polished document."
- Autonomous agents: "They are typically just LLMs using tools based on environmental feedback in a loop."
- Autonomous agents: "Agents' autonomy makes them ideal for scaling tasks in trusted environments."
- Autonomous agents: "The autonomous nature of agents means higher costs, and the potential for compounding errors."
- Simplicity and tools: "Maintain simplicity in your agent's design."
- Simplicity and frameworks: "We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code."

## 第 2 次抽取（原樣保存）

(a) Agentic systems and agents
- "we categorize all these variations as agentic systems"
- "Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage"

(b) Complexity and tradeoff
- "When more complexity is warranted"
- "Agentic systems often trade latency and cost for better task performance"

(c) Orchestrator-workers
- "a central LLM dynamically breaks down tasks, delegates them to worker LLMs"

(d) Evaluator-optimizer
- "In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop."

(e) Ground truth
- "gain "ground truth" from the environment at each step"

(f) Stopping conditions and human checkpoints
- "Agents can then pause for human feedback at checkpoints or when encountering blockers."
- "it's also common to include stopping conditions"

（抽取工具附註：(a)(b)(c)(e) 中有幾句超過 125 字元，只引了最長的精確片段。）
