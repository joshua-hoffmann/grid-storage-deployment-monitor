# Data Dictionary

## Public output files

### outputs/active_operating_by_state.csv

State-level summary of records classified as strict battery records with operating status.

### outputs/planned_pipeline_by_state.csv

State-level summary of records classified as strict battery records with planned status.

### outputs/strict_all_statuses_by_status.csv

Status-level summary of all strict battery classifier records.

## Common fields

### state

State or territory code reported in the EIA-860M source.

### generator_rows

Number of generator-level records in the view.

### unique_plants

Number of unique plant identifiers represented in the view.

### capacity_mw

Sum of nameplate capacity in MW for the records in the view.

### energy_capacity_mwh

Sum of nameplate energy capacity in MWh where available in the source.

### missing_generator_id

Count of rows where generator identifier is missing.

## Interpretation boundary

All values should be interpreted as strict EIA-860M classifier outputs, not final market-total estimates.
