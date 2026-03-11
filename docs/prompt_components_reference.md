# 🗂 Prompt Compose Reference

This document explains the structure, organization, and available building blocks that can be combined to construct modular, reusable, and maintainable prompts.

PromptPro breaks prompts into well-defined components, allowing them to be composed, extended, and managed independently. This ensures consistency, scalability, and clarity across use cases.

## Prompt Categories

The `prompts/` directory contains the core components used to build prompts in PromptPro, organized by category.

```bash
prompts
├── agents
├── pattern_groups
├── patterns
├── roles
└── tasks
```

## Prompt Components

To list **components** by **prompt category**, use:

**Syntax:**

```bash
pp list <agents|pattern_groups|patterns|roles|tasks>
```

**Examples**:

```bash
pp list roles
pp list agents
```

> [!TIP]
> You can filter lists using `grep` patterns:
> ```bash
> pp list roles | grep -E 'te|utor'
> ```

## Lists Of Components

Below is a complete list of components and their features for creating prompts.

> [!TIP]
> **Extend your local version of the list** by adding new components as you create them.  
> For a step-by-step guide on **creating new agents, roles, tasks, and pattern components**, see:
> * [Agents, Roles, Tasks, and Patterns](creating_new_prompt_components.md)

## Default Agents

- [action_agent](./prompts/agents/default_agents.md)
- [cs_instructor](./prompts/agents/default_agents.md)
- [math_tutor](./prompts/agents/default_agents.md)


## Default Pattern Groups

- [didactic](./prompts/pattern_groups/default_pattern_groups.md)
- [didactic_structured](./prompts/pattern_groups/default_pattern_groups.md)

### Default Patterns

- [plan_execute](./prompts/patterns/default_patterns.md)
- [socratic](./prompts/patterns/default_patterns.md)
- [step_by_step](./prompts/patterns/default_patterns.md)
- [structured_output](./prompts/patterns/default_patterns.md)
- [verify_before_execute](./prompts/patterns/default_patterns.md)

## Default Roles

- [executor](./prompts/roles/default_roles.md)
- [technical_instructor](./prompts/roles/default_roles.md)
- [tutor](./prompts/roles/default_roles.md)

## Default Tasks

- [action](./prompts/tasks/default_tasks.md)
- [compose_action](./prompts/tasks/default_tasks.md)
- [explain](./prompts/tasks/default_tasks.md)
