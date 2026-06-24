import pandas as pd

HEADER_ROW = 2

TARGET_SHEETS = [
    "Operating",
    "Planned",
    "Retired",
    "Canceled or Postponed",
    "Operating_PR",
    "Planned_PR",
    "Retired_PR",
]


def load_eia860m(filepath: str):
    xls = pd.ExcelFile(filepath)
    print("Sheets:", xls.sheet_names)

    dfs = []

    for sheet in TARGET_SHEETS:
        if sheet not in xls.sheet_names:
            continue

        df = pd.read_excel(filepath, sheet_name=sheet, header=HEADER_ROW)
        df = df.dropna(how="all")
        df["__sheet"] = sheet
        dfs.append(df)

    if not dfs:
        raise RuntimeError("No target EIA-860M sheets found.")

    combined = pd.concat(dfs, ignore_index=True)
    print("Combined shape:", combined.shape)
    return combined
