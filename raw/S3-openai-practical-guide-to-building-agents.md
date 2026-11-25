---
id: S3
title: A practical guide to building agents
publisher: OpenAI
url: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
fetched: 2026-11-25
how: WebFetch（PDF），一次抽取。
note: 工具抽出的逐字引文集，不是整份 PDF 備份。
---

## 抽取結果（原樣保存）

Agent definition: "Agents are systems that independently accomplish tasks on your behalf."

Agent characteristic (LLM-driven decisions): "It leverages an LLM to manage workflow execution and make decisions."

Agent characteristic (failure handling): "In case of failure, it can halt execution and transfer control back to the user."

Use cases (evaluation): "Before committing to building an agent, validate that your use case can meet these criteria clearly."

Use cases (alternative): "Otherwise, a deterministic solution may suffice."

Core components (overview): "In its most fundamental form, an agent consists of three core components:"

Core component (model): "The LLM powering the agent’s reasoning and decision-making"

Core component (tools): "External functions or APIs the agent can use to take action"

Core component (instructions): "Explicit guidelines and guardrails defining how the agent behaves"

Orchestration (overview): "In general, orchestration patterns fall into two categories:"

Orchestration (single-agent): "Single-agent systems, where a single model equipped with appropriate tools and instructions executes workflows in a loop"

Orchestration (manager): "A central “manager” agent coordinates multiple specialized agents via tool calls, each handling a specific task or domain."

Orchestration (decentralized): "Handoffs are a one way transfer that allow an agent to delegate to another agent."

Guardrails (layered approach): "Think of guardrails as a layered defense mechanism."

Guardrails (SDK behavior): "The Agents SDK treats guardrails as first-class concepts, relying on optimistic execution by default."
