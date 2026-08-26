# VOLUME II: CSRA ADMINISTRATIVE AND TECHNICAL STANDARDS

## Chapter 1: Risk-based licensing

- **Regulation 1.1 — License classes:** SII-2 devices require registration when they mediate an Essential Function. SII-3 and SII-4 systems require premarket certification. SII-5 custodial and continuity services require a fiduciary-grade operator license.
- **Regulation 1.2 — Safety case:** Applicants must submit intended use, architecture, threat model, failure modes, clinical or functional evidence, cybersecurity controls, analog-state performance, update policy, and continuity plan.
- **Regulation 1.3 — Material changes:** A change affecting control, cognition, identity, connectivity, or failure severity requires documented impact assessment and, where material, recertification.

## Chapter 2: Firmware and infrastructure assurance

- **Regulation 2.1 — Signed lifecycle:** Executable components and updates must use authenticated provenance, reproducible build records where feasible, staged deployment, rollback, and vulnerability reporting.
- **Regulation 2.2 — Privileged access:** Remote access must be least-privileged, time-limited, strongly authenticated, user-visible except during a lawful covert order, and immutably logged.
- **Regulation 2.3 — Cryptography:** Protected transmissions and stored cognitive data require current, risk-appropriate encryption. Key custody must avoid a single vendor-controlled point of coercion or failure.
- **Regulation 2.4 — Interoperability:** Essential data and configuration must be exportable in a documented format sufficient for migration to a qualified replacement provider.

## Chapter 3: Analog and continuity standards

- **Regulation 3.1 — Analog Fallback State (AFS):** Every SII-2 through SII-4 integration mediating an Essential Function must enter a tested safe local state after network loss, authentication failure, vendor insolvency, or payment dispute.
- **Regulation 3.2 — Performance disclosure:** Providers must state offline duration, degraded functions, consumable dependencies, maintenance intervals, and foreseeable failure conditions in plain language.
- **Regulation 3.3 — Drills:** SII-3 and SII-4 operators must test AFS at least quarterly without exposing the user to unreasonable risk.
- **Regulation 3.4 — SII-5 continuity:** Custodians must maintain portability, tested restoration, fork controls, and a court-accessible continuity escrow that cannot be used to claim ownership.

## Chapter 4: Audits and assessor independence

- **Regulation 4.1 — Audit frequency:** Audit frequency is risk-based: annual by default, quarterly for unresolved high-severity findings, and event-driven after a serious incident or material change.
- **Regulation 4.2 — Assessor independence:** Assessors may not audit systems they designed, hold material financial interests in an auditee, or receive compensation contingent on approval.
- **Regulation 4.3 — User participation:** Audit programs must include confidential reporting and representative participation by affected biological and synthetic persons.
- **Regulation 4.4 — Findings:** Reports shall distinguish critical, major, and minor findings; state evidence and uncertainty; prescribe cure periods; and publish a non-confidential summary.

## Chapter 5: Enforcement and penalties

- **Regulation 5.1 — Corrective ladder:** The CSRA may issue guidance, remediation orders, monitored probation, administrative penalties, suspension, or revocation according to severity, duration, culpability, cooperation, recurrence, and ability to pay.
- **Regulation 5.2 — Turnover penalties:** For a serious corporate violation, the maximum administrative penalty is the greater of a fixed statutory amount or 2% of relevant global annual turnover; for intentional or repeated violations causing grave harm, 6%.
- **Regulation 5.3 — Individual referral:** Criminal referral requires evidence supporting each offense and individual mental state. Administrative noncompliance alone does not establish guilt.
- **Regulation 5.4 — Remediation fund:** Penalties prioritize victim restoration, continuity migration, and independent monitoring rather than becoming general revenue.

