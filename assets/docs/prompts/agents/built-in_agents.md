# Built-in Agents

Reference implementations of built-in agents designed around different
functional focuses and reasoning patterns.

> [!IMPORTANT]
> **Built-in Agents** are organized by their primary area of focus, which guides how they approach tasks and structure their reasoning. While each built-in agent is designed with a particular focus in mind, they remain capable of assisting with requests beyond that scope when needed.

> [!NOTE]
> Table columns that follow **Pattern** represent matches with corresponding elements in [The Iceberg Of Prompting](../../the_iceberg_of_prompting.md) framework.

## Agent: `software_testing_agent`

### Description

(Desc)

### Specification Table

| Role            | Task   | Pattern               | 🧠 Cognitive Strategy | ⚙️ Execution Mechanism          |
|-----------------|--------|-----------------------|-----------------------|---------------------------------|
| software_tester | action | verify_before_execute | Question-first        | How first, then Do              |
| software_tester | action | verify_before_execute | Iteration loop        | Feedback → Revision → Final     |
| software_tester | action | verify_before_execute | Reasoning instruction | “Think deeply before answering” |
| software_tester | action | verify_before_execute | —                     | Chain-of-Thought                |
| software_tester | action | plan_execute          | Question-first        | How first, then Do              |
| software_tester | action | plan_execute          | Iteration loop        | Feedback → Revision → Final     |
| software_tester | action | plan_execute          | Reasoning instruction | “Think deeply before answering” |
| software_tester | action | plan_execute          | —                     | Chain-of-Thought                |

| Role            | Task   | Pattern           | 🧩 Core Technique | 🎯 Typical Usage |
|-----------------|--------|-------------------|-------------------|------------------|
| software_tester | action | structured_output |Simple tasks       |“Summarize this”  |

| Role            | Task   | Pattern           | 📐 Structural Design | 🚦 Operational Control |
|-----------------|--------|-------------------|----------------------|------------------------|
| software_tester | action | structured_output |Set output format     |Bullets, tables         |

| Role            | Task   | Pattern           | 🧠 Cognitive Strategy | ⚙️ Execution Mechanism                |
|-----------------|--------|-------------------|-----------------------|---------------------------------------|
| software_tester | action | break_assumptions | Reasoning instruction | “Think deeply before answering”       |
| software_tester | action | break_assumptions | Question-first        | How first, then Do                    |
| software_tester | action | break_assumptions | Iteration loop        | Feedback → Revision → Final           |
| software_tester | action | break_assumptions | Problem-solving       | 20% that gets 80% results             |
| software_tester | action | break_assumptions | -                     | Role + Context + Examples + Iteration |

### Flowchart

```mermaid
flowchart TD

A((software_testing_agent))

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
AA --> AB[Question-first]
AB --> AC[⚙️ Execution Mechanism]
AC --> AD[How first, then Do]

Z --> AE[🧠 Cognitive Strategy]
AE --> AF[Iteration loop]

AF --> AG[⚙️ Execution Mechanism]
AG --> AH[Feedback → Revision → Final]

Z --> AI[🧠 Cognitive Strategy]
AI --> AJ[Reasoning instruction]
AJ --> AK[⚙️ Execution Mechanism]
AK --> AL[“Think deeply before answering”]

Z --> AM[⚙️ Execution Mechanism]
AM --> AO[Chain-of-Thought]

F --> AP[structured_output]
AP --> AQ[Level 1]
AQ --> AR[🧩 Core Technique]
AR --> AS[Simple tasks]
AS --> AT[🎯 Typical Usage]
AT --> AU[Simple tasks]

AP --> AV[Level 2]
AV --> AW[📐 Structural Design]
AW --> AX[Set output format]
AX --> AY[🚦 Operational Control]
AY --> AZ[Bullets, tables]

F --> BA[break_assumptions]
BA --> BB[Level 3]
BB --> BC[🧠 Cognitive Strategy]
BC --> BD[Reasoning instruction]
BD --> BE[⚙️ Execution Mechanism]
BE --> BF[“Think deeply before answering”]

BB --> BG[🧠 Cognitive Strategy]
BG --> BH[Question-first]
BH --> BI[⚙️ Execution Mechanism]
BI --> BJ[How first, then Do]

BB --> BK[🧠 Cognitive Strategy]
BK --> BL[Iteration loop]
BL --> BM[⚙️ Execution Mechanism]
BM --> BN[Feedback → Revision → Final]

BB --> BO[🧠 Cognitive Strategy]
BO --> BP[Problem-solving]
BP --> BQ[⚙️ Execution Mechanism]
BQ --> BR[20% that gets 80% results]

BB --> BS[⚙️ Execution Mechanism]
BS --> BT[Role + Context + Examples + Iteration]

%% Color definitions
classDef role fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#111;
classDef task fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#111;
classDef pattern fill:#ffedd5,stroke:#ea580c,stroke-width:2px,color:#111;

%% Apply colors
class B,C role
class D,E task
class F,G,X,AP,BA pattern

```

