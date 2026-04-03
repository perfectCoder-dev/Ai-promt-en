# Prompt Controls

PromptPro uses **control layers** to separate how a prompt runs from how its output is shaped. This makes prompts more **predictable, modular, and easier to manage**.

## 🟦 Pre-Prompt Controls (Execution Layer)

Pre-prompt controls define how the system operates **before generating a response**. They configure the execution environment, model behavior, and memory or tool usage.

These are implemented as **built-in execution controls**, giving you **strong, deterministic influence** over how the AI processes requests.

Use pre-prompt controls when you need consistency, reliability, and precise system behavior.

## 🟩 Post-Prompt Controls (Behavior Layer)

Post-prompt controls define how the response is shaped **during generation**. They guide output formatting, tone, style, and enforce constraints or safeguards.

These are implemented as **built-in behavior controls**, providing **flexible, probabilistic influence** over how the response is expressed.

Use post-prompt controls when you want to refine presentation and communication style.

## 🟥 Control Precedence

Understanding how control layers interact is essential when combining multiple controls.

While prompt order can influence behavior, **precedence in PromptPro is determined by control layers—not position alone**.

PromptPro follows a layered structure:

```txt
[PRE CONTROLS]        → Configuration (how the AI thinks)
[ROLE / TASK / INPUT] → Intent (what the AI does)
[POST CONTROLS]       → Output shaping (how the AI speaks)
[ENFORCE CONTROLS]    → Final validation (what is allowed)
```

Each layer has a distinct role:

* **Pre (`--pre`)** establishes configuration and constraints
* **Input (role/task/user)** introduces intent and potential conflicts
* **Post (`--post`)** refines how the response is expressed
* **Enforce (`--enforce`)** applies final validation and override rules

> [!TIP]
> Effective prompting in PromptPro relies on a hybrid approach:
> **use `pre` to define behavior and `enforce` to guarantee it.**

---

By combining these layers, PromptPro enables a **structured and composable approach to prompting**, making it easier to build clear, reusable, and reliable AI interactions.

## Usage

### Using `build`

#### Without Controls Declared In The Agent YAML File

```bash
pp build math_tutor \
  --pre model/model_fast \
  --pre memory/forget \
  --post translation/translate_sp \
  --post truth/say_dont_know \
  --var input="Linear Algebra"
```

#### With Controls Declared In The Agent YAML File

```bash
pp build action_agent_controlled --post truth/say_dont_know --var action="Make a list of the core skills everyone should have."
```

This example combines controls defined in the agent *YAML* with controls specified via the command line.

The agent preset `action_agent_controlled` is a "controlled" variant of `action_agent`. It includes a `pre` control named `forget` and defines no `post` controls (`post: []`).

action_agent_controlled.yaml:

```yaml
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

The prompt control `forget` is located at  `path/to/promptpro/prompts/controls/pre/memory/forget.md`

More information about YAML: 🔗 [YAML FIle Configuration](yaml_file_configuration.md).

### Using `compose`

#### Basic

```bash
pp compose \
  --role tutor \
  --task explain
```

#### With Control Layers

```bash
pp compose \
  --pre model/model_fast \
  --pre memory/forget \
  --role tutor \
  --task explain \
  --pattern socratic \
  --post translation/translate_sp \
  --post truth/say_dont_know \
  --var input="Linear Algebra"
```

## Exploring Controls

### The Command `list`

`list` works on directories (categories and subcategories.)

```bash
pp list controls/pre/memory
pp list controls/pre/mode
pp list roles
```

### The Command `show`

`show` works on a file path (without extension.)

To view `agents` content:

```bash
pp show agents/action_agent_controlled
```
To view `controls` content:

```bash
pp show controls/pre/memory/forget
pp show controls/pre/mode/agent
pp show controls/post/truth/say_dont_know
```

## Built-in Prompt Controls

All Built-in Prompt Controls are located in: `/path/to/promptpro/prompts/controls`.

Many built-in prompt controls align with corresponding elements in [🔗 The Iceberg Of Prompting](the_iceberg_of_prompting.md) framework.

🔗 [Here](./prompts/controls/built-in_controls.md#control-preconfigconfigurations) is an example illustrating **control precedence** using `--pre` and `--enforce` controls.

You can find a complete list of **built-in prompt controls** in the [🔗 Prompt Components Reference](prompt_components_reference.md#-built-in-controls).

## ⚠️ Caveats

Control behavior depends on the **AI model and application environment**.

Some controls may:

  * Conflict with each other
  
  * Override or weaken other controls

  * Clash with system or platform limitations

✔ Always test configurations in your target environment

### Example 1: Dual-Layer Controls

Some concepts can exist in both layers.

**Language** is a good example:

* Pre → default working language

* Post → final output language (translation)

Suggested naming:

* **Input Language (`pre`)**

```bash
pp show controls/pre/language/input_default
```

* **Output Language (`post`)**

```bash
pp list controls/post/translation
```

Built-in options available (you can create yours):

```output
translate_en
translate_output
translate_sp
```

### Example 2: Using PromptPro Variables Instead Of Controls

You can bypass control layers by embedding everything in a variable.

### Without Controls

#### With `build`

```bash
pp build cs_instructor --var input="Switch, explained for beginners"
```

### With Controls

```bash
pp show agents/cs_instructor
```

Output:

```output
role: technical_instructor
task: explain
patterns:
  - step_by_step
  - structured_output

```

Using `list`:

```bash
pp list controls/post/limits
```

Output:

```output
explain_like_12
for_beginners
```

Using `show`:

```bash
pp show controls/post/limits/for_beginners
```

Output:

```output
Adjust the explanation for beginners.

- Use simple language
- Avoid complex terminology
- Provide intuitive explanations

```

#### With `compose`

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

### Example 3: Overlapping Behavior

Some behaviors can appear across.

**Example**

* Patterns (`step_by_step`, `plan_execute`)
* Tasks (`compose_action`)
* Post controls (`explain_like_12`)

You must decide which one(s) you are going to use.

If you **do not want those behaviors**, you must remove them from you `build` `compose` command.

* Patterns

  ```bash
  pp show patterns/step_by_step
  pp show patterns/plan_execute
  ```

* Tasks

  ```bash
  pp show tasks/compose_action
  ```

* Control layers

  ```bash
  pp show controls/post/limits/explain_like_12
  ```

### Example 4: Over-Constrained Systems

Too many controls can make an agent:

* Rigid
* Over-specialized
* Unable to generalize

Avoid overly restrictive configurations unless necessary.

## Customization & Extensibility

PromptPro is designed to be **fully customizable**.

You are encouraged to:

* Create new **pre/post control categories**

* Add new **control files**

* Restructure directories to match your workflow

* Adapt naming conventions to your domain

There is no fixed “correct” structure — only what works best for your system.

### Design Philosophy

* Treat controls as **modular building blocks**

* Prefer **composition over complexity**

* Keep configurations **testable and observable**

### Final Thought

Control layers turn prompting from a **textual trick** into a **system design discipline**.

They allow you to move from:

> “writing prompts”

to

> “engineering AI behavior”
