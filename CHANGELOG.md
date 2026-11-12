[Unreleased]
└── pending
    └── New model: Autonomous Operations (`dea:maturity-autonomous-operations`) — proposals/0002
        ├── maturity-models/v1-alpha/autonomous-operations.yaml (5 canonical-band levels + AO OODA stages, dimensions/scoring/assessment blocks) + maturity-models/autonomous-operations/ repo-ready bundle (model/scale/evaluation/dimensions + examples + scripts + GOVERNANCE)
        │   └── harvested & cleaned from an industry AO maturity workbook v1.8.0 (6 dims / 32 sub-dims / 151 criteria) → 157 criteria
        │       (2 cross-dimension duplicates merged, 8 gap criteria added, IDs/structure defects fixed)
        ├── proposals/0002-autonomous-operations-maturity-model.md (gap register G1–G20, scoring & ladder design, v1.8.0 mapping)
        ├── maturity-models/index.yaml: content entry + relationships + tags; catalog version 1.0.0-alpha → 1.1.0-alpha (MINOR: new domain model)
        ├── README.md: catalog index row + note
        └── VERSION: 1.1.0-alpha
    └── CR-AM-01-xref: cross-reference to CR-AM-01 (assessment-tools). Documents the Maturity-Decoupling roadmap for this catalog.
        ├── change-requests/CR-AM-01-xref.md (cross-reference, lists every CR-AM-01 section affecting this repo)
        ├── change-requests/README.md (CR index for this repo)
        └── README.md: added Maturity Model Independence section + parking-lot note
    NOTE: No YAML changes. No schema changes. No band-name or score-range changes.
          PR #1 (docs/maturity-scoring-v2-proposal) stays open and is resolved separately.

1.0.0-alpha
└── initial release
    ├── 5 maturity models across EA, modernisation, technology, operations, services delivery
    ├── Uniform 5-level scoring rubric (Ad Hoc → Optimising)
    ├── Each model: characteristics, exit criteria, evidence examples
    ├── Cross-references to assessment-tools and reference-architecture
    └── GitHub Actions CI validates schema and level coverage