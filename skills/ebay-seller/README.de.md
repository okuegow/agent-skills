> 🌐 [English](README.md) · **Deutsch**

# eBay-Seller — Skill für Claude Code

Begleitet den kompletten eBay.de-Verkauf: Foto rein → Artikel erkennen → Vergleichspreise → Foto/Text/Preis vorbereiten → Anzeige ausfüllen → beobachten. Du behältst die Kontrolle: **veröffentlicht wird nie ohne deine Freigabe.**

## Voraussetzungen
- **Pflicht:** Claude Code + die Erweiterung **„Claude in Chrome"**, und ein Chrome, in dem du bei **eBay.de eingeloggt** bist.
- **Optional:** Python 3 + `Pillow` für automatische Foto-Aufbereitung. **Ohne läuft alles trotzdem** — dann nimmst du die Fotos unbearbeitet.
- Läuft auf **macOS und Windows**. Nichts Kompliziertes nachzuinstallieren.

## Installation
Den Ordner `ebay-seller/` hierhin kopieren:
- **macOS/Linux:** `~/.claude/skills/ebay-seller/`
- **Windows:** `%USERPROFILE%\.claude\skills\ebay-seller\`

Claude Code neu starten (oder neue Session). Fertig.

## Benutzung
- Ein **Produktfoto** in den Chat ziehen und z. B. „**auf eBay stellen**" schreiben, **oder** den Befehl **`/ebay-seller`** tippen.
- Beim ersten Mal fragt der Skill kurz deine Verkäufer-Defaults ab (PLZ, Versand, Rücknahme …) und legt `ebay/config.json` an.
- Danach führt er dich Phase für Phase: erkennen → Preise → fertig machen → einstellen → beobachten.

## Gut zu wissen
- **Fotos hochladen** musst du selbst (Drag & Drop in eBay) — automatische Datei-Uploads sind vom Browser aus Sicherheitsgründen gesperrt.
- **Einstellen/Veröffentlichen** klickst du selbst — der Skill füllt alles aus und hält davor an.
- **Login** machst du selbst in Chrome (kein Passwort im Chat).
- Daten liegen in `ebay/items/<artikel>/` (Stand pro Artikel) und `ebay/config.json`.
