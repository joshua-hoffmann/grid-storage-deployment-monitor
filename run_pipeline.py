from src.eia_resolver import select_latest
from src.downloader import download
from src.loader import load_eia860m
from src.transformer_v45 import transform

RAW = "data/raw/eia860m.xlsx"

def main():

    print("=== STEP 1: RESOLVE ===")
    url = select_latest()
    print(url)

    print("=== STEP 2: DOWNLOAD ===")
    download(url, RAW)

    print("=== STEP 3: LOAD ===")
    df = load_eia860m(RAW)

    print("=== STEP 4: TRANSFORM v4.5 ===")
    df_out = transform(df, "EIA-860M")

    output_path = "data/processed/eia_v45.csv"
    df_out.to_csv(output_path, index=False)

    battery_rows = int(df_out["is_battery"].sum())
    hard_rows = int((df_out["battery_class"] == "HARD").sum())
    excluded_rows = int((df_out["battery_class"] == "EXCLUDED_STORAGE").sum())

    print("SAVED:", output_path)
    print("ROWS:", len(df_out))
    print("BATTERY ROWS:", battery_rows)
    print("HARD CLASS:", hard_rows)
    print("EXCLUDED STORAGE:", excluded_rows)
    print("STATE NON-NULL:", int(df_out["state"].notna().sum()))

    if battery_rows == 0:
        raise RuntimeError("Schema v4.5 produced zero battery rows. Stop.")

if __name__ == "__main__":
    main()
