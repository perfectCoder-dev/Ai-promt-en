# Built-in Pattern Groups

> [!NOTE]
> Table columns that follow **Pattern** represent matches with corresponding elements in [The Iceberg Of Prompting](../../the_iceberg_of_prompting.md) framework.

## Pattern Group: `didactic`

### Description

Expands into the patterns `socratic` and `step_by_step`.

### Specification Table

| Pattern | 🧠 Cognitive Strategy | ⚙️ Execution Mechanism      |
|---------|-----------------------|-----------------------------|
|socratic | Question-first        | How first, then Do          |
|socratic | Iteration loop        | Feedback → Revision → Final |

| Pattern     | 🧠 Cognitive Strategy | ⚙️ Execution Mechanism           |
|-------------|-----------------------|----------------------------------|
|step_by_step | Reasoning instruction | “Think deeply before answering”  |
|step_by_step | —                     | Chain-of-Thought                 |

### Flowchart

```mermaid
flowchart TD

A((didactic))

A --> B[pattern]
B --> C[socratic]
C --> D[🧠 Cognitive Strategy]
D --> E[Question-first]
E --> F[⚙️ Execution Mechanism]
F --> G[How first, then Do]

C --> H[🧠 Cognitive Strategy]
H --> I[Iteration loop]
I --> J[⚙️ Execution Mechanism]
J --> K[How first, then Do]

B --> L[step_by_step]
L --> M[🧠 Cognitive Strategy]
M --> O[Reasoning instruction]
O --> P[⚙️ Execution Mechanism]
P --> Q[“Think deeply before answering”]

L --> R[⚙️ Execution Mechanism]
R --> S[Chain-of-Thought]

%% Color definitions
classDef pattern fill:#ffedd5,stroke:#ea580c,stroke-width:2px,color:#111;

%% Apply colors
class B,C,L, pattern

```

### List And Show

```bash
pp list pattern_groups | grep did
pp show pattern_groups/didactic
```

### Usage

#### Agent Configuration

```yaml
patterns:
  - didactic
```

#### With Compose

```bash
pp compose --role <role> --task <task> --pattern didactic --var input="<input>"
```

### Example

```bash
pp compose --role tutor --task explain --pattern didactic --var input="Binary Search Trees" --copy
```

## Pattern Group: `didactic_structured`

### Description

Expands into the patterns `socratic`, `step_by_step`, and `structured_output`.

### Specification Table

| Pattern | 🧠 Cognitive Strategy | ⚙️ Execution Mechanism      |
|---------|-----------------------|-----------------------------|
|socratic | Question-first        | How first, then Do          |
|socratic | Iteration loop        | Feedback → Revision → Final |

| Pattern     | 🧠 Cognitive Strategy | ⚙️ Execution Mechanism           |
|-------------|-----------------------|----------------------------------|
|step_by_step | Reasoning instruction | “Think deeply before answering”  |
|step_by_step | —                     | Chain-of-Thought                 |

| Pattern           | 🧩 Core Technique     | 🎯 Typical Usage                |
|-------------------|-----------------------|---------------------------------|
| structured_output |Simple tasks           |“Summarize this”                 |

| Pattern           | 📐 Structural Design  | 🚦 Operational Control          |
|-------------------|-----------------------|---------------------------------|
| structured_output |Set output format      |Bullets, tables                  |

### Flowchart

```mermaid
flowchart TD

A((didactic_structured))

A --> B[pattern]
B --> C[socratic]
C --> D[🧠 Cognitive Strategy]
D --> E[Question-first]
E --> F[⚙️ Execution Mechanism]
F --> G[How first, then Do]

C --> H[🧠 Cognitive Strategy]
H --> I[Iteration loop]
I --> J[⚙️ Execution Mechanism]
J --> K[Feedback → Revision → Final]

B --> L[step_by_step]
L --> M[🧠 Cognitive Strategy]
M --> O[Reasoning instruction]
O --> P[⚙️ Execution Mechanism]
P --> Q[“Think deeply before answering”]

L --> R[⚙️ Execution Mechanism]
R --> S[Chain-of-Thought]

B --> T[structured_output]
T --> U[🧩 Core Technique]
U --> V[Simple tasks]
V --> W[🎯 Typical Usage]
W --> X[“Summarize this”]

T --> Y[📐 Structural Design]
Y --> Z[Set output format]
Z --> AA[🚦 Operational Control]
AA --> BB[Bullets, tables]

%% Color definitions
classDef pattern fill:#ffedd5,stroke:#ea580c,stroke-width:2px,color:#111;

%% Apply colors
class B,C,L,T pattern

```

### List And Show

```bash
pp list pattern_groups | grep did
pp show pattern_groups/didactic_structured
```

### Usage

#### Agent Configuration

```yaml
patterns:
  - didactic_structured
```

#### With Compose

```bash
pp compose --role <role> --task <task> --pattern didactic_structured --var input="<input>"
```

### Example

```bash
pp compose --role tutor --task explain --pattern didactic_structured --var input="Binary Search Trees" --copy
```

## Pattern Group: `testing_strict`

### Description

