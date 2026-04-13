#!/usr/bin/env python3
################################################################################
#                                   PromptNG                                   #
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
from importlib import resources
from jinja2 import Template
from rich.console import Console
from rich.syntax import Syntax

# Output wrapping is being managed in render_output
# console = Console(soft_wrap=True)
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
    Loads the contents of a Markdown file from the specified category.

    Constructs a file path under BASE_DIR using the given category and name,
    expecting a `.md` file. If the file exists, reads its contents, strips
    leading and trailing whitespace, and returns the result.

    Args:
        category (str): The subdirectory under BASE_DIR where the file is located.
        name (str): The name of the Markdown file (without the `.md` extension).

    Returns:
        str: The stripped contents of the Markdown file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    path = os.path.join(BASE_DIR, category, f"{name}.md")
    if not os.path.exists(path):
        raise FileNotFoundError(f"{category}/{name} not found.")
    with open(path, "r") as f:
        return f.read().strip()


def load_agent(name):
    """
    Loads and parses an agent configuration from a packaged YAML file.

    Locates the specified `.yaml` file within the
    `promptng.prompts.agents` package using importlib.resources. If the
    file exists, reads and safely parses its contents into a Python
    data structure.

    Args:
        name (str): The agent configuration filename (without the `.yaml` extension).

    Returns:
        dict | list | Any: The parsed YAML content as a Python object.

    Raises:
        FileNotFoundError: If the specified agent file does not exist.
        ValueError: If the YAML file is empty or contains no valid data.
        yaml.YAMLError: If the YAML content cannot be parsed.
    """
    resource = resources.files("promptng.prompts.agents").joinpath(f"{name}.yaml")

    if not resource.is_file():
        raise FileNotFoundError(f"Agent '{name}' not found.")

    data = yaml.safe_load(resource.read_text(encoding="utf-8"))

    if data is None:
        raise ValueError(f"Agent '{name}' is empty or invalid.")

    return data


