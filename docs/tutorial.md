# New promptctl Prompt Tutorial

Here’s a practical, hands-on tutorial to create a new prompt example using your current structure — both by reusing existing .md files and by adding new ones.

We’ll assume your project prompts directory looks like this:

```bash
└── prompts
    ├── agents
    │   └── math_tutor.yaml
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
```

You should see:

```output
tutor
explain
socratic
step_by_step
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

### Step 5.1: Create And Build Your Agent With `build`

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

### Step 5.2: Compose Your Prompt With `compose`

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
