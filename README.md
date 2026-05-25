> 🌐 **English** · [Deutsch](README.de.md)

# 🛠️ Agent Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-plugin%20marketplace-d97757)](https://claude.com/claude-code)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Windows-blue)](#)
[![Skills](https://img.shields.io/badge/skills-1-success)](#-included-skills)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#)

A collection of skills for [Claude Code](https://claude.com/claude-code) — small, focused extensions that enable Claude for specific tasks.

## ⚡ Install

**Easiest — just tell Claude Code in any session:**

> "Add the marketplace `okuegow/agent-skills` and install the `ebay-seller` skill."

Claude runs the two commands for you. Or run them yourself:

```bash
claude plugin marketplace add okuegow/agent-skills
claude plugin install ebay-seller@agent-skills
```

Then restart Claude Code. That's it — no manual file copying, no extra installs.

<details>
<summary>Manual install (without the plugin system)</summary>

Copy the skill folder into your local Claude skills directory:

- **macOS / Linux:** `~/.claude/skills/`
- **Windows:** `%USERPROFILE%\.claude\skills\`

The skill lives at `plugins/ebay-seller/skills/ebay-seller/`. Then restart Claude Code.
</details>

## 📦 Included skills

| Skill | Description |
|-------|-------------|
| [`ebay-seller`](plugins/ebay-seller/skills/ebay-seller) | Guides the complete eBay.de selling process per item: photo → identify item → comparable prices → prepare photo/text/price → fill the listing → monitor. Never publishes without approval. |

## ✅ Requirements

Vary per skill — see the respective `README.md`. Most need only Claude Code itself; optional extras (e.g. Python libraries) are noted there.

## 📄 License

[MIT](LICENSE) © 2026 Oliver Kuegow
