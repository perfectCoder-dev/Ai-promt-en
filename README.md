# promptctl

<p align="center">
  <img src="images/promptctl-banner.png" alt="promptctl banner" width="900">
</p>

<p align="center">
  <strong>A control plane for composable AI prompting.</strong>
</p>

## Overview

promptctl is a modular CLI for composing, managing, and orchestrating reusable AI prompt components.

Instead of storing static snippets, promptctl treats prompts as structured building blocks — roles, tasks, and reasoning patterns — that can be assembled, parameterized, and reused across projects.

Designed for users who think in systems, not snippets.

## Why promptctl?

- 🧱 Modular prompt components
- 🧠 Role + task + pattern composition
- 🔁 Agent presets
- 🧩 Variable injection
- 📋 Clipboard export
- ⚡ Terminal-native workflow
- 🗂 Version-controlled prompts

## Installation

```bash
git clone https://github.com/estebantechdev/promptctl.git
cd promptctl
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
chmod +x promptctl.py
sudo ln -s "$(pwd)/promptctl.py" /usr/local/bin/promptctl
```

## 🧪 Usage Examples

### List Roles

```bash
promptctl list roles
```

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
  --var input="Boolean algebra simplification" \
  --var name="John Smith"
```

## How To Pass `--var` Values

Ensure your template uses correct variable syntax.

Your task file must contain:

```markdown

{{ input }}

```

You can exclude the `--var` parameter to get the prompt without inputs.

## 📘 Tutorial

Want a step-by-step guide to creating new roles, tasks, and patterns?

👉 [Read the Tutorial](docs/tutorial.md)

promptctl is designed to grow through modular contributions.

If you create a useful role, reusable task, or powerful reasoning pattern — consider adding it to the repository and sharing it with others.

## Contributions

Contributions are highly encouraged — especially new modular prompt components.

You can contribute:

- 🧠 New **roles** (teaching styles, expert personas, system behaviors)

- 🎯 New **tasks** (analysis, critique, summarization, transformation, etc.)

- 🧩 New **patterns** (reasoning frameworks, output formats, cognitive constraints)

- 🤖 New **agent presets** that combine existing components

- 📚 Documentation improvements and examples

promptctl becomes more powerful as its library of composable parts grows.

If you’ve built something reusable, open a pull request and help expand the ecosystem.

## License

This project is licensed under the [GPL-3.0](LICENSE) - see the [LICENSE](LICENSE) file for details.
