# Built-in Controls

> [!NOTE]
> Throughout this document, selected **controls** are mapped to concepts and sublevels defined in [The Iceberg Of Prompting](../../the_iceberg_of_prompting.md) framework.

## Pre Controls

### Control: `config`/`configurations`

#### Description

Ensures that all defined configurations, parameters, and constraints are strictly respected throughout the execution of the prompt. This control enforces consistency and prevents unintended overrides or deviations from the established setup.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|5|
|6|
|7|
|8|
|9|
|10|
|11|
|12|

#### List And Show

```bash
pp list controls/pre/config
pp show controls/pre/config/configurations
```

---

### Control: `language`/`input_default`

#### Description

Sets the user’s input language as the default working language for the interaction, ensuring consistent communication throughout.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|7|

#### List And Show

```bash
pp list controls/pre/language
pp show controls/pre/language/input_default
```

---

### Control: `mcp`/`mcp_local`

#### Description

Prioritizes the use of local MCP (Model Context Protocol) servers and resources over external services. This control guides the system to favor locally available capabilities to improve performance and maintain data privacy.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|8|
|9|

#### List And Show

```bash
pp list controls/pre/mcp
pp show controls/pre/mcp/mcp_local
```

---

### Control: `mcp`/`mcp_remote`

#### Description

Allows the system to use remote MCP (Model Context Protocol) servers when necessary. This control enables access to external capabilities while maintaining a balance between performance, availability, and result quality.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|8|
|9|

#### List And Show

```bash
pp list controls/pre/mcp
pp show controls/pre/mcp/mcp_remote
```

---

### Control: `memory`/`forget`

#### Description

Forces the system to operate without relying on prior conversations or previously stored context. Each interaction is treated as fully independent, ensuring that only the current input defines behavior.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|1|
|2|
|7|
|8|
|9|

#### List And Show

```bash
pp list controls/pre/memory
pp show controls/pre/memory/forget
```

---

### Control: `mode`/`agent`

#### Description

Configures the system to operate in Agent mode, enabling proactive behavior, autonomous decision-making, and effective use of available resources to accomplish tasks.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|5|
|6|
|7|
|8|
|9|
|12|
|13|

#### List And Show

```bash
pp list controls/pre/mode
pp show controls/pre/mode/agent
```

---

### Control: `mode`/`ask`

#### Description

Configures the system to operate in Ask mode, focusing strictly on responding to the user’s request without taking additional initiative or performing unsolicited actions.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|6|
|7|
|8|
|9|
|13|

#### List And Show

```bash
pp list controls/pre/mode
pp show controls/pre/mode/ask
```

---

### Control: `mode`/`bypass_permissions`

#### Description

Configures the system to operate with relaxed permission handling, allowing it to proceed with execution without being blocked by non-critical permission constraints. This control prioritizes task completion while maintaining awareness of critical boundaries.

In an operating system like Microsoft Windows, macOS, or Linux, **“non-critical permissions”** generally refers to restrictions that do **not affect system integrity, security boundaries, or core functionality**, and can be safely relaxed in controlled contexts.

Here are common examples (that can be used to define more granular permission controls):

🟢 Examples of Non-Critical Permissions

1. File Read/Write in User Space

* Accessing or modifying files in user-owned directories (e.g., Documents, Downloads)

* Not touching system directories like `/etc`, `/System`, or `C:\Windows`

2. Temporary File Creation

* Writing to temp directories (`/tmp`, `%TEMP%`)

* Creating logs or cache files

3. Non-Privileged Network Access

* Making outbound HTTP requests (no firewall or privileged port changes)

* Accessing public APIs

4. UI / Accessibility Prompts (Low-Risk Cases)

* Minor UI automation permissions (depending on OS policies)

* Clipboard access (context-dependent, still sensitive in some cases)

5. Executing Non-Privileged Processes

* Running scripts or binaries that don’t require admin/root

* No elevation (`sudo`, admin rights) involved

6. Environment-Level Configurations

* Modifying environment variables in a local session

* User-level config files (e.g., `.bashrc`, `.zshrc`, app configs)

🔴 What Is NOT Non-Critical (i.e., Critical Permissions)

To clarify the boundary, these are **critical** and should never be bypassed:

* Root/admin privileges (`sudo`, UAC elevation)

* System file modifications (e.g., `/bin`, `/usr`, `C:\Windows\System32`)

* Kernel/module access or driver installation

* Security controls (firewall rules, SELinux, Gatekeeper, antivirus)

* Access to other users’ data

* Credential stores, keychains, or authentication tokens

⚠️ Important Note

Even “non-critical” permissions can become risky depending on context (e.g., scripts modifying many user files). So in practice, this concept should be applied with **clear boundaries and safeguards**, not as a blanket bypass.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|5|
|6|
|7|
|8|
|9|
|13|

#### List And Show

```bash
pp list controls/pre/mode
pp show controls/pre/mode/bypass_permissions
```

---

### Control: `mode`/`plan`

#### Description

Configures the system to operate in Plan mode, focusing exclusively on designing a clear and structured approach to a task without executing it.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|6|
|7|
|8|
|9|
|11|
|13|

#### List And Show

```bash
pp list controls/pre/mode
pp show controls/pre/mode/plan
```

---

### Control: `model`/`model_fast`

#### Description

Configures the system to prioritize speed and responsiveness during execution. This control emphasizes fast completion by reducing verbosity and focusing on direct, efficient responses.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|8|
|9|
|10|
|11|

#### List And Show

```bash
pp list controls/pre/model
pp show controls/pre/model/model_fast
```

