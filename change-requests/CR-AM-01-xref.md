# CR-AM-01 — Cross-Reference (maturity-models)

> This is **not** the full CR. The authoritative CR file lives in the assessment-tools repo:
> https://github.com/Assessment-Models/dea-catalog-assessment-tools/blob/main/change-requests/CR-AM-01.md
>
> This cross-reference exists so that `dea-catalog-maturity-models` has a stable pointer, and so that the items in CR-AM-01 that affect *this* repo are easy to find without re-reading 1870 lines.

## TL;DR

CR-AM-01 ("OpenDEA Assessment Metamodel Evolution") lands as authoritative reference material in the **primary repo** `Assessment-Models/dea-catalog-assessment-tools`. It establishes an 8-phase, 4-release roadmap that **decouples Maturity Model from Assessment** (today they are tightly coupled via the `maturity_target` / `produces-score-for` relationship pair).

For this repo, the practical consequences are:

| When | What changes in this repo |
|------|---------------------------|
| Phase 1 — Metamodel Foundation | New metamodel entity `MaturityModel` becomes formally defined as an *optional interpretation* layer. No code change here. |
| Phase 4 — Decouple Maturity | `maturity_target` continues to validate; treated as shorthand for `interpretation.maturity_models[*]`. Backward-compat alias. |
| Phase 5+ — Capability Catalog | New `dea-catalog-capability-models` repo (created only when content justifies it). Capabilities reference maturity levels, not vice versa. |
| Any future PR | Controlled relationship vocabulary replaces free-form `relationship_type` strings; `produces-score-for` becomes an alias for `interpreted-by`. |

## What CR-AM-01 says about this repo (relevant sections)

| CR-AM-01 section | Topic | What it means for `dea-catalog-maturity-models` |
|------------------|-------|------------------------------------------------|
| §1 (Executive Summary) | Architecture separates Maturity Model from Assessment Result | Maturity Model is no longer the *terminal* output of an Assessment; it is one *interpretation* of a Result. |
| §3.1 (Problem: Assessment coupled to maturity) | The `maturity_target` requirement is inappropriate for capability-only assessments | This repo stays valid as-is; the coupling is relaxed upstream. |
| §13 (Maturity Model) | Relationship evolves from `Assessment → Maturity` to `AssessmentResult → interpreted-by → MaturityModel` | The 5 YAML models in `maturity-models/v1-alpha/` continue to exist and validate; their `relationships` blocks need no change in this PR. |
| §17 (Required Relationship Model) | Controlled vocabulary: `interpreted-by`, `eligible-for`, `compatible-with`, etc. | The existing `produces-score-for` and `scored-by` relationship strings are accepted as legacy aliases (see §20). |
| §20 (Backward Compatibility) | Existing instruments, models, and relationship strings remain supported | **No existing file in this repo needs to change for backward compat.** |
| §25 (Comparability Contract) | Models declare `maturity_compatible: true/false` per version | Future versions of the YAML models in this repo may declare compatibility blocks. Out of scope for this PR. |
| §45 (Acceptance Criteria) | AC-04: One assessment result can be interpreted using more than one compatible maturity model | This capability lands upstream; this repo remains a reusable library of maturity models consumable by many assessments. |
| §56 (Final Recommendation) | Technology Assessment is the pilot | The pilot will eventually reference one of the maturity models in this repo (likely `dea:maturity-technology`). |

## Parked items affecting this repo

- **PR #1 (`docs/maturity-scoring-v2-proposal`)** — non-linear band scheme, renames (Emergent / Structured / Systematic / Adaptive / Self-Optimising), and per-level effort coefficients. **Stays open** until CR-AM-01 Release 1 begins. Decision at that point: fold the proposal into CR-AM-01 Release 1 as v2 of the maturity-model bands, or close superseded.
- **DMM-01 levels** (Discrete / Converged / Composable / Cognitive / Autonomous) — proposed earlier in this thread as a separate maturity ladder. **Parked, not deleted, not promoted.** Will resurface as input to a Capability Model (not a maturity ladder) when `dea-catalog-capability-models` lands in CR-AM-01 Phase 5.

## What this PR does NOT do

- No change to any YAML file under `maturity-models/v1-alpha/`.
- No change to `maturity-models/index.yaml`.
- No change to the band names or score ranges (those are the open question deferred to PR #1 closure).
- No change to the relationship types declared in existing files (`scored-by`, `produces-score-for` continue to be valid).

## What this PR DOES do

- Adds `change-requests/CR-AM-01-xref.md` (this file) — the cross-reference.
- Adds `change-requests/README.md` — CR index for this repo.
- Updates `README.md` with a "Maturity Model Independence" section + pointer to the cross-reference.
- Updates `CHANGELOG.md` with an `[Unreleased]` entry.

## When this repo's schemas actually change

The first actual schema change in this repo lands as part of **CR-AM-01 Phase 4** (Decouple Maturity). That PR will:
- Mark `maturity_target` as deprecated on the consumer side (assessment-tools); this repo stays unchanged.
- Optionally introduce `interpretation: { maturity_models: [...] }` block as a richer alternative for those who want it.
- Optionally add a `compatibility:` block to maturity-model YAML files.

None of that is in scope for this cross-reference PR.

---

**Full CR (authoritative):** https://github.com/Assessment-Models/dea-catalog-assessment-tools/blob/main/change-requests/CR-AM-01.md
**Companion rationale:** https://github.com/Assessment-Models/dea-catalog-assessment-tools/blob/main/docs/rationale/CR-AM-01-companion-rationale.md
**Decision-point index:** https://github.com/Assessment-Models/dea-catalog-assessment-tools/blob/main/docs/rationale/CR-AM-01-decision-points.md