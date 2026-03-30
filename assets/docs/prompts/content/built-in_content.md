# Built-in Content

Content components provide structured input that can be injected into prompts as variables, enabling agents to work with real data. These components are typically stored as files (e.g., `.md` or `.txt`) and loaded using variable sources like `--var-file` for single inputs or `--var-dir` for aggregating multiple files. This allows you to separate what the prompt operates on from how it behaves, making it easy to reuse the same content across different roles, tasks, and patterns. Content components make prompt construction more flexible, scalable, and maintainable.

> [!TIP]
Content components can also include template **placeholders** (e.g., **{{ text }}**). While you can use different placeholder styles such as **[ text ]** or **<< text >>**, using Jinja-style syntax (**{{ ... }}**) is recommended to take full advantage of PromptPro’s syntax highlighting and color theme support. Templating content in this way helps avoid creating multiple agent presets for similar tasks with only minor differences, improving reuse and maintainability.

> [!CAUTION]
Although the `--var-dir` option allows you to inject large amounts of content by aggregating multiple files, it is generally not suitable for templated content, as the resulting prompt can become excessively large and require significant manual editing after copying before it is ready to be submitted to an AI model.

## Content: `boundary_edge_cases`

### Description

Generates boundary and edge case test scenarios for a given **component**, including invalid inputs, null values, and memory constraints to ensure robustness and reliability under extreme conditions.

>[!NOTE]
In this context, component refers to a software component (e.g., function, module, service, or feature). It does not refer to PromptPro prompt components.

Here are good alternatives to **component** depending on context, so you can keep it flexible and reusable:

#### General / Neutral Alternatives

| Term             | When to Use                            |
| ---------------- | -------------------------------------- |
| `component`      | Generic, works in almost any context   |
| `function`       | Standard unit of logic in most programming languages |
| `module`         | Grouped or encapsulated logic          |
| `unit`           | Smallest testable piece (unit testing) |
| `logic`          | Abstract behavior or rules             |
| `implementation` | Concrete code realization              |

#### Backend / API Context

| Term        | When to Use              |
| ----------- | ------------------------ |
| `endpoint`  | HTTP/API routes          |
| `handler`   | Request processing logic |
| `service`   | Business logic layer     |
| `operation` | Defined backend action   |

#### Application / System Level

| Term              | When to Use                    |
| ----------------- | ------------------------------ |
| `feature`         | User-facing functionality      |
| `workflow`        | Multi-step processes           |
| `process`         | System or background execution |
| `system_behavior` | High-level system actions      |

#### Algorithms / Data Processing

| Term        | When to Use               |
| ----------- | ------------------------- |
| `algorithm` | Computational logic       |
| `routine`   | Reusable procedural logic |
| `procedure` | Step-by-step operations   |

#### Testing-Oriented (Recommended)

| Term              | When to Use                    |
| ----------------- | ------------------------------ |
| `unit_under_test` | Most precise, testing-focused  |
| `target_logic`    | Focus on behavior being tested |
| `test_subject`    | Generic testing reference      |

### List And Show

```bash
pp list content/dev/testing | edge
pp show content/dev/testing/boundary_edge_cases
```

### Example With `build`

```bash
pp build dev/software_testing_agent --var-file action=content/dev/testing/boundary_edge_cases
```

### Example With `compose`

```bash
pp compose \
  --role dev/software_tester \
  --task action \
  --pattern testing_strict \
  --var-file action=./content/dev/testing/boundary_edge_cases
```

## Content: `puzzle`

### Description

Provides a logical puzzle scenario designed to be analyzed and explained step by step, encouraging reasoning, deduction, and clear justification of conclusions.

### List And Show

```bash
pp list content | grep puzzle
pp show content/puzzle
```

### Example

```bash
pp compose \
  --role tutor \
  --task explain \
  --pattern socratic \
  --var-file input=content/puzzle.md
```