---

### Control: `model`/`model_selection_active`

#### Description

Defines the active model used for response generation. This control selects one model configuration and ensures it is applied exclusively, preventing conflicts between multiple model selections.

Different models offer varying levels of capability, speed, cost, and reasoning depth, allowing the system to be tailored for tasks ranging from lightweight interactions to complex analysis.

---

### Control: `model`/`model_selection_anthropic_claude_sonnet_4.6`

#### Description

Select the Claude Sonnet 4.6 model for response generation. Optimized for balanced performance, it delivers strong reasoning, high-quality writing, and efficient execution across general-purpose tasks.

---

### Control: `model`/`model_selection_openai_gpt_5.4`

#### Description

Select the GPT-5.4 model for response generation. Designed for high performance, it provides advanced reasoning, coding capability, and reliable results across a wide range of complex tasks.

---

### Control: `model`/`model_temperature`

#### Description

Adjusts the level of randomness and entropy in responses. Lower values produce consistent and predictable outputs, while higher values increase variation, creativity, and exploratory behavior.

---

### Control: `model`/`model_thinking`

#### Description

Configures the system to prioritize deep reasoning and accuracy over speed. This control encourages careful analysis, structured thinking, and well-supported conclusions.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|8|
|9|
|10|
|11|

#### List And Show

```bash
pp list controls/pre/model
pp show controls/pre/model/model_thinking
```

---

### Control: `security`/`no_env_access`

#### Description

Enforces strict restrictions on accessing, handling, or exposing sensitive data and protected systems. This control ensures that all interactions remain within safe and authorized boundaries.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|6|
|7|
|8|
|9|

#### List And Show

```bash
pp list controls/pre/security
pp show controls/pre/security/no_env_access
```

---

### Control: `system`/`system_prompt`

#### Description

Establishes a strict hierarchy for how instructions are interpreted and applied. This control ensures that higher-priority directives always take precedence, enabling predictable and conflict-free behavior within structured prompt systems.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|5|
|6|
|7|

#### List And Show

```bash
pp list controls/pre/system
pp show controls/pre/system/system_prompt
```

---

### Control: `tools`/`tools_call`

#### Description

Guides the system to use tools, APIs, or scripts when they provide clear value in improving accuracy or completing a task. This control promotes informed decision-making between internal reasoning and external execution.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|6|
|7|
|8|
|9|

#### List And Show

```bash
pp list controls/pre/tools
pp show controls/pre/tools/tools_call
```

---

### Control: `tools`/`tools_define`

#### Description

Encourages the use of available tools when they meaningfully improve the quality, accuracy, or completeness of a response. This control promotes smart tool selection, especially for dynamic or externally sourced information.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|6|
|7|
|8|
|9|

#### List And Show

```bash
pp list controls/pre/tools
pp show controls/pre/tools/tools_define
```

---

### Control: `tools`/`tools_off`

#### Description

Disables all tool usage, forcing the system to rely entirely on internal knowledge and reasoning. This control ensures that no external calls are made during execution.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|8|

#### List And Show

```bash
pp list controls/pre/tools
pp show controls/pre/tools/tools_off
```

---

### Control: `tools`/`tools_on`

#### Description

Enables full access to available tools, APIs, and external systems, allowing the system to leverage them when beneficial for accuracy, completeness, or capability.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|8|

#### List And Show

```bash
pp list controls/pre/tools
pp show controls/pre/tools/tools_on
```

## Post Controls

### Control: `limits`/`explain_like_12`

#### Description

Adjusts the response to be easily understood by a 12-year-old reader. This control simplifies language, structure, and concepts to make explanations clear and accessible.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|3|
|6|
|7|

#### List And Show

```bash
pp list controls/post/limits
pp show controls/post/limits/explain_like_12
```

---

### Control: `limits`/`for_beginners`

#### Description

Adapts the response to suit beginners by simplifying language and focusing on intuitive understanding. This control reduces complexity while still conveying the essential concepts clearly.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|3|
|6|
|7|

#### List And Show

```bash
pp list controls/post/limits
pp show controls/post/limits/for_beginners
```

---

### Control: `tone`/`tone_style`

#### Description

Shapes the response to be clear, professional, and friendly. This control ensures communication is approachable while maintaining a high standard of clarity and respect.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|5|

#### List And Show

```bash
pp list controls/post/tone
pp show controls/post/tone/tone_style
```

---

### Control: `translation`/`translate_en`

#### Description

Transforms the final response into English, regardless of the original input or intermediate working language.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|7|

#### List And Show

```bash
pp list controls/post/translation
pp show controls/post/translation/translate_en
```

---

### Control: `translation`/`translate_output`

#### Description

Translates the final response into the language requested by the user. This control ensures that output is delivered in the desired language while preserving meaning and clarity.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|6|
|7|

#### List And Show

```bash
pp list controls/post/translation
pp show controls/post/translation/translate_output
```

---

### Control: `translation`/`translate_sp`

#### Description

Transforms the final response into Spanish, regardless of the original input or intermediate working language.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|7|

#### List And Show

```bash
pp list controls/post/translation
pp show controls/post/translation/translate_sp
```

---

### Control: `truth`/`say_dont_know`

#### Description

Enforces honest responses by requiring the system to explicitly acknowledge uncertainty instead of guessing or fabricating information.

#### Sublevel In The Iceberg of Prompting Framework

|Sublevels|
|---------|
|10|

#### List And Show

```bash
pp list controls/post/truth
pp show controls/post/truth/say_dont_know
```
