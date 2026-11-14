# Proposal 0004 — CR-AM-12 reconciled: review, current-state cross-reflection, and implementation plan

| Field | Value |
|-------|-------|
| Status | PROPOSED (reconciled review of the CR-AM-12 draft) |
| Date | 2026-11-12 |
| Reviews | CR-AM-12 draft "Standardized Maturity Model Repository Architecture, Documentation and Enrichment" |
| Cross-references | CR-AM-11 (§8 taxonomy, §22 manifest, §26/§31 model-per-repo), CR-AM-01 (metamodel decoupling), org `.github/GOVERNANCE.md`, `assessment-registry`, `assessment-ci`, `maturity-model-autonomous-operations` (reference implementation), `maturity-model-digital-transformation` |
| Scope | This proposal reconciles the CR-AM-12 draft against the current ecosystem state and defines tranches + acceptance criteria. It changes no model content. |

---

## 1. Review verdict

**Endorse CR-AM-12 as an Assessment-Models-wide architectural change**, with three reconciliations against what already exists:

1. **The federation already fixed Layer 1.** Org `.github/GOVERNANCE.md` (CR-AM-11 §8) already establishes "centralize contracts/governance/integration; decentralize model ownership", the `maturity-model-<domain>` naming taxonomy, SemVer + immutable `vX.Y.Z` tag releases, and the rule that `technehub-labs/dea-metamodel` owns contracts while Assessment-Models owns assets. CR-AM-12's Layer 1 should **ratify** this, not redesign it.
2. **Layer 2 (repository standard) is the real gap.** No shared repository template / README spec / directory-convention document exists today. Each model repo improvises (the AO repo and DTM repo converged on a similar shape independently: `model.yaml`, `VERSION`, `CHANGELOG.md`, `maturity/`, `examples/`, `scripts/`, two workflow levels). CR-AM-12 should mint that convergence into a written standard.
3. **The AO repo is already ~80% of the reference implementation** (manifest handshake, bound canonical scale, register, Level-1/Level-2 CI, worked example). What lags there: evaluation/questionnaire enrichment (staged on `vibe/reconcile-f5ed1a`), visual explanations, and the written repo standard itself.

The CR's critical principle is correct and is already honored in practice: **standardize the architecture, not the intellectual content** — each model repo keeps its own dimensions, scale, scoring (the AO register is verbatim from its own lineage; the DTM repo has its own composite scale; bands are canonical upstream, never restated locally per CONTRIBUTING rule 2).

## 2. ADR-by-ADR cross-reflection against current state

| ADR | Requirement | Current state (evidence) | Status | Action |
|-----|-------------|--------------------------|--------|--------|
| ADR-AM-12-01 | One standard repo architecture | AO + DTM repos converged on the same shape, but unwritten | **Partial** | Author `docs/REPO-STANDARD.md` (Layer 2 spec) in the AO repo; ratify in CR-AM-12 |
| ADR-AM-12-02 | Reusable repo template + doc spec | None exists | **Lagging** | Tranche T1: template spec + README section spec + directory conventions |
| ADR-AM-12-03 | Preserve domain semantics | AO register verbatim 157/157; DTM composite scale distinct; CONTRIBUTING rule 1 forbids altering level semantics without CR | Satisfied | Keep; encode as standard rule "content is model-owned" |
| ADR-AM-12-04 | Machine-readable definitions authoritative | All models are YAML manifests (`model.yaml`, `maturity/*`); READMEs are explanatory | Satisfied | Encode "YAML authoritative, docs explanatory" in the standard |
| ADR-AM-12-05 | Common evidence/assessment/provenance conventions | AO has assessment block + provenance + questionnaire; not standardized | **Partial** | Tranche T1: evidence-pack, assessment-method, provenance conventions in the standard; AO is the reference |
| ADR-AM-12-06 | Reusable validation/conformance automation | Per-repo `scripts/local_validate.py` + `assessment-ci` reusable `contract-conformance.yml` + `schemas/model-manifest.schema.json` | **Partial** | Tranche T3: make assessment-ci workflows the required Level-1/2/3 CI for every model repo |
| ADR-AM-12-07 | AO as first complete reference implementation | AO repo exists (v1.0.1 tags); enrichment assets staged | **Partial** | Tranche T2: land `vibe/reconcile-f5ed1a` (evaluation v2, questionnaire, docs, visuals) |
| ADR-AM-12-08 | Progressive migration of existing model repos | Catalog is frozen legacy (superseded_by AO repo); DTM repo exists | **Partial** | Tranche T4: migration order + per-repo checklists |
| ADR-AM-12-09 | Separate model definition from assessment execution/results/benchmarking | Already the CR-AM-01 decoupling (`AssessmentResult → interpreted-by → MaturityModel`); org governance Layer 4 | Satisfied | Keep; restate in standard so model repos never host execution/results |
| ADR-AM-12-10 | Optional enrichment without turning model repos into apps | AO enrichment is docs+data assets, not an app | Satisfied | Keep; standard lists optional enrichment slots (visuals, questionnaire, examples) |

