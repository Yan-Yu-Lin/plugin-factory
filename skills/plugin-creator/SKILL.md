---
name: plugin-creator
description: Comprehensive guide for creating Claude Code plugins with commands, agents, skills, hooks, and MCP servers. Use when users want to create, modify, or understand plugins, marketplaces, or any plugin components.
license: Apache 2.0
---

# Plugin Creator

This skill provides comprehensive guidance for creating Claude Code plugins - the universal container for extending Claude Code functionality.

## About Plugins

Plugins are the **universal extension mechanism** for Claude Code. A single plugin can contain any combination of:

1. **Commands** - Custom slash commands (`/command-name`)
2. **Agents** - Specialized subagents for specific tasks
3. **Skills** - Model-invoked capabilities (Claude decides when to use)
4. **Hooks** - Event handlers that respond to Claude Code events
5. **MCP Servers** - External tool integrations via Model Context Protocol

### Plugin vs Individual Components

**Key Understanding**:
- **Skills** are one type of content that goes *inside* plugins
- **Plugins** are the distribution mechanism for skills, commands, agents, hooks, and MCP servers
- A plugin can contain just skills, or mix multiple component types

### Progressive Disclosure

Plugins follow a three-level loading system:
1. **Plugin metadata** - Always in context (~100 words from plugin.json)
2. **Component metadata** - Loaded when relevant (command descriptions, skill descriptions)
3. **Full component content** - Loaded when invoked (SKILL.md body, command body, agent instructions)

## Plugin Creation Workflow

Follow this structured process to create effective plugins:

### Step 1: Define Your Plugin's Purpose

Before creating anything, clearly understand:
- What functionality does this plugin provide?
- Who will use it? (personal, team, community)
- What components does it need? (commands, agents, skills, hooks, MCP)

Ask the user:
- "What functionality should this plugin provide?"
- "Will this be for personal use, team use, or community distribution?"
- "Do you need commands (user-invoked), skills (model-invoked), or both?"

### Step 2: Choose Your Components

Based on the purpose, determine which components to include:

**Use Commands when:**
- Users explicitly invoke functionality with `/command-name`
- Quick prompt snippets or templates
- Workflow steps that need manual control

**Use Skills when:**
- Claude should automatically discover and use capabilities
- Complex workflows with multiple files/scripts
- Requires progressive disclosure (references, assets)

**Use Agents when:**
- Need separate context window for specialized tasks
- Task-specific tool restrictions
- Different model requirements

**Use Hooks when:**
- Automating responses to events (file changes, tool usage)
- Validation, notifications, or side effects
- Integration with external systems

**Use MCP Servers when:**
- Connecting to external tools/services
- Database access, API integrations
- Custom tool implementations

### Step 3: Initialize Plugin Structure

Use the init_plugin.py script to scaffold the plugin:

```bash
python scripts/init_plugin.py <plugin-name> --path <output-directory>
```

The script creates:
```
plugin-name/
├── .claude-plugin/
│   └── plugin.json          # Required: plugin metadata
├── commands/                 # Optional: slash commands
├── agents/                   # Optional: subagents
├── skills/                   # Optional: Agent Skills
├── hooks/                    # Optional: event handlers
│   └── hooks.json
├── .mcp.json                # Optional: MCP servers
└── README.md                # Documentation
```

**Important**: Only `plugin.json` is required. All other directories are optional - create only what you need.

### Step 4: Configure Plugin Metadata

Edit `.claude-plugin/plugin.json`:

```json
{
  "name": "plugin-name",           // Required: kebab-case identifier
  "version": "1.0.0",              // Recommended: semantic versioning
  "description": "Brief description", // Recommended
  "author": {                      // Optional but recommended
    "name": "Your Name",
    "email": "you@example.com"
  }
}
```

For complete schema, see `references/Plugins reference.md`.

### Step 5: Create Plugin Components

**For Commands:**
See `references/Slash Commands.md` for complete details on:
- Creating command files in `commands/` directory
- Using frontmatter (description, allowed-tools, arguments)
- Argument placeholders ($ARGUMENTS, $1, $2, etc.)
- Bash execution with !` `
- File references with @

**For Skills:**
For skill creation, use the **skill-creator skill** from this plugin:
```
Use the skill-creator skill to create a new skill in this plugin
```

Skills go in `skills/skill-name/SKILL.md` within your plugin. The skill-creator skill provides complete guidance.

**For Agents:**
See `references/Subagents.md` for complete details on:
- Agent file format (Markdown with YAML frontmatter)
- Configuring tools, model, description
- Writing effective agent prompts

**For Hooks:**
See `references/Hooks reference.md` for complete details on:
- Hook events (PreToolUse, PostToolUse, UserPromptSubmit, etc.)
- Configuration format in `hooks/hooks.json`
- Input/output schemas
- Using ${CLAUDE_PLUGIN_ROOT} for plugin paths

**For MCP Servers:**
See `references/Connect Claude Code to tools via MCP.md` for complete details on:
- MCP server configuration in `.mcp.json`
- Transport types (stdio, HTTP, SSE)
- Environment variables and authentication

### Step 6: Test Your Plugin Locally

Create a local marketplace for testing:

**Directory structure:**
```
dev-marketplace/
├── .claude-plugin/
│   └── marketplace.json
└── your-plugin/
    └── (your plugin files)
```