### List And Show

```bash
pp list agents/dev | grep test
pp show agents/dev/software_testing_agent
```

### Usage

```bash
pp build dev/software_testing_agent --var action="<action>"
```

### Example

```bash
pp build dev/software_testing_agent --var-file action=content/dev/testing/boundary_edge_cases
```

## Agent: `action_agent`

### Description

An execution-focused agent designed to perform tasks by verifying requirements or planning before acting, using reasoning strategies and structured outputs to ensure accurate and controlled results.

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
AA --> AB[Question-first]
AB --> AC[⚙️ Execution Mechanism]
AC --> AD[How first, then Do]

Z --> AE[🧠 Cognitive Strategy]
AE --> AF[Iteration loop]

AF --> AG[⚙️ Execution Mechanism]
AG --> AH[Feedback → Revision → Final]

Z --> AI[🧠 Cognitive Strategy]
AI --> AJ[Reasoning instruction]
AJ --> AK[⚙️ Execution Mechanism]
AK --> AL[“Think deeply before answering”]

Z --> AM[⚙️ Execution Mechanism]
AM --> AO[Chain-of-Thought]

F --> AP[structured_output]
AP --> AQ[Level 1]
AQ --> AR[🧩 Core Technique]
AR --> AS[Simple tasks]
AS --> AT[🎯 Typical Usage]
AT --> AU[Simple tasks]

AP --> AV[Level 2]
AV --> AW[📐 Structural Design]
AW --> AX[Set output format]
AX --> AY[🚦 Operational Control]
AY --> AZ[Bullets, tables]

%% Color definitions
classDef role fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#111;
classDef task fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#111;
classDef pattern fill:#ffedd5,stroke:#ea580c,stroke-width:2px,color:#111;

%% Apply colors
class B,C role
class D,E task
class F,G,X,AP pattern

```

### List And Show

```bash
pp list agents | grep action
pp show agents/action_agent
```

### Usage

```bash
pp build action_agent --var action="<action>"
```

### Example

```bash
pp build action_agent --var action="Make a shopping list" --copy
```

## Agents: `action_agent_controlled`

### Description

An execution-focused agent designed to perform tasks by verifying requirements or planning before acting, using reasoning strategies and structured outputs to ensure accurate and controlled results.

It has all the `action_agent` features plus an only `pre` prompt control `forget` used as example.

For more information about the `forget` memory pre control, click 🔗 [here](../controls/built-in_controls.md#control-memoryforget).

### List And Show

```bash
pp list agents | grep action
pp show agents/action_agent_controlled
```

### Usage

```bash
pp build action_agent_controlled --var action="<action>"
```

### Example

```bash
pp build action_agent_controlled --post truth/say_dont_know --var action="Make a list of the core skills everyone should have."
```

## Agent: `cs_instructor`

### Description

A technical teaching agent specialized in explaining computer science concepts step by step, using reasoning strategies and structured outputs to make complex topics easier to understand.

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

### List And Show

```bash
pp list agents | grep instructor
pp show agents/cs_instructor
```

### Usage

```bash
pp build cs_instructor --var input="<input>"
```

### Example

```bash
pp build cs_instructor --var input="Switch, explained for beginners" --copy
```

## Agent: `math_tutor`

### Description

An educational agent that teaches mathematical concepts through step-by-step explanations and Socratic questioning, encouraging reasoning and iterative understanding.

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

### List And Show

```bash
pp list agents | grep math
pp show agents/math_tutor
```

### Usage

```bash
pp build math_tutor --var input="<input>"
```

### Example

```bash
pp build math_tutor --var input="Explain recursion" --copy
```
