#!/usr/bin/env python3
"""
Plugin Initializer - Creates a new Claude Code plugin from template

Usage:
    init_plugin.py <plugin-name> --path <path>

Examples:
    init_plugin.py my-plugin --path .
    init_plugin.py team-tools --path ~/projects/plugins
    init_plugin.py dev-utils --path /custom/location
"""

import sys
from pathlib import Path


PLUGIN_JSON_TEMPLATE = """{
  "name": "{plugin_name}",
  "version": "1.0.0",
  "description": "[TODO: Brief description of what this plugin does]",
  "author": {
    "name": "[TODO: Your Name]",
    "email": "[TODO: your.email@example.com]"
  }
}
"""

README_TEMPLATE = """# {plugin_title}

> [TODO: One-line description of what this plugin does]

## Overview

[TODO: Explain what this plugin provides and why someone would use it]

## Components

This plugin includes:

[TODO: List the components included in this plugin]

- **Commands**: [List command names or remove if none]
- **Agents**: [List agent names or remove if none]
- **Skills**: [List skill names or remove if none]
- **Hooks**: [Describe hooks or remove if none]
- **MCP Servers**: [List MCP servers or remove if none]

## Installation

### From local directory

```bash
/plugin marketplace add ./path/to/marketplace
/plugin install {plugin_name}@marketplace-name
```

### From GitHub

```bash
/plugin marketplace add your-org/plugin-repo
/plugin install {plugin_name}@your-org
```

## Usage

[TODO: Provide examples of how to use each component]

### Commands

[TODO: Document each command with examples]

```
/command-name [arguments]
```

### Skills

[TODO: Explain when skills are automatically invoked]

### Agents

[TODO: Explain when to use each agent]

```
Use the agent-name agent to [do something]
```

## Configuration

[TODO: Document any environment variables or settings required]

## Requirements

[TODO: List any dependencies, tools, or prerequisites]

## Development

To modify this plugin:

1. Make your changes to the plugin files
2. Test locally with a development marketplace
3. Version bump in `plugin.json`
4. Update this README

## License

[TODO: Add license information]

## Author

{author_name}
"""

EXAMPLE_COMMAND = """---
description: [TODO: Brief description of what this command does]
---

# Example Command

[TODO: Provide instructions for Claude on how to execute this command]

This is a template command. Replace this content with actual command instructions.

## Guidelines

- Be specific about what Claude should do
- Include examples if helpful
- Reference any files or resources needed

## Examples

- Example usage 1
- Example usage 2
"""

EXAMPLE_AGENT = """---
name: example-agent
description: [TODO: When should this agent be used? Be specific about scenarios and tasks]
tools: Read, Grep, Glob  # Optional - remove to inherit all tools
---

# Example Agent

[TODO: Provide detailed instructions for this specialized agent]

This is a template agent. Replace this content with actual agent instructions.

## Role

[TODO: Define the agent's specialized role and expertise]

## Approach

[TODO: Describe how the agent should approach tasks]

1. Step 1
2. Step 2
3. Step 3

## Constraints

[TODO: Any limitations or guidelines the agent should follow]
"""

HOOKS_JSON_TEMPLATE = """{
  "description": "Example hooks for {plugin_name}",
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "comment": "TODO: Replace with actual hook command",
            "command": "${{CLAUDE_PLUGIN_ROOT}}/scripts/example-hook.sh"
          }
        ]
      }
    ]
  }
}
"""

EXAMPLE_HOOK_SCRIPT = """#!/bin/bash
# Example hook script for {plugin_name}
#
# This script is triggered after Write or Edit tool use.
# Replace with actual hook logic or delete if not needed.
#
# Input: JSON via stdin with tool information
# Output: Exit code 0 for success, 2 to block with stderr message

# Read input from stdin
input=$(cat)

# TODO: Add your hook logic here
# Examples:
# - Validate file contents
# - Run formatters or linters
# - Send notifications
# - Update external systems

echo "Hook executed successfully"
exit 0
"""

MCP_JSON_TEMPLATE = """{
  "mcpServers": {
    "example-server": {
      "command": "${{CLAUDE_PLUGIN_ROOT}}/servers/example-server",
      "args": ["--config", "${{CLAUDE_PLUGIN_ROOT}}/config.json"],
      "env": {
        "SERVER_PORT": "8080"
      }
    }
  }
}
"""


def title_case_plugin_name(plugin_name):
    """Convert hyphenated plugin name to Title Case for display."""
    return ' '.join(word.capitalize() for word in plugin_name.split('-'))