**Create marketplace.json:**
```json
{
  "name": "dev-marketplace",
  "owner": {
    "name": "Developer"
  },
  "plugins": [
    {
      "name": "your-plugin",
      "source": "./your-plugin",
      "description": "Plugin under development"
    }
  ]
}
```

**Test workflow:**
```bash
# From parent directory of dev-marketplace
claude

# In Claude Code:
/plugin marketplace add ./dev-marketplace
/plugin install your-plugin@dev-marketplace

# Test your plugin components
# Then uninstall/reinstall after changes:
/plugin uninstall your-plugin@dev-marketplace
/plugin install your-plugin@dev-marketplace
```

### Step 7: Document Your Plugin

Create a comprehensive README.md:
- Installation instructions
- Component descriptions (what commands, skills, etc. are included)
- Usage examples
- Requirements (dependencies, environment variables)
- Configuration options

### Step 8: Distribute Your Plugin

**For personal use:**
- Keep locally and add with `/plugin marketplace add ./path/to/plugin`

**For team use:**
- Create a git repository
- Add `.claude-plugin/marketplace.json` at repo root
- Team installs with `/plugin marketplace add your-org/plugin-repo`
- Can configure automatic installation via `.claude/settings.json`

**For community:**
- Publish to GitHub
- Add to community marketplace catalogs
- Provide clear documentation and examples

See `references/Plugin marketplaces.md` for complete distribution details.

## Reference Documentation

This skill includes comprehensive reference documentation:

**Plugin System:**
- `references/Plugins.md` - Main plugin overview and quickstart
- `references/Plugins reference.md` - Complete technical specifications

**Plugin Components:**
- `references/Slash Commands.md` - Command creation and features
- `references/Subagents.md` - Agent configuration and usage
- `references/Hooks reference.md` - Event handling and automation
- `references/Connect Claude Code to tools via MCP.md` - MCP server integration

**Distribution:**
- `references/Plugin marketplaces.md` - Creating and managing marketplaces

**Note:** For Skills specifically, use the **skill-creator skill** included in this plugin rather than writing them manually.

## Key Concepts

### Plugin Directory Structure

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json          # REQUIRED - Must be here
├── commands/                 # At plugin root, NOT in .claude-plugin/
├── agents/                   # At plugin root
├── skills/                   # At plugin root
├── hooks/                    # At plugin root
│   └── hooks.json
└── .mcp.json                # At plugin root
```

**Critical**: Only `.claude-plugin/plugin.json` goes in the `.claude-plugin/` directory. All component directories (commands/, agents/, skills/, hooks/) must be at the plugin root.

### Environment Variables

Use `${CLAUDE_PLUGIN_ROOT}` in plugin configurations to reference plugin-relative paths:

```json
{
  "hooks": {
    "PostToolUse": [{
      "hooks": [{
        "type": "command",
        "command": "${CLAUDE_PLUGIN_ROOT}/scripts/validate.sh"
      }]
    }]
  }
}
```

### Component Discovery

- **Commands**: Automatically discovered from `commands/` directory
- **Agents**: Automatically discovered from `agents/` directory
- **Skills**: Automatically discovered from `skills/` directory
- **Hooks**: Loaded from `hooks/hooks.json` or inline in `plugin.json`
- **MCP Servers**: Loaded from `.mcp.json` or inline in `plugin.json`

## Common Patterns

### Single-Purpose Plugin

Plugin with just one type of component:
```
formatter-plugin/
├── .claude-plugin/plugin.json
└── commands/
    └── format.md
```

### Comprehensive Plugin

Plugin with multiple component types:
```
development-plugin/
├── .claude-plugin/plugin.json
├── commands/          # User-invoked workflows
├── agents/           # Specialized subagents
├── skills/           # Model-invoked capabilities
├── hooks/            # Event automation
└── .mcp.json        # External integrations
```

### Team Workflow Plugin

Plugin for standardized team workflows:
```
team-tools/
├── .claude-plugin/plugin.json
├── commands/
│   ├── deploy.md
│   └── review.md
├── skills/
│   └── code-standards/
│       ├── SKILL.md
│       └── references/
└── hooks/
    └── hooks.json
```

## Troubleshooting

**Plugin not loading:**
- Validate `plugin.json` syntax
- Check that plugin name matches directory name
- Use `claude --debug` to see loading errors

**Components not appearing:**
- Verify directories are at plugin root, NOT in `.claude-plugin/`
- Check file names and formats
- Ensure proper frontmatter in component files

**Hooks not firing:**
- Check script permissions (`chmod +x script.sh`)
- Use `${CLAUDE_PLUGIN_ROOT}` for all plugin paths
- Review hook input/output in debug mode

**Path errors:**
- All paths must be relative starting with `./`
- Never use absolute paths in plugin configs
- Use `${CLAUDE_PLUGIN_ROOT}` for plugin-relative paths

## Best Practices

1. **Start simple**: Begin with one component type, add more as needed
2. **Use init script**: Always use `scripts/init_plugin.py` to scaffold
3. **Test locally**: Use local marketplace during development
4. **Document thoroughly**: Clear README with examples
5. **Version properly**: Follow semantic versioning
6. **Name clearly**: Use descriptive, kebab-case names
7. **Validate early**: Use `claude plugin validate .` before distribution
8. **Think about scope**: Consider who will use it (personal/team/community)

## Next Steps

After creating your plugin:
1. Test all components thoroughly
2. Write comprehensive documentation
3. Create example usage scenarios
4. Share with team or community
5. Gather feedback and iterate