## 3. Reconciled target architecture (mapped to real repositories)

```
Layer 1 — Ecosystem governance (org-governed)
  .github (GOVERNANCE.md, taxonomy) · assessment-registry (identity spine, immutable refs)
  · assessment-ci (reusable CI, manifest schema) · technehub-labs/dea-metamodel (canonical contracts, bands)
Layer 2 — Repository standard (NEW — the CR-AM-12 deliverable)
  docs/REPO-STANDARD.md in the reference repo + template: model.yaml manifest (CR-AM-11 §15/§22),
  VERSION, CHANGELOG, maturity/{scale,model,evaluation,assessment-questionnaire}.yaml, examples/,
  scripts/local_validate.py, docs/{GOVERNANCE,EXTRACTION-CHECKLIST,RECONCILIATION}.md, README spec,
  .github/workflows (Level 1 local, Level 2 contract conformance via assessment-ci pin)
Layer 3 — Individual maturity models (independent repos, model-owned content)
  maturity-model-autonomous-operations  ← reference implementation (v1.0.1 + staged enrichment)
  maturity-model-digital-transformation  ← next
  maturity-model-<domain> …              ← migrated per tranche T4
  dea-catalog-maturity-models            ← frozen legacy lineage (superseded_by pointers)
Layer 4 — Assessment consumers (out of scope for model repos)
  assessment-model-*, assessment-tool-*, executions, results, benchmarking
```

Lifecycle (unchanged from the CR draft, confirmed against CR-AM-01): governance → standard → contracts → domain model → assessment model → execution → result → benchmarking.

## 4. Implementation tranches with acceptance criteria

| Tranche | Content | Acceptance criteria |
|---------|---------|---------------------|
| **T0 — Land the CR** | CR-AM-12 registered as a change request (full CR in the CR-authoritative repo per convention; xref in model repos); this proposal linked | CR visible in CR index; proposal 0004 merged |
| **T1 — Layer 2 standard** | `REPO-STANDARD.md` (directory conventions, README spec, metadata conventions, governance rules, conformance requirements) authored in the AO repo; template instantiated | Standard doc merged in reference repo; one other model repo (DTM) adopts it in a PR with zero content changes |
| **T2 — AO reference enrichment** | Push `vibe/reconcile-f5ed1a`: evaluation (v2 bands), questionnaire (157), docs incl. `ARCHITECTURE.md` visuals, examples; validator green | Level 1 CI green on the PR; `local_validate.py` passes incl. new checks; Level 2 conformance green |
| **T3 — Reusable CI** | Every model repo's workflows call `assessment-ci` reusable workflows with an immutable `dea-metamodel` pin; registry Level 3 resolution | contract-conformance workflow green on AO + DTM repos |
| **T4 — Progressive migration** | Per-repo EXTRACTION-CHECKLIST executed for DTM and others; catalog entries marked superseded_by | Each migrated repo has a registry record with immutable tag; catalog shows pointers |
| **T5 — Registry completeness** | `maturity-model-autonomous-operations` record merged in assessment-registry (staged on `vibe/ao-registry-entry-f5ed1a`, validator-passing, tag `v1.0.1`) | `resolve.py <id> --check` OK in registry CI |

## 5. Where we are lagging (explicit list)

1. Layer-2 written standard does not exist anywhere → **T1**.
2. AO enrichment (evaluation/questionnaire/visual docs) staged but unpushed — repo not in this session's repo list → **T2**, blocked on session access.
3. Registry record for AO staged but unpushed — `assessment-registry` not in session repo list → **T5**, same blocker; finish script at `/tmp/finish_ao_extraction.sh`.
4. Visual explanations (architecture/lifecycle diagrams) missing from the AO repo → included in T2 staging as `docs/ARCHITECTURE.md` (mermaid).
5. Catalog supersession PR (#15) still open → maintainer merge click.

## 6. Non-goals (reconciled)

- No changes to canonical bands/scale (owned by `dea:maturity-bands-v2` in dea-metamodel).
- No model-content changes in the frozen v1-alpha catalog lineage.
- No assessment execution/results/benchmarking features inside model repos (ADR-09).
- No git submodules (prohibited, CR-AM-11 §23); contracts are pinned, immutable references.
