# Proposal 0003 — Digital Transformation Operationalized Maturity & Assessment Model

| Field | Value |
|-------|-------|
| Status | PROPOSED |
| Date | 2026-11 |
| Author | Assessment-Models contributor (with assistant analysis) |
| Scope | New model file `maturity-models/v1-alpha/digital-transformation-operationalized.yaml`; `maturity-models/index.yaml`; `README.md`; `CHANGELOG.md` |
| Relationship to PR #1 / proposal 0001 | Additive. Does not touch existing models or bands. Uses v1-alpha bands canonically; carries v2 aliases + effort multipliers as *advisory* metadata aligned with proposal 0001. |

---

## 1. Context and method

We reviewed **TM Forum Digital Maturity Model v5.0.2 (GB997A)** end to end — 17 sheets, 6 dimension
sheets, 31 sub-dimensions, 129 criteria × 5 levels (645 level descriptors) — with automated checks
(ID sequencing, duplicates, level-progression heuristics, focus-area tagging, cross-sheet consistency
against Lite Version and the three mission-hotspot sheets) plus a 54-item keyword coverage scan of
all criteria text against a modern digital-business capability checklist, and targeted web research
for grounded industry definitions (Gartner, TM Forum, GSMA/CAMARA, WEF, ISO/IEC, HMT literature).

## 2. Findings — structural defects in DMM v5.0.2

| # | Location | Defect |
|---|----------|--------|
| S1 | `Strategy (D2)` row 28 | Criterion **2.4.4** sits on the same row as the **2.5** sub-dimension header — 2.5 appears to have 6 criteria, 2.4 only 3 |
| S2 | `Customer (D1)` row 22 | Criterion ID `1.3.6` but level IDs `1.4.6.1–5`; content belongs to 1.4 — ID/level mismatch |
| S3 | `Strategy (D2)` 2.4.2 | **L2/L3 inverted**: L2 claims frameworks + data-driven scenario planning; L3 only annual-report recognition (less mature) |
| S4 | `Technology (D3)` 3.5 | Sub-dimension "Technology Resources Efficiency" contains workforce skills (3.5.1) and agile methods (3.5.2) — Culture content |
| S5 | `Technology (D3)` 3.4.7 | "Physical Security" (CCTV/RBAC) in a *digital* assurance sub-dimension |
| S6 | `Technology (D3)` 3.1.1 vs 3.3.2 | Cloud architecture vs cloud infrastructure criteria duplicate (level texts up to 52% similar; 99.99% vs 99.9% uptime) |
| S7 | `Strategy (D2)` 2.1.4 vs 2.1.6 | Brand Value and Sustainable Competitive Advantage overlap (both brand reputation/market leadership) |
| S8 | `Strategy (D2)` 2.3.4 | "BYOx Personalization" misplaced under Collaborative Ecosystem Strategy |
| S9 | Focus-area tags | Inconsistent conventions: "GOVERNANCE RISK AND COMPLIANCE" vs "(GRC)" variants; 2.2.1 "Emerging Technologies" tagged ARTIFICIAL INTELLIGENCE |
| S10 | Hotspot sheets vs model | Label drift: hotspots cite "AI Use Case Classification" (sheet: 2.5.5 "AI Use Case Prioritization") and "AI-Powered Operational Transformation" (sheet: 2.5.1 "Strategic AI Operational Mandate") |
| S11 | Editorial | "Netral" (Lite), "adhers" (2.4.3), ~15 typos in D3 ("repeatative", "clairty", "accross", "orchestate", "ecosystem-wde apoption", …), mixed en-GB/en-US ("standardised"/"Optimised" vs "standardized"), first-person "we" only in 3.6.2, non-breaking spaces breaking text joins, "3- Performing" header spacing |

## 3. Findings — missing capabilities (gap register)

Keyword scan: **22 of 54** modern digital-business capability areas are absent from all 129 criteria
(some others only incidental). The most material for a *digital business* (not IT) model:

