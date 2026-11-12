# Extraction checklist — `maturity-model-autonomous-operations`

Phase-6 (CR-AM-11 §26/§31) migration of this bundle from the catalog into its own
repository. The bundle is already shaped like a model-per-repo asset, so extraction
is a lift-and-repoint, not a rewrite. Repositories are created through org
governance — contributors do not create repos; this checklist starts once the repo
exists.

| Phase | Step | Action for this model | Done |
|-------|------|------------------------|------|
| IDENTIFY | Locate asset | `dea:maturity-autonomous-operations`; catalog entry `maturity-models/v1-alpha/autonomous-operations.yaml` + this bundle `maturity-models/autonomous-operations/` (merged via PR #5, commit `1a48038`) | ☑ |
| CLASSIFY | Type & class | `type: maturity-model`, `asset_class: assessment`; registry record `maturity-model-autonomous-operations` (see REGISTER) | ☑ |
| EXTRACT | Create repo & lift bundle | Create `Assessment-Models/maturity-model-autonomous-operations` via org governance; copy this bundle **verbatim** to repo root (`model.yaml`, `scale.yaml`, `evaluation.yaml`, `dimensions.yaml`, `examples/`, `scripts/`, `README.md`, `GOVERNANCE.md`, `EXTRACTION-CHECKLIST.md`); keep `id: dea:maturity-autonomous-operations` stable | ☐ |
| NORMALIZE | Contract conformance | Add `conformance:` + `compatibility:` blocks to `model.yaml` (contracts: `maturity-scale-contract`, `maturity-model-contract`, `conformance-contract` ^1.0, per the `maturity-model-digital-transformation` example); add `.github/workflows/` calling the reusable workflows in `Assessment-Models/assessment-ci` (`contract-conformance.yml`, `local-model-ci.yml`) | ☐ |
| VALIDATE | Three CI levels | Level 1: `python3 scripts/local_validate.py` in the new repo (extend it to validate `model.yaml` conformance blocks); Level 2: contract conformance via assessment-ci; Level 3: registry resolution (`resolve.py maturity-model-autonomous-operations --check` must verify the new repo's tag) | ☐ |
| REGISTER | Repoint registry record | In `assessment-registry`: update `registry/maturity-models/maturity-model-autonomous-operations.yaml` → `source.repository: maturity-model-autonomous-operations`, `release.reference`: new repo's `vX.Y.Z` tag (immutable), bump `release.version`; keep `status: active`; run `scripts/validate_registry.py` | ☐ |
| RELEASE | Cut release & supersede catalog copy | Tag `v1.0.0` (promote from `1.0.0-alpha`) in the new repo; CHANGELOG entry; in the catalog, mark `maturity-models/v1-alpha/autonomous-operations.yaml` with `superseded_by` → new repo + registry id (CR-AR-05 pattern), set catalog content entry status accordingly; archive the bundle dir or convert it to a pointer README | ☐ |

## Notes

- Scoring/levels content must not change during extraction (identity is
  `(model, scale, level)`; never normalised across models). Only packaging,
  conformance metadata and references move.
- The catalog CI (`Validate Maturity Models`) keeps validating the catalog entry
  until the supersession commit; after that the entry is a pointer, not content.
- Open questions from `proposals/0002` §7 (weights, gate scope, v2 band timing)
  should be resolved in the new repo, not during the lift.
