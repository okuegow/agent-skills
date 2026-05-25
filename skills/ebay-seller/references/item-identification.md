# Item identification

Goal: derive a clear, sellable item identity from the photo.

## Procedure
1. Analyze the photo with vision: product type, brand, model/variant, color, visible condition, labels/logos/type plate.
2. Verify the exact name + specs via web search (manufacturer page, datasheet).
3. Determine the eBay category and note the category-typical **item specifics** (`artikelmerkmale`, e.g. brand, model, size, material, EAN, condition).
4. If unsure (two plausible models), ask the user SPECIFICALLY instead of guessing.

## Fill into `state.json`
- `artikel.bezeichnung`, `artikel.marke`, `artikel.modell`, `artikel.specs[]`, `artikel.zustand`
- `kategorie`
- `artikelmerkmale{}` as far as possible from photo + research (complete the rest before listing)

## Condition vocabulary (eBay)
Use eBay's German condition labels: Neu · Neu (sonstige) · Generalüberholt · Gebraucht · Für Bastler/defekt. Base the condition honestly on what is visible in the photo.