def init_plugin(plugin_name, path):
    """
    Initialize a new plugin directory with template files.

    Args:
        plugin_name: Name of the plugin (kebab-case)
        path: Path where the plugin directory should be created

    Returns:
        Path to created plugin directory, or None if error
    """
    # Determine plugin directory path
    plugin_dir = Path(path).resolve() / plugin_name

    # Check if directory already exists
    if plugin_dir.exists():
        print(f"❌ Error: Plugin directory already exists: {plugin_dir}")
        return None

    # Create plugin directory structure
    try:
        plugin_dir.mkdir(parents=True, exist_ok=False)
        print(f"✅ Created plugin directory: {plugin_dir}")

        # Create .claude-plugin directory
        claude_plugin_dir = plugin_dir / '.claude-plugin'
        claude_plugin_dir.mkdir(exist_ok=True)
        print("✅ Created .claude-plugin/ directory")
    except Exception as e:
        print(f"❌ Error creating directory: {e}")
        return None

    # Create plugin.json
    plugin_json_content = PLUGIN_JSON_TEMPLATE.format(plugin_name=plugin_name)
    plugin_json_path = claude_plugin_dir / 'plugin.json'
    try:
        plugin_json_path.write_text(plugin_json_content)
        print("✅ Created .claude-plugin/plugin.json")
    except Exception as e:
        print(f"❌ Error creating plugin.json: {e}")
        return None

    # Create README.md
    plugin_title = title_case_plugin_name(plugin_name)
    readme_content = README_TEMPLATE.format(
        plugin_title=plugin_title,
        plugin_name=plugin_name,
        author_name="[Your Name]"
    )
    readme_path = plugin_dir / 'README.md'
    try:
        readme_path.write_text(readme_content)
        print("✅ Created README.md")
    except Exception as e:
        print(f"❌ Error creating README.md: {e}")
        return None

    # Create optional component directories with examples
    print("\n📦 Creating example component directories...")
    print("   (Delete any directories you don't need)")

    try:
        # Commands directory with example
        commands_dir = plugin_dir / 'commands'
        commands_dir.mkdir(exist_ok=True)
        example_command = commands_dir / 'example.md'
        example_command.write_text(EXAMPLE_COMMAND)
        print("✅ Created commands/example.md")

        # Agents directory with example
        agents_dir = plugin_dir / 'agents'
        agents_dir.mkdir(exist_ok=True)
        example_agent = agents_dir / 'example-agent.md'
        example_agent.write_text(EXAMPLE_AGENT)
        print("✅ Created agents/example-agent.md")

        # Skills directory (empty - use skill-creator to add skills)
        skills_dir = plugin_dir / 'skills'
        skills_dir.mkdir(exist_ok=True)
        skills_readme = skills_dir / 'README.md'
        skills_readme.write_text("# Skills\n\nUse the skill-creator skill to add skills to this plugin.\n")
        print("✅ Created skills/ directory")

        # Hooks directory with example
        hooks_dir = plugin_dir / 'hooks'
        hooks_dir.mkdir(exist_ok=True)
        hooks_json = hooks_dir / 'hooks.json'
        hooks_json.write_text(HOOKS_JSON_TEMPLATE.format(plugin_name=plugin_name))
        print("✅ Created hooks/hooks.json")

        # Scripts directory for hook scripts
        scripts_dir = plugin_dir / 'scripts'
        scripts_dir.mkdir(exist_ok=True)
        example_hook = scripts_dir / 'example-hook.sh'
        example_hook.write_text(EXAMPLE_HOOK_SCRIPT.format(plugin_name=plugin_name))
        example_hook.chmod(0o755)
        print("✅ Created scripts/example-hook.sh")

        # MCP configuration (optional)
        mcp_json = plugin_dir / '.mcp.json'
        mcp_json.write_text(MCP_JSON_TEMPLATE)
        print("✅ Created .mcp.json")

    except Exception as e:
        print(f"❌ Error creating component directories: {e}")
        return None

    # Print next steps
    print(f"\n✅ Plugin '{plugin_name}' initialized successfully at {plugin_dir}")
    print("\n📋 Next steps:")
    print("1. Edit .claude-plugin/plugin.json to update metadata")
    print("2. Update README.md with plugin documentation")
    print("3. Customize or delete example components:")
    print("   - commands/example.md")
    print("   - agents/example-agent.md")
    print("   - hooks/hooks.json")
    print("   - .mcp.json")
    print("4. Use skill-creator skill to add skills to skills/ directory")
    print("5. Test locally with a development marketplace")
    print("\n💡 Only .claude-plugin/plugin.json is required.")
    print("   Delete any component directories you don't need.")

    return plugin_dir


def main():
    if len(sys.argv) < 4 or sys.argv[2] != '--path':
        print("Usage: init_plugin.py <plugin-name> --path <path>")
        print("\nPlugin name requirements:")
        print("  - Kebab-case identifier (e.g., 'my-plugin')")
        print("  - Lowercase letters, digits, and hyphens only")
        print("  - Must match directory name exactly")
        print("\nExamples:")
        print("  init_plugin.py my-plugin --path .")
        print("  init_plugin.py team-tools --path ~/projects/plugins")
        print("  init_plugin.py dev-utils --path /custom/location")
        sys.exit(1)

    plugin_name = sys.argv[1]
    path = sys.argv[3]

    print(f"🚀 Initializing plugin: {plugin_name}")
    print(f"   Location: {path}")
    print()

    result = init_plugin(plugin_name, path)

    if result:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
