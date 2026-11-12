# Proposal 0002 — Autonomous Operations Maturity & Assessment Model (`dea:maturity-autonomous-operations`)

| Field | Value |
|-------|-------|
| Status | PROPOSED |
| Date | 2026-11-12 |
| Scope | `maturity-models/v1-alpha/autonomous-operations.yaml` (catalog entry) + `maturity-models/autonomous-operations/` (self-contained repo-ready asset bundle) + `index.yaml` content/relationship/tags + README/CHANGELOG/VERSION |
| Source material | An industry Autonomous Operations maturity workbook v1.8.0 (XLSX, 12 sheets, md5 `61ce82cba20cd8c87ce4e079b8a2e966`), parsed to JSON/CSV; 2025–26 industry sources (ETSI ZSM, Gartner, Forrester, Cisco, Ericsson, Google SRE, IBM) |
| Related proposals | Complements `0001-nonlinear-maturity-scoring.md`: this model adopts the 0001 effort multipliers / effort-adjusted value as scoring metadata while keeping the canonical v1 bands |

---

## 1. Positioning: what this model is (and is not)

**Autonomous Operations (AO)** = the enterprise *operating model*: value streams instrumented with
AI, data and **closed-loop control**; learning, self-governance, self-adaptation; well-defined
**decision/feedback models operating as loops**; automation shifting decision burden from humans to
machines; an explicit human–machine working model. The progression axis used throughout is the
**OODA closed loop — Observe, Orient, Decide, Act — driven by intent/goals**.

Narrower network-domain autonomy ladders exist in the industry and are deliberately **out of scope
and unreferenced** here: this model covers the whole operating model (party, strategy, technology,
operations, culture, data), not one domain of it.

## 2. Rigorous gap register — what the source workbook v1.8.0 is missing

Method: parsed v1.8.0 (6 dims / 32 sub-dims / 151 criteria × 5 levels = 755 level cells), audited against
(a) the AO definition elements above, (b) sibling models in this ecosystem (`dea:maturity-operations`:
observability, SLOs, error budgets, SRE), (c) 2025–26 industry sources, (d) assessment best practice
(evidence, independence, comparability — see CR-AM-01 in the assessment-tools repo).

