# Usage

This document describes how to run the project locally and how to interpret the generated files.

## 1. Install dependencies

Run:

    pip install -r requirements.txt

## 2. Run the pipeline

Run:

    python run_pipeline.py

The pipeline resolves an EIA-860M generator workbook, downloads the source file, loads selected sheets, applies the strict battery classifier, and writes processed files under data/processed/.

## 3. Run the repository health check

Run:

    python tools/health_check.py

The health check verifies the expected public file surface, scans public documentation for private/internal terms, and checks required imports.

## 4. Public outputs

The repository includes selected public summary outputs under outputs/:

- outputs/active_operating_by_state.csv
- outputs/planned_pipeline_by_state.csv
- outputs/strict_all_statuses_by_status.csv

These files are committed so reviewers can inspect the current public output layer without rerunning the full pipeline.

## 5. Local generated files

Running the pipeline may create or update files under:

- data/raw/
- data/processed/

These folders are intentionally ignored by Git because they contain downloaded or generated data.

## 6. Interpretation boundary

All public output values should be interpreted as:

> Based on a strict EIA-860M classifier output, not a final market-total estimate.

The project does not publish forecasts, investment conclusions, policy conclusions, grid-stress scores, or final national deployment totals.

## 7. Recommended review order

1. README.md
2. docs/SOURCE_BOUNDARY.md
3. reports/PUBLIC_RESULTS_BOUNDARY.md
4. reports/VALIDATION_SUMMARY.md
5. outputs/README.md
6. outputs/*.csv
