---
name: ebay-seller
description: Begleitet den kompletten eBay.de-Verkaufsprozess pro Artikel als State-Machine. Use when the user wants to sell an item on eBay, attaches a photo of something to sell, or asks to research prices, draft a listing, or check on a running eBay listing. Triggers - "auf eBay stellen", "Artikel verkaufen", "eBay Anzeige", Foto eines Verkaufsobjekts.
---

# eBay-Seller

Führt jeden Artikel durch feste Phasen. Stand pro Artikel in `<workspace>/ebay/items/<YYYY-MM-DD-slug>/state.json`. Verkäufer-Defaults in `<workspace>/ebay/config.json`. Pro Tag meist ein neuer Artikel; parallel laufen mehrere in verschiedenen Phasen.

`<workspace>` = das aktuelle Projektverzeichnis des Users (Fallback: nachfragen). Auf Windows liegt das `.claude`-Verzeichnis unter `%USERPROFILE%\.claude\`. Referenzen und Templates liegen relativ zu dieser SKILL.md unter `references/` und `templates/`.

## Voraussetzungen
- **Pflicht:** Claude Code + „Claude in Chrome"-Erweiterung, und ein Chrome, in dem der User bei eBay.de **eingeloggt** ist. Mehr braucht es nicht — läuft auf macOS und Windows.
- **Optional (nur Komfort):** Python 3 + `Pillow` für die automatische Foto-Aufbereitung (`scripts/enhance_photo.py`). **Fehlt Python/Pillow, läuft der Skill trotzdem** — dann werden die Fotos unbearbeitet verwendet (der User lädt sie ohnehin selbst hoch).
- Keine Installation nötig: `state.json` verwalte ich direkt (JSON lesen/schreiben), kein Python-Helfer erforderlich.

## Sicherheits-Gates (nicht verhandelbar)
- **Nie ohne explizite Freigabe veröffentlichen.** Anzeige ausfüllen, dann vor dem finalen Klick anhalten.
- Live-Preisänderungen und Gegenangebote nur nach Freigabe.
- Keine Mängel im Foto wegretuschieren (siehe `references/compliance.md`).

## Erststart
Existiert `<workspace>/ebay/config.json` nicht, ist das der erste Lauf: **zuerst eine Kurzanleitung zeigen** (in 3 Sätzen: Foto reinziehen + „auf eBay stellen"; Fotos lädst du selbst hoch; veröffentlicht wird nur mit deiner Freigabe). Dann aus `templates/config-template.json` anlegen und die Felder beim User abfragen (Standort/PLZ, Versandart+kosten, Rücknahme, Bearbeitungszeit, Verkaufsformat-Default, Tonfall). `ebay_benutzername` ist optional. **Login läuft manuell:** Der User loggt sich selbst in Chrome bei eBay ein — kein Passwort im Chat, keine Keychain-Einrichtung nötig.

## Jeder Lauf
1. `<workspace>/ebay/items/` scannen. Übersicht zeigen: Artikel × Phase × heutige Aufgabe.
2. **Neue(s) Foto(s) an der Nachricht?** (eines oder mehrere) — Bezeichnung grob aus dem ersten Foto ableiten, dann in `items/` nach einem Artikel mit ähnlicher Bezeichnung suchen (Dedupe). Treffer → fragen, ob derselbe Artikel; falls ja, die neuen Fotos dem bestehenden hinzufügen. Sonst neuen Artikel anlegen (Phase `neu`).
3. Für Artikel in `beobachten` und `live`: Tages-Update — aber nur wenn `letzter_lauf` ≠ heute (Idempotenz). Sonst überspringen und „heute schon erfasst" melden.
4. User steuert die Phasenübergänge.

**State-Verwaltung:** `state.json` direkt lesen/schreiben. Am Ende eines Schritts in einem Rutsch speichern; bei Tages-Updates dabei `letzter_lauf` auf das heutige Datum setzen. Nie mitten im Browser-Schritt speichern. (Optional, falls Python vorhanden: die Helfer in `scripts/state.py` tun dasselbe.)

## Phasen

### `neu` → identifizieren
- Siehe `references/item-identification.md`.
- Alle mitgeschickten Fotos unter `photos/original-N.jpg` (1..n) ablegen und in `fotos[]` als `{original}` eintragen (erstes = Hauptbild).
- `artikel`, `kategorie`, `artikelmerkmale` (so weit möglich) füllen.
- Erste Sold-Recherche (siehe `references/price-research.md`), ersten `preis_history`-Eintrag schreiben — nur wenn `letzter_lauf` ≠ heute (kein doppeltes Scrapen).
- Phase → `beobachten`.

### `beobachten` → Preisgefühl sammeln
- Täglich (idempotent) Sold-Preise + Konkurrenz erfassen, `preis_history` ergänzen.
- Trend zeigen (Median/Spanne über die Tage).
- User sagt „bereit" → Phase `fertig_machen`.

### `fertig_machen` → Fotos + Preis + Text
- **Foto-Aufbereitung (optional):** Wenn Python 3 + Pillow vorhanden, alle Fotos aufbereiten — aus dem Skill-Ordner heraus:
  `cd "<skill-ordner>" && python3 -c "from scripts import enhance_photo; print(enhance_photo.enhance_all('<absoluter-item-pfad>/photos'))"`
  und die `enhanced`-Namen in `fotos[]` zurückschreiben. **Ohne Python/Pillow diesen Schritt überspringen** und die Originalfotos verwenden.
- Preisvorschlag aus `preis_history` (Median/Range) mit Begründung → `preisvorschlag`. Range = Sofort-Kauf bzw. Startpreis.
- Verkaufstext aus `templates/listing-template.md` → `listing.md` schreiben (siehe `references/listing-guide.md`).
- **Optimierung** (siehe `references/optimization.md`): Titel auf 80 Zeichen mit Synonymen, Hauptbild = Produkt, vollständige Artikelmerkmale, Format-/Preisvorschlag-Strategie, optional kostenloser Versand, Timing — als Vorschläge an den User.
- User-Freigabe → Phase `einstellen`.

### `einstellen` → Anzeige ausfüllen
- Browser: Tab-Kontext prüfen, neuen Tab öffnen. **Sicherstellen, dass der User in Chrome bei eBay eingeloggt ist** — wenn nicht, ihn bitten, sich einzuloggen (siehe `references/login.md`). Dann eBay-Einstellformular.
- Felder aus `state.json`/`config.json`: Titel, Beschreibung, **Kategorie**, **Artikelmerkmale**, Zustand, Bilder (vorhandene `fotos`, erstes = Hauptbild), Preis/Format, Versandprofil, Standort/PLZ.
- **Foto-Upload macht der User selbst** (Datei-Upload ist für die Automatisierung gesperrt): aufbereitete bzw. Originalfotos per Drag & Drop in den Foto-Bereich ziehen.
- Fehlende Pflichtfelder beim User nachfragen.
- **Vor dem finalen Veröffentlichen ANHALTEN.** Nach Freigabe veröffentlichen, `listing_url` speichern, Phase → `live`.

### `live` → beobachten
- Täglich (idempotent) Aufrufe/Beobachter/Angebote ablesen → `live_history`-Eintrag `{ datum, aufrufe, beobachter, angebote }`.
- Auffälligkeiten (kaum Aufrufe, viele Beobachter ohne Kauf) → Preis-/Text-Anpassung VORSCHLAGEN, nur nach Freigabe ändern.
- Verkauft/beendet → Phase `abgeschlossen`.

### `abgeschlossen`
Endzustand, Ordner bleibt zur Historie.

## Browser-Hinweise
- eBay-Tools (Claude in Chrome) sind deferred → vor Nutzung per ToolSearch laden (`select:mcp__claude-in-chrome__...`).
- Vor jeder eBay-Aktion sicherstellen, dass der User eingeloggt ist; bei 2FA/Captcha anhalten und den User bitten.
- Gedrosselt arbeiten (siehe `references/price-research.md`).
