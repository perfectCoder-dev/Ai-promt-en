# Default Agents

Reference implementations of default agents designed around different
functional focuses and reasoning patterns.

> [!IMPORTANT]
> **Default Agents** are organized by their primary area of focus, which guides how they approach tasks and structure their reasoning. While each default agent is designed with a particular focus in mind, they remain capable of assisting with requests beyond that scope when needed.

> [!NOTE]
> Table columns that follow **Pattern** represent matches with corresponding elements in [The Iceberg Of Prompting](../../the_iceberg_of_prompting.md) framework.

## Agent: `action_agent`

### Description

An execution-focused agent designed to perform tasks by verifying requirements or planning before acting, using reasoning strategies and structured outputs to ensure accurate and controlled results.

### Usage

```bash
pp build action_agent --var action="<action>" --copy
```

### Example

```bash
pp build action_agent --var action="Make a shopping list" --copy
```

### Specification Table

| Role                 | Task     | Pattern               | 🧠 Cognitive Strategy | ⚙️ Execution Mechanism          |
|----------------------|----------|-----------------------|-----------------------|---------------------------------|
| executor             | action   | verify_before_execute | Question-first        | How first, then Do              |
| executor             | action   | verify_before_execute | Iteration loop        | Feedback → Revision → Final     |
| executor             | action   | verify_before_execute | Reasoning instruction | “Think deeply before answering” |
| executor             | action   | verify_before_execute | —                     | Chain-of-Thought                |
| executor             | action   | plan_execute          | Question-first        | How first, then Do              |
| executor             | action   | plan_execute          | Iteration loop        | Feedback → Revision → Final     |
| executor             | action   | plan_execute          | Reasoning instruction | “Think deeply before answering” |
| executor             | action   | plan_execute          | —                     | Chain-of-Thought                |

| Role                 | Task    | Pattern           | 🧩 Core Technique     | 🎯 Typical Usage                |
|----------------------|---------|-------------------|-----------------------|---------------------------------|
| executor             | action  | structured_output |Simple tasks           |“Summarize this”                 |

| Role                 | Task    | Pattern           | 📐 Structural Design  | 🚦 Operational Control          |
|----------------------|---------|-------------------|-----------------------|---------------------------------|
| executor             | action  | structured_output |Set output format      |Bullets, tables                  |

### Flowchart

```mermaid
flowchart TD

A((action_agent))

A --> B[Role]
B --> C[executor]

A --> D[Task]
D --> E[action]
E --> F[Pattern]
F --> G[verify_before_execute]
G --> H[Level 3]
H --> I[🧠 Cognitive Strategy]
I --> J[Question-first]
J --> K[⚙️ Execution Mechanism]
K --> L[How first, then Do]

H --> M[🧠 Cognitive Strategy]
M --> O[Iteration loop]
O --> P[⚙️ Execution Mechanism]
P --> Q[Feedback → Revision → Final]

H --> R[🧠 Cognitive Strategy]
R --> S[Reasoning instruction]
S --> T[⚙️ Execution Mechanism]
T --> U[“Think deeply before answering”]

H --> V[⚙️ Execution Mechanism]
V --> W[Chain-of-Thought]

F --> X[plan_execute]
X --> Z[Level 3]
Z --> AA[🧠 Cognitive Strategy]
AA --> BB[Question-first]
BB --> CC[⚙️ Execution Mechanism]
CC --> DD[How first, then Do]

Z --> EE[🧠 Cognitive Strategy]
EE --> FF[Iteration loop]

FF --> GG[⚙️ Execution Mechanism]
GG --> HH[Feedback → Revision → Final]

Z --> II[🧠 Cognitive Strategy]
II --> JJ[Reasoning instruction]
JJ --> KK[⚙️ Execution Mechanism]
KK --> LL[“Think deeply before answering”]

Z --> MM[⚙️ Execution Mechanism]
MM --> OO[Chain-of-Thought]

F --> PP[structured_output]
PP --> QQ[Level 1]
QQ --> RR[🧩 Core Technique]
RR --> SS[Simple tasks]
SS --> TT[🎯 Typical Usage]
TT --> UU[Simple tasks]

PP --> VV[Level 2]
VV --> WW[📐 Structural Design]
WW --> XX[Set output format]
XX --> YY[🚦 Operational Control]
YY --> ZZ[Bullets, tables]

%% Color definitions
classDef role fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#111;
classDef task fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#111;
classDef pattern fill:#ffedd5,stroke:#ea580c,stroke-width:2px,color:#111;

%% Apply colors
class B,C role
class D,E task
class F,G,X,PP pattern

```

## Agent: `cs_instructor`

### Description

A technical teaching agent specialized in explaining computer science concepts step by step, using reasoning strategies and structured outputs to make complex topics easier to understand.

### Usage

```bash
pp build cs_instructor --var input="<input>" --copy
```

### Example

```bash
pp build cs_instructor --var input="Switch, explained for beginners" --copy
```

### Specification Table

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

### Flowchart

```mermaid
flowchart TD

A((cs_instructor))

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

## Agent: `math_tutor`

### Description

An educational agent that teaches mathematical concepts through step-by-step explanations and Socratic questioning, encouraging reasoning and iterative understanding.

### Usage

```bash
pp build math_tutor --var input="<input>" --copy
```

### Example

```bash
pp build math_tutor --var input="Explain recursion" --copy
```

### Specification Table

| Role  | Task    | Pattern        | 🧠 Cognitive Strategy | ⚙️ Execution Mechanism            |
|-------|---------|----------------|-----------------------|-----------------------------------|
| tutor | explain | step_by_step   | Reasoning instruction | “Think deeply before answering”   |
| tutor | explain | step_by_step   | —                     | Chain-of-Thought                  |
| tutor | explain | socratic       | Question-first        | How first, then Do                |
| tutor | explain | socratic       | Iteration loop        | Feedback → Revision → Final       |

### Flowchart

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
