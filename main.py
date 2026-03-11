#!/usr/bin/env python
################################################################################
#                                  PromptPro                                   #
#                                                                              #
# Composes, manages, and orchestrates reusable AI prompt components            #
#                                                                              #
# Change History                                                               #
# 03/03/2026  Esteban Herrera Original code.                                   #
#                           Add new history entries as needed.                 #
#                                                                              #
#                                                                              #
################################################################################
################################################################################
################################################################################
#                                                                              #
#  Copyright (c) 2026-present Esteban Herrera C.                               #
#  stv.herrera@gmail.com                                                       #
#                                                                              #
#  This program is free software; you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation; either version 3 of the License, or           #
#  (at your option) any later version.                                         #
#                                                                              #
#  This program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with this program; if not, write to the Free Software                 #
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA   #

# main.py
# A modular CLI tool for composing, rendering, and managing structured prompts
# from reusable building blocks.

import os
import sys
import yaml
import argparse
import pyperclip
from jinja2 import Template

# Builds an absolute path to a directory named prompts
BASE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "prompts"
)

# ------------------------------------------------------------------------------
# Loaders
# ------------------------------------------------------------------------------

def load_text(category, name):
    """
    Load and return the contents of a Markdown file from the prompts directory.

    The file is resolved using BASE_DIR, the given category subdirectory,
    and the provided name (with a `.md` extension).

    Args:
        category (str): Subdirectory inside the prompts directory.
        name (str): Name of the Markdown file (without extension).

    Returns:
        str: The stripped contents of the file.

    Raises:
        FileNotFoundError: If the constructed file path does not exist.
    """
    path = os.path.join(BASE_DIR, category, f"{name}.md")
    if not os.path.exists(path):
        raise FileNotFoundError(f"{category}/{name} not found.")
    with open(path, "r") as f:
        return f.read().strip()


def load_agent(name):
    """
    Load and parse an agent configuration file from the agents directory.

    The function builds the path using BASE_DIR, the "agents" subdirectory,
    and the provided agent name with a `.yaml` extension. The YAML file
    is safely parsed and returned as a Python object.

    Args:
        name (str): The agent configuration filename (without extension).

    Returns:
        dict | list | Any: The parsed YAML content as a Python data structure.

    Raises:
        FileNotFoundError: If the specified agent file does not exist.
        yaml.YAMLError: If the YAML file cannot be parsed.
    """
    path = os.path.join(BASE_DIR, "agents", f"{name}.yaml")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Agent '{name}' not found.")
    with open(path, "r") as f:
        return yaml.safe_load(f)


def load_pattern_group(name):
    """
    Load and parse a pattern group configuration from the pattern_groups directory.

    Pattern group files are expected to be stored under BASE_DIR/prompts/pattern_groups
    with a `.yaml` extension. If the specified file does not exist, the function
    returns None instead of raising an exception.

    Args:
        name (str): The pattern group filename (without extension).

    Returns:
        dict | list | Any | None: The parsed YAML content as a Python data
        structure, or None if the file does not exist.

    Raises:
        yaml.YAMLError: If the YAML file exists but cannot be parsed.
    """
    path = os.path.join(
        BASE_DIR, "pattern_groups", f"{name}.yaml"
    )
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return yaml.safe_load(f)


# ------------------------------------------------------------------------------
# Pattern Resolution
# ------------------------------------------------------------------------------

def resolve_patterns(pattern_list, seen=None):
    """
    Recursively resolve and expand pattern groups into a flat list of patterns.

    For each entry in `pattern_list`, the function checks whether it refers
    to a pattern group (via `load_pattern_group`). If so, the group's
    subpatterns are recursively expanded. If not, the pattern is treated
    as a leaf and appended to the result.

    A `seen` set is used to track already-visited group names in order
    to prevent infinite recursion caused by circular references.

    Args:
        pattern_list (list[str] | None): A list of pattern names or group names
            to resolve. If None or empty, an empty list is returned.
        seen (set[str] | None): Internal tracking set of visited group names
            used to prevent cyclic expansion. Intended for recursive use.

    Returns:
        list[str]: A flattened list of resolved pattern names with all
        groups recursively expanded.
    """
    if seen is None:
        seen = set()

    resolved = []

    for pattern in pattern_list or []:

        if pattern in seen:
            continue

        group = load_pattern_group(pattern)

        if group:
            seen.add(pattern)
            subpatterns = group.get("patterns", [])
            resolved.extend(resolve_patterns(subpatterns, seen))
        else:
            resolved.append(pattern)

    return resolved


# ------------------------------------------------------------------------------
# Composition
# ------------------------------------------------------------------------------

