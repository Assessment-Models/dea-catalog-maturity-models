# Changelog — dea:maturity-autonomous-operations

Model-level changelog for the Autonomous Operations bundle (catalog entry:
`maturity-models/v1-alpha/autonomous-operations.yaml` in dea-catalog-maturity-models).

## [1.0.0-alpha] — 2026-11-12
### Added
- Initial model harvested & cleaned from an industry AO maturity workbook v1.8.0
  (6 dimensions / 32 sub-dimensions / 151 criteria → 157 after merge/rename/gap-fill),
  with full provenance (source md5, dropped duplicates, renames) in `model.yaml`.
- 5-level scale on the canonical catalog bands + AO stages
  (Manual & Reactive → Instrumented & Assisted → Closed-Loop Automated →
  Goal-Driven Autonomy → Self-Improving Ecosystem) with OODA progression per level (`scale.yaml`).
- Evaluation contract: AO Autonomy Index 0–100, dimension weight profiles
  (default, comms-provider), weakest-link gate on in-scope gating criteria,
  effort-adjusted value (proposal 0001 metadata), assessment method with
  evidence pack / assessor independence / confidence (`evaluation.yaml`).
- Assessment questionnaire covering all 157 criteria (`assessment-questionnaire.yaml`).
- Examples: worked assessment with gate (`examples/assessment-example.yaml`),
  weight-profile benchmark (`examples/benchmark-weight-profiles.yaml`).
- `scripts/local_validate.py` (schema, levels, bands, weights+profiles, OODA ladder,
  questionnaire coverage, hygiene scan).
- `EXTRACTION-CHECKLIST.md` (Phase-6 model-per-repo migration), `GOVERNANCE.md`.
- Gap register with sources: `proposals/0002` in the catalog repo; `decisions` block
  resolving its open questions.
