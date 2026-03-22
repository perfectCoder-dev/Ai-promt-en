#!/usr/bin/env python3
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

import argparse
import os
import pyperclip
import sys
import yaml
from jinja2 import Template
from rich.console import Console
from rich.syntax import Syntax

console = Console()

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


def load_control(control_type, name):
    """
    Load the content of a control file by name and type.

    The function searches for a Markdown file in the following order:
    1. Flat structure: controls/<control_type>/<name>.md
    2. Nested structure: controls/<control_type>/**/<name>.md (recursive)

    Args:
        control_type (str): The control category (e.g., "pre", "post").
        name (str): The name of the control file (without extension).

    Returns:
        str: The stripped contents of the matched control file.

    Raises:
        FileNotFoundError: If no matching control file is found.
    """
    base_path = os.path.join(BASE_DIR, "controls", control_type)

    # 1. Try flat structure
    flat_path = os.path.join(base_path, f"{name}.md")
    if os.path.exists(flat_path):
        with open(flat_path, "r") as f:
            return f.read().strip()

    # 2. Search recursively in subdirectories
    for root, _, files in os.walk(base_path):
        for file in files:
            if file == f"{name}.md":
                with open(os.path.join(root, file), "r") as f:
                    return f.read().strip()

    raise FileNotFoundError(f"controls/{control_type}/{name} not found.")


def load_controls(control_type, control_list):
    """
    Load multiple control files and return their contents as a list.

    Iterates over the provided control names and retrieves each control
    using `load_control`. If the list is empty or None, an empty list is returned.

    Args:
        control_type (str): The control category (e.g., "pre", "post").
        control_list (Iterable[str] | None): A collection of control names
            (without file extensions), or None.

    Returns:
        list[str]: A list containing the contents of each loaded control file,
        in the same order as provided.

    Raises:
        FileNotFoundError: If any control in the list cannot be found.
    """
    parts = []

    for item in control_list or []:
        parts.append(load_control(control_type, item))

    return parts

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