def compose_from_agent(agent_name):
    """
    Build a composed prompt string from an agent configuration.

    The function loads the specified agent YAML definition, retrieves its
    associated role and task Markdown files, resolves any declared pattern
    groups into a flat list of patterns, and loads each corresponding
    pattern file. All loaded sections are concatenated into a single
    string separated by blank lines.

    Args:
        agent_name (str): The agent configuration filename (without extension).

    Returns:
        str: A fully composed prompt string including role, task,
        and all resolved pattern contents.

    Raises:
        FileNotFoundError: If the agent file or any referenced Markdown
        file (role, task, or pattern) does not exist.
        yaml.YAMLError: If the agent YAML configuration cannot be parsed.
        KeyError: If required keys such as "role" or "task" are missing
        from the agent configuration.
    """
    agent = load_agent(agent_name)

    parts = []

    parts.append(load_text("roles", agent["role"]))
    parts.append(load_text("tasks", agent["task"]))

    resolved = resolve_patterns(agent.get("patterns", []))

    for pattern in resolved:
        parts.append(load_text("patterns", pattern))

    return "\n\n".join(parts)


def compose_manual(role, task, patterns):
    """
    Manually compose a prompt string from the given role, task, and patterns.

    Unlike `compose_from_agent`, this function does not rely on an agent
    configuration file. Instead, it directly receives the role name,
    task name, and a list of pattern or pattern-group names. Pattern
    groups are recursively resolved before loading their corresponding
    Markdown files.

    Any provided section (role or task) is included only if it is not None.
    All loaded sections are concatenated into a single string separated
    by blank lines.

    Args:
        role (str | None): The role filename (without extension) located
            under the "roles" directory.
        task (str | None): The task filename (without extension) located
            under the "tasks" directory.
        patterns (list[str] | None): A list of pattern or pattern-group
            names to resolve and include.

    Returns:
        str: A composed prompt string containing the selected role,
        task, and resolved pattern contents.

    Raises:
        FileNotFoundError: If any referenced Markdown file does not exist.
        yaml.YAMLError: If a referenced pattern group exists but cannot
            be parsed.
    """
    parts = []

    if role:
        parts.append(load_text("roles", role))

    if task:
        parts.append(load_text("tasks", task))

    resolved = resolve_patterns(patterns)

    for pattern in resolved:
        parts.append(load_text("patterns", pattern))

    return "\n\n".join(parts)


# ------------------------------------------------------------------------------
# Rendering
# ------------------------------------------------------------------------------

def render_prompt(prompt_text, variables):
    """
    Render a prompt template using the provided variables.

    The function creates a Template instance from the given prompt text
    and renders it by injecting the supplied variables as keyword
    arguments.

    Args:
        prompt_text (str): The raw template string containing placeholders.
        variables (dict): A dictionary of values to substitute into the
            template. Keys must match the placeholder names defined in
            the template.

    Returns:
        str: The rendered prompt string with all placeholders replaced.

    Raises:
        TypeError: If `variables` is not a mapping suitable for unpacking.
        Exception: Any rendering-related error raised by the Template
            engine (e.g., undefined variables or syntax issues).
    """
    template = Template(prompt_text)
    return template.render(**variables)


# ------------------------------------------------------------------------------
# Utilities
# ------------------------------------------------------------------------------

def list_category(category):
    """
    List available items within a given content category.

    The function prints the names (without file extensions) of all
    `.md` and `.yaml` files found inside the specified category
    directory under BASE_DIR. It also supports a top‑level “pattern_groups” 
    category for listing top-level category "pattern_groups".

    If the category directory does not exist, a message is printed
    and the function exits without raising an exception.

    Args:
        category (str): The name of the category directory to list
            (e.g., "roles", "tasks", "patterns", or "pattern_groups").

    Returns:
        None: Results are printed directly to standard output.
    """
    if category == "pattern_groups":
        path = os.path.join(BASE_DIR, "pattern_groups")
    else:
        path = os.path.join(BASE_DIR, category)

    if not os.path.exists(path):
        print("Category not found.")
        return
    for file in os.listdir(path):
        if file.endswith(".md") or file.endswith(".yaml"):
            print(file.replace(".md", "").replace(".yaml", ""))


def copy_to_clipboard(text):
    """
    Copy the given text to the system clipboard.

    This function uses the `pyperclip` library to place the provided
    string into the clipboard, making it available for pasting in
    other applications. A confirmation message is printed after
    the operation completes.

    Args:
        text (str): The text content to copy to the clipboard.

    Returns:
        None: The function performs a side effect (clipboard update)
        and prints a confirmation message.

    Raises:
        pyperclip.PyperclipException: If the clipboard operation fails
        (e.g., missing system dependencies or unsupported platform).
    """
    pyperclip.copy(text)
    print("Prompt copied to clipboard.")


