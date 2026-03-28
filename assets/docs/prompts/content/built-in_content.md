# Built-in Content

Content components provide structured input that can be injected into prompts as variables, enabling agents to work with real data. These components are typically stored as files (e.g., `.md` or `.txt`) and loaded using variable sources like `--var-file` for single inputs or `--var-dir` for aggregating multiple files. This allows you to separate what the prompt operates on from how it behaves, making it easy to reuse the same content across different roles, tasks, and patterns. Content components make prompt construction more flexible, scalable, and maintainable.

> [!TIP]
Content components can also include template placeholders (e.g., **{{ text }}**). While you can use different placeholder styles such as **[ text ]** or **<< text >>**, using Jinja-style syntax (**{{ ... }}**) is recommended to take full advantage of PromptPro’s syntax highlighting and color theme support. Templating content in this way helps avoid creating multiple agent presets for similar tasks with only minor differences, improving reuse and maintainability.

> [!CAUTION]
Although the `--var-dir` option allows you to inject large amounts of content by aggregating multiple files, it is generally not suitable for templated content, as the resulting prompt can become excessively large and require significant manual editing after copying before it is ready to be submitted to an AI model.

## Content: `boundary_edge_cases`

### Description

Generates boundary and edge case test scenarios for a given function, including invalid inputs, null values, and memory constraints to ensure robustness and reliability under extreme conditions.

#### List And Show

```bash
pp list content/dev/testing | edge
pp show content/dev/testing/boundary_edge_cases
```

#### Example

```bash
pp build software_tester --var-file=content/dev/testing/boundary_edge_cases
```

## Content: `puzzle`

### Description

Provides a logical puzzle scenario designed to be analyzed and explained step by step, encouraging reasoning, deduction, and clear justification of conclusions.

#### List And Show

```bash
pp list content | grep puzzle
pp show content/puzzle
```

#### Example

```bash
pp compose \
  --role tutor \
  --task explain \
  --pattern socratic \
  --var-file input=content/puzzle.md
```
