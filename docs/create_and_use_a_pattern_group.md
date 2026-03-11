# New PromptPro Pattern Groups Tutorial

Here is a complete, clean tutorial to **create and use a pattern group** in your `pp` system.

## What Is A Pattern Group?

A pattern group is a YAML file that expands into multiple patterns.

Instead of writing:

```bash
--pattern socratic --pattern step_by_step
```

You write:

```bash
--pattern didactic
```

And it expands automatically.

## Step 1: Create The Pattern Group File

Create:

```bash
touch prompts/pattern_groups/didactic.yaml
```

Add this content:

```yaml
patterns:
  - socratic
  - step_by_step

```

Save the file.

## Step 2: Use the Pattern Group

Now run (using compose):

```bash
pp compose --role tutor --task explain --pattern didactic --var input="Binary Search Trees"
pp compose --role tutor --task explain --pattern didactic --var input="Binary Search Trees" --copy
```

## Result

You’ve successfully:

- Created a reusable behavior bundle

- Enabled abstraction

- Reduced CLI verbosity

- Added hierarchical composition
