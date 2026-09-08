# ANNEX A — SII VERSION 1.0 TECHNICAL BASELINE

This Annex is incorporated as the technical implementation baseline for Part V. It is not a Personhood test and does not create downstream legal eligibility.

## A.1 Assessment pipeline

An SII assessment SHOULD:

1. discover the actual Person-technology configuration;
2. identify Essential Functions supported or mediated;
3. build the dependency graph from function through device, local software, power, authentication, network, remote service, controller and surrounding infrastructure;
4. mark Material Control edges, including realistically exercisable dormant authority;
5. evaluate tested fallback, severability, reversibility and recovery;
6. evaluate failure consequence and cascade;
7. construct the multidimensional profile;
8. apply rule-based tier logic without averaging or additive device scoring;
9. produce an explanation, evidence gaps, confidence and reassessment triggers;
10. require human review for disputed or high-consequence classifications.

## A.2 Multidimensional profile

| Dimension | Meaning |
|---|---|
| FM — Functional Mediation | 0 none → 4 function substantially executed or mediated by synthetic system |
| ND — Network/Remote Dependence | 0 none → 4 continuing Essential Function requires external network/service |
| SA — Software Authority | 0 advisory → 4 software can materially determine availability or operation of Essential Function |
| MC — Material Control Exposure | 0 none → 4 third party/system can initiate, prevent, redirect, terminate or reassign relevant function authority |
| FB — Fallback Assurance | 4 independently tested meaningful fallback → 0 no safe fallback; positive assurance, not risk points |
| RV — Reversibility/Severability | 4 safely reversible/severable → 0 severance threatens continuity or Essential Functions |
| FC — Failure Consequence | 0 inconvenience → 4 life/identity/continuity-critical consequence |
| CX — Cascade/Combination | 0 isolated → 4 one failure/control path propagates across multiple Essential Functions |
| SX — Security Exposure | 0 isolated/physical → 4 remotely reachable/high-authority attack surface |
| CP — Composition Metadata | descriptive biological/synthetic composition where meaningful; never the governing SII score |

## A.3 Tier logic

The operative tier descriptions are stated in Article 24.

## A.4 Dominance and combination rules

1. A life-, identity- or continuity-critical control path cannot be averaged away.
2. Multiple low-tier devices do not automatically produce a higher tier.
3. Combined dependency can justify uplift where it creates a shared control or failure path.
4. Claimed fallback does not reduce dependency without relevant testing.
5. Remote telemetry alone does not create Material Control.
6. Software-only architecture change may trigger reassessment.
7. The tier belongs to a configuration and time, not permanently to the Person.
8. Missing evidence may require SII-Pending.

## A.5 Mandatory assessment output

A material SII report SHOULD contain:

- configuration ID, version and date;
- relevant systems and unmatched components;
- Essential Functions and basis;
- dependency-graph summary;
- decisive control paths;
- SII tier and multidimensional profile;
- evidence grade, confidence and unknowns;
- tested fallback duration and failure envelope;
- Material Control actors;
- reassessment triggers;
- the explicit notice that SII alone MUST NOT decide Personhood, benefits, insurance, employment, healthcare, licensing, citizenship or civic permissions.

---
