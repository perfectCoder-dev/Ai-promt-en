# Glossary

A reference guide for key terms and concepts used in PromptPro and AI prompting.

---

## A

### Action

A task type in PromptPro designed for executing operations and producing results. Unlike explanatory tasks, action tasks focus on completing a specific request rather than describing or reasoning about a concept.

**Source:** `docs/prompts/tasks/default_tasks.md`

### Action Agent

A predefined agent preset in PromptPro designed to perform tasks by verifying requirements or planning before acting. It uses reasoning strategies and structured outputs to ensure accurate and controlled results.

**Source:** `docs/prompts/agents/default_agents.md`

### Agent / Agent Preset

A reusable prompt configuration stored as a YAML file that combines a role, a task, and one or more patterns into a single, callable preset. Agents provide a convenient way to reuse complex prompt compositions.

**Source:** `docs/prompts/agents/default_agents.md`, `main.py:82-104`

### API (Application Programming Interface)

A set of protocols and tools that allows different software applications to communicate with each other. In PromptPro, APIs are used to send generated prompts to AI models and receive responses.

**Source:** `docs/prompt_pipelines.md`

### Argparse

A Python standard library module used to build command-line interfaces. PromptPro uses argparse to define subcommands (`list`, `show`, `build`, `compose`) and their options.

**Source:** `main.py:37, 550-582`

### Ask Mode

A pre-prompt control that configures the AI for direct question-answering interactions without planning or execution steps.

**Source:** `docs/prompt_control_layers.md`

---

## B

### BASE_DIR

The base directory variable in `main.py` that points to the `prompts/` folder containing all prompt components (agents, patterns, roles, tasks, and controls).

**Source:** `main.py:48-52`

### Behavior Layer

The post-prompt control layer in PromptPro that defines how the response is shaped after generation begins. It includes output formatting, tone, style, and constraints.

**Source:** `docs/prompt_control_layers.md`

### Build Command

A PromptPro CLI subcommand that generates a prompt from a predefined agent configuration. Usage: `pp build <agent> [--var key=value] [--pre control] [--post control] [--copy]`

**Source:** `docs/command_usage.md`, `main.py:563-570`

---

## C

### Chain-of-Thought (CoT)

A reasoning technique that encourages the AI to think step-by-step before providing a final answer, making the reasoning process explicit and improving accuracy on complex problems.

**Source:** `docs/the_iceberg_of_prompting.md`

### CLI (Command Line Interface)

A text-based interface for interacting with software through commands entered in a terminal. PromptPro is a CLI tool invoked with the `pp` command.

**Source:** `README.md`

### Clipboard Export

The ability to copy generated prompts directly to the system clipboard using the `--copy` flag, enabling quick pasting into AI interfaces.

**Source:** `README.md`, `main.py:470-491`

### Command Substitution

A shell feature that allows capturing the output of one command to use as input for another. Syntax: `$(command)` or backticks.

**Source:** `docs/bash_variables.md`

### Compose Command

A PromptPro CLI subcommand that builds a prompt by manually combining a role, task, and patterns. Usage: `pp compose --role <role> --task <task> --pattern <pattern>`

**Source:** `docs/command_usage.md`, `main.py:573-582`

### Context

Background information, constraints, and audience description that helps the AI understand the scope and purpose of a request.

**Source:** `docs/the_iceberg_of_prompting.md`

### Context Window

The maximum number of tokens (words and fragments) that an AI model can process in a single request, including both input and output. Large inputs may exceed this limit and cause truncation.

**Source:** `README.md`

### Control Layers

PromptPro's architecture that separates execution control (pre-prompt) from output behavior (post-prompt). This separation makes prompts more modular, predictable, and composable.

**Source:** `docs/prompt_control_layers.md`

### Copy Option

The `--copy` flag in PromptPro that copies the rendered prompt to the system clipboard instead of printing it to stdout.

**Source:** `docs/command_usage.md`, `main.py:676-679`

### CS Instructor

A computer science teaching agent that specializes in explaining CS concepts step by step with structured outputs.

**Source:** `docs/prompts/agents/default_agents.md`

---

## D

### Deep Prompting

Level 3 of the Iceberg of Prompting framework, involving guided reasoning, iteration, and strategic refinement. Designed for complex problems and high-stakes decisions.

**Source:** `docs/the_iceberg_of_prompting.md`

### Didactic

A pattern group that expands into the `socratic` and `step_by_step` patterns. It combines inquiry-based questioning with sequential reasoning.

**Source:** `docs/prompts/pattern_groups/default_pattern_groups.md`

