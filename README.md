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
sudo ln -s $(pwd)/promptctl.py /usr/local/bin/promptctl
```

Optional (for interactive picker):

```bash
sudo apt install fzf
```
