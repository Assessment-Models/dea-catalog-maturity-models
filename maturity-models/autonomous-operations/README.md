# Autonomous Operations Maturity Model — asset bundle

> **SUPERSEDED / POINTER** — the canonical home of this model is now
> `Assessment-Models/maturity-model-autonomous-operations` @ `4c6d865` (v1.0.1, canonical v2 bands,
> L-0..L-4 scale). This bundle is retained as the frozen v1-alpha lineage and provenance record.
> Reconciliation report: `docs/RECONCILIATION.md` in the canonical repo.

Self-contained, repo-ready package for **`dea:maturity-autonomous-operations`**
(Autonomous Operations Maturity & Assessment Model, v1.0.0-alpha).

This directory is the contained space for all of the model's assets. Per the org's
model-per-repo convention (CR-AM-11 §26/§31, as in `maturity-model-digital-transformation`),
this bundle is designed to be lifted **verbatim** into a dedicated repository
`Assessment-Models/maturity-model-autonomous-operations` when that repo is created
(repositories are created through org governance, not by contributors). Until then it
lives here and is registered in the catalog at
`maturity-models/v1-alpha/autonomous-operations.yaml` (the CI-validated catalog entry).

## Layout (mirrors the model-per-repo convention)

| File | Contents |
|------|----------|
| `model.yaml` | Core registration: id, name, domain, version, description, owner, provenance, relationships, tags |
| `scale.yaml` | The 5-level scale: canonical org bands (`band-1..band-5` from the catalog `index.yaml`) + ambitious AO stages + OODA closed-loop progression per level + scoring metadata (level points, effort multipliers) |
| `evaluation.yaml` | Evaluation contract: AO Autonomy Index aggregation, weakest-link gate, effort-adjusted value, and the assessment method (inputs, steps, assessor independence, confidence, cadence) |
| `dimensions.yaml` | The harvested, cleaned, gap-filled structure: 6 dimensions / 32 sub-dimensions / 157 criteria |
| `assessment-questionnaire.yaml` | Assessment instrument: one entry per criterion (157), evidence-to-request per dimension, level anchors, gating flags |
| `examples/` | Worked assessment example (`assessment-example.yaml`) + weight-profile benchmark (`benchmark-weight-profiles.yaml`) |
| `scripts/local_validate.py` | Local validation (schema, 5 levels, unique IDs/names, bands, weights + profile sums, questionnaire coverage) — run before any PR |
| `GOVERNANCE.md` | How this model stays governed inside the org (catalog, registry, CI, change requests) |
| `CHANGELOG.md` | Model-level changelog (semver) |

## Level stages (canonical band → AO stage)

| Band (catalog `index.yaml`) | Canonical level | Score range | AO stage | Loop driver |
|---|---|---|---|---|
| band-1 | Ad Hoc | 0–25 | **Manual & Reactive** | none — open loop, humans react |
| band-2 | Defined | 26–50 | **Instrumented & Assisted** | human-set goals; machines monitor & recommend |
| band-3 | Managed | 51–75 | **Closed-Loop Automated** | human-set goals/SLOs drive the automated loop |
| band-4 | Quantitatively Managed | 76–90 | **Goal-Driven Autonomy** | intent/goals drive the loop; system owns Observe–Orient–Decide–Act within guardrails |
| band-5 | Optimising | 91–100 | **Self-Improving Ecosystem** | intent/goals negotiated ecosystem-wide drive self-learning loops |

Progression axis per level is the **OODA closed loop** (Observe–Orient–Decide–Act):
`levels[].progression.ooda` says who performs each OODA stage (human / system-assisted /
system / system-within-rules / system-learning), and `loop_driver` states how intent/goals
drive the loop. `loop_closure` goes open → partial → closed → closed autonomous →
self-learning. See `scale.yaml` for the full definitions.

## Scoring in one paragraph

Score each criterion by achieved level (L0 absent=0, L1=20 … L5=100) → dimension score =
mean of its criteria → **AO Autonomy Index** = weighted mean of dimension scores
(strategy .20, operations .20, technology .20, data .15, party .15, culture .10) →
band through the catalog bands → org level, **capped by the weakest-link gate** on the
closed-loop spine criteria (4.1.1–4.1.4). Effort multipliers (1.0/1.5/2.5/4.0/6.0) yield
the effort-adjusted value so diminishing returns are explicit (proposal 0001).

## Validate

```bash
python3 scripts/local_validate.py        # from this directory
```

Org CI (schema + level coverage) runs on the catalog entry; on extraction to a
model-per-repo repository, the reusable workflows in `Assessment-Models/assessment-ci`
apply (see GOVERNANCE.md).
