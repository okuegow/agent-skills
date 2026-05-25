> 🌐 [English](README.md) · **Deutsch**

# 🛠️ Agent Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-plugin%20marketplace-d97757)](https://claude.com/claude-code)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Windows-blue)](#)
[![Skills](https://img.shields.io/badge/skills-1-success)](#-enthaltene-skills)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#)

Eine Sammlung von Skills für [Claude Code](https://claude.com/claude-code) — kleine, fokussierte Erweiterungen, die Claude für bestimmte Aufgaben befähigen.

## ⚡ Installation

**Am einfachsten — sag es Claude Code einfach in einer beliebigen Session:**

> „Füge den Marketplace `okuegow/agent-skills` hinzu und installiere den Skill `ebay-seller`."

Claude führt die beiden Befehle für dich aus. Oder du tippst sie selbst:

```bash
claude plugin marketplace add okuegow/agent-skills
claude plugin install ebay-seller@okuegow-skills
```

Danach Claude Code neu starten. Fertig — kein Dateien-Kopieren, keine Zusatz-Installation.

<details>
<summary>Manuelle Installation (ohne Plugin-System)</summary>

Den Skill-Ordner in dein lokales Claude-Skills-Verzeichnis kopieren:

- **macOS / Linux:** `~/.claude/skills/`
- **Windows:** `%USERPROFILE%\.claude\skills\`

Der Skill liegt unter `plugins/ebay-seller/skills/ebay-seller/`. Danach Claude Code neu starten.
</details>

## 📦 Enthaltene Skills

| Skill | Beschreibung |
|-------|--------------|
| [`ebay-seller`](plugins/ebay-seller/skills/ebay-seller) | Begleitet den kompletten eBay.de-Verkaufsprozess pro Artikel: Foto → Artikel erkennen → Vergleichspreise → Foto/Text/Preis vorbereiten → Anzeige ausfüllen → beobachten. Veröffentlicht nie ohne Freigabe. |

## ✅ Voraussetzungen

Variiert je Skill — siehe die jeweilige `README.md`. Die meisten brauchen nur Claude Code selbst; optionale Extras (z. B. Python-Bibliotheken) sind dort vermerkt.

## 📄 Lizenz

[MIT](LICENSE) © 2026 Oliver Kuegow
