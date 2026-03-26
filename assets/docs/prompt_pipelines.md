# Prompt Pipelines

Because PromptPro outputs plain text, it integrates naturally with the **Unix philosophy**: small tools connected through pipes.

This allows generated prompts to flow directly into other programs and services.

Below are several examples of tools that can receive PromptPro output.

## 🔊 1. Text → Voice

Make the AI **speak the response**.

Supported tools:

* espeak-ng
* festival
* RHVoice

Example:

```bash
pp build math_tutor --var input="Explain recursion" | espeak-ng
```

## 🧠 2. Send To An LLM

Chain prompts into another AI model.

Supported tools:

* Ollama
* Open Interpreter

Example:

```bash
pp build math_tutor --var input="Explain recursion" | ollama run llama3
```

## 🖥️ 3. Show A Graphical Popup

Turn your pipeline into a **desktop assistant**.

Supported tools:

* zenity
* yad

Example:

```bash
pp build math_tutor --var input="Explain recursion" | zenity --text-info
```

## 🔔 4. Send A Desktop Notification

Trigger a notification when your AI response is ready.

Tool:

* notify-send

Example:

```bash
notify-send "AI Response" "$(pp build math_tutor --var input='Explain recursion')"
```

## 📝 5. Convert To Documents

Turn AI responses into formatted documents.

Tool:

* Pandoc

Example:

```bash
pp build math_tutor --var input="Explain recursion" | pandoc -f markdown -t html
```

## 🌐 6. Send Over HTTP

Send the prompt or response to a web API.

Tool:

* curl

Example:

```bash
pp build math_tutor --var input="Explain recursion" \
| curl -X POST http://localhost:8000/api -d @-
```

`@-` tells `curl` to read the request body from **stdin**.

## 📡 7. Send To Another Machine

Stream prompts across the network.

Tool:

* netcat

Example:

```bash
pp build math_tutor --var input="Explain recursion" | nc 192.168.1.10 9000
```

## 📊 8. Log Or Analyze Output

Process responses using standard text tools.

Tools:

* jq
* grep
* awk

Example:

```bash
pp build math_tutor --var input="Explain recursion" | grep recursion
```

## 🎨 9. Terminal Art

Transform responses into visual terminal output.

Tools:

* figlet
* lolcat

Example:

```bash
pp build math_tutor --var input="Explain recursion" | figlet | lolcat
```

## 🤖 10. Terminal Chat Interfaces

Pipe responses into terminal UI tools.

Tool:

* gum

Example:

```bash
pp build math_tutor --var input="Explain recursion" | gum pager
```

## 🧩 11. Pipe Into A Script Engine

Use PromptPro output as input to scripts.

Example:

```bash
pp build math_tutor --var input="Explain recursion" | python3 myscript.py
```

Example script:

```python
import sys

prompt = sys.stdin.read()
print(prompt)
```

## ⚡ Example Super Pipeline

### Voice AI Tutor

Generate a prompt, send it to a local model, and read the response aloud.

```bash
pp build math_tutor --var input="Explain recursion" \
| ollama run llama3 \
| espeak-ng
```

Pipeline flow:

```
PromptPro → LLM → speech synthesis
```

### AI → Popup → Log

Send the response to a file and a graphical window.

```bash
pp build math_tutor --var input="Explain recursion" \
| tee response.txt \
| zenity --text-info
```

Pipeline flow:

```
PromptPro → log file → desktop popup
```

## 💡 PromptPro As A Prompt Bus

Because PromptPro prints prompts to **standard output**, it can act as a universal **prompt bus** that feeds multiple downstream systems.

```
pp → AI → voice
pp → AI → API
pp → AI → GUI
pp → AI → database
pp → AI → robot
```

This makes PromptPro useful not only for prompt generation, but also as a **control layer for AI-driven pipelines**.

By combining PromptPro with existing CLI tools, you can build powerful automation workflows without modifying your prompt components.
