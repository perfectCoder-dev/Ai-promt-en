# Default Pattern Groups

> [!NOTE]
> Table columns that follow **Pattern** represent matches with corresponding elements in [The Iceberg Of Prompting](../../the_iceberg_of_prompting.md) framework.

## Pattern Group: `didactic`

### Description

Expands into the patterns `socratic` and `step_by_step`.

### Usage

```bash
pp compose --role <role> --task <task> --pattern didactic --var input="<input>"
```

### Example

```bash
pp compose --role tutor --task explain --pattern didactic --var input="Binary Search Trees" --copy
```

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

## Pattern Group: `didactic_structured`

### Description

Expands into the patterns `socratic`, `step_by_step`, and `structured_output`.

### Usage

```bash
pp compose --role <role> --task <task> --pattern didactic_structured --var input="<input>"
```

### Example

```bash
pp compose --role tutor --task explain --pattern didactic_structured --var input="Binary Search Trees" --copy
```

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
J --> K[How first, then Do]

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
