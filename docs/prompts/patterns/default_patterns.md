# Default Patterns

> [!NOTE]
> Table columns that follow **Pattern** represent matches with corresponding elements in [The Iceberg Of Prompting](../../the_iceberg_of_prompting.md) framework.

## Pattern: `plan_execute`

### Description

### Usage

### Example

### Specification Table

### Flowchart

## Pattern: `socratic`

### Description

Encourages the model to guide reasoning through reflective questioning before presenting a final answer, prompting the user to examine assumptions, clarify thinking, and progressively arrive at a well-supported conclusion.

### Usage

### Example

```bash
pp compose \
  --role tutor \
  --task explain \
  --pattern socratic \
  --var input="Random text"
```

### Specification Table

| Pattern | 🧠 Cognitive Strategy | ⚙️ Execution Mechanism      |
|---------|-----------------------|-----------------------------|
|socratic | Question-first        | How first, then Do          |
|socratic | Iteration loop        | Feedback → Revision → Final |

### Flowchart

## Pattern: `step_by_step`

### Description

### Usage

### Example

### Specification Table

| Pattern     | 🧠 Cognitive Strategy | ⚙️ Execution Mechanism           |
|-------------|-----------------------|----------------------------------|
|step_by_step | Reasoning instruction | “Think deeply before answering”  |
|step_by_step | —                     | Chain-of-Thought                 |

### Flowchart

## Pattern: `structured_output`

### Description

### Usage

### Example

### Specification Table

### Flowchart

## Pattern: `verify_before_execute`

### Description

### Usage

### Example

### Specification Table

| Pattern           | 🧩 Core Technique     | 🎯 Typical Usage                |
|-------------------|-----------------------|---------------------------------|
| structured_output |Simple tasks           |“Summarize this”                 |

| Pattern           | 📐 Structural Design  | 🚦 Operational Control          |
|-------------------|-----------------------|---------------------------------|
| structured_output |Set output format      |Bullets, tables                  |

### Flowchart
