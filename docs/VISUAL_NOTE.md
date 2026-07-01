# Visual Note

## Purpose

These visuals provide a source-bounded view of strict EIA-860M battery classifier summaries. They are intended to make the public CSV outputs easier to inspect without expanding the project claim.

## Source files used

- `outputs/active_operating_by_state.csv`
- `outputs/planned_pipeline_by_state.csv`
- `outputs/strict_all_statuses_by_status.csv`

## Generated visuals

- `visuals/active_operating_by_state.png`
- `visuals/planned_pipeline_by_state.png`
- `visuals/status_breakdown.png`

## Chart captions

### Operating strict battery records by state

State-level operating records classified by the strict EIA-860M battery rule; not a final market-total or deployment estimate.

### Planned strict battery records by state

State-level planned records classified by the strict EIA-860M battery rule; not a forecast or buildout prediction.

### Strict battery records by source-reported status

Strict EIA-860M battery classifier records grouped by source-reported status; categories should not be combined into final deployment totals.

## Sorting rule

State-level bar charts are sorted by `capacity_mw` for readability only. This sorting is not a leaderboard, ranking, recommendation, or assessment of state performance.

## Status separation rule

Operating, planned, other, and retired records are shown separately. Planned records are source-reported planned records, not forecasts or buildout predictions. Categories should not be combined into final market-total estimates.

## Limitations

These visuals are strict EIA-860M classifier summaries. They are not final market-total estimates, not forecasts, not grid reliability findings, not grid stress findings, not policy conclusions, not investment conclusions, not operational advice, not recommendations, and not infrastructure adequacy findings.