def compose_from_agent(agent_name, cli_pre=None, cli_post=None):
    """
    Compose a complete prompt from an agent definition and optional CLI controls.

    This function builds a prompt by:
    1. Loading the agent configuration.
    2. Resolving and merging control definitions from the agent YAML and CLI input.
       - CLI controls are appended to agent-defined controls.
    3. Loading control contents (`pre` and `post`).
    4. Assembling the final prompt in the following order:
       - Pre-controls
       - Role
       - Task
       - Resolved patterns
       - Post-controls

    Args:
        agent_name (str): Name of the agent to load.
        cli_pre (Iterable[str] | None): अतिरिक्त pre controls provided via CLI.
        cli_post (Iterable[str] | None): Additional post controls provided via CLI.

    Returns:
        str: The fully composed prompt as a single string, with sections separated
        by double newlines.

    Raises:
        FileNotFoundError: If any referenced agent, control, or text component
        cannot be found.
        KeyError: If required agent fields (e.g., "role", "task") are missing.
    """
    agent = load_agent(agent_name)

    parts = []

    # --------------------------------------------------------------------------
    # Controls (from agent YAML)
    # --------------------------------------------------------------------------
    controls = agent.get("controls", {})

    agent_pre = controls.get("pre", [])
    agent_post = controls.get("post", [])

    # --------------------------------------------------------------------------
    # Merge with CLI controls (CLI overrides / extends)
    # --------------------------------------------------------------------------
    final_pre = (agent_pre or []) + (cli_pre or [])
    final_post = (agent_post or []) + (cli_post or [])

    # Load control content
    pre_parts = load_controls("pre", final_pre)
    post_parts = load_controls("post", final_post)

    # --------------------------------------------------------------------------
    # Core prompt
    # --------------------------------------------------------------------------
    parts.extend(pre_parts)

    parts.append(load_text("roles", agent["role"]))
    parts.append(load_text("tasks", agent["task"]))

    resolved = resolve_patterns(agent.get("patterns", []))

    for pattern in resolved:
        parts.append(load_text("patterns", pattern))

    parts.extend(post_parts)

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
    List subcategories and items within a given category path.

    This function inspects the directory located under BASE_DIR using the
    provided category path, which may refer to either a top-level category
    or a nested subdirectory (e.g., "controls/pre"). It prints all immediate
    entries in sorted order.

    - Subdirectories are treated as subcategories and displayed with a
      trailing slash (e.g., "pre/").
    - Files with `.md` or `.yaml` extensions are treated as items and are
      displayed without their file extensions.

    If the specified path does not exist, a message is printed and the
    function exits without raising an exception.

    Args:
        category (str): The category or subcategory path relative to BASE_DIR.

    Returns:
        None: Results are printed directly to standard output.

    Notes:
        - Only the immediate contents of the directory are listed; this
          function does not perform recursive traversal.
        - Output is intended for CLI display and not structured for parsing.
    """
    path = os.path.join(BASE_DIR, category)

    if not os.path.exists(path):
        print("Category not found.")
        return

    entries = sorted(os.listdir(path))

    for entry in entries:
        full_path = os.path.join(path, entry)

        if os.path.isdir(full_path):
            print(f"{entry}/")
        elif entry.endswith(".md") or entry.endswith(".yaml"):
            name = entry.replace(".md", "").replace(".yaml", "")
            print(f"{name}")


def show_path(path):
    """
    Display the contents of a prompt item with syntax highlighting.

    This function resolves a file path relative to BASE_DIR and prints its
    contents to the terminal using rich syntax highlighting. The file is
    located without requiring an explicit extension by checking supported
    formats in order (`.md`, then `.yaml`).

    Rendering behavior:
        - If the file contains Jinja template markers (e.g., `{{ ... }}` or
          `{% ... %}`), it is highlighted using a Jinja-compatible lexer.
        - Otherwise, the content is rendered as Markdown.
        - Output is displayed using the Rich library with a configurable theme.

    If the resolved path corresponds to a directory, the user is informed
    and advised to use the `list` command instead.

    If no matching file is found but the parent directory exists, the function
    prints a list of nearby subdirectories and items as suggestions to help
    locate the intended resource.

    Args:
        path (str): Relative path to the target item (without file extension).
            May include nested subdirectories (e.g., "tasks/explain").

    Returns:
        None: Output is printed directly to standard output.

    Notes:
        - File resolution order is `.md` first, then `.yaml`.
        - Only the first matching file is displayed.
        - Suggestions include both subdirectories (with trailing `/`)
          and valid item names (without file extensions).
        - Output is intended for interactive CLI usage and is not structured
          for machine parsing.
    """
    base_path = os.path.join(BASE_DIR, path)

    # Detect directory
    if os.path.isdir(base_path):
        print("This is a directory. Use 'pp list'.")
        return

    # Try .md first, then .yaml
    for ext in [".md", ".yaml"]:
        file_path = base_path + ext
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                content = f.read()

            lexer = "jinja" if "{{" in content or "{%" in content else "markdown"
            syntax = Syntax(
                content,
                lexer,            # key part
                theme="dracula",  # optional (try "monokai", "default", etc.)
                line_numbers=False
            )

            # console.print(f"[bold cyan]{path}[/bold cyan]\n")
            console.print(syntax)
            return

    # Suggest nearby items
    parent = os.path.dirname(base_path)

    if os.path.exists(parent):
        print("Item not found.")
        print("\nDid you mean:")

        for entry in sorted(os.listdir(parent)):
            entry_path = os.path.join(parent, entry)

            if os.path.isdir(entry_path):
                print(f"  {entry}/")
            elif entry.endswith(".md") or entry.endswith(".yaml"):
                name = entry.replace(".md", "").replace(".yaml", "")
                print(f"  {name}")
        return

    print("Item not found.")


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
    Run the PromptPro command-line interface.

    This function parses CLI arguments, dispatches subcommands, assembles prompts,
    applies control layers, injects variables, and outputs the final result.

    Supported subcommands:
        - list <category>: List available items in a category.
        - show <path>: Display the contents of a file or resource.
        - build <agent>: Compose a prompt from an agent configuration.
        - compose: Manually compose a prompt from role, task, and patterns.

    Controls:
        - Pre and post controls can be provided via CLI (`--pre`, `--post`)
          and are merged with agent-defined controls (for `build`).
        - Controls are loaded from:
            prompts/controls/pre/
            prompts/controls/post/
        - Application order:
            1. Pre-controls
            2. Core prompt
            3. Post-controls

    Variables:
        - Supports variable injection from multiple sources:
            --var key=value        (literal values)
            --var-file key=path    (file contents)
            --var-dir key=path     (recursive directory contents)
        - Resolution order (later overrides earlier):
            1. --var
            2. --var-file
            3. --var-dir

    Execution flow:
        1. Parse CLI arguments.
        2. Execute command:
            - list/show: immediate output.
            - build: compose from agent.
            - compose: build from manual inputs.
        3. Load and merge controls (if applicable).
        4. Resolve variables.
        5. Render the final prompt.
        6. Output to stdout or copy to clipboard.

    Raises:
        FileNotFoundError: If a file specified in --var-file does not exist.
        NotADirectoryError: If a path specified in --var-dir is invalid.
        ValueError: If variable arguments are not in key=value format.
    """
    parser = argparse.ArgumentParser(prog="pp")

    subparsers = parser.add_subparsers(dest="command")

    # list
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("category")

    # show
    show_parser = subparsers.add_parser("show")
    show_parser.add_argument("path")

    # build from agent
    build_parser = subparsers.add_parser("build")
    build_parser.add_argument("agent")
    build_parser.add_argument("--pre", action="append", help="Pre-prompt controls")
    build_parser.add_argument("--post", action="append", help="Post-prompt controls")
    build_parser.add_argument("--var", action="append", help="Literal variables (key=value)")
    build_parser.add_argument("--var-file", action="append", help="Variables from file (key=filepath)")
    build_parser.add_argument("--var-dir", action="append", help="Variables from directory (key=dirpath)")
    build_parser.add_argument("--copy", action="store_true")

    # compose manually
    compose_parser = subparsers.add_parser("compose")
    compose_parser.add_argument("--pre", action="append", help="Pre-prompt controls")
    compose_parser.add_argument("--role")
    compose_parser.add_argument("--task")
    compose_parser.add_argument("--pattern", action="append")
    compose_parser.add_argument("--post", action="append", help="Post-prompt controls")
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
    # Show
    # --------------------------------------------------------------------------
    if args.command == "show":
        show_path(args.path)
        return

    # --------------------------------------------------------------------------
    # Build
    # --------------------------------------------------------------------------
    if args.command == "build":
        prompt = compose_from_agent(
            args.agent,
            cli_pre=getattr(args, "pre", None),
            cli_post=getattr(args, "post", None),
        )

    # --------------------------------------------------------------------------
    # Compose
    # --------------------------------------------------------------------------
    elif args.command == "compose":
        prompt = compose_manual(args.role, args.task, args.pattern)

    else:
        parser.print_help()
        return

    # --------------------------------------------------------------------------
    # Variable Processing
    # --------------------------------------------------------------------------
    variables = {}

    # 1 Literal variables
    if args.var:
        for item in args.var:
            key, value = item.split("=", 1)
            variables[key] = value

    # 2 Single file variables
    if args.var_file:
        for item in args.var_file:
            key, filepath = item.split("=", 1)

            if not os.path.isfile(filepath):
                raise FileNotFoundError(f"File not found: {filepath}")

            with open(filepath, "r") as f:
                variables[key] = f.read()

    # 3 Recursive directory variables
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
    full_prompt = prompt

    rendered = render_prompt(full_prompt, variables)

    # --------------------------------------------------------------------------
    # Output
    # --------------------------------------------------------------------------
    if args.copy:
        copy_to_clipboard(rendered)
    else:
        print(rendered)

if __name__ == "__main__":
    main()
