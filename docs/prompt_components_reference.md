# 🗂 Prompt Composable Elements Reference

This document serves as a reference guide for the composable prompt system used in PromptPro. It explains the structure, organization, and available building blocks that can be combined to construct modular, reusable, and maintainable prompts.

The goal of this system is to separate prompts into well-defined components—such as agents, roles, patterns, pattern groups, and tasks—so they can be composed, extended, and managed independently. This approach improves consistency, scalability, and clarity when designing prompts for different use cases.

## Prompt Category Structure

The `prompts/` directory contains the core components used to build prompts in PromptPro, organized by category.

### Categories

```bash
prompts
├── agents
├── pattern_groups
├── patterns
├── roles
└── tasks
```

You can list **prompt composable elements** by category in several ways, such as:

```bash
pp list roles
pp list roles | grep -E 'te|utor'
```

Below is a **complete list of elements** and their features available in PromptPro for building prompts, composing them, and creating new ones.

**You can extend your own local version of the list** by adding new elements as you create them.

Here is a step-by-step guide to **creating new agents, roles, tasks, and pattern elements** for your Prompctl:

* [Agents, Roles, Tasks, And Patterns](docs/new_roles_tasks_and_patterns.md)

## Agents

### Default Agents

- [action_agent](./prompts/agents/default_agents.md)
- [cs_instructor](./prompts/agents/default_agents.md)
- [math_tutor](./prompts/agents/default_agents.md)

## Pattern Groups

### Default Pattern Groups

- [didactic](./prompts/pattern_groups/default_pattern_groups.md)
- [didactic_structured](./prompts/pattern_groups/default_pattern_groups.md)

## Patterns

### Default Patterns

- [plan_execute](./prompts/patterns/default_patterns.md)
- [socratic](./prompts/patterns/default_patterns.md)
- [step_by_step](./prompts/patterns/default_patterns.md)
- [structured_output](./prompts/patterns/default_patterns.md)
- [verify_before_execute](./prompts/patterns/default_patterns.md)

## Roles

### Default Roles

- [executor](./prompts/roles/default_roles.md)
- [technical_instructor](./prompts/roles/default_roles.md)
- [tutor](./prompts/roles/default_roles.md)

## Tasks

### Default Tasks

- [action](./prompts/tasks/default_tasks.md)
- [action_with_context](./prompts/tasks/default_tasks.md)
- [action_with_context_and_examples](./prompts/tasks/default_tasks.md)
- [action_with_examples](./prompts/tasks/default_tasks.md)
- [explain](./prompts/tasks/default_tasks.md)
