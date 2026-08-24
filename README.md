# dea-catalog-maturity-models

Enterprise Architecture Maturity Models — five-level progression framework for assessing and advancing EA capability across domains.

---

## Overview

This catalog defines **maturity models** for Enterprise Architecture practice. Each model describes five levels of capability progression, from *Ad Hoc* through *Optimising*, with defined exit criteria per level.

The catalog is part of the [DEA framework](https://github.com/technehub-labs/dea-metamodel). It is consumed by:

- **dea-catalog-assessment-tools** — assessment instruments map results to maturity levels
- **dea-cli** — `dea maturity score` reports organisational maturity across domains
- **dea-web-viewer** — visualises maturity radar charts per domain

---

## Maturity Bands (uniform across all domains)

| Band | Score | Description |
|------|-------|-------------|
| **Level 1 — Ad Hoc** | 0–25 | EA practices are informal, person-dependent. No shared framework. |
| **Level 2 — Defined** | 26–50 | Core entities and patterns are documented but not consistently enforced. |
| **Level 3 — Managed** | 51–75 | Architecture framework is formal, tooling-enabled, governance active. |
| **Level 4 — Quantitatively Managed** | 76–90 | Metrics-driven decision-making, predictable delivery, mature review. |
| **Level 5 — Self-Optimized** | 91–100 | Framework is self-sustaining, continuously improving, mentoring others. |

> **Band names are subject to an open proposal** ([PR #1](https://github.com/Assessment-Models/dea-catalog-maturity-models/pull/1) — `docs/maturity-scoring-v2-proposal`): renames to *Emergent / Structured / Systematic / Adaptive / Self-Optimising*, non-linear bands (20/25/25/18/12), and per-level `effort_multiplier` coefficients. **That PR stays open** until [CR-AM-01](change-requests/CR-AM-01-xref.md) Release 1 begins. The two converge at that point; this PR does not pre-empt that decision.

---

## Catalog Index

The catalog is the canonical registry of all maturity models and their versions.

| Model | Domain | Path | Status |
|-------|--------|------|--------|
| EA Capability | Overall EA practice | `maturity-models/v1-alpha/ea-capability.yaml` | draft |
| Architecture Modernization | Modernisation programmes | `maturity-models/v1-alpha/modernization.yaml` | draft |
| Technology | Tech stack fitness, debt, lifecycle | `maturity-models/v1-alpha/technology.yaml` | draft |
| Operations | Ops, incident response, SRE | `maturity-models/v1-alpha/operations.yaml` | draft |
| Services Delivery | Time-to-market, outcomes | `maturity-models/v1-alpha/services-delivery.yaml` | draft |

---

## Model Schema

Each model file follows:

```yaml
id:                  dea:maturity-<domain>
name:                <Human name>
domain:              <Domain>
version:             "1.0.0-alpha"
metamodel_version:   "^0.1.0"
description:         <one-line summary>
owner:               <role responsible for updates>

levels:
  - id:               level-1
    name:             Ad Hoc
    score_range:      [0, 25]
    characteristics:  <what is true at this level>
    exit_criteria:    <what must be true to leave this level>
    evidence:
      - <observable evidence of being at this level>

  # ... levels 2-5

relationships:
  - source_id: dea:maturity-<domain>
    target_id: dea:catalog-assessment-<domain>
    relationship_type: scored-by
    description: Assessment results are mapped to maturity levels
```

---

## Cross-References

Maturity models are related to:

- **dea-catalog-assessment-tools** — assessments produce scores that map to levels
- **dea-metamodel** — `ReferenceModel` and `Metric` entity types underpin the catalog
- **dea-catalog-reference-architecture** — DERA Phase 4 governance activation uses maturity scores

---

## Versioning

This catalog follows [Semantic Versioning](https://semver.org/):

- **MAJOR** — level definitions change (e.g., new band added)
- **MINOR** — new domain model added
- **PATCH** — clarifications, corrections, additional evidence examples

---

## Contributing

See `CONTRIBUTING.md`. Each domain model requires an owner; submit PR with model file and CI will validate the schema.

---

## Maturity Model Independence

Maturity Models in this catalog are **independent reusable interpretation models**, not coupled outputs of any single assessment.

Today the relationship is:

```
Assessment → Score → Maturity
```

Under [CR-AM-01](change-requests/CR-AM-01-xref.md) (OpenDEA Assessment Metamodel Evolution, accepted as authoritative reference), the relationship evolves to:

```
Assessment → AssessmentResult → interpreted-by → MaturityModel
```

This means:

- One assessment result can be interpreted using more than one compatible maturity model (CR-AM-01 AC-04).
- Maturity models can be referenced by capability assessments, scenario assessments, and benchmark models alike — not only by domain-rubric instruments.
- The four-domain taxonomy (EA / Modernization / Technology / Operations / Services Delivery) remains valid as organisational metadata. It is not the upper-level ontology.
- `maturity_target` continues to validate as a backward-compatible shorthand.

**No file in this catalog needs to change to participate in this evolution.** The YAML models in `maturity-models/v1-alpha/` remain valid as-is. New interpretations may *reference* these models from many places.

The first concrete pilot under CR-AM-01 is the **Technology Assessment migration** (Phase 3), which will eventually consume `dea:maturity-technology` from this catalog alongside new `assessment_model`, `capabilities`, `scenarios`, `measures`, and `evidence` blocks. That pilot lands in a separate PR.

### CR rationale table

| CR | Why | Consequence |
|----|-----|-------------|
| [CR-AM-01-xref](change-requests/CR-AM-01-xref.md) | Current architecture couples Assessment → Maturity, preventing capability reuse and scenario-based benchmarking. | Maturity Models in this catalog become optional, reusable interpretation layers over Assessment Results. No existing model is invalidated; the four-domain structure stays valid as organisational metadata. |

### What is **not** changing in this PR

- No change to any YAML file under `maturity-models/v1-alpha/`.
- No change to `maturity-models/index.yaml`.
- No change to band names, score ranges, level definitions, or exit criteria.
- No change to the `scored-by` / `produces-score-for` relationship strings (they remain valid; controlled vocabulary arrives in CR-AM-01 Phase 4).
- PR #1 (`docs/maturity-scoring-v2-proposal`) stays open and is resolved separately.

### Parking lot

- **PR #1 — non-linear bands + renames + effort coefficients.** Stays open until CR-AM-01 Release 1.
- **DMM-01 levels** (Discrete / Converged / Composable / Cognitive / Autonomous). Parked, not deleted. Resurfaces as input to a Capability Model in CR-AM-01 Phase 5, not a maturity ladder.

---

## License

MIT — see `LICENSE`.
