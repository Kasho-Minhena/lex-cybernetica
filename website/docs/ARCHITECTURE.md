# Lex-Cybernetica Public Website v1.0 — Architecture

Status: ARCHITECT APPROVED FOR IMPLEMENTATION
Project: PUB-WEB-01
Canonical name: Lex-Cybernetica
Primary domain: https://lex-cybernetica.com

## Purpose
The website is the public front door to Lex-Cybernetica. It introduces the framework, explains the research programme, points readers to authoritative publication records, and invites structured participation without duplicating the full GitBook.

## Public-system boundary
- Website: orientation, discovery, public communication.
- GitBook: structured book/framework reading surface.
- GitHub: version/source and release record.
- Zenodo: permanent publication/archive record.
- Lex Studio: private research/development system; never linked to internal endpoints, data, or private materials.

## Runtime architecture
- Static site only: HTML5 + CSS + minimal vanilla JavaScript.
- No database, server runtime, cookies, analytics, user accounts, or paid backend in v1.
- Deploy target: GitHub Pages, zero hosting cost.
- Custom domain: lex-cybernetica.com.
- DNS remains at Spaceship; GitHub Pages records added only at release gate.
- HTTPS via GitHub Pages certificate.

## Source layout
website/
  index.html
  framework.html
  research.html
  publications.html
  cases.html
  about.html
  participate.html
  404.html
  assets/css/site.css
  assets/js/site.js
  assets/img/*
  CNAME
  robots.txt
  sitemap.xml
  docs/*              # repository-only engineering records; excluded from Pages artifact
  tests/*             # repository-only QA/CI; excluded from Pages artifact

## Information architecture
1. Home
2. Framework
3. Research
4. Publications
5. Cases & Future Law
6. About
7. Contact / Participate

## Design system
- Scholarly, forward-looking, institutional; not a generic tech startup aesthetic.
- High-contrast typography, generous whitespace, restrained motion.
- Responsive from 320px upward.
- Semantic HTML landmarks and keyboard-accessible navigation.
- Respect prefers-reduced-motion.
- No external font dependency in v1; system font stack for privacy/performance.

## Content rules
- Canonical project name is always “Lex-Cybernetica”.
- Version 2.0.0 is described as a Consultation Draft / Working Legal Framework.
- Never describe the framework as enacted law.
- Preserve All Rights Reserved and legal-status notices.
- GitBook/GitHub/Zenodo are authoritative external surfaces; website summaries do not supersede them.
- No unverified DOI, ISBN, GitBook URL, LinkedIn URL, or institutional endorsement may be invented.

## Security/privacy baseline
- No forms posting personal data to a backend in v1.
- Participation links use explicit external destinations or mailto only after owner approval.
- No third-party scripts, trackers, ad pixels, embedded social widgets, or remote JavaScript.
- Rel=noopener on external new-tab links.
- Content Security Policy compatible with a static site.
- Referrer policy: strict-origin-when-cross-origin.
- Permissions policy disables unused browser capabilities.

## SEO/discovery baseline
- Unique title/description for each page.
- Canonical URLs on lex-cybernetica.com.
- Open Graph metadata.
- robots.txt and sitemap.xml.
- Schema.org ScholarlyArticle/CreativeWork metadata on publication surfaces where accurate.

## Release gates
No production DNS or main-branch release until:
1. Algorithm design approved.
2. Three independent engineering passes complete.
3. SDET complete test pass 1.
4. SDET complete test pass 2.
5. Automated accessibility/link/security/adversarial checks pass.
6. CTO release review approves.
