# AI Systems Integration

PromptNG includes built-in support for integrating with external AI systems and codebases, allowing you to centralize `agents`, `skills`, `commands`, and other interaction logic within a shared `prompts/` directory.

With this feature, you can organize both **global** and **project-specific** AI components, eliminate duplication across repositories, and seamlessly connect external projects using symbolic links—making it easier to maintain a clean, modular, and scalable architecture.

## Purpose

This approach is designed to:

- Centralize all AI prompt logic in a single directory (`prompts/`)

- Avoid scattering `agents.md` and `SKILL.md` files across multiple codebases

- Enable reuse of standardized AI capabilities (skills)

- Support scalable, maintainable **agentic systems**

- Treat prompts as **shared infrastructure** instead of **local assets**

## Recommended Structure

```bash
prompts/
├── skills/                  # Global reusable skills
│   ├── web_research/
│   │   └── SKILL.md
│   └── reasoning/
│       └── SKILL.md
│
└── projects/
    ├── project_a/
    │   ├── agents.md
    │   └── skills/          # Optional overrides / custom skills
    │       └── custom_skill/
    │           └── SKILL.md
    │
    ├── project_b/
    │   ├── agents.md
    │   └── skills/
    │
    ├── openclaw/
    │   └── clawd_mds/

```

### Conceptual Model

| Layer         | Purpose                                                  |
| ------------- | -------------------------------------------------------- |
| `skills/`     | Global reusable AI capabilities (shared across projects) |
| `projects/*/` | Project-specific agent definitions and overrides         |
| `agents.md`   | Agent orchestration and composition                      |
| `SKILL.md`    | Encapsulated AI capability (behavior + instructions)     |

## External Definitions (Agentic Systems)

The following definitions reflect common usage across modern agent-based AI systems and orchestration frameworks.

### agents.md

In agentic AI systems, an `agents.md` (or equivalent agent configuration file) is typically a declarative specification that defines autonomous or semi-autonomous agents, including their roles, responsibilities, constraints, and interaction patterns.

Agents are commonly used to:

- Represent distinct roles within a system (e.g., planner, coder, researcher)

- Coordinate multi-step workflows

- Delegate tasks to tools or skills

- Maintain structured behavior across interactions

### Skills (SKILL.md / Skills)

In modern agent architectures, a "skill" refers to a reusable, modular capability that an agent can invoke to perform a specific function.

Skills are generally characterized by:

- Encapsulated behavior (single responsibility)

- Reusability across multiple agents or workflows

- Clear input/output expectations

- Independence from orchestration logic

Skills are often treated as composable building blocks within agent frameworks, enabling systems to scale through reuse rather than duplication.

## How It Works

### 1. Global Skills (Reusable)

Located in:

```bash
/path/to/promptng/prompts/skills/
```

These act as a **standard library** of AI capabilities.

**Examples**

* Web research

* Reasoning strategies

* Data extraction

* Code generation patterns

### 2. Project Skills (Overrides / Extensions)

Located in:

```bash
/path/to/promptng/prompts/projects/<project>/skills/
```

Used to:

* Override global behavior

* Add project-specific capabilities

* Customize execution logic

### 3. Agents Definition

Each project defines its agents in:

```bash
/path/to/promptng/prompts/projects/<project>/agents.md
```

Agents orchestrate:

* Roles

* Tasks

* Patterns

* Skills

## Skill Resolution Strategy

When resolving a skill:

1. Check project-level skill:

   ```
   prompts/projects/<project>/skills/
   ```

2. Fallback to global skill:

   ```
   prompts/skills/
   ```

This allows:

* Safe overrides

* Controlled customization

* Shared evolution of capabilities

> [!CAUTION]
> Skill resolution conflicts may occur between PromptNG-defined `controls` and agentic system behaviors.
When both define overlapping capabilities, one may override or bypass the other depending on resolution order and scope.
>
> This can lead to unexpected behavior if multiple layers define competing instructions for the same action (e.g., tool usage, retrieval, or execution logic).
>
> Always ensure that:
> - Skill boundaries are clearly defined
> - Overrides are intentional and documented
> - Global and project-level behaviors do not duplicate control logic
>
> In case of conflict, project-level definitions typically take precedence over global skills unless explicitly configured otherwise.
>
> **Example**  
> Control `controls/pre/tools/web/lookup` VS skill `skills/web_research/SKILL.md`.
>
> The `web_lookup` control and the `web-research` skill are not in conflict—they are complementary with some overlap. `web_lookup` is a simple, low-level tool that retrieves information based on a query, while `web-research` is a higher-level capability that builds on that idea by searching, cross-checking sources, and synthesizing a more reliable summary.
>
> In practice, `web_lookup` is best for quick facts or straightforward queries, whereas `web-research` is better for complex or uncertain topics that need validation and structured analysis. So, one acts as a basic building block, and the other as a more intelligent workflow that could even use the first internally.

> [!TIP]
Compare two or more prompt components using your preferred AI to determine whether they conflict, overlap, or complement each other. Validate how they behave together before relying on them in the same workflow.

> [!TIP]
Create a separate, focused prompt to test how components interact. This makes conflicts and overlaps easier to detect and reason about.

## Integrating With Codebases

Instead of duplicating prompt files inside each codebase, you can link them using **symbolic links (symlinks)**.

This keeps your codebases clean while still accessing centralized prompt logic.

### Example: Linking `agents.md`

**Linux / MacOS**

```bash
ln -s /path/to/promptng/prompts/projects/project_a/agents.md project/AGENTS.md
```

**Windows (PowerShell)**

```powershell
New-Item -ItemType SymbolicLink -Path "project\AGENTS.md" -Target "C:\path\to\promptng\prompts\projects\project_a\agents.md"
```

### Example: Linking Skills Directory

**Linux / MacOS**

```bash
ln -s /path/to/promptng/prompts/projects/project_a/skills project/skills
```

**Windows (PowerShell)**

```powershell
New-Item -ItemType SymbolicLink -Path "project\skills" -Target "C:\path\to\prompts\projects\project_a\skills"
```

### Benefits Of Symlinks

* Single source of truth

* No duplication

* Instant updates across projects

* Cleaner repositories

## Listing And Showing Skills

**Example skill**

```bash
/path/to/promptng/prompts/skills/web_research/SKILL.md
```

**PromptNG commands**

```bash
pp list skills/web-research/
pp show skills/web-research/SKILL
```

### Complete Skill documentation

- 🔗 [web-search](./prompts/skills/built-in_skills.md#skill-web-research)

## Why This Matters

This architecture allows PromptNG to function as a **true prompt control plane**:

* Prompts become **modular infrastructure**

* Skills become **reusable capabilities**

* Agents become **composable systems**

* Projects remain **clean and lightweight**

## Best Practice Summary

* Use `prompts/skills/` for shared capabilities

* Use `prompts/projects/*/skills/` for overrides

* Keep `agents.md` per project

* Link codebases via symlinks instead of copying files