1. **Agentic AI / AI agents / multi-agent orchestration** — no agency levels, no agent registry, no agent security/identity (only incidental mentions).
2. **AI TRiSM** — no AI trust/risk/security management: model inventory & risk scoring, explainability, bias/fairness, guardrails, guardian agents, EU AI Act readiness (only "ethics-by-design" wording in 2.5.4).
3. **Human–agent teaming / human-in/on-the-loop** — the human–machine working model is not a scored capability anywhere.
4. **Network APIs / GSMA Open Gateway / CAMARA** (number verification, SIM swap, location, quality-on-demand, edge discovery, carrier billing), **NaaS, slicing** — absent; core to telecom digital-business monetization. No 5G/6G capability coverage.
5. **Business-model innovation** — no servitization/XaaS/outcome-based models, no dynamic/usage-based pricing, no revenue assurance/fraud management (billing only).
6. **Customer marketing stack** — no CDP/martech/next-best-action/journey orchestration/NPS-CSAT as capabilities; no composable commerce/headless.
7. **Platform engineering / IDP / DevEx / golden paths** — absent.
8. **Regulatory resilience** — no DORA/NIS2/TLPT; no third-party/vendor risk, concentration, or exit strategy; no post-quantum crypto roadmap; no DEI; no ERM/internal audit; no regtech/legal-tech; no venturing/open-source/standards participation.
9. **Assessment mechanics** — no evidence/artifact columns per level, no MECE enforcement rules, no assessor calibration/repeatability guidance (Lite + hotspots exist as sheets only, not derived from a single registry).

## 4. Grounded definitions used to frame the new model

| Concept | Grounded definition | Source |
|---|---|---|
| Digital transformation / digital business | Exploiting digital technologies and capabilities to create a robust new **digital business model**; digitalization = using digital tech to change a business model; digital business blurs digital and physical worlds | Gartner IT Glossary; WEF (transformation = business-model reimagining, not an IT initiative; leaner operating models, customers/employees at center) |
| Agentic AI / agents | Software entities that perceive, decide, act and achieve goals with minimal human supervision; systems that plan and act autonomously; graded levels of agency + guardrails required | Gartner Top Strategic Technology Trends 2025: Agentic AI |
| Autonomy ladder | AN L0–L5: who owns awareness→analysis→decision→execution→intent per domain; L4 = closed-loop intent-driven, intent shared human-machine; L5 = system sets its own intents | TM Forum AN framework, IG1253 |
| Digital twins & simulation / DTO | Dynamic software model on operational/contextual data that understands, simulates and responds — incl. the Digital Twin of an Organization used to plan/simulate/scale initiatives | Gartner DTO definition & DTO platform market guides |
| Human-agent teaming | People + AI systems collaborating/coordinating toward shared goals as teammates; trust calibration, delegation, adaptive autonomy, human oversight | See et al. 2007; Demir et al. 2021; arXiv 2503.16518 / 2504.05755 |
| Network APIs | Federated standardized operator APIs (CAMARA/Open Gateway) exposing network capabilities as products; NaaS/slicing | GSMA Open Gateway / CAMARA 2025–2026 |
| AI TRiSM | AI trust, risk and security management: continuous monitoring, validation, enforcement — inventory, explainability, bias, guardrails, guardian agents, EU AI Act readiness | Gartner AI TRiSM (2025–2026) |
| Evidence-based assessment | Objective, consistent, **repeatable** assessment — a second assessor reaches the same rating from the same artifacts; cumulative maturity levels | ISO/IEC 33002:2015; CMMI v3; EDM DCAM |

## 5. The new model — design

**`dea:maturity-digital-transformation-operationalized` v1.0.0-alpha** — "Digital Transformation
Operationalized Maturity & Assessment Model":

### 5.1 Level ladder — design review and canonical correlation

The ladder semantics (ad hoc → piloted → standardized → measured/predictive → autonomous/intent-driven)
are kept — they map cleanly onto CMMI's cumulative rule, the TM Forum AN L0–L5 ladder, and the catalog's
exit-criteria convention. What changed after review is **how the levels are named and sold**, because the
names are what an organization sees in a radar chart or board pack:

- **Names now denote value, not just state**: primary level names describe the *value state* an
  organization has reached — **Unrealized → Proven → Standardized → Compounding → Leading**
  (value identified but not captured → proven in governed pilots → repeatable org-wide →
  scaled/measured/predictive → self-optimizing and benchmark-setting). The v2 state-names
  (Emergent/Structured/Systematic/Adaptive/Self-Optimising) are kept as `v2_name` aliases, so
  proposal 0001 tooling and the canonical correlation are unaffected. Every level also carries
  `unlocks` (business value unlocked) — names + unlocks together make the ambition explicit in
  a radar chart or board pack.
- **Explicit correlation to the canonical scale**: model level N ↔ canonical ordinal N−1 (**L-0..L-4**),
  carried per level as `canonical: {scale_level, ordinal, canonical_name, v2_band, v2_score_range,
  effort_multiplier}` plus a model-level `level_correlation.mapping` table. `score_range` keeps the uniform
  catalog v1-alpha bands (0–25/26–50/51–75/76–90/91–100); `legacy_id`/`legacy_name` keep v1-alpha resolvable.
  Known semantic offset documented: catalog v1 level-1 "Ad Hoc" spans canonical L-0+L-1; this model splits it
  via Emergent (L-0) and Structured (L-1).