### Didactic Structured

A pattern group that expands into `socratic`, `step_by_step`, and `structured_output` patterns. A comprehensive teaching bundle.

**Source:** `docs/prompts/pattern_groups/default_pattern_groups.md`

### Domain

The subject area or field of expertise relevant to a prompt. In role definitions, the domain helps shape the AI's perspective and terminology.

**Source:** `docs/creating_new_prompt_components.md`

---

## E

### Executor

A role in PromptPro that prioritizes carrying out requested actions efficiently and directly. The focus is on task completion rather than explanation or teaching.

**Source:** `docs/prompts/roles/default_roles.md`

### Execution Layer

The pre-prompt control layer that defines how the system operates before generating any response. It includes execution environment setup, model configuration, and memory management.

**Source:** `docs/prompt_control_layers.md`

### Execution Mechanism

The methods used to implement cognitive strategies in prompts, such as "Think deeply before answering" or "Chain-of-Thought."

**Source:** `docs/the_iceberg_of_prompting.md`

### Explain

A task type in PromptPro designed for presenting concepts through clear, step-by-step explanations that build understanding progressively.

**Source:** `docs/prompts/tasks/default_tasks.md`

### Explain Like I'm 5

A post-prompt control that adjusts explanations for absolute beginners, using simple language and intuitive analogies.

**Source:** `docs/prompt_control_layers.md`

---

## F

### Few-shot Prompting

A prompting technique that includes multiple examples in the prompt to guide the AI toward the desired output format or reasoning pattern.

**Source:** `docs/the_iceberg_of_prompting.md`

---

## G

### Glossary

This document—a reference guide containing definitions of key terms and concepts used in PromptPro and AI prompting.

---

## H

### Hierarchical Composition

Building complex prompts from nested or layered components (agents containing patterns, patterns within pattern groups) rather than flat, monolithic prompts.

**Source:** `docs/create_and_use_a_pattern_group.md`

---

## I

### Iceberg of Prompting

A framework by Ruben Hassid that visualizes prompting depth in three levels: surface prompting (Level 1), structured prompting (Level 2), and deep prompting (Level 3).

**Source:** `docs/the_iceberg_of_prompting.md`

### Inquiry-based

A teaching approach that guides learning through targeted questions rather than direct instruction, encouraging exploration and reasoning.

**Source:** `docs/prompts/roles/default_roles.md`

### Iteration Loop

A cognitive strategy involving feedback, revision, and final output. The AI refines its response based on self-assessment or external feedback.

**Source:** `docs/the_iceberg_of_prompting.md`

---

## J

### Jinja / Jinja2

A template engine for Python that PromptPro uses for variable injection. Variables are referenced using `{{ variable_name }}` syntax.

**Source:** `README.md`, `main.py:42, 333-334`

---

## L

### Level 1 Prompting

Surface prompting—simple, direct requests with minimal context. Fast for basic tasks but limited for complex or precise requirements.

**Source:** `docs/the_iceberg_of_prompting.md`

### Level 2 Prompting

Structured prompting with clear roles, defined tasks, added context, and output constraints. Improves reliability and consistency for real-world work.

**Source:** `docs/the_iceberg_of_prompting.md`

### Level 3 Prompting

Deep prompting with guided reasoning, iteration, and strategic refinement. Designed for complex problems and optimized results.

**Source:** `docs/the_iceberg_of_prompting.md`

### List Command

A PromptPro CLI subcommand that displays available components in a category. Usage: `pp list <roles|agents|patterns|tasks|controls>`

**Source:** `docs/command_usage.md`, `main.py:341-384`

### LLM (Large Language Model)

A type of AI model trained on vast amounts of text data to understand and generate human language. Examples include GPT, Claude, and Llama.

**Source:** `docs/prompt_control_layers.md`

### Load Agent

A function in `main.py` that parses an agent's YAML configuration file and returns it as a Python dictionary.

**Source:** `main.py:82-104`

### Load Controls

A function in `main.py` that retrieves pre-prompt or post-prompt control fragments from the controls directory.

**Source:** `main.py:134-167`

### Load Pattern Group

A function in `main.py` that parses a pattern group's YAML configuration and returns the nested pattern definitions.

**Source:** `main.py:107-131`

### Load Text

A function in `main.py` that reads and returns the contents of a Markdown prompt component file.

**Source:** `main.py:58-79`

---

## M

### Math Tutor

An educational agent that teaches mathematical concepts through step-by-step explanations and Socratic questioning.

**Source:** `docs/prompts/agents/default_agents.md`

### MCP (Model Context Protocol)

