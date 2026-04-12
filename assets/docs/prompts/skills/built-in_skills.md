# Built-in Skills

> [!NOTE]
> Throughout this document, selected **skill** are mapped to concepts and sublevels defined in 🔗 [The Iceberg Of Prompting](../../the_iceberg_of_prompting.md) framework.

## Skill: `web-research`

### Description

The web-research skill enables structured retrieval of up-to-date, reliable information from external sources by combining search, cross-checking, and concise synthesis into a single workflow. It is used when current or externally verified knowledge is required, especially in cases of uncertainty or incomplete internal data. The skill prioritizes recent, trustworthy sources and produces clear, compact summaries with key facts and supporting references when available, ensuring accurate and efficient information delivery within an agentic system.

|Sublevels|
|---------|
|8|

### List And Show

```bash
pp list skills/web-research/
pp show skills/web-research/SKILL
```

### Usage

This skill is not invoked directly by the user, but is instead triggered by the agentic system as part of its orchestration logic. Agents decide when to use it based on context.
