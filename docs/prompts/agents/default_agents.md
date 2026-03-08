# Default Agents

The columns that follow **Pattern** represent matches with corresponding elements in [The Iceberg Of Prompting](../../the_iceberg_of_prompting.md) framework.

## action_agent

TODO: ChatGTP

## cs_instructor

| Role                 | Task    | Pattern           | 🧠 Cognitive Strategy | ⚙️ Execution Mechanism          |
|----------------------|---------|-------------------|-----------------------|---------------------------------|
| technical_instructor | explain | step_by_step      | Reasoning instruction | “Think deeply before answering” |
| technical_instructor | explain | step_by_step      | —                     | Chain-of-Thought                |

| Role                 | Task    | Pattern           | 🧩 Core Technique     | 🎯 Typical Usage                |
|----------------------|---------|-------------------|-----------------------|---------------------------------|
| technical_instructor | explain | structured_output |Simple tasks           |“Summarize this”                 |

| Role                 | Task    | Pattern           | 📐 Structural Design  | 🚦 Operational Control          |
|----------------------|---------|-------------------|-----------------------|---------------------------------|
| technical_instructor | explain | structured_output |Set output format      |Bullets, tables                  |

```mermaid
flowchart TD

A((math_tutor))

A --> B[Role]
B --> C[tutor]

A --> D[Task]
D --> E[explain]
E --> F[Pattern]
F --> G[step_by_step]
G --> H[Level 3]
H --> I[🧠 Cognitive Strategy]
I --> J[Reasoning instruction]
J --> K[⚙️ Execution Mechanism]
K --> L[“Think deeply before answering”]

H --> M[⚙️ Execution Mechanism]
M --> N[Chain-of-Thought]

F --> O[structured_output]
O --> P[Level 1]
P --> Q[🧩 Core Technique]
Q --> R[Simple tasks]
R --> S[🎯 Typical Usage]
S --> T[“Summarize this”]

O --> U[Level 2]
U --> V[📐 Structural Design]
V --> W[Set output format]
W --> X[🚦 Operational Control]
X --> Y[Bullets, tables]

%% Color definitions
classDef role fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#111;
classDef task fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#111;
classDef pattern fill:#ffedd5,stroke:#ea580c,stroke-width:2px,color:#111;

%% Apply colors
class B,C role
class D,E task
class F,G,O pattern

```

## math_tutor

| Role  | Task    | Pattern        | 🧠 Cognitive Strategy | ⚙️ Execution Mechanism            |
|-------|---------|----------------|-----------------------|-----------------------------------|
| tutor | explain | step_by_step   | Reasoning instruction | “Think deeply before answering”   |
| tutor | explain | step_by_step   | —                     | Chain-of-Thought                  |
| tutor | explain | socratic       | Question-first        | How first, then Do                |
| tutor | explain | socratic       | Iteration loop        | Feedback → Revision → Final       |

```mermaid
flowchart TD

A((math_tutor))

A --> B[Role]
B --> C[tutor]

A --> D[Task]
D --> E[explain]
E --> F[Pattern]

F --> G[step_by_step]
G --> H[Level 3]
H --> I[🧠 Cognitive Strategy]
I --> J[Reasoning instruction]

J --> K[⚙️ Execution Mechanism]
K --> L[“Think deeply before answering”]

H --> M[⚙️ Execution Mechanism]
M --> N[Chain-of-Thought]

F --> O[socratic]
O --> P[Level 3]

P --> Q[🧠 Cognitive Strategy]
Q --> R[Question-first]
R --> S[⚙️ Execution Mechanism]
S --> T[How first, then Do]

P --> U[🧠 Cognitive Strategy]
U --> V[Iteration loop]
V --> W[⚙️ Execution Mechanism]
W --> X[Feedback → Revision → Final]

%% Color definitions
classDef role fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#111;
classDef task fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#111;
classDef pattern fill:#ffedd5,stroke:#ea580c,stroke-width:2px,color:#111;

%% Apply colors
class B,C role
class D,E task
class F,G,O pattern

```