A protocol that enables integration between AI models and external tools or services. PromptPro supports MCP configurations.

**Source:** `docs/prompt_control_layers.md`

### Memory Management

Pre-prompt controls that handle context retention, such as instructing the AI to "forget" previous context or manage session state.

**Source:** `docs/prompt_control_layers.md`

### Model Selection

Choosing between different AI models based on task requirements, such as "thinking" models for complex reasoning or "fast" models for quick responses.

**Source:** `docs/prompt_control_layers.md`

### Modular

An architectural approach where prompts are composed of independent, reusable building blocks (roles, tasks, patterns) that can be mixed and matched.

**Source:** `README.md`

---

## O

### One-shot Prompting

A prompting technique that includes a single example in the prompt to demonstrate the expected format or approach.

**Source:** `docs/the_iceberg_of_prompting.md`

### Operational Control

Constraints that define limits and boundaries for AI responses, such as restrictions on content, length, or formatting.

**Source:** `docs/the_iceberg_of_prompting.md`

### Output Format

The structure in which an AI presents its response, such as bullet points, tables, numbered lists, or labeled sections.

**Source:** `docs/the_iceberg_of_prompting.md`

---

## P

### Pattern

A reusable fragment of prompt text that defines a reasoning strategy or output instruction. Patterns are combined with roles and tasks to build complete prompts.

**Source:** `docs/prompts/patterns/default_patterns.md`

### Pattern Group

A YAML file that bundles multiple patterns together under a single name. When referenced, a pattern group expands into its constituent patterns.

**Source:** `docs/create_and_use_a_pattern_group.md`

### Pipeline

In Unix philosophy, a chain of commands where the output of one command becomes the input of the next. PromptPro outputs plain text, enabling seamless pipeline integration.

**Source:** `docs/prompt_pipelines.md`

### Plan Mode

A pre-prompt control that instructs the AI to outline steps before executing a task, separating planning from action.

**Source:** `docs/prompt_control_layers.md`

### Plan Execute

A pattern that instructs the model to first outline a concise sequence of steps and then carry them out in order, improving clarity and reliability.

**Source:** `docs/prompts/patterns/default_patterns.md`

### Post-prompt Controls

Behavior layer controls that shape how the response is generated and presented, including translation, tone, and truthfulness safeguards.

**Source:** `docs/prompt_control_layers.md`

### Pre-prompt Controls

Execution layer controls that define how the system operates before generating any response, including model selection and memory configuration.

**Source:** `docs/prompt_control_layers.md`

### Prompt Bus

A concept where PromptPro acts as a universal prompt distributor, feeding generated prompts to multiple downstream systems (AI models, APIs, databases, etc.).

**Source:** `docs/prompt_pipelines.md`

### Prompt Components

The modular building blocks that make up prompts in PromptPro: agents, roles, tasks, patterns, pattern groups, and controls.

**Source:** `docs/prompt_components_reference.md`

### Prompt Engineering

The discipline of crafting effective prompts to elicit desired responses from AI models. It involves understanding model behavior and structuring inputs strategically.

**Source:** `docs/the_iceberg_of_prompting.md`

### PromptPro

A modular CLI tool for composing, managing, and orchestrating reusable AI prompt components. It treats prompts as structured building blocks that can be assembled and reused.

**Source:** `README.md`

### Pyperclip

A Python library used by PromptPro to copy generated prompts to the system clipboard.

**Source:** `main.py:39, 470-491`

---

## Q

### Question-first

A cognitive strategy that approaches problems by asking "how" questions before attempting to "do" or execute a solution.

**Source:** `docs/the_iceberg_of_prompting.md`

---

## R

### Reasoning Instruction

A directive in prompts that instructs the AI to think deeply before answering, such as "Think step by step" or "Consider all angles."

**Source:** `docs/the_iceberg_of_prompting.md`

### Recursive Resolution

The process by which PromptPro expands pattern groups into their constituent patterns, including nested groups within groups.

**Source:** `main.py:173-214`

### Render

The process of applying variable substitution to a prompt template, replacing placeholders like `{{ input }}` with actual values.

**Source:** `main.py:311-334`

### Resolve Patterns

A function in `main.py` that recursively expands pattern groups into a flat list of individual patterns.

**Source:** `main.py:173-214`

### Rich

A Python library used by PromptPro for terminal output formatting, including syntax highlighting for YAML and Markdown files.

**Source:** `main.py:43-44, 439-447`

### Role

A persona or behavioral identity assigned to the AI, such as "tutor," "executor," or "technical_instructor." The role shapes the AI's communication style and approach.

