# Plugin Factory

> Comprehensive toolkit for creating Claude Code plugins and skills

## Overview

Plugin Factory provides everything you need to create, develop, and distribute Claude Code plugins. Whether you're building simple command plugins or complex systems with skills, agents, hooks, and MCP servers, this plugin guides you through the entire process.

## What's Included

This plugin contains **two complementary skills**:

### 1. plugin-creator

The main skill for creating and managing Claude Code plugins.

**Use this skill when you want to:**
- Create a new plugin from scratch
- Understand plugin structure and components
- Add commands, agents, hooks, or MCP servers to plugins
- Learn about plugin distribution and marketplaces
- Troubleshoot plugin issues

**Key features:**
- Complete plugin creation workflow
- Scaffolding script (`init_plugin.py`) to generate plugin structure
- Comprehensive reference documentation
- Testing and debugging guidance
- Distribution strategies

### 2. skill-creator

The specialized skill for creating Agent Skills (which can be standalone or part of plugins).

**Use this skill when you want to:**
- Create a new Agent Skill
- Add a skill to an existing plugin
- Understand skill structure and best practices
- Package and validate skills

**Key features:**
- Skill creation workflow from the original Anthropic skill-creator
- Scaffolding script (`init_skill.py`) to generate skill structure
- Validation and packaging tools
- Reference documentation on Agent Skills spec

## Installation

### From GitHub

```bash
# In Claude Code
/plugin marketplace add anthropics/skills
/plugin install plugin-factory@anthropic-agent-skills
```

### From Local Directory (Development)

```bash
# Clone this repository
git clone <repo-url>

# In Claude Code
/plugin marketplace add ./path/to/plugin-factory
/plugin install plugin-factory@marketplace-name
```

## Usage

### Creating a New Plugin

Simply ask Claude to create a plugin:

```
Create a new plugin called "my-tools" for team development workflows
```

Claude will use the plugin-creator skill to guide you through:
1. Defining the plugin's purpose
2. Choosing components (commands, agents, skills, hooks, MCP)
3. Scaffolding the structure with `init_plugin.py`
4. Creating and configuring components
5. Testing locally
6. Distribution options

### Creating a New Skill

Ask Claude to create a skill:

```
Create a new skill for PDF processing
```

Claude will use the skill-creator skill to help you:
1. Structure the skill appropriately
2. Generate SKILL.md with proper frontmatter
3. Organize supporting resources (scripts, references, assets)
4. Validate and package the skill

### Reference Documentation

Both skills include comprehensive reference documentation:

**Plugin-Creator References:**
- Plugins overview and quickstart
- Complete plugin technical specifications
- Slash commands guide
- Subagents configuration
- Hooks reference
- MCP integration guide
- Plugin marketplaces

**Skill-Creator References:**
- Agent Skills specification
- Additional Agent Skills documentation

## Component Overview

### Skills

Both skills are located in `skills/` directory:
- `plugin-creator/` - Main plugin creation skill
- `skill-creator/` - Skill creation skill

### Scripts

Utility scripts in each skill's `scripts/` directory:

**plugin-creator scripts:**
- `init_plugin.py` - Scaffold new plugin structure

**skill-creator scripts:**
- `init_skill.py` - Scaffold new skill structure
- `package_skill.py` - Package skills for distribution
- `quick_validate.py` - Validate skill structure

## Requirements

- Claude Code 1.0 or later
- Python 3.6+ (for scaffolding scripts)
- Basic familiarity with command-line tools

## Development

To modify or extend this plugin:

1. Clone the repository
2. Make your changes to skills or scripts
3. Test locally using a development marketplace
4. Submit pull requests with improvements

## Architecture

```
plugin-factory/
├── .claude-plugin/
│   └── plugin.json                 # Plugin metadata
├── skills/
│   ├── plugin-creator/
│   │   ├── SKILL.md               # Plugin creation workflow
│   │   ├── references/            # 7 comprehensive docs
│   │   └── scripts/
│   │       └── init_plugin.py     # Plugin scaffolding
│   └── skill-creator/
│       ├── SKILL.md               # Skill creation workflow
│       ├── LICENSE.txt
│       ├── references/
│       │   ├── agent_skills_spec.md
│       │   └── additional/
│       │       └── Agent Skills.md
│       └── scripts/
│           ├── init_skill.py      # Skill scaffolding
│           ├── package_skill.py   # Skill packaging
│           └── quick_validate.py  # Validation
└── README.md
```

## Examples

### Example 1: Creating a Team Tools Plugin

```
Create a plugin called "team-tools" with:
- A /deploy command for deployment workflows
- A code-reviewer agent for PR reviews
- A hook that runs linters after file edits
```

### Example 2: Adding a Skill to Existing Plugin

```
Add a new skill for API documentation to my existing dev-tools plugin
```

### Example 3: Understanding Plugin Components

```
Explain the difference between commands, skills, and agents in plugins
```

## Best Practices

1. **Start Simple**: Begin with one or two components, expand as needed
2. **Use Scaffolding**: Always use `init_plugin.py` and `init_skill.py` scripts
3. **Test Locally**: Use local marketplaces during development
4. **Document Thoroughly**: Include clear READMEs and examples
5. **Version Properly**: Follow semantic versioning
6. **Organize Logically**: Group related components together

## Troubleshooting

Common issues and solutions:

**Plugin not loading:**
- Verify `.claude-plugin/plugin.json` syntax
- Check that component directories are at plugin root
- Use `claude --debug` to see loading errors

**Skills not activating:**
- Ensure SKILL.md has proper YAML frontmatter
- Check that `description` field is specific and actionable
- Verify skill directory is in `skills/` at plugin root

**Scripts not executing:**
- Check file permissions (`chmod +x script.sh`)
- Verify paths use `${CLAUDE_PLUGIN_ROOT}`
- Test scripts independently first

## Contributing

Contributions are welcome! Please:
1. Test your changes thoroughly
2. Update documentation
3. Follow existing code style
4. Include examples for new features

## License

Apache 2.0

## Credits

- **skill-creator** based on original Anthropic skill-creator
- **plugin-creator** created specifically for this plugin
- Reference documentation from official Claude Code docs

## Support

For issues or questions:
- Check the comprehensive reference documentation included in each skill
- Review the official Claude Code documentation
- Open an issue in the repository

## Version History

### 1.0.0 (Initial Release)
- plugin-creator skill with complete workflow
- skill-creator skill (from Anthropic)
- init_plugin.py scaffolding script
- Comprehensive reference documentation
- Example templates and best practices
