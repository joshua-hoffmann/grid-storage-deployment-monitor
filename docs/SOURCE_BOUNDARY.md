# Source Boundary

## Primary source

This project uses EIA-860M generator data as its current source boundary.

## Scope of use

The source is used to identify and process generator records that can be classified as battery records under a strict rule.

## Current boundary

The project separates records by source-reported status:

- operating
- planned
- retired
- canceled or postponed

These categories are kept separate to avoid treating all records as active deployment.

## Exclusions

The current strict battery workflow does not treat every storage-related record as a battery record.

Non-battery storage technologies are excluded or separated where identifiable.

## Claim limitation

Outputs from this project are classifier-derived and source-boundary constrained.

They should not be interpreted as final national market totals or complete deployment estimates.
