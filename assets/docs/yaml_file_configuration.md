# YAML Files Configuration

This guide explains how to **define agent presets (`.yaml`)** and **pattern group files (`.yaml`)** for PromptNG. It includes syntax, best practices, and notes on indentation, spacing, and line breaks.

## 1. Agent Preset YAML Files

An **agent preset** defines the combination of **role**, **task**, **patterns**, and optional **controls**.

### Basic Structure

```yaml
role: <role_name>
task: <task_name>

patterns:
  - <pattern_1>
  - <pattern_2>

controls:
  pre:
    - <pre_control_1>
    - <pre_control_2>
  post:
    - <post_control_1>
    - <post_control_2>

```

- `role`: Behavioral identity of the agent (e.g., technical_instructor, tutor, executor)

- `task`: The action the agent performs (e.g., explain, action, compose_action)

- `patterns`: Ordered list of patterns or pattern groups that define cognitive and execution strategies

- `controls` (optional): Pre- and post-prompt layers to influence execution and output

> [!TIP]
You can skip `controls` if not needed; PromptNG will use default behavior.

> [!WARNING]
YAML indentation, spacing, and empty lines are strictly enforced. Always use consistent indentation (2 spaces) and avoid tabs.

**Example with pre controls**

```yml
role: executor
task: action

patterns:
  - verify_before_execute
  - plan_execute
  - structured_output

controls:
  pre:
    - forget
  post: []

```

**Example without controls**

```yml
role: tutor
task: explain
patterns:
  - step_by_step
  - socratic

```

## 2. Pattern Group YAML Files

A pattern group bundles multiple patterns into a single identifier. This simplifies the CLI and allows hierarchical composition.

### Basic Structure

```yml
patterns:
  - <pattern_1>
  - <pattern_2>
  - <pattern_3>

```

**Example: `didactic` pattern group**

```yml
patterns:
  - socratic
  - step_by_step

```

- Use `--pattern` `didactic` instead of repeating each pattern individually

- Expands automatically into all included patterns

**Example: `didactic_structured` pattern group**

```yml
patterns:
  - socratic
  - step_by_step
  - structured_output
```

> [!TIP]
Pattern groups improve abstraction, reduce CLI verbosity, and enable reusable behavior bundles.
