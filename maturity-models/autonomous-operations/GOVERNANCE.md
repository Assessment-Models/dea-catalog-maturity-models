# Governance — how this model stays governed inside the org

1. **Catalog registration** — the CI-validated entry is
   `maturity-models/v1-alpha/autonomous-operations.yaml` in
   `dea-catalog-maturity-models`, listed in `maturity-models/index.yaml` (`content:`,
   `relationships:`, tags). Catalog versioning is semver; adding/changing a domain model
   is a MINOR bump.
2. **Model-per-repo extraction** — this bundle (`maturity-models/autonomous-operations/`)
   is lifted verbatim into a dedicated repo `maturity-model-autonomous-operations`
   (created via org governance, per the CR-AM-11 §26/§31 pattern exemplified by
   `maturity-model-digital-transformation`). On extraction: keep `id:
   dea:maturity-autonomous-operations` stable; add the repo to
   `assessment-registry` (`registry/maturity-models/`) per the registration schema;
   enable the reusable conformance workflows from `Assessment-Models/assessment-ci`.
3. **CI** — while in the catalog, `.github/workflows/ci.yml` (`Validate Maturity Models`)
   validates the entry (schema + exactly 5 levels + per-level fields). The bundle is
   additionally checked by `scripts/local_validate.py`, which also verifies the split
   files (`model/scale/evaluation/dimensions.yaml`) are consistent with the catalog entry.
4. **Change control** — model changes go through a PR with rationale and a CHANGELOG entry
   (semver: MAJOR = level/band definition change, MINOR = new dimension/criteria, PATCH =
   clarifications/evidence). Cross-repo impacts are tracked as change requests in
   `change-requests/` (CR-MM series) per the CR convention (`land-as-authored`, xref files
   for CRs owned elsewhere).
5. **Relationships** — declared in `model.yaml` `relationships:` (instance-of catalog,
   scored-by assessment-tools, extends operations, harvested-from source workbook,
   references OODA closed-loop model). Use controlled vocabulary types; legacy aliases
   (`scored-by`, `produces-score-for`) remain valid per CR-AM-01 §20.
6. **Comparability** — level `id`/`name`/`score_range` always match the catalog's
   canonical bands; AO stage names are additive metadata (`ao_stage`), never replacing
   canonical names, so scores stay comparable across models (CR-AM-01 §25).
