# Roadmap

Ideas for improving this skill collection. Not commitments — a prioritized backlog to pick from.

## Quick wins
- [ ] CI via GitHub Actions: run `pytest` + `claude plugin validate` on every push → "build passing" badge.
- [ ] Demo GIF / screenshots in the README to lower the entry barrier.
- [ ] `CHANGELOG.md` + SemVer git tags per skill (`claude plugin tag`).
- [ ] `CONTRIBUTING.md` + issue templates.
- [ ] Make the dependency + secret scan a routine pre-publish step.

## ebay-seller skill
- [ ] **Biggest lever — eBay Sell API instead of browser form.** Removes today's pain points: blocked photo upload, the re-login before publishing, brittle reactive-form scrolling, two-session autosave clobber. One-time setup (eBay developer account + OAuth). Browser stays as fallback.
- [ ] **Pricing feedback loop:** learn from `preis_history` + `live_history` (predicted vs. realized price, time-to-sell per strategy) to sharpen future price suggestions.
- [ ] **Scheduled monitoring:** optional schedule for the `live` phase that only pings the user on signals (many watchers, no sale → suggest price drop).
- [ ] **More platforms:** Kleinanzeigen.de in parallel / cross-posting; other eBay locales.
- [ ] **No-Python photo enhancer:** small browser/Canvas-based crop/cleanup so enhancement works without Pillow (zero dependencies).

## Process for future skills
- [ ] Validate real end-to-end feasibility against live services early (we discovered upload/login limits late). Put "can the automation actually do this?" checks into the spec phase.
- [ ] Design for zero-install / minimal dependencies from the start when a skill is meant to be shared.
- [ ] Reuse the brainstorm → spec → plan → subagent-driven build pipeline as the repeatable template for new skills.

## Suggested order
1. CI badge + demo GIF + pricing feedback loop (high value, low effort)
2. Scheduled monitoring
3. eBay Sell API integration (biggest payoff, larger project)
