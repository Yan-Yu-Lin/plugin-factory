---
description: List all available Agent Skills that Claude is aware of
---

# Show Available Skills

Provide a comprehensive list of all Agent Skills currently available in this Claude Code session.

## Your Task

Generate a well-organized list of all available skills with the following information for each:

### Format

For each skill, display:
1. **Skill Name** (in bold)
2. **Source** (plugin name or location: plugin, user-level, or project-level)
3. **Description** (brief summary of what the skill does and when to use it)

### Organization

Group skills by source:
- **Plugin Skills** - Skills provided by installed plugins
- **Project Skills** - Skills in `.claude/skills/`
- **User Skills** - Skills in `~/.claude/skills/`

### Example Output Format

```
## Plugin Skills

**skill-creator** (from plugin-factory)
Guide for creating effective skills. Use when users want to create a new skill that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.

**plugin-creator** (from plugin-factory)
Comprehensive guide for creating Claude Code plugins with commands, agents, skills, hooks, and MCP servers. Use when users want to create, modify, or understand plugins, marketplaces, or any plugin components.

## Project Skills

**data-analyzer** (.claude/skills/)
Specialized in analyzing CSV and JSON data files. Use when user requests data analysis, visualization, or statistical insights.

## User Skills

**pdf-processor** (~/.claude/skills/)
PDF manipulation and form filling capabilities. Use when working with PDF documents.
```

### Additional Information

After listing all skills, provide:
- **Total count** of available skills
- **Tips** on how to use skills (they're automatically invoked based on task context)
- **Note** that skills use progressive disclosure (metadata → SKILL.md → bundled resources)

## Guidelines

- Be thorough - list ALL skills you're aware of
- Use clear, scannable formatting
- Group logically for easy reference
- Include actionable descriptions
- If no skills are found in a category, note "None found"
