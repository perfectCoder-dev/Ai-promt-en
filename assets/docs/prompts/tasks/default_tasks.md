# Default Tasks

## Task: `action`

### Description

Executes a specified action by utilizing any relevant tools, methods, or capabilities available. The process adapts to the requirements of the task, selecting appropriate resources to effectively carry out the requested operation.

### Usage

```bash
pp build action_agent --var action="<action>"
```

### Example

```bash
pp build action_agent --var action="Make a shopping list"
```

### Specification Table

| Command | Agent        | Role     | Task   |
|---------|--------------|----------|--------|
| build   | action_agent | executor | action |

## Task: `compose_action`

### Description

Carries out a specified action while incorporating any available contextual information and examples. Context is used to guide understanding and decision-making, while examples provide reference for structure, formatting, or expected behavior, helping ensure the execution aligns with the intended outcome.

### Usage

```bash
pp compose \
  --role executor \
  --task compose_action \
  --pattern <pattern> \
  --var action="<action>" \
  --var context="<context>" \
  --var examples="<examples>"
```

### Example

```bash
pp compose \
  --role executor \
  --task compose_action \
  --pattern verify_before_execute \
  --pattern plan_execute \
  --pattern structured_output \
  --var action="Make a shopping list" \
  --var context="I am at the computer store" \
  --var examples="|Item |Brand |Price | |Mouse |Genius |$45.75 |"
```

### Specification Table

| Command | Role     |  Task          | --var                     |
|---------|----------|----------------|---------------------------|
| compose | executor | compose_action | action, context, examples |

## Task: `explain`

### Description

Presents a concept through a clear, step-by-step explanation that builds understanding progressively. The explanation introduces ideas in a logical sequence, helping the reader grasp foundational elements before moving to more detailed or complex aspects.

### Usage

```bash
pp compose --role <role> --task explain --pattern <pattern> --var input="<input>"
```

### Example

```bash
pp compose \
  --role technical_instructor \
  --task explain \
  --pattern step_by_step \
  --pattern structured_output \
  --var input="Switch, explained for beginners" \
```

### Specification Table

| Command       | Task    |
|---------------|---------|
| build/compose | explain |
