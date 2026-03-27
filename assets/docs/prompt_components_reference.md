# Prompt Components Reference

PromptPro organizes prompts into well-defined components that can be composed, extended, and managed independently. This approach improves consistency, scalability, and maintainability across use cases.

## Prompt Categories

The `prompts` directory contains all prompt components, organized into categories (such as agents, roles, and tasks). Each category groups related components by purpose.

```bash
pp show prompts
```

**Output structure**

```bash
prompts
├── agents
├── content
├── controls
├── pattern_groups
├── patterns
├── roles
└── tasks
```

## Prompt Components

Each prompt is built by combining components such as a role (who is speaking), a task (what to do), optional patterns (how to think), and controls (constraints or behavior modifiers).

### Listing Prompt Components

To list components within a specific category, use:

**Syntax**

```bash
pp list <agents|content|controls|pattern_groups|patterns|roles|tasks>
```

**Examples**

```bash
pp list roles
pp list agents | grep instructor
pp list content/dev/testing | more
```

> [!TIP]
> You can filter lists using command-line tools such as `grep` to locate components whose names match a specific pattern.
> 
> ```bash
> pp list roles | grep -E 'te|utor'
> ```

### Creating Prompt Components

Refer to the following guides for creating new components:

- Agents, roles, tasks, and patterns:

  [🔗 Agents, Roles, Tasks, and Patterns](creating_new_prompt_components.md)
 
- Pattern groups:

  🔗 [Creating And Using Pattern Groups](assets/docs/create_and_use_a_pattern_group.md)
 
- Control layers:

  🔗 [Prompt Control Layers](assets/docs/prompt_control_layers.md)

## Built-in Components

Below is a **complete list** of built-in components and their features for creating prompts, divided by category.

> [!TIP]
> Extend this built-in list by adding your own components as you create them.

### Built-in Agents

- [🔗 action_agent](./prompts/agents/built-in_agents.md#agent-action_agent)

- [🔗 cs_instructor](./prompts/agents/built-in_agents.md#agent-cs_instructor)
 
- [🔗 math_tutor](./prompts/agents/built-in_agents.md#agent-math_tutor)

---

### Built-in Pattern Groups

- [🔗 didactic](./prompts/pattern_groups/built-in_pattern_groups.md#pattern-group-didactic)

- [🔗 didactic_structured](./prompts/pattern_groups/built-in_pattern_groups.md#pattern-group-didactic_structured)

---

### Built-in Patterns

- [🔗 plan_execute](./prompts/patterns/built-in_patterns.md#pattern-plan_execute)

- [🔗 socratic](./prompts/patterns/built-in_patterns.md#pattern-socratic)

- [🔗 step_by_step](./prompts/patterns/built-in_patterns.md#pattern-step_by_step)

- [🔗 structured_output](./prompts/patterns/built-in_patterns.md#pattern-structured_output)

- [🔗 verify_before_execute](./prompts/patterns/built-in_patterns.md#pattern-verify_before_execute)

---

### Built-in Roles

- [🔗 executor](./prompts/roles/built-in_roles.md#role-executor)

- [🔗 technical_instructor](./prompts/roles/built-in_roles.md#role-technical_instructor)

- [🔗 tutor](./prompts/roles/built-in_roles.md#role-tutor)

---

### Built-in Tasks

- [🔗 action](./prompts/tasks/built-in_tasks.md#task-action)

- [🔗 compose_action](./prompts/tasks/built-in_tasks.md#task-compose_action)

- [🔗 explain](./prompts/tasks/built-in_tasks.md#task-explain)

---

### Built-in Controls

#### **Pre Controls**

**`config`**

- [🔗 configurations](./prompts/controls/built-in_controls.md#control-configconfigurations)

**`language`**

- [🔗 input_default](./prompts/controls/built-in_controls.md#control-languageinput_default)

**`mcp`**

- [🔗 mcp_local](./prompts/controls/built-in_controls.md#control-mcpmcp_local)

- [🔗 mcp_remote](./prompts/controls/built-in_controls.md#control-mcpmcp_remote)

**`memory`**

- [🔗 forget](./prompts/controls/built-in_controls.md#control-memoryforget)

**`mode`**

- [🔗 agent](./prompts/controls/built-in_controls.md#control-modeagent)

- [🔗 ask](./prompts/controls/built-in_controls.md#control-modeask)

- [🔗 bypass_permissions](./prompts/controls/built-in_controls.md#control-modebypass_permissions)

- [🔗 plan](./prompts/controls/built-in_controls.md#control-modeplan)

**`model`**

- [🔗 model_fast](./prompts/controls/built-in_controls.md#control-modelmodel_fast)

- [🔗 model_thinking](./prompts/controls/built-in_controls.md#control-modelmodel_thinking)

**`security`**

- [🔗 no_env_access](./prompts/controls/built-in_controls.md#control-securityno_env_access)

**`system`**

- [🔗 system_prompt](./prompts/controls/built-in_controls.md#control-systemsystem_prompt)

**`tools`**

- [🔗 tools_call](./prompts/controls/built-in_controls.md#control-toolstools_call)

- [🔗 tools_define](./prompts/controls/built-in_controls.md#control-toolstools_define)

- [🔗 tools_off](./prompts/controls/built-in_controls.md#control-toolstools_off)

- [🔗 tools_on](./prompts/controls/built-in_controls.md#control-toolstools_on)

#### **Post Controls**

**`limits`**

- [🔗 explain_like_12](./prompts/controls/built-in_controls.md#control-limitsexplain_like_12)

- [🔗 for_beginners](./prompts/controls/built-in_controls.md#control-limitsfor_beginners)

**`tone`**

- [🔗 tone_style](./prompts/controls/built-in_controls.md#control-tonetone_style)

**`translation`**

- [🔗 translate_en](./prompts/controls/built-in_controls.md#control-translationtranslate_en)

- [🔗 translate_output](./prompts/controls/built-in_controls.md#control-translationtranslate_output)

- [🔗 translate_sp](./prompts/controls/built-in_controls.md#control-translationtranslate_sp)

**`truth`**

- [🔗 say_dont_know](./prompts/controls/built-in_controls.md#control-truthsay_dont_know)
