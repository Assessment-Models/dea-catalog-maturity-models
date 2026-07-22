# Contributing to dea-catalog-maturity-models

## Adding a new maturity model

1. Fork this repo
2. Create `maturity-models/v1-alpha/<your-domain>.yaml`
3. Use the schema — see `maturity-models/v1-alpha/ea-capability.yaml` as a worked example
4. All five levels are required (Ad Hoc, Defined, Managed, Quantitatively Managed, Optimising)
5. Each level needs: `summary`, `characteristics`, `exit_criteria`, `evidence`
6. Add the model to `maturity-models/index.yaml` `content:` array
7. Add a relationship entry for your domain in `index.yaml` `relationships:`
8. Open a PR — CI validates schema and level coverage

## Updating an existing model

- PR with rationale for changes
- Increment version (PATCH for clarifications, MINOR for new evidence examples)
- CHANGELOG.md entry required

## Versioning

This catalog follows Semantic Versioning:
- **MAJOR** — level definitions change (new band added, band definitions change)
- **MINOR** — new domain model added
- **PATCH** — clarifications, corrections, additional evidence examples

## Code of Conduct

Be respectful. Argue ideas, not people. PR reviews are learning opportunities.