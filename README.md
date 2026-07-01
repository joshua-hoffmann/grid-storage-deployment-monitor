# Grid Storage Deployment Monitor

A validation-first data pipeline for turning EIA-860M generator records into a strict, source-boundary constrained battery storage inventory layer.

The project focuses on one narrow but important problem:

> How can battery storage generator records be identified, separated by status, and summarized without overstating what the source data can support?

## What this project produces

The repository includes public, source-boundary constrained outputs:

- `outputs/active_operating_by_state.csv`
- `outputs/planned_pipeline_by_state.csv`
- `outputs/strict_all_statuses_by_status.csv`

These outputs are derived from a strict EIA-860M battery classifier and separated by project status.

## Why this matters

EIA-860M generator data includes multiple storage-related technologies and project statuses. Treating all storage-related records as active battery deployment can create misleading results.

This project therefore separates:

- operating battery records
- planned battery records
- retired records
- canceled or postponed records
- non-battery storage technologies where identifiable

## Current classifier boundary

The current public baseline uses a strict battery-only rule.

Battery records are included only when the EIA source fields support battery classification through:

- EIA technology classified as `Batteries`
- battery-code signals where available

The current public baseline does not use broad text matching as the accepted output basis.

## Public outputs

### `outputs/active_operating_by_state.csv`

State-level summary of strict battery records with operating status.

### `outputs/planned_pipeline_by_state.csv`

State-level summary of strict battery records with planned status.

### `outputs/strict_all_statuses_by_status.csv`

Status-level summary of all strict battery classifier records.

## Reports

- `reports/VALIDATION_SUMMARY.md`
- `reports/DATA_DICTIONARY.md`
- `reports/PUBLIC_RESULTS_BOUNDARY.md`
- `docs/SOURCE_BOUNDARY.md`
- `docs/METHODOLOGY.md`
- `docs/VALIDATION.md`

## Pipeline overview

The pipeline:

1. resolves the EIA-860M generator workbook
2. downloads the source file
3. loads selected workbook sheets with explicit header handling
4. applies a strict battery classifier
5. writes generator-level classified output
6. supports internal aggregation and validation views
7. publishes selected source-boundary constrained summary outputs

## Run the pipeline

```bash
python run_pipeline.py
```

The pipeline writes processed files under `data/processed/`.

Raw and processed data are not committed to the repository.

## Interpretation boundary

The public outputs should be read as:

> Based on a strict EIA-860M classifier output, not a final market-total estimate.

This repository does not present forecasts, investment conclusions, policy conclusions, grid-stress scores, or final national deployment totals.

## Current status

The current repository state supports:

- technical review
- source-boundary review
- validation review
- limited public summary outputs

Charts, dashboards, and broader analytical claims are intentionally not included in the current public scope.
## Visual outputs

This project includes source-bounded visual outputs:

- `visuals/active_operating_by_state.png`
- `visuals/planned_pipeline_by_state.png`
- `visuals/status_breakdown.png`

See `docs/VISUAL_NOTE.md` for chart captions, sorting rules, status separation, and limitations.

