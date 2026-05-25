# Price research (eBay.de)

## Data source
- **Sold items** (real selling prices): search eBay for the item name → enable the "Verkaufte Artikel" (sold items) filter.
- **Active competition** (market pressure): current listings of the same thing, count + price range.

## Analysis
- Per run capture: title, final price, date, condition.
- Compute median and range of the sold prices; mark outliers (different condition/bundle), do not count them in.
- Entry in `preis_history`: `{ datum, sold_preise[], sold_median, sold_spanne, konkurrenz_anzahl, konkurrenz_preise[] }`.
- The suggested price range means the **fixed (Sofort-Kauf) price** resp. the **auction start price** — for an auction this is not the expected final price.

## Robustness / account protection (IMPORTANT)
- Max. **1 research run per item per day**, sequential (no parallel tabs), with human-like pauses.
- Before writing, check: is `letzter_lauf` already today → if so, do NOT capture again.
- Captcha / login wall / 2FA → stop, ask the user to resolve it manually, then continue.
- Research failed / no hits → **no** `preis_history` entry, phase stays, retry next day, report clearly to the user.
- Write at the end of the run atomically (single save), then set `letzter_lauf`.
- If the sold filter breaks permanently → fall back to the official eBay Browse/Marketplace Insights API (out of scope for v1, documented here only).
