# PromptPro 🎯

![Python](https://img.shields.io/badge/python-3.9–3.13-blue)
![License](https://img.shields.io/github/license/estebantechdev/prompt-pro)

<p align="center">
  <img src="images/pp-banner.jpg" alt="PromptPro banner" width="900">
</p>

<p align="center">
  <strong>A control plane for composable AI prompting</strong>
</p>

## 📖 Overview

PromptPro is a modular CLI for composing, managing, and orchestrating reusable AI prompt components.

Instead of storing static snippets, PromptPro treats prompts as structured building blocks — roles, tasks, and reasoning patterns — that can be assembled, parameterized, and reused across projects.

Designed for users who think in systems, not snippets.

 🧱 Why Prompt Pro?

- 🧱 Modular prompt components
- 🧠 Role + task + pattern composition
- 🔁 Agent presets
- 🧩 Variable injection
- 📋 Clipboard export
- ⚡ Terminal-native workflow
- 🗂 Version-controlled prompts

## 📥 Quick Install

```shell
# Get the source code
git clone https://github.com/estebantechdev/prompt-pro.git

# Enter the project directory
cd prompt-pro

# Create virtual environment (optional)
python3 -m venv .venv
source .venv/bin/activate  # Activate it

# Install dependencies
python -m pip install -r requirements.txt  # For normal users
python -m pip install -r requirements-lock.txt  # For developers / CI

# Make executable
chmod +x main.py

# Install system-wide
sudo ln -s "$(pwd)/main.py" /usr/local/bin/pp
```

#### 🐧 Linux Prerequisite (Debian/Ubuntu)

If you are using Debian-based systems (such as Ubuntu) and encounter an error when creating a virtual environment, you may need to install the `venv` package:

```bash
sudo apt update
sudo apt install python3-venv
```

## 🧪 Usage Examples

### Listing Prompt Components

#### Roles

List available roles:

```bash
pp list roles
```

Filter results using multiple patterns (`te` or `utor`):

```bash
pp list roles | grep -E 'te|utor'
```

Example output:

```text
technical_instructor
tutor
```

> [!NOTE]
> The `list` command also works with:
> - `agents`
> - `pattern_groups`
> - `patterns`
> - `tasks`

### Creating A Prompt With `build`

> [!NOTE]
> PromptPro supports two workflows:
> - `build` generates a prompt using a predefined **agent preset**.
> - `compose` generates a prompt by manually combining **role**, **task**, and **pattern** components.

Create a prompt using a predefined agent:

```bash
pp build math_tutor --var input="Explain recursion"
```

Copy the generated prompt directly to the clipboard:

```bash
pp build math_tutor --var input="Explain recursion" --copy
```

### `compose` A Prompt From Components

Compose a prompt by combining a `role`, `task`, and `pattern`:

```bash
pp compose \
  --role tutor \
  --task explain \
  --pattern step_by_step \
  --var input="Boolean algebra simplification"
```

Including multiple patterns and variables:

```bash
pp compose \
  --role tutor \
  --task explain \
  --pattern socratic \
  --pattern step_by_step \
  --var input="Gravity: Force vs Curvature of Space" \
  --var theorist="Albert Einstein"
```

> [!NOTE]
Replacing "Albert Einstein" with "Isaac Newton" will result in different AI responses.
>
> The variable `theorist` does not exist in the default version of the task `explain`.

## 💉 Using `--var` Variables

To inject dynamic values into your prompt, the template must reference them using *Jinja* syntax.

Your **task file** (inside `tasks/`) must include at least one variable placeholder. For example:

```django
{{ input }}
```

The variable name in the template must match the key used in the command line.

> [!NOTE]
> If you omit the `--var` parameter, the prompt will be generated without injected values. This allows you to preview, copy, or reuse the base prompt structure independently.

## 📁 Variable Sources

PromptPro supports three types of variable sources:

### 1. Literal Variables (--var)

Pass a value directly from the command line.

```bash
pp compose \
  --role tutor \
  --task explain \
  --pattern socratic \
  --var input="Random text"
```

### 2. Single File (--var-file)

Load the variable value from a file (for example: .txt or .md).

```bash
pp compose \
  --role tutor \
  --task explain \
  --pattern socratic \
  --var-file input=./texts/puzzle.txt
```

The entire file content becomes the variable value.

### 3. Recursive Directory (--var-dir)

Load variable content from all files inside a directory (recursively).

```bash
pp compose \
  --role tutor \
  --task explain \
  --pattern socratic \
  --var-dir input=./texts \
  --copy
```

All file contents are combined into a single variable value.

### Combining All Variable Types

You can combine multiple variable sources in the same command:

```bash
pp compose \
  --role tutor \
  --task explain \
  --pattern didactic \
  --var input="Random text" \
  --var-file input2=./texts/puzzle.txt \
  --var-dir input3=./texts \
  --copy
```

This allows complex prompt construction from multiple sources.

> [!NOTE]
The variables `input2` and `input3` don't exist in the default version of the task `explain`.

#### ⚠️ Variable Overwriting Behavior

> [!IMPORTANT]
> If the same variable name is used multiple times, the **last processed value overrides previous ones**.
> * Processing order: `--var` → `--var-file` → `--var-dir`

Example:

```bash
pp compose \
  --role tutor \
  --task explain \
  --pattern didactic \
  --var input="Random text" \
  --var-file input=./texts/puzzle.txt \
  --var-dir input=./texts \
  --copy
```

> [!TIP]
> ✔ Use unique variable names whenever possible.  
> ✔ Declare expected variables clearly in your task templates.  
> ✔ Reuse variable names only when intentional overwriting is desired.

## ⚙️ Types Of Tasks

By default, PromptPro provides two main types of tasks: `explain` and `action`, which together cover most AI-human interaction scenarios.

▶️ Action — Start / Run the task and produce a result.  
💬 Explain — Describe the reasoning without performing any tasks.

We introduced the explain task in the previous examples. Now it's time to look at a couple of examples using the action task.

### Creating Action Prompts With `build`

To create an action prompt with `build`, you must use the `action_agent` agent and pass a **single variable** named `action` as a command parameters. The **entire action request** must be included as the value of `action` after the `=` sign.

Example:

```bash
pp build action_agent --var action="Make a shopping list"
```

### Creating Action Prompts With `compose`

To create an action prompt with `compose`, you must use the `action_agent` agent and pass a **single task** named `compose_action` in the command parameters. The action request must be **composed** using the `action` variable. The `context` and `examples` variables are optional, but their use is strongly recommended in most cases.

The following example includes `context` and `examples`, which help an AI language model interpret the request more accurately and produce more reliable output:

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

## 📘 Tutorials

Want a step-by-step guide to **creating new agents, roles, tasks, and patterns**?

🔗 [Creating And Using New Prompt Components](docs/creating_new_prompt_components.md)

Complete tutorial on how to create and use a pattern group.

🔗 [Creating And Using Pattern Groups](docs/create_and_use_a_pattern_group.md)

## 🗂 Prompt Components

The `prompts/` directory contains the core components used to build prompts in PromptPro.

Each subdirectory represents a specific type of component such as roles, tasks, patterns, or agent presets.

See the **complete reference**:

🔗 [Prompt Components Reference](docs/prompt_components_reference.md)

## 🧠 Concepts

Understanding modern prompting frameworks helps you use PromptPro more effectively.

🔗 [The Iceberg Of Prompting](docs/the_iceberg_of_prompting.md)

## 🤝 Contributions

Contributions are highly encouraged — especially new prompt components.

You can contribute:

- New **roles** (teaching styles, expert personas, system behaviors)
- New **tasks** (analysis, critique, summarization, transformation, etc.)
- New **patterns** (reasoning frameworks, output formats, cognitive constraints)
- New **pattern groups** (reusable bundles that combine multiple patterns into higher-level behavioral modes)
- New **agent presets** that combine existing components
- Documentation improvements and examples

PromptPro becomes more powerful as its library of components grows.

If you’ve built something reusable, open a pull request and help expand the ecosystem.

## 📜 License

This project is licensed under the [GPL-3.0](LICENSE) - see the [LICENSE](LICENSE) file for details.
