# 🗂 Prompt Composable Elements Reference

TODO: Intro. Describe what this doc is made for ...

## Prompt Category Structure

The `prompts/` directory contains the core components used to build prompts in promptctl, organized by category.

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
promptctl list roles
promptctl list roles | grep -E 'te|utor'
```

Below is a **complete list of elements** and their features available in promptctl for building prompts, composing them, and creating new ones. **Users can extend their own local version of this list** by adding new elements as they create them.

Alternatively, users can open the corresponding **element file** to review or edit its contents. **Any changes will affect all elements associated with the modified element**.

## Agents

### Default Agents

- [cs_instructor](./prompts/agents/default_agents.md)
- [math_tutor](./prompts/agents/default_agents.md)

## Pattern Groups

### Default Pattern Groups

- [didactic](./prompts/pattern_groups/default_pattern_groups.md)
- [didactic_structured](./prompts/pattern_groups/default_pattern_groups.md)

## Patterns

### Default Patterns

- [socratic](./prompts/patterns/default_patterns.md)
- [step_by_step](./prompts/patterns/default_patterns.md)
- [structured_output](./prompts/patterns/default_patterns.md)

## Roles

### Default Roles

- [technical_instructor](./prompts/roles/default_roles.md)
- [tutor](./prompts/roles/default_roles.md)

## Tasks

### Default Tasks

- [action](./prompts/tasks/default_tasks.md)
- [action_with_context](./prompts/tasks/default_tasks.md)
- [action_with_context_and_examples](./prompts/tasks/default_tasks.md)
- [action_with_examples](./prompts/tasks/default_tasks.md)
- [explain](./prompts/tasks/default_tasks.md)