# ------------------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------------------

def main():
    """
    Entry point for the PromptPro CLI application.

    This function:
    - Defines the command-line interface using argparse.
    - Supports the following subcommands:
        - `list <category>`: List available prompts in a category.
        - `build <agent>`: Build a prompt from a predefined agent configuration.
        - `compose`: Manually compose a prompt using role, task, and patterns.

    It also supports flexible variable injection through:
        - --var key=value
        - --var-file key=filepath
        - --var-dir key=directory_path (recursively reads all files)

    Variable resolution order:
        1. Literal variables (--var)
        2. File-based variables (--var-file)
        3. Directory-based variables (--var-dir)

    After parsing arguments:
        - The appropriate prompt is generated.
        - Variables are collected and merged.
        - The final prompt is rendered.
        - Output is either printed to stdout or copied to the clipboard
          depending on the --copy flag.

    If no valid command is provided, help information is displayed.

    Raises:
        FileNotFoundError: If a file specified in --var-file does not exist.
        NotADirectoryError: If a path specified in --var-dir is not a directory.
    """
    parser = argparse.ArgumentParser(prog="pp")

    subparsers = parser.add_subparsers(dest="command")

    # list
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("category")

    # build from agent
    build_parser = subparsers.add_parser("build")
    build_parser.add_argument("agent")
    build_parser.add_argument("--var", action="append", help="Literal variables (key=value)")
    build_parser.add_argument("--var-file", action="append", help="Variables from file (key=filepath)")
    build_parser.add_argument("--var-dir", action="append", help="Variables from directory (key=dirpath)")
    build_parser.add_argument("--copy", action="store_true")

    # compose manually
    compose_parser = subparsers.add_parser("compose")
    compose_parser.add_argument("--role")
    compose_parser.add_argument("--task")
    compose_parser.add_argument("--pattern", action="append")
    compose_parser.add_argument("--var", action="append", help="Literal variables (key=value)")
    compose_parser.add_argument("--var-file", action="append", help="Variables from file (key=filepath)")
    compose_parser.add_argument("--var-dir", action="append", help="Variables from directory (key=dirpath)")
    compose_parser.add_argument("--copy", action="store_true")

    # --------------------------------------------------------------------------
    # Parse
    # --------------------------------------------------------------------------
    args = parser.parse_args()

    # --------------------------------------------------------------------------
    # List
    # --------------------------------------------------------------------------
    if args.command == "list":
        list_category(args.category)
        return

    # --------------------------------------------------------------------------
    # Build
    # --------------------------------------------------------------------------
    if args.command == "build":
        prompt = compose_from_agent(args.agent)

    # --------------------------------------------------------------------------
    # Compose
    # --------------------------------------------------------------------------
    elif args.command == "compose":
        prompt = compose_manual(args.role, args.task, args.pattern)

    else:
        parser.print_help()
        return

    # --------------------------------------------------------------------------
    # Variable Processing (NEW DESIGN)
    # --------------------------------------------------------------------------
    variables = {}

    # 1️⃣ Literal variables
    if args.var:
        for item in args.var:
            key, value = item.split("=", 1)
            variables[key] = value

    # 2️⃣ Single file variables
    if args.var_file:
        for item in args.var_file:
            key, filepath = item.split("=", 1)

            if not os.path.isfile(filepath):
                raise FileNotFoundError(f"File not found: {filepath}")

            with open(filepath, "r") as f:
                variables[key] = f.read()

    # 3️⃣ Recursive directory variables
    if args.var_dir:
        for item in args.var_dir:
            key, dirpath = item.split("=", 1)

            if not os.path.isdir(dirpath):
                raise NotADirectoryError(f"Not a directory: {dirpath}")

            collected = []

            for root, _, files in os.walk(dirpath):
                for file in sorted(files):
                    file_path = os.path.join(root, file)

                    if os.path.isfile(file_path):
                        with open(file_path, "r") as f:
                            collected.append(f.read())

            variables[key] = "\n\n".join(collected)

    # --------------------------------------------------------------------------
    # Render
    # --------------------------------------------------------------------------
    rendered = render_prompt(prompt, variables)

    # --------------------------------------------------------------------------
    # Output
    # --------------------------------------------------------------------------
    if args.copy:
        copy_to_clipboard(rendered)
    else:
        print(rendered)

if __name__ == "__main__":
    main()
