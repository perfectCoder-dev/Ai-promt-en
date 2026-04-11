# AI Systems Integration

PromptNG includes built-in support for integrating with external AI systems and codebases, allowing you to centralize agents, skills, commands, and other interaction logic within a shared prompts/ directory.

With this feature, you can organize both global and project-specific AI components, eliminate duplication across repositories, and seamlessly connect external projects using symbolic links—making it easier to maintain a clean, modular, and scalable architecture.

## 🎯 Purpose

This approach is designed to:

- Centralize all AI prompt logic in a single directory (`prompts/`)

- Avoid scattering `agents.md` and `SKILL.md` files across multiple codebases

- Enable reuse of standardized AI capabilities (skills)

- Support scalable, maintainable agentic systems

- Treat prompts as shared infrastructure instead of local assets

## 🧱 Recommended Structure

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