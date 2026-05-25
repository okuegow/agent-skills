# Listing-Leitfaden

## Titel (max. 80 Zeichen)
- Marke + Modell + Kerneigenschaft + Zustand, suchstark.
- Keine Spam-Zeichen, keine erfundenen Attribute.
- Beispiel: „Nikon AF-S 50mm f/1.8G Festbrennweite Vollformat – sehr guter Zustand".

## Verkaufstext (`listing.md` aus Template)
- Aufmacher: 1–2 Sätze Nutzen/Highlight.
- Zustand ehrlich beschreiben (inkl. sichtbarer Gebrauchsspuren).
- Eigenschaften als Stichpunkte (aus `artikel.specs`).
- Lieferumfang exakt.
- Versand/Abholung aus `config.json`.
- Tonfall aus `config.tonfall` (Default: verkaufsstark aber ehrlich).

## Pflichtfelder beim Einstellen
Ohne diese lässt eBay nicht veröffentlichen:
- **Kategorie** (`state.kategorie`)
- **Artikelmerkmale / item specifics** (`state.artikelmerkmale`) — kategorieabhängig pflichtig
- **Zustand**
- **Bilder:** alle `photos/enhanced-N.jpg` hochladen, erstes = Hauptbild
- **Versandprofil** (aus `config.json`)
- Preis (Sofort-Kauf) bzw. Startpreis (Auktion), Format aus `config.verkaufsformat_default`
Fehlt etwas → beim User nachfragen, NICHT erfinden.

## Optimierung
Vor dem Einstellen die Hebel aus `optimization.md` prüfen: 80-Zeichen-Titel mit Synonymen, Hauptbild = Produkt (nicht Verpackung), vollständige Artikelmerkmale, Format-/Preisvorschlag-Strategie, optional kostenloser Versand, Timing (So-Abend). Als Vorschläge an den User, dann umsetzen.
