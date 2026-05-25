# Artikel-Erkennung

Ziel: aus dem Foto eine eindeutige, verkaufsfähige Artikelidentität ableiten.

## Vorgehen
1. Foto per Vision auswerten: Produkttyp, Marke, Modell/Variante, Farbe, sichtbarer Zustand, Beschriftungen/Logos/Typenschild.
2. Genaue Bezeichnung + Specs per Websuche verifizieren (Herstellerseite, Datenblatt).
3. eBay-Kategorie bestimmen und die kategorietypischen **Artikelmerkmale** notieren (z. B. Marke, Modell, Größe, Material, EAN, Zustand).
4. Bei Unsicherheit (zwei plausible Modelle) GEZIELT nachfragen statt raten.

## In `state.json` füllen
- `artikel.bezeichnung`, `artikel.marke`, `artikel.modell`, `artikel.specs[]`, `artikel.zustand`
- `kategorie`
- `artikelmerkmale{}` so weit wie aus Foto + Recherche möglich (Rest vor dem Einstellen ergänzen)

## Zustands-Wortschatz (eBay)
Neu · Neu (sonstige) · Generalüberholt · Gebraucht · Für Bastler/defekt. Zustand ehrlich am sichtbaren Foto festmachen.
