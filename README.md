# promptctl 🚩

<p align="center">
  <img src="images/promptctl-banner.jpg" alt="promptctl banner" width="900">
</p>

<p align="center">
  <strong>A control plane for composable AI prompting.</strong>
</p>

## 📖 Overview

promptctl is a modular CLI for composing, managing, and orchestrating reusable AI prompt components.

Instead of storing static snippets, promptctl treats prompts as structured building blocks — roles, tasks, and reasoning patterns — that can be assembled, parameterized, and reused across projects.

Designed for users who think in systems, not snippets.

 🧱 Why promptctl?

- 🧱 Modular prompt components
- 🧠 Role + task + pattern composition
- 🔁 Agent presets
- 🧩 Variable injection
- 📋 Clipboard export
- ⚡ Terminal-native workflow
- 🗂 Version-controlled prompts

## ⚙️ Installation

```shell
# Get the source code
git clone https://github.com/estebantechdev/promptctl.git

# Enter the project directory
cd promptctl

# Create virtual environment (optional)
python3 -m venv .venv
source .venv/bin/activate  # Activate it

# Install dependencies
python -m pip install -r requirements.txt

# Make executable
chmod +x promptctl.py

# Install system-wide
sudo ln -s "$(pwd)/promptctl.py" /usr/local/bin/promptctl
```

#### 🐧 Linux Prerequisite (Debian/Ubuntu)

If you are using Debian-based systems (such as Ubuntu) and encounter an error when creating a virtual environment, you may need to install the `venv` package:

```bash
sudo apt update
sudo apt install python3-venv
```

## 🧪 Usage Examples

### List Prompt Composable Elements By Category

#### List Roles

```bash
promptctl list roles
```

Or filter results that match multiple patterns (`te` or `utor`):

```bash
promptctl list roles | grep -E 'te|utor'
```

Example output:

```output
technical_instructor
tutor
```

You can also list `agents`, `pattern_groups`, `patterns`, and `tasks`.

### Build From Agent

```bash
promptctl build math_tutor --var input="Explain recursion"
```

Copy directly:

```bash
promptctl build math_tutor --var input="Explain recursion" --copy
```

### Manual Composition

```bash
promptctl compose \
  --role tutor \
  --task explain \
  --pattern step_by_step \
  --var input="Boolean algebra simplification"
```

Including multiple patterns and variables:

```bash
promptctl compose \
  --role tutor \
  --task explain \
  --pattern socratic \
  --pattern step_by_step \
  --var input="Gravity: Force vs Curvature of Space" \
  --var theorist="Albert Einstein"
```

Replacing "Albert Einstein" with "Isaac Newton" will result in different AI responses.

Note: The variable `theorist` does not exist in the default version of the task `explain`.

## 🔧 Using `--var` Variables

To inject dynamic values into your prompt, your template must reference them using Jinja syntax.

Your **task file** (inside `tasks/`) must include at least one variable placeholder. For example:

```js
{{ input }}
```

The variable name inside the template must match the key used in the command line.

If you omit the `--var` parameter, the prompt will be generated without injected values. This allows you to preview, copy, or reuse the base prompt structure independently.

## 🔀 Variable Sources

promptctl supports three explicit variable types:

### 1. Literal Variables (--var)

Pass direct text values.

```bash
promptctl compose \
  --role tutor \
  --task explain \
  --pattern socratic \
  --var input="Random text"
```

### 2. Single File (--var-file)

Load variable content from a file (e.g.: .txt or .md).

```bash
promptctl compose \
  --role tutor \
  --task explain \
  --pattern socratic \
  --var-file input=./texts/puzzle.txt
```

The entire file content becomes the variable value.

### 3. Recursive Directory (--var-dir)

Load all files inside a directory (recursively).

```bash
promptctl compose \
  --role tutor \
  --task explain \
  --pattern socratic \
  --var-dir input=./texts \
  --copy
```

All file contents are combined into a single variable.

### Combining All Variable Types

You can mix them in the same command:

```bash
promptctl compose \
  --role tutor \
  --task explain \
  --pattern didactic \
  --var input="Random text" \
  --var-file input2=./texts/puzzle.txt \
  --var-dir input3=./texts \
  --copy
```

This allows complex prompt construction from multiple sources.

Note: The variables `input2` and `input3` don't exist in the default version of the task `explain`.

#### ⚠️ Variable Overwriting Behavior

If the same variable name is used multiple times, the last one processed will overwrite the previous value.

* Processing order: --var, --var-file, --var-dir

Example:

```bash
promptctl compose \
  --role tutor \
  --task explain \
  --pattern didactic \
  --var input="Random text" \
  --var-file input=./texts/puzzle.txt \
  --var-dir input=./texts \
  --copy
```

#### 💡 Recommended Practice

✔ Use unique variable names  
✔ Declare expected variables clearly inside your task templates  
✔ Only reuse names intentionally when overwriting is desired

## 📘 Tutorials

Want a step-by-step guide to **creating new roles, tasks, and patterns**?

🔗 [Roles, Tasks, And Patterns](docs/new_roles_tasks_and_patterns.md)

Complete clean tutorial on how to create and use a pattern group

🔗 [Pattern Groups](docs/create_and_use_a_pattern_group.md)

## 🗂 Prompt Composable Elements

The `prompts/` directory contains the core components used to build prompts in promptctl.

Each subdirectory represents a specific type of composable element such as roles, tasks, patterns, or agent presets.

See the **complete reference**:

🔗 [Prompt Composable Elements Reference](docs/prompt_composable_elememts_reference.md)

## 🧠 Concepts

Understanding modern prompting frameworks helps you use promptctl more effectively.

🔗 [The Iceberg Of Prompting](docs/the_iceberg_of_prompting.md)

## 🤝 Contributions

Contributions are highly encouraged — especially new modular prompt components.

You can contribute:

- New **roles** (teaching styles, expert personas, system behaviors)
- New **tasks** (analysis, critique, summarization, transformation, etc.)
- New **patterns** (reasoning frameworks, output formats, cognitive constraints)
- New **pattern groups** (reusable bundles that combine multiple patterns into higher-level behavioral modes)
- New **agent presets** that combine existing components
- Documentation improvements and examples

promptctl becomes more powerful as its library of composable parts grows.

If you’ve built something reusable, open a pull request and help expand the ecosystem.

## 📜 License

This project is licensed under the [GPL-3.0](LICENSE) - see the [LICENSE](LICENSE) file for details.