- **Ambition mechanics**: every level now carries `unlocks` — the business value unlocked at that level
  (e.g., Adaptive unlocks "major changes simulated in the DTO before a dollar is committed") — and the
  non-linear v2 bands + effort multipliers (1.0/1.5/2.5/4.0/6.0) make diminishing returns *visible* instead of
  hiding them in linear bands, so the cost of the next level is honest.
- **Progression semantics are identical to the canonical scale** (recorded in `advancement.progression_semantics`):
  linear topology, exponential effort, forward-only with no skipping, exit-criteria + evidence gates,
  highest-conformant-level resolution.

| Model level (value name) | v2 state-name alias | Catalog v1 (legacy) | Canonical scale | Ordinal | v1 band | v2 band | Effort mult |
|---|---|---|---|---|---|---|---|
| level-1 Unrealized | Emergent | level-1-ad-hoc Ad Hoc | L-0 Absent | 0 | 0–25 | 0–20 | 1.0 |
| level-2 Proven | Structured | level-2-defined Defined | L-1 Piloting | 1 | 26–50 | 21–45 | 1.5 |
| level-3 Standardized | Systematic | level-3-managed Managed | L-2 Defined | 2 | 51–75 | 46–70 | 2.5 |
| level-4 Compounding | Adaptive | level-4-quantitatively-managed | L-3 Scaled | 3 | 76–90 | 71–88 | 4.0 |
| level-5 Leading | Self-Optimising | level-5-optimising Optimising | L-4 Self-Optimising | 4 | 91–100 | 89–100 | 6.0 |

### 5.2 Structure and mechanism

- **Positioning**: digital transformation = the operating model of a digitally mature organization —
  advanced tech adoption (AI, agentic AI, autonomous systems, composable platforms, twins) expressed
  through novel operating models across all concerns, customer/ecosystem-centric strategy, and a designed
  human–agent working model. Technology is an enabler, not the subject.
- **MECE structure**: 6 dimensions (Customer & Ecosystem Value; Strategy, Business Model & Value;
  Digital Platforms & Technology Enablement; Operations & Autonomous Service Delivery; People, Culture &
  Human–Agent Teaming; Data & the Intelligent Enterprise) → 23 sub-dimensions → **70 criteria**. Each
  criterion lives in exactly one sub-dimension; cross-cutting themes are **transversal levers** (12 tags:
  agentic-ai, autonomy, digital-twins, human-agent-teaming, ecosystem-platforms incl. network APIs,
  trust-security-privacy incl. AI TRiSM, sustainability-esg, composability, business-value, innovation, grc,
  data-intelligence).
- **Progression ladder (novel advancement)**: every criterion carries 5 evidence-anchored levels
  (Emergent/ad hoc → Structured/piloted-defined → Systematic/standardized-governed → Adaptive/measured-predictive-orchestrated →
  L5 autonomous/intent-driven/self-optimizing). Advancement is cumulative (no skipping), gated by
  weakest-link on mandatory dimensions (d1–d4) and by per-level exit criteria; `delta_to_next_level`
  headroom is reported per dimension. Autonomy criteria reference the AN L0–L5 ladder explicitly.
- **Intuitive scale mechanism**: criterion 1–5 → 0–100; sub-dimension = mean; dimension = mean;
  overall = weighted mean (0.20/0.20/0.20/0.15/0.10/0.15) banded into the catalog's uniform 5 bands
  (0–25/26–50/51–75/76–90/91–100) with highest-conformant-level resolution. Advisory v2 aliases
  (Emergent/Structured/Systematic/Adaptive/Self-Optimising) and effort multipliers (1.0/1.5/2.5/4.0/6.0)
  per proposal 0001 are carried as metadata. Lite rapid path: one 5-point Likert question per sub-dimension.
- **Assessability**: every level anchor is written as observable evidence (artifacts, metrics, logs,
  governance records); assessment rules require independent-assessor verification, ISO/IEC 33002-style
  repeatability and calibration.

## 5b. Appendix — complete findings register from the D4/D5/D6 deep review (post-merge)

Same battery as D2/D3 (row layout, ID sequencing, level-ID match, duplicates, progression
heuristics, focus tags, typos/punctuation, cross-dimension similarity):

