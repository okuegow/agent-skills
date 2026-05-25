> 🌐 **English** · [Deutsch](README.de.md)

# eBay-Seller — a Claude Code skill

Guides the complete eBay.de sale: photo in → identify item → comparable prices → prepare photo/text/price → fill the listing → monitor. You stay in control: **nothing is published without your approval.** Listings are written in German for eBay.de.

## Requirements
- **Required:** Claude Code + the **"Claude in Chrome"** extension, and a Chrome where you are **logged in to eBay.de**.
- **Optional:** Python 3 + `Pillow` for automatic photo enhancement. **Everything still works without it** — you then use the photos unedited.
- Runs on **macOS and Windows**. Nothing complicated to install.

## Installation
**Easiest — tell Claude Code:** "Add the marketplace `okuegow/agent-skills` and install `ebay-seller`." Or run:
```bash
claude plugin marketplace add okuegow/agent-skills
claude plugin install ebay-seller@okuegow-skills
```
**Manual alternative:** copy this `ebay-seller/` folder into `~/.claude/skills/` (macOS/Linux) or `%USERPROFILE%\.claude\skills\` (Windows).

Restart Claude Code (or start a new session). Done.

## Usage
- Drag a **product photo** into the chat and write e.g. "**sell on eBay**", **or** type the command **`/ebay-seller`**.
- On first use the skill briefly asks for your seller defaults (ZIP, shipping, returns …) and creates `ebay/config.json`.
- After that it guides you phase by phase: identify → prices → finalize → list → monitor.

## Good to know
- **You upload the photos yourself** (drag & drop into eBay) — automatic file uploads are blocked by the browser for security reasons.
- **You click publish yourself** — the skill fills everything in and stops before that.
- **You log in yourself** in Chrome (no password in chat).
- Data lives in `ebay/items/<item>/` (per-item state) and `ebay/config.json`.
