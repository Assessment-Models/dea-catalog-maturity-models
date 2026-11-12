[Unreleased]
├── proposal 0002: Digital Transformation Operationalized maturity & assessment model
│   ├── maturity-models/v1-alpha/digital-transformation-operationalized.yaml (new model: 6 dimensions / 23 sub-dimensions / 70 criteria, 5 evidence-anchored levels each, 12 transversal levers, weighted 0-100 scoring with cumulative advancement gates)
│   ├── proposals/0002-digital-transformation-operationalized.md (gap review of TM Forum DMM v5.0.2, grounded definitions, design rationale)
│   ├── maturity-models/index.yaml: content + relationship entries
│   ├── README.md: catalog table row
│   └── NOTE: no changes to existing models, bands, or score ranges
└── pending
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