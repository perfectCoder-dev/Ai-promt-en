# Prompt Controls

PromptNG uses **control layers** to separate how a prompt runs from how its output is shaped, making prompts more predictable, modular, and easier to manage.

These layers help provide a structured and composable approach to prompting, enabling clear, reusable, and reliable AI interactions.

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

While prompt order can influence behavior, **precedence in PromptNG is determined by control layers—not position alone**.

PromptNG follows a layered structure:

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
> Effective prompting in PromptNG relies on a hybrid approach:
> **use `pre` to define behavior and `enforce` to guarantee it.**

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

The prompt control `forget` is located at  `/path/to/promptng/prompts/controls/pre/memory/forget.md`

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

Many built-in prompt controls align with corresponding elements in [🔗 The Iceberg Of Prompting](the_iceberg_of_prompting.md) framework and existing *agentic systems*.

All Built-in Prompt Controls are located at: `/path/to/promptng/prompts/controls`.

Within this directory, you can organize controls by creating additional **category** and **subcategory** folders, as well as **define new control files**.

### 🟦 🟩 Built-in Controls List

You can find a complete list of **built-in prompt controls** in the [🔗 Prompt Components Reference](prompt_components_reference.md#-built-in-controls).

### 🟥 Control Precedence

🔗 [Here](./prompts/controls/built-in_controls.md#control-preconfigconfigurations) is an example illustrating **control precedence** using `--pre` and `--enforce` controls.

## Limitations

While PromptNG introduces a structured and layered approach to prompt engineering, it does not remove the fundamental constraints of large language models (LLMs). In fact, highly detailed and deeply layered prompts can introduce their own challenges. As prompts grow in size and complexity—especially when combining multiple control layers, patterns, and variables—the model may struggle to consistently interpret and prioritize all instructions.

This can lead to reduced output quality, weaker adherence to controls, or unexpected behavior. Understanding the underlying limitations of model processing is essential when designing robust PromptNG configurations.

### Context Window

Large language models operate within a finite **context window**, which defines how much input text can be processed at once. This includes everything: pre-controls, role/task definitions, user input, post-controls, and any embedded variables.

When prompts become extremely large:

* **Important instructions may be truncated** if the total input exceeds the model’s capacity
* **Earlier context (such as pre-controls)** may lose influence as newer tokens dominate the window
* **Signal dilution occurs**, where critical instructions are buried within excessive detail

In PromptNG, this is especially relevant because multiple layers are composed into a single prompt. Overloading the context window with too many controls, long descriptions, or verbose variables can reduce clarity and effectiveness.

✔ **Guideline:** Keep prompts concise and prioritize high-impact controls. Avoid unnecessary verbosity in control definitions and inputs.

### Attention Window

Even within the available context window, models do not treat all tokens equally. They rely on attention mechanisms that prioritize certain parts of the input over others. This creates a practical **attention window**, where some instructions receive more focus than others.

With extremely detailed prompts:

* **Instruction competition** can occur between control layers (e.g., `pre` vs `post`)
* **Later or more explicit instructions** may override earlier ones unintentionally
* **Conflicting or redundant controls** can fragment attention and reduce coherence
* **Over-specification** can make the model less flexible, leading to rigid or unnatural outputs

In PromptNG, this is particularly important because layered controls are designed to interact. If too many constraints are applied, or if they overlap semantically, the model may fail to properly balance them.

✔ **Guideline:** Design control layers with clear separation of responsibility. Minimize overlap, avoid redundancy, and ensure that the most critical instructions are prominent and unambiguous.

---

In practice, effective PromptNG usage is not about maximizing detail, but about **optimizing signal clarity within model constraints**.

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

### Example 2: Using PromptNG Variables Instead Of Controls

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

PromptNG is designed to be **fully customizable**.

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
