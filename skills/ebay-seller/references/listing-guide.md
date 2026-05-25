# Listing guide

Write the actual title and description **in German** (eBay.de buyers).

## Title (max. 80 characters)
- Brand + model + key feature + condition, search-strong.
- No spam characters, no invented attributes.
- Example: „Nikon AF-S 50mm f/1.8G Festbrennweite Vollformat – sehr guter Zustand".

## Description (`listing.md` from template)
- Opening: 1–2 sentences on benefit/highlight.
- Describe the condition honestly (including visible wear).
- Features as bullet points (from `artikel.specs`).
- Exact scope of delivery.
- Shipping/pickup from `config.json`.
- Tone from `config.tonfall` (default: strong-selling but honest).

## Required fields when listing
Without these eBay will not publish:
- **Category** (`state.kategorie`)
- **Item specifics** (`state.artikelmerkmale`) — category-dependent, mandatory
- **Condition**
- **Images:** upload all `photos/enhanced-N.jpg` (or originals), first = main image
- **Shipping profile** (from `config.json`)
- Price (fixed) resp. start price (auction), format from `config.verkaufsformat_default`
If something is missing → ask the user, do NOT invent it.

## Optimization
Before listing, apply the levers from `optimization.md`: 80-character title with synonyms, main image = product (not the box), complete item specifics, format/best-offer strategy, optional free shipping, timing (Sunday evening). Present as suggestions to the user, then apply.
