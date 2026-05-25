# Login (eBay.de)

## Standard: manueller Login (plattformunabhängig, keine Installation)
1. Prüfen, ob der User in Chrome bei eBay eingeloggt ist (Signed-in-Indikator im Header).
2. Wenn nicht: den User bitten, sich **selbst in Chrome bei eBay einzuloggen**, dann fortfahren.
3. Bei 2FA / Geräte-Verifizierung / Captcha: anhalten, der User erledigt es, dann weiter.

Das ist der empfohlene Weg — funktioniert auf macOS und Windows, ohne Passwort im Chat und ohne Setup.

## Sicherheit (nicht verhandelbar)
- Niemals ein Passwort abfragen, anzeigen, loggen oder in `config.json`/`state.json` schreiben.
- Anmeldung immer durch den User selbst.

## Optional (nur macOS): Auto-Login via Keychain
Wer mag, kann das Passwort einmalig im macOS-Keychain hinterlegen, damit der Skill Benutzernamen + Passwort beim Login einträgt:

    security add-generic-password -s ebay-seller -a "<benutzername>" -w   # einmalig, durch den User
    security find-generic-password -s ebay-seller -a "<benutzername>" -w  # Abruf zur Laufzeit

`ebay_benutzername` dann in `config.json`. Bei 2FA/Captcha trotzdem anhalten. Auf Windows nicht verfügbar — dort den manuellen Login nutzen.
