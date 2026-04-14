# PromptNG Command Usage

## General Structure

```bash
pp <command> [options]
```

## Command Syntax (Quick Reference)

```plaintext
Commands:
    search:
        Search across components using flexible matching (exact, prefix, substring, wildcard).
        Usage: pp [--theme THEME] search <query> [--category <name>] [--limit N] [--json]

    list:
        List available items in a given category.
        Usage: pp [--theme THEME] list <category>

    show:
        Display the contents of a resource with syntax highlighting.
        Usage: pp [--theme THEME] show <path>

    build:
        Compose a prompt from an agent definition.
        Usage: pp [--theme THEME] build <agent> [--pre ...] [--post ...] [--enforce ...]
                                                [--var key=value] [--var-file key=path]
                                                [--var-dir key=dir] [--copy]

    compose:
        Manually compose a prompt from role, task, and patterns.
        Usage: pp [--theme THEME] compose [--role ROLE] [--task TASK] [--pattern ...]
                                          [--pre ...] [--post ...] [--enforce ...]
                                          [--var key=value] [--var-file key=path]
                                          [--var-dir key=dir] [--copy]
```

## Searching Components

Search across `agents`, `content`, `controls`, `pattern_groups`, `patterns`, `projects`, `skills`, and `tasks` components using flexible matching.

It supports ranking, and is useful for discovering reusable building blocks.

### Usage

```bash
pp search <query> [--category <name>] [--limit N] [--json]
```

### Examples

#### Complete Words

```bash
pp search math_tutor
pp search guard
```

#### Wildcards

```bash
pp search cs*
pp search *tor
pp search *config*
```

#### Prefix / Suffix

```bash
pp search cs_
pp search _instructor
```

#### Strings With Spaces

```bash
pp search "🌐 Web"
pp search "🌐 Web Research"
```

#### Multi-Keyword Search

```bash
pp search "config math web"
```

#### Filter By Category

```bash
pp search socratic --category agents
pp search socratic --category patterns
```

#### Limit Results

```bash
pp search mode --limit 1
pp search mode --limit 8
```

#### JSON Output (Agent Mode)

```bash
pp search language --json
```

### Output Format

```text
[category] name  (score: X)
  → /category/path
```

### Matching Behavior

Results are ranked using a relevance **score**, based on how closely they match the query across filename, category, and content:

* **Exact match (filename)** → highest score, heavily boosted
* **Prefix match (filename)** → very high score
* **Substring match (filename)** → medium score
* **Content matches** → lower weight, cumulative
* **Category matches** → small boost
* **Wildcard match (`*`)** → flexible matching with adjusted scoring

Additional boosts are applied when the query closely matches the **filename** or **category**, ensuring that the most relevant files appear first even if content is similar.

**Example output (ordered by score)**

```text
[patterns] config              (score: 18.5)
[patterns] config_loader       (score: 12.0)
[patterns] app_config_loader   (score: 9.5)
[patterns] legacy_sys_config   (score: 6.0)
```

> [!NOTE]
Scores are relative and only meaningful within the same search.

> [!NOTE]
File content evaluation is limited to the first 2000 characters for performance.

> [!NOTE]
> Only files with supported extensions (`.md`, `.yaml`, `.json`, `.txt`) are scanned by `search`. Files without an extension are ignored.
>
> To include them, rename files like `my_component` to `my_component.yaml` or `my_component.md`.

## Listing Components

```bash
pp list <category>
```

**Categories**

- `agents` → Agent presets
- `roles` → Role definitions
- `content` Raw content files (external or user-provided resources)
- `controls` → Pre/post/enforce processing controls
- `pattern_groups` → Pattern groups
- `patterns` → Reasoning/output patterns
- `tasks` → Task definitions

**Example**

```bash
# Single category
pp list roles

# Subcategories
pp list roles/dev
```

**Filtering with single patterns**

```bash
# Linux / macOS
pp list roles | grep -E '<pattern>'

# Windows (PowerShell)
pp list roles | findstr '<pattern>'
```

**Filtering with multiple patterns**

```bash
# Linux / macOS
pp list roles | grep -E '<pattern1>|<pattern2>'

# Windows (PowerShell)
pp list roles | Select-String -Pattern "<pattern1>|<pattern2>"
```

### Listing Controls