def load_pattern_group(name):
    """
    Loads and parses a pattern group configuration from a YAML file.

    Constructs a file path under BASE_DIR/pattern_groups using the given
    name. If the file exists, reads and safely parses its contents into
    a Python data structure. If the file does not exist, returns None.

    Args:
        name (str): The pattern group filename (without the `.yaml` extension).

    Returns:
        dict | list | Any | None: The parsed YAML content as a Python object,
        or None if the file does not exist.

    Raises:
        yaml.YAMLError: If the YAML content cannot be parsed.
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
    Loads the contents of a control file by type and name.

    Searches for a `.md` file under BASE_DIR/controls/<control_type> using
    two strategies: first checks a flat structure, then performs a recursive
    search through subdirectories. If a matching file is found, reads its
    contents, strips leading and trailing whitespace, and returns the result.

    Args:
        control_type (str): The control category (e.g., "pre", "post").
        name (str): The name of the control file (without the `.md` extension).

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
    Loads multiple control files and returns their contents as a list.

    Iterates over the provided control names and loads each one using
    `load_control`. If the input list is None or empty, returns an empty list.

    Args:
        control_type (str): The control category (e.g., "pre", "post").
        control_list (Iterable[str] | None): A collection of control names
            (without file extensions), or None.

    Returns:
        list[str]: A list containing the contents of each loaded control file,
        in the same order as provided.

    Raises:
        FileNotFoundError: If any control file cannot be found.
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
    Resolves and expands pattern groups into a flat list of patterns.

    Iterates over the provided pattern list and checks whether each entry
    corresponds to a pattern group. If a group is found, recursively expands
    its subpatterns. Otherwise, treats the entry as a leaf pattern and includes
    it in the result. Tracks visited groups to prevent infinite recursion
    caused by circular references.

    Args:
        pattern_list (list[str] | None): A list of pattern or group names to resolve.
        seen (set[str] | None): A set of already visited group names used to
            prevent cyclic expansion. Intended for internal recursive use.

    Returns:
        list[str]: A flattened list of resolved pattern names.
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
def compose_from_agent(agent_name, cli_pre=None, cli_post=None, cli_enforce=None):
    """
    Composes a complete prompt from an agent definition and optional CLI controls.

    Loads the specified agent configuration and builds a structured prompt by
    combining control blocks, core role and task content, and optional pattern
    expansions. Merges agent-defined controls with CLI-provided controls, with
    CLI values appended to the agent configuration.

    Assembles the final prompt in the following order:
        pre → role → task → patterns → post → enforce

    Args:
        agent_name (str): The name of the agent configuration to load.
        cli_pre (list[str] | None): Optional list of "pre" control names provided via CLI.
        cli_post (list[str] | None): Optional list of "post" control names provided via CLI.
        cli_enforce (list[str] | None): Optional list of "enforce" control names provided via CLI.

    Returns:
        str: The fully composed prompt as a single string, with sections
        separated by double newlines.

    Raises:
        KeyError: If required agent fields (e.g., "role", "task") are missing.
        Exception: Propagates errors raised by helper functions.
    """
    agent = load_agent(agent_name)

    parts = []

    # --------------------------------------------------------------------------
    # Controls (from agent YAML)
    # --------------------------------------------------------------------------
    controls = agent.get("controls", {})

    agent_pre = controls.get("pre", [])
    agent_post = controls.get("post", [])
    agent_enforce = controls.get("enforce", [])

    # --------------------------------------------------------------------------
    # Merge with CLI controls (CLI overrides / extends)
    # --------------------------------------------------------------------------
    final_pre = (agent_pre or []) + (cli_pre or [])
    final_post = (agent_post or []) + (cli_post or [])
    final_enforce = (agent_enforce or []) + (cli_enforce or [])

    # Load control content
    pre_parts = load_controls("pre", final_pre)
    post_parts = load_controls("post", final_post)
    enforce_parts = load_controls("enforce", final_enforce)

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
    parts.extend(enforce_parts)

    return "\n\n".join(parts)


def compose_manual(role, task, patterns, cli_pre=None, cli_post=None, cli_enforce=None):
    """
    Composes a complete prompt from manually provided inputs and CLI controls.

    Builds a structured prompt using the given role, task, and patterns,
    along with optional control blocks specified via CLI. Does not rely on
    an agent configuration. Resolves patterns recursively and loads their
    content before assembling the final prompt.

    Assembles the final prompt in the following order:
        pre → role → task → patterns → post → enforce

    Args:
        role (str | None): The role identifier to load, or None to omit.
        task (str | None): The task identifier to load, or None to omit.
        patterns (list[str] | None): A list of pattern or group names to resolve.
        cli_pre (list[str] | None): Optional list of "pre" control names.
        cli_post (list[str] | None): Optional list of "post" control names.
        cli_enforce (list[str] | None): Optional list of "enforce" control names.

    Returns:
        str: The fully composed prompt as a single string, with sections
        separated by double newlines.

    Raises:
        Exception: Propagates errors raised by helper functions.
    """
    parts = []

    # --------------------------------------------------------------------------
    # Controls (CLI only, since there's no agent YAML here)
    # --------------------------------------------------------------------------
    pre_parts = load_controls("pre", cli_pre)
    post_parts = load_controls("post", cli_post)
    enforce_parts = load_controls("enforce", cli_enforce)

    parts.extend(pre_parts)

    # --------------------------------------------------------------------------
    # Core prompt
    # --------------------------------------------------------------------------
    if role:
        parts.append(load_text("roles", role))

    if task:
        parts.append(load_text("tasks", task))

    resolved = resolve_patterns(patterns)

    for pattern in resolved:
        parts.append(load_text("patterns", pattern))

    parts.extend(post_parts)
    parts.extend(enforce_parts)

    return "\n\n".join(parts)


# ------------------------------------------------------------------------------
# Rendering
# ------------------------------------------------------------------------------

def render_prompt(prompt_text, variables):
    """
    Renders a prompt template using the provided variables.

    Creates a Jinja2 Template from the given prompt text and renders it
    by injecting the supplied variables as keyword arguments.

    Args:
        prompt_text (str): The template string containing placeholders.
        variables (dict): A mapping of values to substitute into the template.

    Returns:
        str: The rendered prompt with all placeholders replaced.

    Raises:
        TypeError: If variables is not a mapping suitable for unpacking.
        Exception: Propagates any template rendering errors.
    """
    template = Template(prompt_text)
    return template.render(**variables)


# ------------------------------------------------------------------------------
# Utilities
# ------------------------------------------------------------------------------

def list_category(category):
    """
    Lists subcategories and items within a given category path.

    Inspects the directory under BASE_DIR corresponding to the provided
    category and prints its immediate contents in sorted order.
    Subdirectories are displayed with a trailing slash, while `.md` and
    `.yaml` files are displayed without their file extensions.

    Args:
        category (str): The category or subcategory path relative to BASE_DIR.

    Returns:
        None

    Notes:
        Prints results directly to standard output.
        Does not perform recursive traversal.

    Behavior:
        Prints "Category not found." if the specified path does not exist.
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


