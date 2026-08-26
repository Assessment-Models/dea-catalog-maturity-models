# Migration — v1-alpha catalog to federated v2-canonical ecosystem

> **Status:** legacy. This catalog is preserved as reference content.

## Supersession

The maturity models in this repository were authored against the v1-alpha
scoring scheme (linear 0–25 / 26–50 / 51–75 / 76–90 / 91–100 bands,
CMMI-era level naming). They predate the v2 maturity architecture
(CR-AM-09 §17 — non-linear Emergent / Structured / Systematic / Adaptive
/ Self-Optimising bands with superlinear effort multipliers) and are
therefore **not** a target consumer for the federated contract suite.

The canonical migration plan lives at:

**`technehub-labs/dea-metamodel/assessment-models/governance/legacy-migration-plan.md`**

That document captures both Plan A (fold v2 in — port each model to
v2-canonical) and Plan B (freeze as legacy — register with `superseded_by`
in the assessment-registry). The decision itself is deferred to
**CR-AM-01 Release 1**.

## What consumers should do

1. Check the **status** of any asset registered in
   `Assessment-Models/assessment-registry`. Records with
   `status: legacy` (including this catalog) are exempt from the six
   §16 contract families by design (CR-AM-11 Phase 6 legacy handling).
2. Route to the **canonical replacement**:
   - maturity models → `technehub-labs/dea-metamodel/assessment-models/maturity/`
     for v2-canonical scales, evaluation models, and benchmark baselines
   - components → `technehub-labs/dea-metamodel/assessment-models/maturity/components/registry.yaml`
     for the canonical registry (CR-AM-11 Phase 5)
   - composite patterns → the Digital Transformation reference model at
     [`Assessment-Models/maturity-model-digital-transformation`](https://github.com/Assessment-Models/maturity-model-digital-transformation)
3. Until CR-AM-01 Release 1, the catalog stays **read-only** under its
   current commit pin
   (`fa2f9d57b75227a65d052fa13f426171c1cd295c`); no edits, no new
   releases.

## Open questions for Release 1

- **Plan A vs Plan B** — see the migration plan doc.
- **Consumer mapping** — who currently uses each v1-alpha model and how
  do they migrate.
- **Archival commit** for Plan A, or a `superseded_by` registry field
  for Plan B.

---
*Established under [CR-AM-11 — Federated Assessment Model Ecosystem](https://github.com/technehub-labs/dea-metamodel/blob/main/change-requests/CR-AM-11.md) Phase 6.*