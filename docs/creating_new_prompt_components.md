# Creating And Using New Prompt Components

Here’s a practical, hands-on tutorial to create a new prompt — both by reusing existing .md files and by adding new ones.

## Example

### Prerequisite

You need to know the meaning of **"switch"** (in computer networks).

### Typical Workflow

- You type a low-quality prompt:

  > What is a switch?

- The result is **insufficient** or ambiguous.

- You remain in the prompting loop, asking follow-up questions until you eventually get a convincing answer.

- At this point, you realize that your prompt **lacked context and structure**, so the AI had too much freedom in how to answer.

- You improve the prompt by specifying the **role**, **scope**, and **structure** of the explanation:

  > Act as a computer networking engineer and instructor. If you are uncertain about any part of the concept, state that clearly and focus on explaining only well-established fundamentals. Your task is to explain the concept of a network switch in a clear and structured way suitable for beginners: begin with a brief definition, then describe in simple terms how a switch works in a network, outline its main components, summarize its typical operations and functions, and discuss its advantages and limitations. Conclude with a few simple real-world examples of how switches are used in computer networks, using clear language and avoiding unnecessary jargon.

- You submit the improved prompt.

- The response becomes **clearer, more structured, and closer to your expectations**.

- You reduce the number of iterations in the prompting loop and reach a useful answer **faster**.

### What Fixes The Error

The issue is resolved by **adding specificity and structure to the prompt**. Instead of asking a vague question, the user provides enough information to guide the AI toward the intended explanation.

The improved prompt introduces several key elements:

- **Role** — “computer networking engineer and instructor”
- **Domain** — “network switch” in computer networking
- **Structure** — definition, operation, components, advantages, limitations, and examples
- **Audience** — beginners

These additions reduce ambiguity and guide the AI toward producing a **focused, structured, and relevant response**.

The original AI user error was the **initial vague prompt** (“What is a switch?”), which lacked context and allowed multiple interpretations.

This type of error can be prevented from the start by using tools or workflows that help users **formulate clearer and more structured prompts**.

### Key Takeaway

This example illustrates a common issue in AI interactions: **vague prompts lead to vague answers**. When a prompt lacks context, scope, or structure, the AI must guess the user’s intent, which often results in ambiguous or insufficient responses.

PromptPro helps prevent this problem **from the very beginning**. Instead of forcing users into a trial-and-error prompting loop, it guides them in **constructing clear, structured prompts** by defining the role, domain, audience, expected output format, etc. This approach reduces ambiguity, shortens the iteration cycle, and helps users obtain **useful, well-structured answers faster**.

In the next section, you will see how **PromptPro** helps transform a vague prompt into a clear and structured one. The following steps demonstrate a simple workflow for defining the role, domain, audience, and output structure so the AI can produce more accurate and useful responses from the start.

### Step 1: Define A Custom Prompt To Build

Let’s say we want:

- Role: Technical instructor
- Task: Explaining
- Patterns: Step by step, structured output
- Topic: "Switch"
- Audience: beginners

### Step 2: Inspect Existing Prompt Components

> [!NOTE]
> At this stage, you will identify which patterns you:
> - Need
> - Can modify
> - Can reuse

List the available components:

```bash
pp list <agents|pattern_groups|patterns|roles|tasks>
```

You should see:

```output
tutor
explain
socratic
step_by_step
didactic_structured
didactic
...
```

You determine that you need a new `pattern` and a new `role`, and that you should reuse an existent `role`, and `task`.

> [!TIP]
> Make a table to help you define the required components.
> |Agent         |Role                 |Task + Audience         | Patterns                       |
> |--------------|---------------------|------------------------|--------------------------------|
> |cs_instructor |technical_instructor |explain + for beginners |step_by_step, structured_output |

### Step 3: Create A New Pattern

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

Verify that the pattern has been created:

```bash
pp list patterns
pp list patterns | grep structure
```

You should now see:

```output
structured_output
```

### Step 4: Create A New Role

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
pp build cs_instructor --var input="Hash Tables"
```

That’s your reusable agent configuration.

### Step 5.2: Compose Your Prompt With `compose`

```bash
pp compose \
  --role technical_instructor \
  --task explain \
  --pattern step_by_step \
  --pattern structured_output \
  --var input="Hash Tables" \
  --copy
```

Now it's copied to your clipboard.

## Tips For PromptPro Prompt Creators

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

* [Prompt Components Reference](../docs/prompt_components_reference.md)

* [Creating And Using Pattern Groups](../docs/create_and_use_a_pattern_group.md)
