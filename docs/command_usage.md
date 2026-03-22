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
* `controls`

**Example:**

```bash
pp list roles
```

**With filtering:**

```bash
pp list roles | grep -E '<pattern>'
```

### Listing Controls

```bash
pp list controls/<pre|post>/<category>
```

**Categories:**

* `pre` → Pre-processing controls (mode, language, memory)
* `post` → Post-processing controls (translation, limits, truth)

**Example:**

```bash
pp list controls/pre/mode
pp list controls/post/translation
```

## Showing Components

```bash
pp show <component>/<name>
pp show controls/<pre|post>/<category>/<name>
```

## Showing Content

```bash
pp show ../content/<category>/<name>
pp show <path-to-file>
```

**Components:**

* `agents` → Agent presets
* `patterns` → Reasoning/output patterns
* `pattern_groups` → Pattern groups
* `tasks` → Task definitions
* `roles` → Role definitions
* `controls` → Pre/post processing controls

**Example:**

```bash
pp show agents/cs_instructor
pp show patterns/step_by_step
pp show tasks/compose_action
pp show controls/pre/mode/agent
pp show controls/post/truth/say_dont_know
```

## Theme Selection (Output Styling)

```bash
pp --theme <theme> <command> [options]
```

Apply syntax highlighting themes to the output of supported commands.

**Supported commands:**

* `show`
* `build`
* `compose`

**Parameters:**

* `--theme` → Syntax highlighting theme (e.g., `dracula`, `monokai`, `friendly`, `default`, `vim`)

**Examples:**

```bash
pp --theme monokai show tasks/explain
pp --theme friendly show ../content/dev/testing/boundary_edge_cases
pp --theme dracula build math_tutor --var input="Explain recursion"
pp --theme default compose --role tutor --task explain --pattern step_by_step --var input="Boolean algebra simplification"
```

**Notes:**

* The `--theme` option must be placed **before the command**.
* If not specified, the default theme is `dracula`.
* Themes affect only terminal rendering and do not modify the generated content.

## Build (Agent-Based Prompt Generation)

```bash
pp build <agent> \
  [--pre <pre_control> ...] \
  [--post <post_control> ...] \
  --var <key>=<value> [--var <key>=<value> ...] \
  [--copy]
```

**Parameters:**

* `<agent>` → Agent preset name
* `--pre` → Pre-processing control (e.g., model selection, memory)
* `--post` → Post-processing control (e.g., translation, truthfulness)
* `--var` → Inject variables into the prompt
* `--copy` → Copy output to clipboard

**Example:**

```bash
pp build math_tutor --var input="Explain recursion"
```

**Example with controls:**

```bash
pp build math_tutor \
  --pre model/model_fast \
  --pre memory/forget \
  --post translation/translate_sp \
  --post truth/say_dont_know \
  --var input="Linear Algebra"
```

## Compose (Component-Based Prompt Generation)

```bash
pp compose \
  [--pre <pre_control> ...] \
  [--post <post_control> ...] \
  --role <role> \
  --task <task> \
  --pattern <pattern> [--pattern <pattern> ...] \
  [--var <key>=<value> ...] \
  [--var-file <key>=<path> ...] \
  [--var-dir <key>=<path> ...] \
  [--copy]
```

**Parameters:**

* `--pre` → Pre-processing control (e.g., model selection, memory)
* `--post` → Post-processing control (e.g., translation, truthfulness)
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

**Example with controls:**

```bash
pp compose \
  --pre model/model_fast \
  --pre memory/forget \
  --role technical_instructor \
  --task explain \
  --pattern step_by_step \
  --post limits/for_beginners \
  --var input="Switch"
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
