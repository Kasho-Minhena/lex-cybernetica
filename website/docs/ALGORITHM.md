# Lex-Cybernetica Public Website v1.0 — Algorithm / Behaviour Design

Status: ALGORITHM DESIGNER APPROVED FOR ENGINEERING

## A. Build algorithm
1. Read canonical public metadata from the existing Lex-Cybernetica repository.
2. Map canonical concepts to seven website routes without copying the full book.
3. Generate a common semantic shell: skip link, header/nav, main, footer.
4. Render route-specific content and calls to authoritative public records.
5. Mark unverified external destinations as configuration items and block them from release until resolved.
6. Generate discovery files: 404, robots, sitemap, CNAME.
7. Run structural, link, accessibility, metadata, responsive and security checks.
8. Permit release only if every mandatory gate passes.

## B. Navigation algorithm
- Desktop: visible primary navigation for the seven routes.
- Mobile: one menu button controls one navigation panel.
- JS enhancement only; links remain usable when JavaScript is disabled.
- Current page gets aria-current=page.
- Escape/outside selection closes menu; focus remains predictable.

## C. Page-content mapping
Home:
- Project proposition.
- Consultation status.
- Four-surface public ecosystem explanation.
- Key research areas.
- Primary pathways: Explore Framework / Read Publication / Participate.

Framework:
- Explain 11-part framework and annexes using the canonical table of contents.
- Present thematic clusters, not full legal text.

Research:
- Explain research questions, doctrine development, consultation, evidence/review boundaries.
- Clearly distinguish public research from private Lex Studio operations.

Publications:
- Version 2.0.0 card with date/status.
- Links to GitHub release, GitBook, Zenodo DOI and downloadable formats only when verified.

Cases & Future Law:
- Explain prospective cases/scenarios as analytical tools, not legal advice or predictions of enacted law.
- v1 may ship with methodology and “case programme” structure even before case catalogue is populated.

About:
- Explain purpose, authorship and legal status.
- Do not claim affiliations or endorsements not in canonical records.

Contact / Participate:
- Explain categories of participation: legal review, ethics/bioethics, AI/cybernetics, medicine, governance, philosophy, public comment.
- v1 stores no submissions; route users to approved public contact destination.

## D. External-link resolution
Known authoritative GitHub repository:
https://github.com/Kasho-Minhena/lex-cybernetica

Known GitHub v2.0.0 release:
https://github.com/Kasho-Minhena/lex-cybernetica/releases/tag/v2.0.0

GitBook, Zenodo DOI and LinkedIn destinations:
- Resolve and verify before release.
- Never infer or manufacture URLs.

## E. Failure handling
- Unknown route -> custom 404 with safe navigation home.
- Missing optional public destination -> hide/disable CTA rather than link to an unverified target.
- JavaScript failure -> all content and ordinary navigation still function.
- CSS failure -> semantic reading order remains usable.

## F. Acceptance conditions
- All seven routes load from static hosting.
- No broken internal links.
- No private Lex Studio reference exposing location, API, repository, credential, internal workflow, or research data.
- No unverified legal claim, DOI, ISBN, endorsement, or status.
- WCAG-oriented keyboard/focus/contrast checks pass.
- 320px, 768px, 1024px, 1440px layouts remain readable without horizontal overflow.
- Lighthouse-compatible static architecture; no render-blocking third-party scripts.
- Production release only after mandatory process gates.