```bash
pp list controls/<pre|post|enforce>/<category><name>
```

**Categories**

* `pre` → Pre-processing controls (mode, language, memory)
* `post` → Post-processing controls (translation, limits, truth)
* `enforce` → Final validation controls (policies, safety rules, hard constraints, output restrictions)

**Example**

```bash
pp list controls/pre/mode
pp list controls/post/translation
pp list controls/enforce/config
```

## Showing Components

```bash
# With a single category
pp show <category>/<name>

# With subcategories (e.g., controls)
pp show controls/<pre|post|enforce>/<category>/<name>
```

### Showing Content

```bash
# With a single subcategory
pp show content/<category>/<name>
```

**Example**

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

**Supported commands**

* `show`
* `build`
* `compose`

**Parameters**

* `--theme` → Syntax highlighting theme (e.g., `dracula`, `monokai`, `friendly`, `default`, `vim`)

**Examples**

```bash
pp --theme monokai show tasks/explain
pp --theme friendly show content/dev/testing/boundary_edge_cases
pp --theme dracula build math_tutor --var input="Explain recursion"
pp --theme default compose --role tutor --task explain --pattern step_by_step --var input="Boolean algebra simplification"
```

**Notes**

* The `--theme` option must be placed **before the command**.
* If not specified, the default theme is `dracula`.
* Themes affect only terminal rendering and do not modify the generated content.

## Build (Agent-Based Prompt Generation)

```bash
pp build <agent> \
  [--pre <pre_control> ...] \
  [--post <post_control> ...] \
  [--enforce <enforce_control> ...] \
  --var <key>=<value> [--var <key>=<value> ...] \
  [--copy]
```

**Parameters**

* `<agent>` → Agent preset name
* `--pre` → Pre-processing control (e.g., model selection, memory)
* `--post` → Post-processing control (e.g., translation, truthfulness)
*  `--enforce` → Enforce-processing control (e.g., configurations_guard, Configurations_guard_hardened)
* `--var` → Inject variables into the prompt
* `--copy` → Copy output to clipboard

**Example**

```bash
pp build math_tutor --var input="Explain recursion"
```

**Example with controls**

```bash
pp build math_tutor \
  --pre model/model_fast \
  --pre memory/forget \
  --pre config/configurations \
  --post translation/translate_sp \
  --post truth/say_dont_know \
  --enforce config/configurations_guard_hardened \
  --var input="Linear Algebra"
```

> [!NOTE]
> This example is intentionally over-configured and may not represent a practical or meaningful setup.
> 
> It is used to demonstrate how multiple control layers (`pre`, `post`, and `enforce`) can be combined.

## Compose (Component-Based Prompt Generation)

```bash
pp compose \
  [--pre <pre_control> [--pre <pre_control> ...]] \
  --role <role> \
  --task <task> \
  --pattern <pattern> [--pattern <pattern> ...] \
  [--post <post_control> [--post <post_control> ...]] \
  [--enforce <enforce_control> [--enforce <enforce_control> ...]] \
  [--var <key>=<value> ...] \
  [--var-file <key>=<path> ...] \
  [--var-dir <key>=<path> ...] \
  [--copy]
```

**Parameters**

* `--pre` → Pre-processing control (e.g., model selection, memory)
* `--role` → Role component
* `--task` → Task definition
* `--pattern` → One or more reasoning/output patterns
* `--post` → Post-processing control (e.g., translation, truthfulness)
* `--enforce` → Enforce-processing control (e.g., configurations_guard, Configurations_guard_hardened)
* `--var` → Inline variable
* `--var-file` → Load variable from file
* `--var-dir` → Load variable from directory (recursive)
* `--copy` → Copy output to clipboard

**Example**

```bash
pp compose \
  --role tutor \
  --task explain \
  --pattern socratic \
  --pattern step_by_step \
  --var input="Gravity"
```

**Example with controls**

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

**Example**

```bash
pp build math_tutor --var input="Explain recursion" > my_prompt.txt
```

## Pipelines

```bash
pp <command> | <external_command> [| <external_command> ...]
```

**Example**

```bash
pp build math_tutor --var input="Explain recursion" \
| ollama run llama3 \
| espeak-ng
```

## Bash Integration

```bash
pp build <agent> --var <key>="${variable}"
```

**Example**

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

🔗 [Command Examples](./command_examples.md)
