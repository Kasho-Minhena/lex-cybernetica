# PUB-WEB-01 — Final Test Report

Date: 6 September 2026
Release candidate: Website v1.0

## SDET complete pass 1
- 22/22 automated tests passed.
- Static CI checker passed.
- JavaScript syntax check passed.

## SDET complete pass 2
- 22/22 automated tests passed.
- Static CI checker passed.
- JavaScript syntax check passed.

## Automated bug / adversarial testing
- 9/9 dedicated adversarial/security tests passed.
- Mutation guard correctly rejected:
  - javascript: URL injection
  - localhost/private-host leakage
  - broken internal navigation
- 24 viewport renders passed: 8 pages × mobile/tablet/desktop.
- No horizontal overflow detected at 390, 768 or 1440 CSS pixels.
- Mobile/tablet menu ARIA state and Escape-key close behaviour passed.

## Verified constraints
- No paid backend.
- No database.
- No trackers/analytics.
- No cookies.
- No user-data collection form.
- No remote JavaScript.
- No private Lex Studio infrastructure exposed.
- All public external links are HTTPS and hardened when opened in a new tab.
- Legal-status notice is present on every page.

Result: PASS

## RC2 regression after desktop hero refinement
- SDET complete pass 1: 22/22 tests passed.
- SDET complete pass 2: 22/22 tests passed.
- Dedicated adversarial/security suite: 9/9 passed.
- Static CI checker: PASS.
- JavaScript syntax check: PASS.
- Human visual recheck at 100% browser zoom is required before production deployment.
