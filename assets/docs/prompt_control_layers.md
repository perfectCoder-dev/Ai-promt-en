# Prompt Control Layers

PromptPro introduces **control layers** to separate how a prompt is executed from how its output is shaped.

This enables a more **engineered, predictable, and modular prompting system**.

## Core Idea

PromptPro distinguishes between two types of control:

### 🟦 Pre-Prompt Controls (Execution Layer)

Define how the system operates **before generating any response**.

* Execution environment setup

* Model and system behavior

* Memory and tool configuration

**Pre-prompt = deterministic intent**: you configure the *system*.

### 🟩 Post-Prompt Controls (Behavior Layer)

Define how the response is shaped **after generation begins**.

* Output formatting

* Tone and style

* Constraints and safeguards

**Post-prompt = probabilistic influence**: you guide the *behavior/output*.

## Control Strength

This separation reflects how *LLMs* actually behave:

* **Pre controls → stronger, structural influence**
* **Post controls → softer, behavioral influence**

## Final Insight

You now have a system where:

* **Pre controls → shape how the AI thinks**
* **Post controls → shape how the AI speaks**

This separation is what makes PromptPro **powerful, composable, and predictable**.

## CLI Usage Example

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

> [!NOTE]
> This agent file is a controlled variant of `action_agent`. It includes a `pre` control named `forget`, located at `controls/pre/memory/forget.md`, and defines no `post` controls (`post: []`).

The command:

```bash
pp build action_agent_controlled --post truth/say_dont_know --var action="Make a list of the core skills everyone should have."
```

> [!NOTE]
> This example combines controls defined in the agent YAML with controls specified via the command line.

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
pp list roles
pp list controls/pre/mode
```

### The Command `show`

`show` works on a file path (without extension.)

```bash
pp show controls/pre/mode/agent
pp show controls/post/truth/say_dont_know
```

## Built-in Prompt Controls List

All Prompt Controls are located in `prompts/controls`.

### 🟦 Built-in Pre-Prompts (Execution Controls)

These define how the system runs before any response is produced.

```bash
pre
├── config
│   └── configurations.md
├── language
│   └── input_default.md
├── mcp
│   ├── mcp_local.md
│   └── mcp_remote.md
├── memory
│   └── forget.md
├── mode
│   ├── agent.md
│   ├── ask.md
│   └── plan.md
├── model
│   ├── model_fast.md
│   └── model_thinking.md
├── security
│   └── no_env_access.md
├── system
│   └── system_prompt.md
└── tools
    ├── tools_call.md
    ├── tools_define.md
    ├── tools_off.md
    └── tools_on.md
```

### 🟩 Built-in Post-Prompts (Behavior Controls)

These shape how the answer is generated and presented.

```bash
post
├── limits
│   ├── explain_like_12.md
│   └── for_beginners.md
├── tone
│   └── tone_style.md
├── translation
│   ├── translate_en.md
│   ├── translate_output.md
│   └── translate_sp.md
└── truth
    └── say_dont_know.md
```

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
