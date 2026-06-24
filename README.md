# Grid Storage Deployment Monitor

A source-boundary constrained data pipeline for processing EIA-860M generator data and identifying battery storage records under a strict classification rule.

## Current scope

This repository currently focuses on:

- resolving and downloading EIA-860M generator data
- loading the workbook with explicit header handling
- applying a strict battery-only classifier
- producing generator-level and plant-level internal outputs
- separating operating, planned, retired, and canceled/postponed records
- maintaining validation gates before public-facing claims

## Current classifier boundary

The current strict classifier is designed to include battery records only when the source fields support a battery classification.

The current workflow does not treat all storage technologies as batteries.

Excluded or separated technologies include non-battery storage categories such as pumped storage and flywheels.

## What this project does not claim

This project does not currently claim:

- definitive U.S. battery market size
- final validated deployment totals
- investment implications
- policy conclusions
- grid-stress conclusions
- forecasts
- market opportunity rankings

## Repository status

The current repository state supports limited technical documentation only.

Charts, dashboards, market-size claims, and executive summaries are not part of the current public scope.

## Documentation

- docs/SOURCE_BOUNDARY.md
- docs/METHODOLOGY.md
- docs/VALIDATION.md
