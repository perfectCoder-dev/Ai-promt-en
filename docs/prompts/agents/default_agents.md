# Default Agents

The columns that follow **Pattern** represent matches with corresponding elements in [The Iceberg Of Prompting](../../the_iceberg_of_prompting.md) framework.

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

| Role                 | Task    | Pattern           | 🧠 Cognitive Strategy | ⚙️ Execution Mechanism          |
|----------------------|---------|-------------------|-----------------------|---------------------------------|
| technical_instructor | explain | structured_output |Choose the right model |Thinking vs Fast                 |
| technical_instructor | explain | structured_output | —                     |Say “I don’t know” if unsure     |

```mermaid
flowchart TD

A((math_tutor))

A --> B[Role]
B --> C[tutor]

A --> D[Task]
D --> E[explain]
E --> F[Pattern]

F --> G[step_by_step]
G --> H[🧠 Cognitive Strategy]
H --> I[Reasoning instruction]

I --> J[⚙️ Execution Mechanism]
J --> K[“Think deeply before answering”]

G --> L[⚙️ Execution Mechanism]
L --> M[Chain-of-Thought]

F --> N[structured_output]

N --> O[Level 1]
O --> P[🧩 Core Technique]
P --> Q[Simple tasks]
Q --> R[🎯 Typical Usage]
R --> S[“Summarize this”]

N --> T[Level 2]
T --> U[📐 Structural Design]
U --> V[Set output format]
V --> W[🚦 Operational Control]
W --> X[Bullets, tables]

N --> Y[Level 3]
Y --> Z[🧠 Cognitive Strategy]
Z --> AA[Choose the right model]
AA --> AB[⚙️ Execution Mechanism]
AB --> AC[Thinking vs Fast ]

Y --> AD[⚙️ Execution Mechanism]
AD --> AE[Say “I don’t know” if unsure]

%% Color definitions
classDef role fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#111;
classDef task fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#111;
classDef pattern fill:#ffedd5,stroke:#ea580c,stroke-width:2px,color:#111;

%% Apply colors
class B,C role
class D,E task
class F,G,N pattern

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
G --> H[🧠 Cognitive Strategy]
H --> I[Reasoning instruction]

I --> J[⚙️ Execution Mechanism]
J --> K[“Think deeply before answering”]

G --> L[⚙️ Execution Mechanism]
L --> M[Chain-of-Thought]

F --> N[socratic]
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