def render_output(content, theme="dracula"):
    """
    Renders formatted content to the console with syntax highlighting.

    Determines the appropriate lexer based on the presence of Jinja
    template delimiters and applies syntax highlighting using the
    specified Rich theme. Outputs the formatted content directly
    to the console.

    Args:
        content (str): The text content to render.
        theme (str, optional): The syntax highlighting theme to use.
            Defaults to "dracula".

    Returns:
        None

    Raises:
        Exception: Propagates any errors raised during rendering.
    """
    lexer = "jinja" if "{{" in content or "{%" in content else "markdown"

    syntax = Syntax(
        content,
        lexer,
        theme=theme,
        line_numbers=False,
        word_wrap=True
    )

    console.print(syntax)


def show_path(path, theme="dracula"):
    """
    Displays the contents of a file located under the base directory.

    Resolves the given path relative to BASE_DIR and attempts to locate
    a corresponding `.md` or `.yaml` file. If found, reads and renders
    the file content using syntax highlighting. If the path refers to a
    directory, prints a message suggesting the use of the list command.
    If no file is found, suggests nearby items from the same parent directory.

    Args:
        path (str): The relative path (without extension) to the target file.
        theme (str, optional): The syntax highlighting theme to use.
            Defaults to "dracula".

    Returns:
        None

    Behavior:
        Prints a message if the path is a directory.
        Prints suggestions if the file is not found.
        Outputs content directly to the console.
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

            # console.print(f"[bold cyan]{path}[/bold cyan]\n")
            render_output(content, theme)
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
    Copies the given text to the system clipboard.

    Uses the pyperclip library to place the provided text into the
    clipboard, making it available for pasting in other applications.
    Prints a confirmation message after the operation completes.

    Args:
        text (str): The text content to copy to the clipboard.

    Returns:
        None

    Raises:
        pyperclip.PyperclipException: If the clipboard operation fails.
    """
    pyperclip.copy(text)
    print("Prompt copied to clipboard.")


# ------------------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------------------

