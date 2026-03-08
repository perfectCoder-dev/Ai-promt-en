# Default Agents

**Full Match** and **Partial Match** columns correspond to **items** from [The Iceberg Of Prompting](../../the_iceberg_of_prompting.md) framework.

## cs_instructor

TODO:

## math_tutor

|Role|Task|Patterns|Full Matches|Partial Matches|
|----|----|--------|------------|---------------|
|tutor|explain|step by step|Reasoning instruction (Think deeply before answering,	Chain-of-Thought) |-|
| | |socratic|Question-first (How first, then Do). Iteration loop (Feedback → Revision → Final)|-|

flowchart TD

A((math_tutor))

A --> B[Role]
B --> C[tutor]

A --> D[Task]
D --> E[explain]

E --> F[Pattern: step by step]
F --> G[Reasoning instruction]
G --> H[Think deeply before answering]
G --> I[Chain-of-Thought]

E --> J[Pattern: socratic]
J --> K[Question-first: How first then Do]
J --> L[Iteration loop]
L --> M[Feedback → Revision → Final]

%% Color definitions
classDef role fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#111;
classDef task fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#111;
classDef pattern fill:#ffedd5,stroke:#ea580c,stroke-width:2px,color:#111;

%% Apply colors
class B,C role
class D,E task
class F,G,H,I,J,K,L,M pattern