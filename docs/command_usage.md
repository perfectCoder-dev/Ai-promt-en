# PromptPro Command Syntax

## General Structure

```bash
pp <command> [options]
```

## Listing Components

```bash
pp list <component>
```

**Components:**

* `roles`
* `agents`
* `pattern_groups`
* `patterns`
* `tasks`

**Example:**

```bash
pp list roles
```

**With filtering:**

```bash
pp list roles | grep -E '<pattern>'
```

## Build (Agent-Based Prompt Generation)

```bash
pp build <agent> --var <key>=<value> [--var <key>=<value> ...] [--copy]
```

**Parameters:**

* `<agent>` → Agent preset name
* `--var` → Inject variables into the prompt
* `--copy` → Copy output to clipboard

**Example:**

```bash
pp build math_tutor --var input="Explain recursion"
```

## Compose (Component-Based Prompt Generation)

```bash
pp compose \
  --role <role> \
  --task <task> \
  --pattern <pattern> [--pattern <pattern> ...] \
  [--var <key>=<value> ...] \
  [--var-file <key>=<path> ...] \
  [--var-dir <key>=<path> ...] \
  [--copy]
```

**Parameters:**

* `--role` → Role component
* `--task` → Task definition
* `--pattern` → One or more reasoning/output patterns
* `--var` → Inline variable
* `--var-file` → Load variable from file
* `--var-dir` → Load variable from directory (recursive)
* `--copy` → Copy output to clipboard

**Example:**

```bash
pp compose \
  --role tutor \
  --task explain \
  --pattern socratic \
  --pattern step_by_step \
  --var input="Gravity"
```

## Output Redirection

```bash
pp <command> > <file>
```

**Example:**

```bash
pp build math_tutor --var input="Explain recursion" > my_prompt.txt
```

## Pipelines

```bash
pp <command> | <external_command> [| <external_command> ...]
```

**Example:**

```bash
pp build math_tutor --var input="Explain recursion" \
| ollama run llama3 \
| espeak-ng
```

## Bash Integration

```bash
pp build <agent> --var <key>="${variable}"
```

**Example:**

```bash
pp build math_tutor --var input="Explain ${topic} in ${language}"
```

## Notes

* Multiple `--pattern` and `--var` flags are supported.
* Variable precedence:

  ```text
  --var → --var-file → --var-dir
  ```
* Output is plain text, enabling seamless Unix-style composition.

## Command Examples

[Command Examples](./command_examples.md)