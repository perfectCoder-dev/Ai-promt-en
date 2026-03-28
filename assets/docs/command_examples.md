# PromptPro Command Examples

## Change Themes

| Command                                                             |
|---------------------------------------------------------------------|
| pp --theme monokai show tasks/explain                               |
| pp --theme friendly show content/dev/testing/boundary_edge_cases |
| pp --theme dracula build math_tutor --var input="Explain recursion" |
| pp --theme default compose --role tutor --task explain --pattern step_by_step --var input="Boolean algebra simplification" |

## Listing Prompt Components

| Command                             |
|-------------------------------------|
| pp list roles                       |
| pp list agents                      |
| pp list pattern_groups              |
| pp list patterns                    |
| pp list tasks                       |
| pp list roles \| grep -E 'te\|utor' |
| pp list controls/pre/mode           |
| pp list controls/post/translation   |
| pp list controls/post/limits        |

## Showing Prompt Components

| Command                                            |
|----------------------------------------------------|
| pp show agents/cs_instructor                       |
| pp show patterns/step_by_step                      |
| pp show patterns/plan_execute                      |
| pp show tasks/compose_action                       |
| pp show content/dev/testing/boundary_edge_cases |
| pp show controls/pre/mode/agent                    |
| pp show controls/pre/language/input_default        |
| pp show controls/post/truth/say_dont_know          |
| pp show controls/post/limits/for_beginners         |
| pp show controls/post/limits/explain_like_12       |

## Generating Prompts With `build`

| Command                                                    |
|------------------------------------------------------------|
| pp build math_tutor --var input="Explain recursion"        |
| pp build math_tutor --var input="Explain recursion" --copy |
| pp build action_agent --var action="Make a shopping list"  |
| pp build math_tutor --pre model/model_fast --pre memory/forget --post translation/translate_sp --post truth/say_dont_know --var input="Linear Algebra" |
| pp build action_agent_controlled --post truth/say_dont_know --var action="Make a list of the core skills everyone should have." |
| pp build dev/software_testing_agent --var-file action=content/dev/testing/boundary_edge_cases |

## Generating Prompts With `compose`

| Command                                                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------|
| pp compose --role tutor --task explain --pattern step_by_step --var input="Boolean algebra simplification"                              |
| pp compose --role tutor --task explain --pattern socratic --pattern step_by_step --var input="Gravity" --var theorist="Albert Einstein" |
| pp compose --role tutor --task explain --pattern socratic --pattern step_by_step --var input="Gravity, by Isaac Newton" --copy          |
| pp compose --role tutor --task explain --pattern socratic --var input="Random text"                                                     |
| pp compose --role tutor --task explain --pattern didactic --var input="Random text" --var-file input2=./content/puzzle.txt --var-dir input3=./content --copy |
| pp compose --role executor --task compose_action --pattern verify_before_execute --pattern plan_execute --pattern structured_output --var action="Make a shopping list" --var context="I am at the computer store" --var examples="|Item |Brand |Price | |Mouse |Genius |$45.75 |" |
| pp compose --pre model/model_fast --pre memory/forget --role technical_instructor --task explain --pattern step_by_step --post limits/for_beginners --var input="Switch" |
| pp compose --role dev/software_tester --task action --pattern testing_strict --var-file action=content/dev/testing/boundary_edge_cases |

## Saving / Redirecting Output

| Command                                                             |
|---------------------------------------------------------------------|
| pp build math_tutor --var input="Explain recursion" > my_prompt.txt |

## Pipelines

| Command                                                                               |
|---------------------------------------------------------------------------------------|
| pp build math_tutor --var input="Explain recursion" \| ollama run llama3 \| espeak-ng |

## Bash Scripting

| Command                                                           |
|-------------------------------------------------------------------|
| pp build math_tutor --var input="Explain ${topic} in ${language}" |
