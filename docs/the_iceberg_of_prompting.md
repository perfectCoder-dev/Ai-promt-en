# The Iceberg Of Prompting

<p align="center">
  <img src="../images/iceberg.png" alt="Iceberg of Prompting" width="250">
</p>

At first glance, prompting seems simple: ask a question, receive an answer. But what appears effortless on the surface often rests on a much deeper structure beneath it. Like an iceberg, most of the power in effective prompting is hidden from view.

The visible tip consists of straightforward requests—summaries, rewrites, quick ideas. These work well for basic tasks. Beneath the surface, however, lies structured prompting: defining roles, clarifying context, setting constraints, and shaping output formats. Deeper still is strategic prompting—reasoning guidance, iteration loops, model selection, and deliberate refinement.

Mastery is not about making prompts longer. It is about knowing how deep to go. The Iceberg of Prompting is a framework for understanding that depth—when it matters, how it works, and how to use it intentionally.

## Level 1: Surface Prompting

Simple, direct requests with minimal context. Fast and useful for basic tasks, but limited when complexity or precision increases.

**Item types**: 🧩 Core Technique | 🎯 Typical Usage

|Sublevel |✨ Possibilities           |🧩 Core Technique    |🎯 Typical Usage |🧩 Core Technique   |🎯 Typical Usage     |                       
|--------:|---------------------------|---------------------|-----------------|--------------------|---------------------|
|1        |                           |Zero-shot prompting |“just ask”        | -                  |Rewrite this like me |
|2        |                           |One-shot prompt     |“1 example        | -                  |Without context      |
|3        |                           |Few-shot prompt     |“2+ examples”     |Explain like I’m 5  | -                   |
|4        |“I can’t dive into that"   |Brainstorm 10 ideas | -                |Simple tasks        |“Summarize this”     |

## Level 2: Structure Prompting

Clear roles, defined tasks, added context, and output constraints. Improves reliability, clarity, and consistency for real-world work.

**Item types**: 📐 Structural Design | 🚦 Operational Control

|Sublevel |✨ Possibilities           |📐 Structural Design             |🚦 Operational Control              |
|--------:|---------------------------|---------------------------------|------------------------------------|
|5        |                           |**Role**                         |Who to be                           |
|5        |                           | -                               |Specify tone & style                |
|5        |                           | -                               |Plan > Act > Sumarize               |
|6        |Real work zone starts here |**Task**                         |The exact action                    |
|6        |                           |Add stop conditions              |Limits, boundaries                  |
|7        |                           |**Context**                      |Background, constraints, audience   |
|7        |                           | -                               |Temporary chats                     |
|8        |                           |**Set output format**            |Bullets, tables                     |
|8        |                           |Tool policy                      |Browsing on/off                     |
|9        |                           |**Use examples of good outputs** | -                                  |
|9        |                           | -                               |Memory management, projects set ups |

## Level 3: Deep Prompting

Guided reasoning, iteration, and strategic refinement. Designed for complex problems, high-stakes decisions, and optimized results.

**Item types**: 🧠 Cognitive Strategy | ⚙️ Execution Mechanism

|Sublevel |✨ Possibilities        | 🧠 Cognitive Strategy |⚙️ Execution Mechanism          |🧠 Cognitive Strategy |⚙️ Execution Mechanism               |
|--------:|------------------------|-----------------------|--------------------------------|----------------------|--------------------------------------|
|10       |                        |Choose the right model |Thinking vs Fast                | -                    |Say “I don’t know” if unsure          |
|11       |Where the magic happens |Reasoning instruction  |“Think deeply before answering” | -                    |Chain-of-Thought                      |
|12       |                        |Question-first         |How first, then Do              |Iteration loop        |Feedback → Revision → Final           |
|13       |                        |Problem-solving        |20% that gets 80% results       | -                    |Role + Context + Examples + Iteration |

## Credits

The **Layers of Prompting** diagram and concept were created by Ruben Hassid.
This repository references and summarizes the ideas presented in his original visual.