def main():
    """
    Serves as the entry point for the PromptNG CLI (`pp`).

    Defines and parses command-line arguments, dispatches commands, composes prompts (either
    from an agent or manually), processes variable inputs, renders the final prompt, and outputs
    or copies the result.

    Commands:
        search:
            Search across components using flexible matching (exact, prefix, substring, wildcard).
            Usage: pp [--theme THEME] search <query> [--category <name>] [--limit N] [--json]

        list:
            List available items in a given category.
            Usage: pp [--theme THEME] list <category>

        show:
            Display the contents of a resource with syntax highlighting.
            Usage: pp [--theme THEME] show <path>

        build:
            Compose a prompt from an agent definition.
            Usage: pp [--theme THEME] build <agent> [--pre ...] [--post ...] [--enforce ...]
                                                    [--var key=value] [--var-file key=path]
                                                    [--var-dir key=dir] [--copy]

        compose:
            Manually compose a prompt from role, task, and patterns.
            Usage: pp [--theme THEME] compose [--role ROLE] [--task TASK] [--pattern ...]
                                            [--pre ...] [--post ...] [--enforce ...]
                                            [--var key=value] [--var-file key=path]
                                            [--var-dir key=dir] [--copy]

    Global Options:
        --theme (str):
            Syntax highlighting theme for output (default: "dracula").

    Variable Handling:
        Variables are collected and injected into the prompt via `render_prompt`.

        1. Literal variables (`--var key=value`)
            Direct key-value pairs.

        2. File variables (`--var-file key=filepath`)
            Loads content from a file. Resolution order:
                - Direct path (with optional .md/.txt extension)
                - Relative to BASE_DIR
                - Recursive search inside BASE_DIR/content
            Provides suggestions if the file is not found.

        3. Directory variables (`--var-dir key=dirpath`)
            Recursively loads `.md` and `.txt` files from a directory,
            concatenating their contents. Hidden and non-text files are ignored.

    Behavior:
        - Parses CLI arguments using `argparse`.
        - Dispatches to the appropriate command handler.
        - Executes search queries with ranked matching when `search` is used.
        - Composes the prompt via `compose_from_agent` or `compose_manual`.
        - Resolves and injects variables into the prompt.
        - Outputs the rendered prompt using `render_output`, or copies it to
          the clipboard if `--copy` is specified.

    Notes:
        - Command execution stops early for `list` and `show`.
        - Search results can be formatted for humans or emitted as JSON.
        - File and directory resolution includes fallback strategies and
          user-friendly suggestions.
        - External helper functions are responsible for I/O, rendering,
          and clipboard interaction.

    Raises:
        SystemExit: On argument parsing errors or unresolved file/directory inputs.
        Exception: Propagates errors from helper functions.
    """
    parser = argparse.ArgumentParser(prog="pp")

    # Make --theme a global option
    parser.add_argument(
    "--theme",
    default="dracula",
    help="Syntax highlighting theme (e.g., dracula, monokai, default)"
)
    subparsers = parser.add_subparsers(dest="command")

    # Search
    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("query")
    search_parser.add_argument("--category")
    search_parser.add_argument("--limit", type=int, default=10)
    search_parser.add_argument("--json", action="store_true")

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
    build_parser.add_argument("--enforce", action="append", help="Enforcement controls")
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
    compose_parser.add_argument("--enforce", action="append", help="Enforcement controls")
    compose_parser.add_argument("--var", action="append", help="Literal variables (key=value)")
    compose_parser.add_argument("--var-file", action="append", help="Variables from file (key=filepath)")
    compose_parser.add_argument("--var-dir", action="append", help="Variables from directory (key=dirpath)")
    compose_parser.add_argument("--copy", action="store_true")

    # --------------------------------------------------------------------------
    # Parse
    # --------------------------------------------------------------------------
    args = parser.parse_args()

    # --------------------------------------------------------------------------
    # Search
    # --------------------------------------------------------------------------
    if args.command == "search":
        # lazy import inside the command handler, which is technically fine, but
        # there are trade-offs.
        from .search import search, print_human
        results = search(args.query, args.category, args.limit)

        if args.json:
            import json
            print(json.dumps(results, indent=2))
        else:
            print_human(results)

        return

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
        show_path(args.path, theme=args.theme)
        return

    # --------------------------------------------------------------------------
    # Build
    # --------------------------------------------------------------------------
    if args.command == "build":
        prompt = compose_from_agent(
            args.agent,
            cli_pre=getattr(args, "pre", None),
            cli_post=getattr(args, "post", None),
            cli_enforce=getattr(args, "enforce", None),
        )

    # --------------------------------------------------------------------------
    # Compose
    # --------------------------------------------------------------------------
    elif args.command == "compose":
        prompt = compose_manual(
            args.role,
            args.task,
            args.pattern,
            cli_pre=getattr(args, "pre", None),
            cli_post=getattr(args, "post", None),
            cli_enforce=getattr(args, "enforce", None),
        )

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

            resolved_path = None

            # ------------------------------------------------------------------
            # 1. Try direct paths (as-is)
            # ------------------------------------------------------------------
            direct_candidates = [filepath]

            if not os.path.splitext(filepath)[1]:
                direct_candidates.extend([
                    filepath + ".md",
                    filepath + ".txt"
                ])

            for path in direct_candidates:
                if os.path.isfile(path):
                    resolved_path = path
                    break

            # ------------------------------------------------------------------
            # 2. Try BASE_DIR paths
            # ------------------------------------------------------------------
            if not resolved_path:
                base_candidates = [
                    os.path.join(BASE_DIR, filepath)
                ]

                if not os.path.splitext(filepath)[1]:
                    base_candidates.extend([
                        os.path.join(BASE_DIR, filepath + ".md"),
                        os.path.join(BASE_DIR, filepath + ".txt")
                    ])

                for path in base_candidates:
                    if os.path.isfile(path):
                        resolved_path = path
                        break

            # ------------------------------------------------------------------
            # 3. Recursive search inside BASE_DIR/content
            # ------------------------------------------------------------------
            if not resolved_path:
                content_root = os.path.join(BASE_DIR, "content")

                name = os.path.basename(filepath)
                name_no_ext, _ = os.path.splitext(name)

                for root, _, files in os.walk(content_root):
                    for file in files:
                        file_name, file_ext = os.path.splitext(file)

                        if (
                            file == name or
                            file_name == name_no_ext
                        ) and file_ext in [".md", ".txt", ""]:
                            resolved_path = os.path.join(root, file)
                            break

                    if resolved_path:
                        break

            # ------------------------------------------------------------------
            # 4. Error handling (ONLY AFTER ALL ATTEMPTS)
            # ------------------------------------------------------------------
            if not resolved_path:
                print(f"Error: file not found -> {filepath}")

                base_candidate = os.path.join(BASE_DIR, filepath)
                dir_path = os.path.dirname(base_candidate)

                while dir_path and not os.path.exists(dir_path):
                    dir_path = os.path.dirname(dir_path)

                if dir_path and os.path.isdir(dir_path):
                    print("\nDid you mean:")

                    for entry in sorted(os.listdir(dir_path)):
                        entry_path = os.path.join(dir_path, entry)

                        if os.path.isfile(entry_path):
                            print(f"  {entry}")

                sys.exit(1)

            # ------------------------------------------------------------------
            # Load file
            # ------------------------------------------------------------------
            with open(resolved_path, "r") as f:
                variables[key] = f.read()

    # 3 Recursive directory variables
    if args.var_dir:
        for item in args.var_dir:
            key, dirpath = item.split("=", 1)

            resolved_dir = None

            # ------------------------------------------------------------------
            # 1. Try direct path (as-is)
            # ------------------------------------------------------------------
            if os.path.isdir(dirpath):
                resolved_dir = dirpath

            # ------------------------------------------------------------------
            # 2. Try BASE_DIR path
            # ------------------------------------------------------------------
            if not resolved_dir:
                base_path = os.path.join(BASE_DIR, dirpath)
                if os.path.isdir(base_path):
                    resolved_dir = base_path

            # ------------------------------------------------------------------
            # 3. Error handling (only after all attempts)
            # ------------------------------------------------------------------
            if not resolved_dir:
                print(f"Error: directory not found -> {dirpath}")

                # Try to suggest from closest valid directory
                base_candidate = os.path.join(BASE_DIR, dirpath)
                dir_candidate = base_candidate

                # Walk up until we find an existing directory
                while dir_candidate and not os.path.exists(dir_candidate):
                    dir_candidate = os.path.dirname(dir_candidate)

                if dir_candidate and os.path.isdir(dir_candidate):
                    print("\nDid you mean:")

                    for entry in sorted(os.listdir(dir_candidate)):
                        entry_path = os.path.join(dir_candidate, entry)

                        if os.path.isdir(entry_path):
                            print(f"  {entry}/")

                sys.exit(1)

            # ------------------------------------------------------------------
            # 4. Load directory recursively (filtered)
            # ------------------------------------------------------------------
            collected = []

            for root, _, files in os.walk(resolved_dir):
                for file in sorted(files):

                    # Skip hidden files
                    if file.startswith("."):
                        continue

                    # Only allow .md and .txt
                    if not file.endswith((".md", ".txt")):
                        continue

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
        render_output(rendered, args.theme)


if __name__ == "__main__":
    main()
