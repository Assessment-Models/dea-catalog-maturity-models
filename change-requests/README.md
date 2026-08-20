# Change Requests — `dea-catalog-maturity-models`

This index tracks every Change Request (CR) that has landed in this repository.

CRs follow the **land-as-authored** convention: the file in `change-requests/` is byte-identical to the originating attachment (md5-verified) where the full CR lives here. For cross-references where the full CR lives in another repo, the cross-reference file points at the source of truth.

| CR | Title | Type | Status | Source |
|----|-------|------|--------|--------|
| [CR-AM-01-xref](CR-AM-01-xref.md) | OpenDEA Assessment Metamodel Evolution — Maturity-decoupling cross-reference | Cross-reference | Accepted | [Full CR in assessment-tools repo](https://github.com/Assessment-Models/dea-catalog-assessment-tools/blob/main/change-requests/CR-AM-01.md) |

---

## CR-AM-01 quick links

| Document | Purpose |
|----------|---------|
| [`CR-AM-01-xref.md`](CR-AM-01-xref.md) | This repo's cross-reference; lists every CR-AM-01 section that affects this repo |
| [Full CR-AM-01 (assessment-tools repo)](https://github.com/Assessment-Models/dea-catalog-assessment-tools/blob/main/change-requests/CR-AM-01.md) | The authoritative CR spec (1870 lines, 56 sections) |
| [CR-AM-01 companion rationale](https://github.com/Assessment-Models/dea-catalog-assessment-tools/blob/main/docs/rationale/CR-AM-01-companion-rationale.md) | Explanatory companion |
| [CR-AM-01 decision-points index](https://github.com/Assessment-Models/dea-catalog-assessment-tools/blob/main/docs/rationale/CR-AM-01-decision-points.md) | Decision-point digest |

---

## Convention notes

- **Naming**: `CR-<series>-NN[-suffix].md` where `<series>` is a short tag (`AM` = Assessment Metamodel, `MM` = future specific maturity-model CRs).
- **Suffix `-xref`**: indicates a cross-reference where the full CR lives in another repo. Avoids divergence.
- **Status values**: `Proposed` → `Accepted` → `Implemented` → `Superseded`.