| # | Gap | Evidence in v1.8.0 | Why it matters (source) | Addressed in new model |
|---|-----|--------------------|--------------------------|------------------------|
| G1 | No Level-0 "Absent" baseline in the grid (concepts diagram has "Zero"; grid starts at 1) | Levels begin at "1 - Initiating" | An org with *no* AO capability needs a scoreable state (the org's composite model scale uses L-0 Absent) | `scoring.level_points` includes L0=0; unassessed criteria score 0 |
| G2 | **No scoring/rollup mechanism at all** — no weights, no aggregation from 151 criteria to a dimension/org score, no banding | Workbook has levels but no math | A maturity model without a scale mechanism is not assessable | `evaluation.yaml` scoring: AO Autonomy Index 0–100, weights, banding, weakest-link gate, effort-adjusted value |
| G3 | **No assessment methodology / required inputs** — scope, granularity, evidence pack, assessor independence, sampling, confidence, cadence | None | Per-scenario + org-rollup assessment practice; CR-AM-01 comparability; assessor-observability requirement | `assessment` block: inputs, 6-step method, independence, confidence levels, cadence |
| G4 | Observability / event intelligence not a first-class criterion | Only implicit (real-time data transmission) | Gartner renamed the AIOps market category to *Event Intelligence Solutions* (2025); sibling ops model requires an observability stack | New criterion **3.3.8 Observability & Event Intelligence** |
| G5 | SLO / error-budget management missing as a criterion | Self-governed SLAs + assurance exist, but no explicit SLO/error-budget criterion | Google SRE; sibling ops model L2–L3 exit criteria are SLO/error-budget based | New criterion **4.2.5 SLO & Error Budget Management** |
| G6 | Agent lifecycle management (AgentOps) missing | Intelligence/orchestration covered, agent *ops* not | IBM/Fabrix AgentOps; Cisco AgenticOps; Gartner: 40% of enterprise apps carry task-specific agents by end-2026 | New criterion **3.1.8 Agent Lifecycle Management (AgentOps)** |
| G7 | Guardrails, escalation & auditability of autonomous actions missing | Trust/hardening criteria exist, but no guardrail/audit-trail criterion | Forrester AEGIS; ETSI ZSM operation autonomy = delegation + escalation; Cisco policy-governed autonomy with audit trails; requirement that an independent assessor can observe outcomes | New criterion **2.4.7 Autonomous Action Guardrails, Escalation & Audit** |
| G8 | Multi-agent orchestration & loop conflict resolution only partial | Closed-loop orchestration covered generically | ETSI GR ZSM 020 multi-agent systems; Ericsson utility-based conflict resolution across loops | New criterion **3.1.9 Multi-Agent Orchestration & Loop Coordination** |
| G9 | Human oversight / exception-handling design not explicit | Scattered across employee-engagement and culture criteria | Ericsson: balance machine autonomy with human oversight in the OODA loop; Gartner: autonomy creates *more* human oversight work, not less | New criterion **5.3.4 Human Oversight & Exception Handling Design** |
| G10 | Simulation / digital-twin validation before acting | Simulation exists as a tech capability but is not wired into ops loops | ETSI ZSM digital twins; Ericsson digital twin as a safe sandbox for proposed actions | New criterion **4.1.5 Simulation & Digital-Twin Validation Before Act** |
| G11 | Machine customers / agent-to-agent commerce | Partner engagement is human-partner oriented | Gartner: machine customers could drive or influence $18T in purchases by 2030 | New criterion **1.5.6 Machine Customer & Agent-to-Agent Readiness** |
| G12 | Cross-dimension duplicate criteria (MECE violation) | "Catalog Driven Service Realization" = 3.4.2 **and** 4.6.1; "Intelligent Productization" = 3.4.3 **and** 4.6.2; "Formulate and decide solution" = 4.1.3 **and** 4.5.3 | MECE requirement | Merged/renamed; recorded in `provenance.dropped_duplicates` / `renamed` |
| G13 | Structural/ID defects | 6 float IDs (`1.1000000000000001`…); 6.2.5 under the 6.3 header; shifted level columns in several Strategy/Data rows; map counts (33) drift from sheet IDs (32); map labels drift from sheet labels | Breaks any downstream processing/CI | Cleaned in harvest; IDs stored as text; 6.2.5 → 6.3.5 |
| G14 | Level-text quality: 755 cells — 161 multi-sentence (21%), 13 >45 words, 1 empty, stale review comments ("more than one statement", misplaced email) | automated lint | Requirement: concise, single-statement, evidencable, assessor-observable levels | One explicit OODA/closed-loop ladder (`levels[].progression`) applied uniformly; per-level characteristics/exit/evidence instead of 755 ad-hoc cells |
| G15 | Progression not monotonic/consistent across criteria | 0 of 151 criteria follow a strict scope ladder; two criteria non-monotonic | Requirement: each next stage is a genuine progression from the last | The shared ladder is monotonic by construction (scope ⊆, OODA human→system, loop open→closed→self-learning) |
| G16 | Value realization not wired to value-operations metrics | Value-model criteria exist but no KPI evidence expectations | Industry value-operations practice (R.I.S.E.-style value models) | L3+ exit criteria require value tracking against a value-operations model |
| G17 | AI/model risk only generic | Risk + hardening + security criteria exist | Trust-in-AI practice (lifecycle trust management) | Retained + strengthened by G7 criterion |
| G18 | Assessment workflow inputs (baseline, target, roadmap, stakeholders) | Roadmap exists; no assessment process | Usability | `assessment.inputs_required`, `assessment.method` |
| G19 | Ecosystem level endpoint inconsistent | Many L5 cells say "ecosystem" but not all | L5 should be uniformly ecosystem + self-learning | Ladder fixes L5 = ecosystem-wide, self-learning, intent negotiated |
| G20 | Sustainability present but thin | Sustainability criteria exist | Keep, add carbon KPIs inside the loop | L5 characteristics include net-zero autonomously optimized with carbon KPIs in the loop |

Net effect: 151 source criteria → **157** in the new model (−2 duplicates, +8 gap criteria; 6.2.5
renumbered to 6.3.5), 32 sub-dimensions, 6 dimensions — same spine, cleaned and gap-filled.

## 3. Level design — ambitious AO stages on canonical org bands, OODA-driven

Requirement: levels must drive ambition, correlate to the org's canonical levels, and use
closed-loop / decision-model / OODA language with intent/goals driving the loops — no
network-domain ladders or their cognitive-dimension vocabulary.

| Band (`index.yaml`) | Canonical level | Range | **AO stage** (`ao_stage`) | Loop driver (`progression.loop_driver`) |
|---|---|---|---|---|
| band-1 | Ad Hoc | 0–25 | **Manual & Reactive** | none — open loop; humans react to events |
| band-2 | Defined | 26–50 | **Instrumented & Assisted** | human-set goals; machines monitor & recommend |
| band-3 | Managed | 51–75 | **Closed-Loop Automated** | human-set goals/SLOs drive the automated loop |
| band-4 | Quantitatively Managed | 76–90 | **Goal-Driven Autonomy** | intent/goals drive the loop; system owns Observe–Orient–Decide–Act within guardrails |
| band-5 | Optimising | 91–100 | **Self-Improving Ecosystem** | intent/goals negotiated ecosystem-wide drive self-learning loops |

Each level also carries `progression.ooda` (who performs Observe / Orient / Decide / Act:
human → system-assisted → system-within-rules → system → system-learning), `scope`
(ad hoc → some → most → org → ecosystem), `human_role` (does → approves → exceptions →
audits → sets goals), and `loop_closure` (open → partial → closed → closed autonomous →
self-learning). Canonical correlation is explicit: every level keeps its catalog
`id`/`name`/`score_range` and adds `canonical_band: band-N`, so scores remain comparable
across the org's models (CR-AM-01 §25 comparability contract).

Why these stage names: each names the *state the organization reaches*, not the process
regime — "Goal-Driven Autonomy" and "Self-Improving Ecosystem" describe an ambition an
executive can buy into, and each is one OODA step beyond the previous.

## 4. Scale mechanism (evaluation.yaml)

Criterion level → points (L0=0, L1=20 … L5=100) → dimension mean → **AO Autonomy Index**
(weighted mean of 6 dimension scores: strategy .20, operations .20, technology .20,
data .15, party .15, culture .10) → catalog band → org level, **capped by the weakest-link
gate** on the closed-loop spine criteria (4.1.1–4.1.4: a loop that cannot Observe/Orient/
Decide/Act cannot make the org autonomous). Effort multipliers 1.0/1.5/2.5/4.0/6.0 and the
effort-adjusted value formula (proposal 0001 §4) make diminishing returns explicit.
Worked example: `examples/assessment-example.yaml`.

## 5. Asset bundle & model-per-repo cascade

`maturity-models/autonomous-operations/` is a self-contained package (model.yaml,
scale.yaml, evaluation.yaml, dimensions.yaml, examples/, scripts/local_validate.py,
README.md, GOVERNANCE.md) following the org's model-per-repo layout. When the dedicated
`maturity-model-autonomous-operations` repository is created through org governance, the
bundle is lifted verbatim, registered in `assessment-registry`
(`registry/maturity-models/`), and wired to the reusable CI in `assessment-ci`
(GOVERNANCE.md lists the exact steps). The catalog entry in
`v1-alpha/autonomous-operations.yaml` remains the CI-validated registration and stays in
sync with the bundle (`scripts/local_validate.py` checks consistency).

## 6. Mapping from the source workbook v1.8.0

- Dimensions/sub-dimensions keep their source IDs (1.x party … 6.x data); criteria keep IDs except:
  - `3.4.2` → merged into `4.6.1`; `3.4.3` → merged into `4.6.2`; `4.5.3` → renamed "Formulate and decide energy & carbon solution"; `6.2.5` → `6.3.5`; `1.7.1` → "Autonomous Onboarding (Smart Things)"; `3.1.5` → "Autonomous Integration & Interoperability".
  - New: `1.5.6`, `2.4.7`, `3.1.8`, `3.1.9`, `3.3.8`, `4.1.5`, `4.2.5`, `5.3.4`.
- Source level names (Initiating/Emerging/Performing/Advancing/Leading) map to the canonical bands by ordinal; AO stage names are additive metadata, not replacements.
- Machine-readable source: parsed model JSON/CSV kept with the original workbook.

## 7. Open questions — RESOLVED (decisions recorded in the model's `decisions` block)

1. **Dimension weights** — default kept at 20/20/20/15/15/10 (strategy/operations/technology are the
   execution core; data/party/culture enabling; sums to 1). A **comms-provider profile**
   (15/25/20/15/15/10, operations-weighted) ships in `scoring.weight_profiles` and is selected in the
   scope charter; profile choice is recorded in the assessment result. Revisit both at v1.1.0 with
   real assessment data.
2. **Weakest-link gate scope** — gate applies only to gating criteria (4.1.1–4.1.4) that are
   **in the assessment scope**; criteria excluded by the scope charter do not gate. Other
   Operations flows (4.2/4.3) are scored but not gating.
3. **v2 band boundaries** — deferred to CR-AM-01 Release 1 per the catalog README parking note;
   this model keeps the canonical v1 bands and uses proposal 0001 effort multipliers as scoring
   metadata only.
4. **Repo extraction timing** — Phase 6 (CR-AM-11 §26/§31), after the CR-AM-01 Release 1 decision;
   runbook ready in the bundle's `EXTRACTION-CHECKLIST.md` (PR #8).

## 8. Verification (acceptance criteria)

- CI `Validate Maturity Models` passes (schema + exactly 5 levels + per-level fields).
- `index.yaml` bands contiguous 0–100; content entry + relationship present.
- `scripts/local_validate.py` passes: bundle consistent with catalog entry, unique criterion ids/names, bands aligned, weights sum to 1, every level has a full OODA progression + loop driver, and **zero legacy references** (network-domain autonomy ladders and their cognitive-dimension vocabulary) in any bundle file.
- Worked example reproduced: index 60 with gating min level 2 → org level 2 (see `examples/assessment-example.yaml`).
