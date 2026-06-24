# Methodology

## Workflow overview

The pipeline follows these stages:

1. resolve the EIA-860M source file
2. download the workbook
3. load selected workbook sheets
4. apply explicit header handling
5. classify strict battery records
6. create generator-level outputs
7. create plant-level aggregation outputs
8. separate records into status-specific views
9. run validation checks before public-facing use

## Strict battery classification

The current classifier is intentionally conservative.

Battery records are included only when source fields support battery classification through technology or battery-code signals.

Soft text matches are not used as the accepted public-facing baseline.

## Entity handling

The pipeline creates generator-level entity outputs and plant-level aggregate outputs.

Plant-level aggregation is used for internal analytical review and validation.

## Status separation

The workflow separates:

- active operating records
- planned records
- retired records
- canceled or postponed records
- all strict-status records

This separation prevents inactive or planned records from being presented as active deployment.

## Limitation

The methodology is designed for source-boundary tracking and validation-first analysis.

It is not a forecasting model, investment model, policy model, or grid-stress model.
