# Proposal 0001 — Non-Linear Maturity Scoring: Rename, Rescale, Effort Coefficients

| Field | Value |
|-------|-------|
| Status | PROPOSED |
| Date | 2026-08-18 |
| Author | Coder (for eaojnr) |
| Scope | `maturity-models/index.yaml` bands; all `maturity-models/v1-alpha/*.yaml` level definitions |
| Consumers affected | dea-cli (`dea maturity score`), dea-web-viewer (radar charts), dea-catalog-assessment-tools |

---

## 1. Context

The current five-level model (Ad Hoc / Defined / Managed / Quantitatively Managed /
Optimising) is inherited from CMMI-era vocabulary and uses a 0–100 scale split into
bands of 25/25/25/15/10 points.

Two structural criticisms:

1. **Archaic naming.** The names describe 1990s software-process culture, not modern
   engineering organisations. "Quantitatively Managed" in particular is a barrier to
   adoption outside process-improvement circles.

2. **Linear presentation hides diminishing returns.** Capability maturity exhibits two
   crossing curves:
   - **Effort is superlinear** (roughly exponential): each level costs
     disproportionately more organisational effort than the previous. L1→L2 is
     documentation; L3→L4 requires metrics infrastructure and instrumented pipelines;
     L4→L5 requires cultural and feedback-loop rewiring.
   - **Value is sublinear** (roughly logarithmic): the largest outcome gains come
     early (L1→L3 eliminates chaos and establishes repeatability). L4→L5 gains are
     real but marginal — optimisation at the edges.

   The narrowing top bands in the current model already encode this *implicitly*.
   This proposal makes it *explicit and computable*.

### Caveats (model honesty)

- Returns are not monotonic everywhere. Some transitions unlock **compounding**
  returns (crossing into measured, SLO-driven operations enables automation that
  accelerates everything below). These are documented per level as `inflection`
  notes, not treated as violations.
- Maturity is multi-axis. Diminishing returns apply per domain; portfolio
  allocation across domains is a separate concern (out of scope).

---

## 2. Proposed Level Names

| Level | Current (v1-alpha) | Proposed | Rationale |
|-------|--------------------|----------|-----------|
| 1 | Ad Hoc | **Emergent** | Practice exists but is person-dependent and informal |
| 2 | Defined | **Structured** | Documented, agreed, but inconsistently enforced |
| 3 | Managed | **Systematic** | Formal, tooling-enabled, governance active |
| 4 | Quantitatively Managed | **Adaptive** | Metrics-driven; organisation senses and responds |
| 5 | Optimising | **Self-Optimising** | Continuous improvement is autonomous, not programme-driven |

Design rules for the new names:
- Single word per level (current set mixes 1–3 words; inconsistent in charts/CLI).
- All adjectives describing *the organisation's state*, not the process regime.
- No acronym collision with existing DEA catalogue vocabulary.

---

## 3. Proposed Scoring Bands (Non-Linear)

Band width now explicitly represents **effort-to-traverse**, not linear progress:

| Level | Name | Range | Width | Effort Multiplier |
|-------|------|-------|-------|-------------------|
| 1 | Emergent | 0–20 | 20 | 1.0× |
| 2 | Structured | 21–45 | 25 | 1.5× |
| 3 | Systematic | 46–70 | 25 | 2.5× |
| 4 | Adaptive | 71–88 | 18 | 4.0× |
| 5 | Self-Optimising | 89–100 | 12 | 6.0× |

Rationale:
- L1 shrinks (25→20): escaping chaos is high-value, comparatively low-effort. A small
  score band reflects how quickly this should happen if leadership commits.
- L4/L5 narrow further (15→18/12 distribution shifts): each point at the top costs
  more to earn; fewer points available signals diminishing headroom.
- **Effort multiplier** is the relative organisational cost of earning one point
  *within* that band, normalised to L1 = 1.0×. Multipliers are superlinear
  (1.0 → 1.5 → 2.5 → 4.0 → 6.0), consistent with the exponential effort curve.

---

## 4. Effort-Adjusted Value (computable ROI signal)

Raw score answers "where are we?" It does not answer "was it worth it, and what's
the next marginal point worth?" The effort multiplier enables a second computed
metric:

```
value_realised(score) = Σ over bands b:  points_earned_in(b) / effort_multiplier(b)
```

Worked example — an organisation scoring 80 (Adaptive):

| Band | Points earned | Multiplier | Value units |
|------|---------------|------------|-------------|
| Emergent | 20 | 1.0 | 20.0 |
| Structured | 25 | 1.5 | 16.7 |
| Systematic | 25 | 2.5 | 10.0 |
| Adaptive | 10 | 4.0 | 2.5 |
| **Total** | **80 (raw)** | | **49.2 (effort-adjusted)** |

Interpretation for tooling and governance dashboards:
- **Raw score** (80/100) — capability position, comparable across domains.
- **Effort-adjusted value** (49.2) — diminishing-returns curve made visible: the
  last 10 points delivered 2.5 value units; the first 20 delivered 20.
- **Marginal point cost** at Adaptive = 4.0× baseline → next-point ROI can be
  compared *across domains* (raising Operations from 68→70 costs 2.5×/point;
  raising Technology from 44→46 crosses into Systematic at 2.5×/point) — this is
  the portfolio-allocation signal the current model cannot produce.

---

## 5. Migration Plan (on approval)

Phased, no big-bang:

1. **Phase A — registry**: add proposed bands + `effort_multiplier` to
   `maturity-models/index.yaml` under a new `bands_v2` block alongside `bands`.
   v1 stays canonical; v2 is advisory. Tooling reads v1; dashboards may preview v2.
2. **Phase B — model files**: cut `maturity-models/v1-beta/` copies with new level
   ids (`level-1-emergent` … `level-5-self-optimising`), `legacy_name` alias field,
   and `score_range` updated to v2 bands. v1-alpha frozen, not edited.
3. **Phase C — consumers**: dea-cli gains `--scoring v2`; dea-web-viewer renders
   both band sets (toggle). Assessment-tools mappings updated.
4. **Phase D — promotion**: after one full assessment cycle on v2, v2 becomes
   canonical; v1-alpha archived with `superseded-by` links.

No model content (characteristics, exit criteria, evidence) changes in this
proposal — only names, bands, and scoring metadata.

---

## 6. Backward Compatibility

- v1-alpha ids (`level-1-ad-hoc` etc.) remain valid forever in v1-alpha files.
- `legacy_name` alias on every v2 level lets existing assessment data resolve.
- Band boundary change (25→20, etc.) is a **scoring change**, not a data change;
  historical raw scores remain meaningful because underlying assessment answers
  are unchanged — only the band they map to shifts. Dea-cli will report both
  mappings during the transition window.

---

## 7. Verification (acceptance criteria for Phase B)

- `index.yaml` validates: v2 bands are contiguous, non-overlapping, cover 0–100.
- Every v1-beta level carries `legacy_name` matching its v1-alpha counterpart.
- Worked example in §4 reproduced by dea-cli unit test (score 80 → value 49.2 ± 0.1).
- Viewer renders 5-band radar with new names and v2 boundaries behind a feature flag.
