# Validation

## Validation approach

This project uses staged validation before public-facing documentation or claims.

Validation checks include:

- source availability
- workbook loading
- header detection
- required column presence
- battery classification behavior
- false-positive review
- generator entity uniqueness
- plant-level aggregation checks
- status-specific view separation
- missingness checks
- capacity reasonableness checks

## Current accepted internal baseline

The current accepted internal baseline uses:

- strict v4.5 classifier
- v5 generator entity outputs
- v5 plant aggregation outputs
- validation v3 active-scope views
- internal summary layer v1

## Public-use boundary

Validation currently supports limited technical documentation.

Validation does not yet authorize:

- charts
- dashboards
- market-size claims
- investment claims
- policy claims
- forecasts
- definitive deployment totals

## Required wording for any future numeric use

Any future numeric value must be labeled as:

"Based on a strict EIA-860M classifier output, not a final market-total estimate."
