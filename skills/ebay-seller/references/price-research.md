# Preisrecherche (eBay.de)

## Datenquelle
- **Verkaufte Artikel** (echte Verkaufspreise): eBay-Suche nach Bezeichnung → Filter „Verkaufte Artikel" aktivieren.
- **Laufende Konkurrenz** (Marktdruck): aktuelle Angebote derselben Sache, Anzahl + Preisspanne.

## Auswertung
- Pro Durchlauf erfassen: Titel, Endpreis, Datum, Zustand.
- Median und Spanne der sold-Preise bilden; Ausreißer (anderer Zustand/Set) markieren, nicht einrechnen.
- Eintrag in `preis_history`: `{ datum, sold_preise[], sold_median, sold_spanne, konkurrenz_anzahl, konkurrenz_preise[] }`.
- Der vorgeschlagene Preis-Range meint **Sofort-Kauf-Preis** bzw. **Auktions-Startpreis** — bei Auktion ist das nicht der erwartete Endpreis.

## Robustheit / Account-Schutz (WICHTIG)
- Max. **1 Recherche-Durchlauf pro Artikel pro Tag**, sequenziell (keine parallelen Tabs), mit menschenähnlichen Pausen.
- Vor dem Schreiben prüfen: `already_ran_today` → wenn heute schon gelaufen, NICHT erneut erfassen.
- Captcha / Login-Wall / 2FA → anhalten, User bitten es manuell zu lösen, dann fortsetzen.
- Recherche fehlgeschlagen / keine Treffer → **kein** `preis_history`-Eintrag, Phase bleibt, Retry am Folgetag, dem User klar melden.
- Schreiben am Ende des Laufs atomar über `state.save_state`, danach `state.mark_ran`.
- Dauerhafter Bruch des sold-Filters → Ausweichweg eBay Browse-/Marketplace-Insights-API (out of scope v1, hier nur dokumentiert).
