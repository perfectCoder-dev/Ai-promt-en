# Using Bash Variables With PromptPro

PromptPro integrates naturally with shell scripting.  

You can combine **literal values** and **Bash variables** when passing values to the `--var` option.

Because Bash expands variables **before executing a command**, the final value is constructed by the shell and then passed to PromptPro.

## Basic Example

You can append a Bash variable to a prompt value.

```bash
lang="in Python"

pp build math_tutor --var input="Explain recursion ${lang}"
```

Resulting value passed to PromptPro:

```text
Explain recursion in Python
```

## Using Parentheses With A Variable

You can embed a variable inside parentheses or any other text.

```bash
spec="with an example"

pp build math_tutor --var input="Explain recursion ($spec)"
```

Result:

```text
Explain recursion (with an example)
```

## Using Command Substitution

You can also insert the output of another command.

```bash
spec=$(date)

pp build math_tutor --var input="Explain recursion ($spec)"
```

Or directly:

```bash
pp build math_tutor --var input="Explain recursion ($(date))"
```

## Building The Variable First (Recommended For Scripts)

For complex scripts, it is often cleaner to build the variable first.

```bash
topic="Explain recursion"
input="${topic} with a Python example"

pp build math_tutor --var input="$input"
```

This approach improves readability and reduces quoting issues.

## Dynamic Prompt Construction

You can construct prompts dynamically using multiple variables.

```bash
topic="recursion"
language="Python"

pp build math_tutor --var input="Explain ${topic} in ${language}"
```

Result:

```text
Explain recursion in Python
```

## Important Notes

* Bash variables are expanded **before** PromptPro receives the argument.

* Always quote variables to avoid issues with spaces.

Example:

```bash
pp build math_tutor --var input="$input"
```

Unquoted variables may break arguments if they contain spaces or special characters.

## Summary

PromptPro works seamlessly with Bash variables, allowing you to:

* Combine static text with dynamic values

* Inject data from scripts

* Insert outputs from other commands

* Build flexible automation pipelines

This makes PromptPro easy to integrate into **shell scripts, CI pipelines, and CLI automation workflows**.
