# Login (eBay.de)

## Default: manual login (cross-platform, no installation)
1. Check whether the user is logged in to eBay in Chrome (signed-in indicator in the header).
2. If not: ask the user to **log in to eBay in Chrome themselves**, then continue.
3. On 2FA / device verification / captcha: stop, the user handles it, then continue.

This is the recommended path — works on macOS and Windows, without a password in chat and without setup.

## Security (non-negotiable)
- Never ask for, display, log, or write a password into `config.json`/`state.json`.
- Sign-in is always done by the user.

## Optional (macOS only): auto-login via Keychain
If desired, the password can be stored once in the macOS Keychain so the skill fills username + password at login:

    security add-generic-password -s ebay-seller -a "<username>" -w   # once, by the user
    security find-generic-password -s ebay-seller -a "<username>" -w  # retrieve at runtime

Set `ebay_benutzername` in `config.json`. Still stop on 2FA/captcha. Not available on Windows — use the manual login there.