Expands into the patterns `verify_before_execute`, `plan_execute`, `break_assumptions`, and `structured_output`.

### Specification Table

| Pattern               | 🧠 Cognitive Strategy | ⚙️ Execution Mechanism          |
|-----------------------|-----------------------|---------------------------------|
| verify_before_execute | Reasoning instruction | “Think deeply before answering” |
| verify_before_execute | —                     | Chain-of-Thought                |
| verify_before_execute | Question-first        | How first, then Do              |
| verify_before_execute | Iteration loop        | Feedback → Revision → Final     |
| plan_execute          | Reasoning instruction | “Think deeply before answering” |
| plan_execute          | —                     | Chain-of-Thought                |
| plan_execute          | Question-first        | How first, then Do              |
| plan_execute          | Iteration loop        | Feedback → Revision → Final     |

| Pattern           | 🧩 Core Technique | 🎯 Typical Usage |
|-------------------|-------------------|------------------|
| structured_output |Simple tasks       |“Summarize this”  |

| Pattern           | 📐 Structural Design | 🚦 Operational Control |
|-------------------|----------------------|------------------------|
| structured_output |Set output format     |Bullets, tables         |

| Pattern           | 🧠 Cognitive Strategy | ⚙️ Execution Mechanism                |
|-------------------|-----------------------|---------------------------------------|
| break_assumptions | Reasoning instruction | “Think deeply before answering”       |
| break_assumptions | Question-first        | How first, then Do                    |
| break_assumptions | Iteration loop        | Feedback → Revision → Final           |
| break_assumptions | Problem-solving       | 20% that gets 80% results             |
| break_assumptions | -                     | Role + Context + Examples + Iteration |

### Flowchart

```mermaid
flowchart TD

A((testing_strict))

A --> B[pattern]
B --> C[verify_before_execute]
C --> D[🧠 Cognitive Strategy]
D --> E[Question-first]
E --> F[⚙️ Execution Mechanism]
F --> G[How first, then Do]

C --> H[🧠 Cognitive Strategy]
H --> I[Iteration loop]
I --> J[⚙️ Execution Mechanism]
J --> K[Feedback → Revision → Final]

C --> L[🧠 Cognitive Strategy]
L --> M[Reasoning instruction]
M --> O[⚙️ Execution Mechanism]
O --> P[“Think deeply before answering”]

C --> Q[⚙️ Execution Mechanism]
Q --> R[Chain-of-Thought]

B --> S[plan_execute]
S --> T[🧠 Cognitive Strategy]
T --> U[Question-first]
U --> V[⚙️ Execution Mechanism]
V --> W[How first, then Do]

S --> X[🧠 Cognitive Strategy]
X --> Y[Iteration loop]
Y --> Z[⚙️ Execution Mechanism]
Z --> AA[Feedback → Revision → Final]

S --> AB[🧠 Cognitive Strategy]
AB --> AC[Reasoning instruction]
AC --> AD[⚙️ Execution Mechanism]
AD --> AE[“Think deeply before answering”]

S --> AF[⚙️ Execution Mechanism]
AF --> AG[Chain-of-Thought]

B --> AH[break_assumptions]
AH --> AI[🧠 Cognitive Strategy]
AI --> AJ[Reasoning instruction]
AJ --> AK[⚙️ Execution Mechanism]
AK --> AL[“Think deeply before answering”]

AH --> AM[🧠 Cognitive Strategy]
AM --> AN[Question-first]
AN --> AO[⚙️ Execution Mechanism]
AO --> AP[How first, then Do]

AH --> AQ[🧠 Cognitive Strategy]
AQ --> AR[Iteration loop]
AR --> AS[⚙️ Execution Mechanism]
AS --> AT[Feedback → Revision → Final]

AH --> AU[🧠 Cognitive Strategy]
AU --> AV[Problem-solving]
AV --> AW[⚙️ Execution Mechanism]
AW --> AX[20% that gets 80% results]

AH --> AY[⚙️ Execution Mechanism]
AY --> AZ[Role + Context + Examples + Iteration]

B --> BA[Level 1]
BA --> BB[structured_output]
BB --> BC[🧩 Core Technique]
BC --> BD[Simple tasks]
BD --> BE[🎯 Typical Usage]
BE --> BF[“Summarize this”]

B --> BG[Level 2]
BG --> BH[structured_output]
BH --> BI[📐 Structural Design]
BI --> BJ[Set output format]
BJ --> BK[🚦 Operational Control]
BK --> BL[Bullets, tables]

%% Color definitions
classDef pattern fill:#ffedd5,stroke:#ea580c,stroke-width:2px,color:#111;

%% Apply colors
class B,C,S,AH,BB,BH pattern

```

### List And Show

```bash
pp list pattern_groups | grep strict
pp show pattern_groups/testing_strict
```

### Usage

#### Agent Configuration

```yaml
patterns:
  - testing_strict
```

#### With Compose

```bash
pp compose --role <role> --task <task> --pattern testing_strict --var input="<input>"
```

### Example

```bash
pp compose --role dev/software_tester --task action --pattern testing_strict --var-file action=content/dev/testing/boundary_edge_cases
```
