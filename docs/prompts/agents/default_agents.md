# Default Agents

**Matched** columns correspond to **items** from [The Iceberg Of Prompting](../../the_iceberg_of_prompting.md) framework.

## cs_instructor

TODO:

## math_tutor

| Role  | Task    | Pattern        | 🧠 Cognitive Strategy | ⚙️ Execution Mechanism            |
|-------|---------|----------------|-----------------------|-----------------------------------|
| tutor | explain | step by step   | Reasoning instruction | “Think deeply before answering”   |
| tutor | explain | step by step   | —                     | Chain-of-Thought                  |
| tutor | explain | Socratic       | Question-first        | How first, then Do                |
| tutor | explain | Socratic       | Iteration loop        | Feedback → Revision → Final       |

```mermaid
flowchart TD

A((math_tutor))

A --> B[Role]
B --> C[tutor]

A --> D[Task]
D --> E[explain]
E --> F[Pattern]

F --> G[step by step]
G --> H[🧠 Cognitive Strategy]
H --> I[Reasoning instruction]

I --> J[⚙️ Execution Mechanism]
J --> K[“Think deeply before answering”]

G --> L[⚙️ Execution Mechanism]
L --> M[Chain-of-Thought]

F --> N[Socratic]
N --> O[🧠 Cognitive Strategy]
O --> P[Question-first]
P --> Q[⚙️ Execution Mechanism]
Q --> R[How first, then Do]

N --> S[🧠 Cognitive Strategy]
S --> T[Iteration loop]
T --> U[⚙️ Execution Mechanism]
U --> V[Feedback → Revision → Final]

%% Color definitions
classDef role fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#111;
classDef task fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#111;
classDef pattern fill:#ffedd5,stroke:#ea580c,stroke-width:2px,color:#111;

%% Apply colors
class B,C role
class D,E task
class F,G,N pattern

```