**Structural: clean.** D4/D5/D6 sheet layouts are correct — no misplaced header rows, criterion
IDs contiguous per sub-dimension, every criterion has exactly its 5 level IDs. (Contrast D1's
1.3.6/1.4.6.x mismatch and D2's row-28 placement.) Minor: trailing ideographic space (`　`) in
D6 row 9 col I; `\xa0` in the 5.5 sub-dimension name.

**Additional defects found:**

| # | Location | Defect |
|---|----------|--------|
| S12 | D4 4.4.1 "Value Network" | L1 text ends mid-sentence ("...Collaboration, trust."); L2/L3/L5 contain " ." artifacts with truncated tails — level descriptors corrupted |
| S13 | D4 many (4.1.1, 4.1.2, 4.2.1, 4.3.1, 4.3.3, 4.3.4, 4.3.5, 4.4.1, 4.5.3, 4.6.1, 4.6.4, 4.6.6) | "space before period" (" .") artifacts throughout level texts |
| S14 | D4 4.4.4 criterion text | "The organization implemented  Integrated SOC/NOC operation" — double space + grammar ("implements") |
| S15 | D5 5.1.6 label | "AI Leadership/ Talent" — stray space after slash |
| S16 | D5 5.6.3 L5, D6 6.3.3 L4 | Missing final period |
| S17 | D4 4.6.6 ↔ D5 5.3.2 | Real topical duplication: "Agile-Driven Operations" (D4) vs "Agile Ways of Working" (D5) — agile ways-of-working scored in two dimensions (MECE violation; cf. S4) |
| S18 | D5 focus tags | 9/25 Culture criteria tagged TRANSFORMATIONAL CHANGE — tag noise; culture criteria should carry people/culture-relevant levers |

Progression heuristics flagged dips in 5.1.6, 4.4.1, 4.1.1, 4.1.3, 4.3.4, 4.4.1, 5.1.5, 5.2.3,
5.4.1, 5.4.5, 5.5.2, 5.6.1 — reviewed manually: all are keyword-heuristic noise except the S12
truncation; no semantic L2/L3-style inversion found in D4/D5/D6 (the one real inversion remains
D2 2.4.2, S3).

## 5c. Self-review of the new model (post-build)

- **MECE**: 0 near-duplicate criterion statements across sub-dimensions (pairwise sim > 0.55);
  every criterion in exactly one sub-dimension; all 12 transversal levers have ≥4 criteria
  (coverage: business-value 16, data-intelligence 14, innovation 12, grc 12, composability 10,
  agentic-ai 10, trust-security-privacy 9, autonomy 9, ecosystem-platforms 8, human-agent-teaming 5,
  digital-twins 4, sustainability-esg 4).
- **Progression**: anchor maturity-score heuristic flags 5 criteria (d1c4, d2c6, d3c4, d5c8,
  d6c11) — manually reviewed; all are keyword noise, anchors are semantically monotonic
  (L1 negative → L5 autonomous/intent-driven) with evidence per level.
- CI-equivalent + custom checks pass on the merged file (run 43257210108: "OK — 7 maturity
  models validated").

### 5.3 Hotspot views per transversal lever

The model ships **12 hotspot views** (one per transversal lever) — the equivalent of DMM v5's
mission-hotspot sheets (CITE / AI&Data / AN&O). Each view lists the criteria that must reach a
minimum level for that theme (58 entries total; thresholds min_level 2–4, mirroring the
"Level >= 3 / Level 5" convention), e.g.: agentic-ai → d3c8 ≥ L4, d3c9 ≥ L3, d4c6 ≥ L4, d5c9 ≥ L3,
d6c7 ≥ L3; autonomy → d4c4 ≥ L4, d4c5 ≥ L4, d4c2 ≥ L3; digital-twins → d4c7/d4c8 ≥ L3, d4c9 ≥ L4.
Validated: every hotspot entry references an existing criterion and lever, min_level within 1–5.

## 6. Verification (acceptance criteria)

- CI (`.github/workflows/ci.yml`) passes: all `v1-alpha/*.yaml` have id/name/domain/version + exactly
  5 levels with id/name/score_range/summary/characteristics/exit_criteria/evidence. ✅ (validated locally)
- Custom checks pass: unique IDs; 5 anchors per criterion covering levels 1–5; every criterion has
  evidence; lever references resolve; dimension weights sum to 1.0; bands match the catalog. ✅
- index.yaml content + relationships updated; README catalog table updated; CHANGELOG entry added.

## 7. Parking lot / follow-ups

- Fix-forward of DMM v5.0.2 defects S1–S11 belongs to the TM Forum GB997 change process (upstream),
  not to this catalog.
- If the ecosystem later promotes this model to its own `maturity-model-<domain>` repository per
  CR-AM-11 §22, register the first release in `assessment-registry` (immutable tag/SHA reference).
