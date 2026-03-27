# Prompt Components Reference

This document explains the structure, organization, and available building blocks that can be combined to construct modular, reusable, and maintainable prompts.

PromptPro breaks prompts into well-defined components, allowing them to be composed, extended, and managed independently. This ensures consistency, scalability, and clarity across use cases.

## Prompt Categories

The `prompts` directory contains the core components used to build prompts in PromptPro, organized by category.

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

## List Of Components

Below is a complete list of built-in components and their features for creating prompts.

> [!TIP]
> **Extend the built-in version of the list** by adding new components as you create them.  
> For a step-by-step guide on **creating new agents, roles, tasks, and pattern components**, see:
> * [Agents, Roles, Tasks, and Patterns](creating_new_prompt_components.md)

### Built-in Agents

- [action_agent](./prompts/agents/built-in_agents.md#agent-action_agent)
- [cs_instructor](./prompts/agents/built-in_agents.md#agent-cs_instructor)
- [math_tutor](./prompts/agents/built-in_agents.md#agent-math_tutor)

---

### Built-in Pattern Groups

- [didactic](./prompts/pattern_groups/built-in_pattern_groups.md#pattern-group-didactic)
- [didactic_structured](./prompts/pattern_groups/built-in_pattern_groups.md#pattern-group-didactic_structured)

---

### Built-in Patterns

- [plan_execute](./prompts/patterns/built-in_patterns.md#pattern-plan_execute)
- [socratic](./prompts/patterns/built-in_patterns.md#pattern-socratic)
- [step_by_step](./prompts/patterns/built-in_patterns.md#pattern-step_by_step)
- [structured_output](./prompts/patterns/built-in_patterns.md#pattern-structured_output)
- [verify_before_execute](./prompts/patterns/built-in_patterns.md#pattern-verify_before_execute)

---

### Built-in Roles

- [executor](./prompts/roles/built-in_roles.md#role-executor)
- [technical_instructor](./prompts/roles/built-in_roles.md#role-technical_instructor)
- [tutor](./prompts/roles/built-in_roles.md#role-tutor)

---

### Built-in Tasks

- [action](./prompts/tasks/built-in_tasks.md#task-action)
- [compose_action](./prompts/tasks/built-in_tasks.md#task-compose_action)
- [explain](./prompts/tasks/built-in_tasks.md#task-explain)

---

### Built-in Controls

#### Pre Controls

Category: `config`

- [configurations](./prompts/controls/built-in_controls.md#control-configconfigurations)

Category: `language`

- [input_default](./prompts/controls/built-in_controls.md#control-languageinput_default)

Category: `mcp`

- [mcp_local](./prompts/controls/built-in_controls.md#control-mcpmcp_local)

- [mcp_remote](./prompts/controls/built-in_controls.md#control-mcpmcp_remote)

Category: `memory`

- [forget](./prompts/controls/built-in_controls.md#control-memoryforget)

Category: `mode`

- [agent](./prompts/controls/built-in_controls.md#control-modeagent)

- [ask](./prompts/controls/built-in_controls.md#control-modeask)

- [bypass_permissions](./prompts/controls/built-in_controls.md#control-modebypass_permissions)

- [plan](./prompts/controls/built-in_controls.md#control-modeplan)

Category: `model`

- [model_fast](./prompts/controls/built-in_controls.md#control-modelmodel_fast)

- [model_thinking](./prompts/controls/built-in_controls.md#control-modelmodel_thinking)

Category: `security`

- [no_env_access](./prompts/controls/built-in_controls.md#control-securityno_env_access)

Category: `system`

- [system_prompt](./prompts/controls/built-in_controls.md#control-systemsystem_prompt)

Category: `tools`

- [tools_call](./prompts/controls/built-in_controls.md#control-toolstools_call)

- [tools_define](./prompts/controls/built-in_controls.md#control-toolstools_define)

- [tools_off](./prompts/controls/built-in_controls.md#control-toolstools_off)

- [tools_on](./prompts/controls/built-in_controls.md#control-toolstools_on)

#### Post Controls

Category: `limits`

- [explain_like_12](./prompts/controls/built-in_controls.md#control-limitsexplain_like_12)

- [for_beginners](./prompts/controls/built-in_controls.md#control-limitsfor_beginners)

Category: `tone`

- [tone_style](./prompts/controls/built-in_controls.md#control-tonetone_style)

Category: `translation`

- [translate_en](./prompts/controls/built-in_controls.md#control-translationtranslate_en)

- [translate_output](./prompts/controls/built-in_controls.md#control-translationtranslate_output)

- [translate_sp](./prompts/controls/built-in_controls.md#control-translationtranslate_sp)

Category: `truth`

- [say_dont_know](./prompts/controls/built-in_controls.md#control-truthsay_dont_know)