**Source:** `docs/prompts/roles/default_roles.md`

### Role-based Prompting

Assigning a specific expertise persona to the AI to leverage specialized knowledge and communication patterns.

**Source:** `docs/the_iceberg_of_prompting.md`

---

## S

### Show Command

A PromptPro CLI subcommand that displays the contents of a specific prompt component with syntax highlighting. Usage: `pp show <path>`

**Source:** `docs/command_usage.md`, `main.py:387-468`

### Socratic

A pattern that encourages the AI to guide reasoning through reflective questioning, prompting users to examine assumptions and progressively arrive at conclusions.

**Source:** `docs/prompts/patterns/default_patterns.md`

### Standard Input/Output (stdin/stdout)

The default data streams in Unix systems. stdin receives input from the user or piped data; stdout sends output to the terminal or another command.

**Source:** `docs/prompt_pipelines.md`

### Step-by-step

A pattern that guides the AI to structure its reasoning as a sequence of clearly numbered steps, making each stage of thought explicit.

**Source:** `docs/prompts/patterns/default_patterns.md`

### Stop Conditions

Limits and boundaries defined in prompts to control the scope or length of AI responses.

**Source:** `docs/the_iceberg_of_prompting.md`

### Structured Output

A pattern that instructs the AI to organize its response in labeled sections with bullet points and a concluding summary.

**Source:** `docs/prompts/patterns/default_patterns.md`

### Structured Prompting

An approach to prompting that uses well-defined components (roles, tasks, context, constraints) to produce more reliable and consistent results.

**Source:** `docs/the_iceberg_of_prompting.md`

### Surface Prompting

Level 1 of the Iceberg framework—simple, direct requests with minimal context. Fast for basic tasks but limited for precision.

**Source:** `docs/the_iceberg_of_prompting.md`

### Syntax Highlighting

Color-coded display of code or text in the terminal. PromptPro uses Rich to highlight YAML and Markdown with appropriate colors.

**Source:** `main.py:439-447`

### System Prompt

Base instructions that define fundamental AI behavior, typically loaded before user input.

**Source:** `docs/prompt_control_layers.md`

---

## T

### Task

A component that defines the action or type of work the AI is expected to perform, such as "explain," "action," or "compose_action."

**Source:** `docs/prompts/tasks/default_tasks.md`

### Template

A prompt skeleton containing variable placeholders (e.g., `{{ input }}`) that are replaced with actual values during rendering.

**Source:** `main.py:333-334`

### Token

The basic unit of text that AI models process. Tokens can be partial words, full words, or punctuation marks. Context windows are measured in tokens.

**Source:** `README.md`

### Tone

The style and manner of AI communication, such as formal, casual, technical, or friendly.

**Source:** `docs/prompt_control_layers.md`

### Translate

A post-prompt control that converts the AI's output into a specified language.

**Source:** `docs/prompt_control_layers.md`

### Tutor

An inquiry-based teaching role that guides learners through problem-solving using targeted questions rather than direct answers.

**Source:** `docs/prompts/roles/default_roles.md`

---

## U

### Unix Philosophy

A design principle favoring simple, focused programs that do one thing well, connected through pipes. PromptPro outputs plain text, embracing this philosophy for pipeline integration.

**Source:** `docs/prompt_pipelines.md`

---

## V

### Variable Injection

The process of inserting dynamic values into prompt templates using the `--var`, `--var-file`, or `--var-dir` options.

**Source:** `docs/bash_variables.md`

### Variable Sources

The three methods PromptPro supports for providing variable values:
- `--var`: Literal values from the command line
- `--var-file`: Values loaded from a single file
- `--var-dir`: Values loaded from all files in a directory

**Source:** `docs/command_usage.md`

### Verify Before Execute

A pattern that ensures all necessary information is present and clear before performing an action, pausing to identify missing inputs instead of proceeding with incomplete data.

**Source:** `docs/prompts/patterns/default_patterns.md`

---

## W

### Workflow

A repeatable sequence of steps for creating prompts, such as the `build` workflow (using agent presets) or the `compose` workflow (manual component combination).

**Source:** `README.md`

---

## Y

### YAML

A human-readable data serialization format used for configuration files in PromptPro, including agents and pattern groups.

**Source:** `docs/create_and_use_a_pattern_group.md`, `main.py:41, 104`

---

## Z

### Zero-shot Prompting

A prompting technique where the AI is asked to perform a task without any examples, relying solely on its pre-trained knowledge.

**Source:** `docs/the_iceberg_of_prompting.md`
