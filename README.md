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
| **Level 5 — Optimising** | 91–100 | Framework is self-sustaining, continuously improving, mentoring others. |

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

## License

MIT — see `LICENSE`.