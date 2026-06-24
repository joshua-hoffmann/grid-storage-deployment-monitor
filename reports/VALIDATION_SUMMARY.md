# Validation Summary

This project uses a validation-first workflow to avoid presenting raw classifier output as a final market estimate.

## Current accepted public boundary

The current public outputs are based on a strict EIA-860M battery classifier.

The classifier is intentionally conservative. It includes battery records where the EIA technology field or battery-code fields support a battery classification.

## Current public output files

- outputs/active_operating_by_state.csv
- outputs/planned_pipeline_by_state.csv
- outputs/strict_all_statuses_by_status.csv

## Validation checks completed

The current workflow includes checks for:

- workbook loading and header detection
- strict battery classification
- exclusion of non-battery storage technologies where identifiable
- generator-level entity uniqueness
- state and generator identifier missingness
- separation of operating, planned, retired, and canceled/postponed records
- status-specific summary generation

## Important limitation

These outputs are based on a strict EIA-860M classifier output, not a final market-total estimate.

The repository does not claim definitive U.S. battery market size, deployment totals, investment implications, policy conclusions, or forecasts.
