# New promptctl Prompt Tutorial

Here’s a practical, hands-on tutorial to create a new prompt example — both by reusing existing .md files and by adding new ones.

We’ll assume your project prompts directory looks like this:

```bash
prompts
├── agents
│   └── math_tutor.yaml
├── pattern_groups
│   ├── didactic_structured.yaml
│   └── didactic.yaml
├── patterns
│   ├── socratic.md
│   └── step_by_step.md
├── roles
│   └── tutor.md
└── tasks
    └── explain.md

```

## Full Custom Prompt Build

Let’s say we want:

- Technical instructor

- Explaining

- Step by step

- Structured output

- Topic = "Hash Tables"

### Step 1: Inspect Existing Files

You can list available items:

```bash
promptctl list roles
promptctl list tasks
promptctl list patterns
promptctl list pattern_groups
```

You should see:

```output
tutor
explain
socratic
step_by_step
didactic_structured
didactic
```

### Step 2: Creating A New Pattern

```bash
touch prompts/patterns/structured_output.md
```

Example content:

```markdown
- Use clear section headers
- Use bullet points when possible
- End with a short summary
- Avoid unnecessary verbosity

```

Verify it exists:

```bash
promptctl list patterns
```

You should now see:

```output
socratic
step_by_step
structured_output
```

### Step 3: Create New Role File

```bash
touch prompts/roles/technical_instructor.md
```

Example content:

```markdown
You are a precise and analytical technical instructor.

- Focus on correctness
- Use formal terminology
- Avoid metaphors
- Provide definitions before explanations

```

### Step 4.1: Create And Build Your Agent With `build`

```bash
touch prompts/agents/cs_instructor.yaml
```

Example:

```yml
role: technical_instructor
task: explain
patterns:
  - step_by_step
  - structured_output

```

Now you can use:

```bash
promptctl build cs_instructor --var input="Hash Tables"
```

That’s your reusable agent configuration.

### Step 4.2: Compose Your Prompt With `compose`

```bash
promptctl compose \
  --role technical_instructor \
  --task explain \
  --pattern step_by_step \
  --pattern structured_output \
  --var input="Hash Tables" \
  --copy
```

Now it's copied to your clipboard.

## Tips For Promptctl creators

### 💡 Separate The Three Layers Clearly

Use different **naming styles** for each layer.

Try to keep:

|Layer |Naming Style        |Example     |
|------|--------------------|------------|
|agent |concrete capability	|action_agent|
|role	 |behavioral identity	|executor    |
|task	 |verb                |action      |

### 💡 Default Architectural Design

The definition of **default agents** has evolved into `3` agent families:

|# |Family              |Role                 |Task    |
|--|--------------------|---------------------|--------|
|1 |Teaching	          |tutor	              |explain |
|2 |Technical teaching	|technical_instructor	|explain |
|3 |Operations	        |executor	            |action  |

This separation is very clean and scalable.

### 💡 Editing Existing Elements 

Alternatively, instead of creating new agents, roles, tasks, and/or patterns, you can open the corresponding **element file** to review or edit its contents. 🚨 However, **any changes to existing elements will affect all elements associated with the modified one**. To avoid unintentionally impacting other agents and related elements, the recommended approach is to **clone an existing agent and rename it as your new preset**, then modify the cloned version instead of the original.

### 💡 Understand How To Proceed Clearly

Read the related documentation:

* [Composable Elements Reference](docs/prompt_composable_elements_reference.md)

* [Pattern Groups](docs/create_and_use_a_pattern_group.md)
