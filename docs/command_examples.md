# PromptPro Command Examples

## Listing Prompt Components

| Command |
|--------|
| pp list roles |
| pp list agents |
| pp list pattern_groups |
| pp list patterns |
| pp list tasks |
| pp list roles \| grep -E 'te\|utor' |

## Generating Prompts (build)

| Command |
|--------|
| pp build math_tutor --var input="Explain recursion" |
| pp build math_tutor --var input="Explain recursion" --copy |
| pp build action_agent --var action="Make a shopping list" |

## Generating Prompts (compose)

| Command |
|--------|
| pp compose --role tutor --task explain --pattern step_by_step --var input="Boolean algebra simplification" |
| pp compose --role tutor --task explain --pattern socratic --pattern step_by_step --var input="Gravity" --var theorist="Albert Einstein" |
| pp compose --role tutor --task explain --pattern socratic --pattern step_by_step --var input="Gravity, by Isaac Newton" --copy |
| pp compose --role tutor --task explain --pattern socratic --var input="Random text" |
| pp compose --role tutor --task explain --pattern didactic --var input="Random text" --var-file input2=./texts/puzzle.txt --var-dir input3=./texts --copy |
| pp compose --role executor --task compose_action --pattern verify_before_execute --pattern plan_execute --pattern structured_output --var action="Make a shopping list" --var context="I am at the computer store" --var examples="|Item |Brand |Price | |Mouse |Genius |$45.75 |" |

## Saving / Redirecting Output

| Command |
|--------|
| pp build math_tutor --var input="Explain recursion" > my_prompt.txt |

## Pipelines

| Command |
|--------|
| pp build math_tutor --var input="Explain recursion" \| ollama run llama3 \| espeak-ng |

## Bash Scripting

| Command |
|--------|
| pp build math_tutor --var input="Explain ${topic} in ${language}" |
