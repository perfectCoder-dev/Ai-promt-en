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

  🔗 [ Agents, Roles, Tasks, and Patterns](creating_new_prompt_components.md)
 
- Pattern groups:

  🔗 [Creating And Using Pattern Groups](create_and_use_a_pattern_group.md)
 
- Control layers:

  🔗 [Prompt Control Layers](prompt_control_layers.md)

## Built-in Components

Below is a **complete list** of built-in components and their features for creating prompts, divided by category.

> [!TIP]
> Extend this built-in list by adding your own components as you create them.

### 🔗 [Built-in Agents](./prompts/agents/built-in_agents.md)

Agents are ready-to-use compositions that combine roles, tasks, and patterns into practical, goal-oriented configurations. They serve as reference implementations for how different reasoning strategies and execution styles can be applied to real use cases.

- 🔗 [software_testing_agent](./prompts/agents/built-in_agents.md#agent-software_testing_agent)

- 🔗 [action_agent](./prompts/agents/built-in_agents.md#agent-action_agent)

- 🔗 [action_agent_controlled](./prompts/agents/built-in_agents.md#agent-action_agent_controlled)

- 🔗 [cs_instructor](./prompts/agents/built-in_agents.md#agent-cs_instructor)
 
- 🔗 [math_tutor](./prompts/agents/built-in_agents.md#agent-math_tutor)

---

### 🔗 [Built-in Pattern Groups](./prompts/pattern_groups/built-in_pattern_groups.md)

Pattern groups provide higher-level abstractions that bundle multiple patterns into reusable configurations. They simplify composition by allowing a single reference to expand into a coordinated set of reasoning strategies and execution mechanisms.

- 🔗 [didactic](./prompts/pattern_groups/built-in_pattern_groups.md#pattern-group-didactic)

- 🔗 [didactic_structured](./prompts/pattern_groups/built-in_pattern_groups.md#pattern-group-didactic_structured)

- 🔗 [testing_strict](./prompts/pattern_groups/built-in_pattern_groups.md#pattern-group-testing_strict)

---

### 🔗 [Built-in Patterns](./prompts/patterns/built-in_patterns.md)

Patterns define reusable reasoning and execution behaviors that shape how a task is approached. They operate at a lower level than roles, providing specific strategies such as planning before acting, guiding reasoning through questions, or structuring outputs.

Each pattern encapsulates a distinct cognitive approach and can be combined with others to create more sophisticated behaviors. By composing patterns, agents gain flexibility in how they reason, validate, and present results.

- 🔗 [break_assumptions](./prompts/patterns/built-in_patterns.md#pattern-break_assumptions)

- 🔗 [plan_execute](./prompts/patterns/built-in_patterns.md#pattern-plan_execute)

- 🔗 [self_critique](./prompts/patterns/built-in_patterns.md#pattern-self_critique)

- 🔗 [socratic](./prompts/patterns/built-in_patterns.md#pattern-socratic)

- 🔗 [step_by_step](./prompts/patterns/built-in_patterns.md#pattern-step_by_step)

- 🔗 [structured_output](./prompts/patterns/built-in_patterns.md#pattern-structured_output)

- 🔗 [verify_before_execute](./prompts/patterns/built-in_patterns.md#pattern-verify_before_execute)

---

### 🔗 [Built-in Roles](./prompts/roles/built-in_roles.md)

Roles define the core behavior of an agent. They determine how a task is approached, influencing execution style, level of guidance, and reasoning strategy.

Each role represents a distinct way of operating—such as executing actions, explaining concepts, or guiding learning.

- 🔗 [software_tester](./prompts/roles/built-in_roles.md#role-software_tester)

- 🔗 [executor](./prompts/roles/built-in_roles.md#role-executor)

- 🔗 [technical_instructor](./prompts/roles/built-in_roles.md#role-technical_instructor)

- 🔗 [tutor](./prompts/roles/built-in_roles.md#role-tutor)

---

### 🔗 [Built-in Tasks](./prompts/tasks/built-in_tasks.md)

Tasks define what is expected to be done. They represent the objective or operation to be performed, such as executing an action, composing a response with context, or explaining a concept.

While roles determine how an agent behaves and patterns define how it reasons, tasks specify the actual goal. By combining tasks with roles, patterns, and variables, agents can be precisely configured to handle a wide range of use cases.

- 🔗 [action](./prompts/tasks/built-in_tasks.md#task-action)

- 🔗 [compose_action](./prompts/tasks/built-in_tasks.md#task-compose_action)

- 🔗 [explain](./prompts/tasks/built-in_tasks.md#task-explain)

---

### 🔗 [Built-in Controls](./prompts/controls/built-in_controls.md)

Built-in controls define behavior across the full execution lifecycle—before, during, and after response generation. They function as modular switches that control reasoning patterns, permissions, language handling, tool usage, and output shaping, enabling deterministic and composable behavior.

#### `pre/config`

- 🔗 [configurations](./prompts/controls/built-in_controls.md#control-preconfigconfigurations)

#### `enforce/config`

- 🔗 [configurations_guard](./prompts/controls/built-in_controls.md#control-enforceconfigconfigurations_guard)

#### `enforce/config`

- 🔗 [configurations_guard_hardened](./prompts/controls/built-in_controls.md#control-enforceconfigconfigurations_guard_hardened)

#### `pre/language`

- 🔗 [input_default](./prompts/controls/built-in_controls.md#control-prelanguageinput_default)

#### `pre/mcp`

- 🔗 [mcp_local](./prompts/controls/built-in_controls.md#control-premcpmcp_local)

- 🔗 [mcp_remote](./prompts/controls/built-in_controls.md#control-premcpmcp_remote)

#### `pre/memory`

- 🔗 [forget](./prompts/controls/built-in_controls.md#control-prememoryforget)

#### `pre/mode`

- 🔗 [agent](./prompts/controls/built-in_controls.md#control-premodeagent)

- 🔗 [ask](./prompts/controls/built-in_controls.md#control-premodeask)

- 🔗 [bypass_permissions](./prompts/controls/built-in_controls.md#control-premodebypass_permissions)

- 🔗 [plan](./prompts/controls/built-in_controls.md#control-premodeplan)

#### `pre/model`

- 🔗 [model_fast](./prompts/controls/built-in_controls.md#control-premodelmodel_fast)

- 🔗 [model_selection_active](./prompts/controls/built-in_controls.md#control-premodelmodel_selection_active)

- 🔗 [model_selection_anthropic_claude_sonnet_4.6](./prompts/controls/built-in_controls.md#control-premodelmodel_selection_anthropic_claude_sonnet_46)

- 🔗 [model_selection_openai_gpt_5.4_pro](./prompts/controls/built-in_controls.md#control-premodelmodel_selection_openai_gpt_54_pro)

- 🔗 [model_temperature](./prompts/controls/built-in_controls.md#control-premodelmodel_temperature)

- 🔗 [model_thinking](./prompts/controls/built-in_controls.md#control-premodelmodel_thinking)

#### `pre/security`

- 🔗 [no_env_access](./prompts/controls/built-in_controls.md#control-presecurityno_env_access)

#### `pre/system`

- 🔗 [system_prompt](./prompts/controls/built-in_controls.md#control-presystemsystem_prompt)

#### `pre/tools`

- 🔗 [tools_call](./prompts/controls/built-in_controls.md#control-pretoolstools_call)

- 🔗 [tools_define](./prompts/controls/built-in_controls.md#control-pretoolstools_define)

- 🔗 [tools_off](./prompts/controls/built-in_controls.md#control-pretoolstools_off)

- 🔗 [tools_on](./prompts/controls/built-in_controls.md#control-pretoolstools_on)

#### `post/limits`

- 🔗 [explain_like_12](./prompts/controls/built-in_controls.md#control-postlimitsexplain_like_12)

- 🔗 [for_beginners](./prompts/controls/built-in_controls.md#control-postlimitsfor_beginners)

#### `post/tone`

- 🔗 [tone_style](./prompts/controls/built-in_controls.md#control-posttonetone_style)

#### `post/translation`

- 🔗 [translate_en](./prompts/controls/built-in_controls.md#control-posttranslationtranslate_en)

- 🔗 [translate_output](./prompts/controls/built-in_controls.md#control-posttranslationtranslate_output)

- 🔗 [translate_sp](./prompts/controls/built-in_controls.md#control-posttranslationtranslate_sp)

#### `post/truth`

- 🔗 [say_dont_know](./prompts/controls/built-in_controls.md#control-posttruthsay_dont_know)

---

### 🔗 [Built-in Content](./prompts/content/built-in_content.md)

Built-in content defines structured inputs that can be used when building or composing prompts, providing reusable data that can be composed independently of behavior and applied across agents, roles, tasks, and other configurations.

#### `/dev/testing`

- 🔗 [boundary_edge_cases](./prompts/content/built-in_content.md#content-boundary_edge_cases)

- 🔗 [boundary_edge_cases_function](./prompts/content/built-in_content.md#content-boundary_edge_cases_function)

#### `/`

- 🔗 [puzzle](./prompts/content/built-in_content.md#content-puzzle)
