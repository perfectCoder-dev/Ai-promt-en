#!/usr/bin/env python3

import os
import sys
import yaml
import argparse
import pyperclip
from jinja2 import Template

BASE_DIR = os.path.join(os.path.dirname(__file__), "prompts")


# -------------------------
# Loaders
# -------------------------

def load_text(category, name):
    path = os.path.join(BASE_DIR, category, f"{name}.md")
    if not os.path.exists(path):
        raise FileNotFoundError(f"{category}/{name} not found.")
    with open(path, "r") as f:
        return f.read().strip()


def load_agent(name):
    path = os.path.join(BASE_DIR, "agents", f"{name}.yaml")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Agent '{name}' not found.")
    with open(path, "r") as f:
        return yaml.safe_load(f)


# -------------------------
# Composition
# -------------------------

def compose_from_agent(agent_name):
    agent = load_agent(agent_name)

    parts = []

    parts.append(load_text("roles", agent["role"]))
    parts.append(load_text("tasks", agent["task"]))

    for pattern in agent.get("patterns", []):
        parts.append(load_text("patterns", pattern))

    return "\n\n".join(parts)


def compose_manual(role, task, patterns):
    parts = []

    if role:
        parts.append(load_text("roles", role))

    if task:
        parts.append(load_text("tasks", task))

    if patterns:
        for pattern in patterns:
            parts.append(load_text("patterns", pattern))

    return "\n\n".join(parts)


# -------------------------
# Rendering
# -------------------------

def render_prompt(prompt_text, variables):
    template = Template(prompt_text)
    return template.render(**variables)


# -------------------------
# Utilities
# -------------------------

def list_category(category):
    path = os.path.join(BASE_DIR, category)
    if not os.path.exists(path):
        print("Category not found.")
        return
    for file in os.listdir(path):
        if file.endswith(".md") or file.endswith(".yaml"):
            print(file.replace(".md", "").replace(".yaml", ""))


def copy_to_clipboard(text):
    pyperclip.copy(text)
    print("Prompt copied to clipboard.")


# -------------------------
# CLI
# -------------------------

def main():
    parser = argparse.ArgumentParser(prog="promptctl")

    subparsers = parser.add_subparsers(dest="command")

    # list
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("category")

    # build from agent
    build_parser = subparsers.add_parser("build")
    build_parser.add_argument("agent")
    build_parser.add_argument("--var", action="append", help="Variables (key=value)")
    build_parser.add_argument("--copy", action="store_true")

    # compose manually
    compose_parser = subparsers.add_parser("compose")
    compose_parser.add_argument("--role")
    compose_parser.add_argument("--task")
    compose_parser.add_argument("--pattern", action="append")
    compose_parser.add_argument("--var", action="append")
    compose_parser.add_argument("--copy", action="store_true")

    args = parser.parse_args()

    if args.command == "list":
        list_category(args.category)

    elif args.command == "build":
        prompt = compose_from_agent(args.agent)

        variables = {}
        if args.var:
            for item in args.var:
                key, value = item.split("=", 1)
                variables[key] = value

        rendered = render_prompt(prompt, variables)

        if args.copy:
            copy_to_clipboard(rendered)
        else:
            print(rendered)

    elif args.command == "compose":
        prompt = compose_manual(args.role, args.task, args.pattern)

        variables = {}
        if args.var:
            for item in args.var:
                key, value = item.split("=", 1)
                variables[key] = value

        rendered = render_prompt(prompt, variables)

        if args.copy:
            copy_to_clipboard(rendered)
        else:
            print(rendered)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
