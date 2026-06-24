import pandas as pd


def norm(value):
    if value is None:
        return ""
    return str(value).lower().strip()


def clean_value(value):
    if value is None:
        return None
    if pd.isna(value):
        return None
    text = str(value).strip()
    if text == "" or text.lower() == "nan":
        return None
    return value


def get_value(row, candidates):
    for key in candidates:
        if key in row.index:
            value = clean_value(row.get(key))
            if value is not None:
                return value
    return None


def detect_battery(row, sheet):
    flags = []

    energy_source = norm(get_value(row, [
        "Energy Source Code",
        "Energy Source Code 1",
        "Energy Source 1",
        "Energy Source",
    ]))

    prime_mover = norm(get_value(row, [
        "Prime Mover Code",
        "Prime Mover",
    ]))

    technology = norm(get_value(row, [
        "Technology",
        "Technology Description",
        "Generator Technology",
    ]))

    if "pumped storage" in technology or "hydroelectric pumped storage" in technology:
        flags.append("excluded_pumped_storage")
        return False, 0.0, "EXCLUDED_STORAGE", 0.0, flags

    if "flywheel" in technology:
        flags.append("excluded_flywheel")
        return False, 0.0, "EXCLUDED_STORAGE", 0.0, flags

    if technology != "batteries" and "battery" not in technology and energy_source != "ba" and prime_mover != "ba":
        return False, 0.0, "NONE", 0.0, flags

    if energy_source == "ba" or prime_mover == "ba":
        flags.append("hard_ba_code")

    if technology == "batteries" or "battery" in technology:
        flags.append("hard_battery_technology")

    return True, 1.0, "HARD", 10.0, flags


def map_status(sheet):
    s = norm(sheet)

    if "operating" in s:
        return "Operating"
    if "planned" in s:
        return "Planned"
    if "retired" in s:
        return "Retired"
    if "canceled" in s or "postponed" in s:
        return "Other"

    return "Other"


def transform(df, sheet):
    out = []

    for _, row in df.iterrows():
        source_sheet = row.get("__sheet", sheet)
        is_battery, confidence, battery_class, score, flags = detect_battery(row, source_sheet)

        out.append({
            "plant_id": get_value(row, ["Plant ID", "Plant Code"]),
            "generator_id": get_value(row, ["Generator ID"]),
            "plant_name": get_value(row, ["Plant Name"]),
            "state": get_value(row, ["Plant State", "State"]),
            "county": get_value(row, ["County"]),

            "technology": get_value(row, ["Technology"]),
            "prime_mover": get_value(row, ["Prime Mover Code", "Prime Mover"]),
            "energy_source": get_value(row, ["Energy Source Code", "Energy Source Code 1", "Energy Source 1", "Energy Source"]),

            "status": map_status(source_sheet),

            "capacity_mw": get_value(row, ["Nameplate Capacity (MW)"]),
            "summer_capacity_mw": get_value(row, ["Net Summer Capacity (MW)", "Summer Capacity (MW)"]),
            "winter_capacity_mw": get_value(row, ["Net Winter Capacity (MW)", "Winter Capacity (MW)"]),
            "energy_capacity_mwh": get_value(row, ["Nameplate Energy Capacity (MWh)"]),
            "dc_net_capacity_mw": get_value(row, ["DC Net Capacity (MW)"]),

            "latitude": get_value(row, ["Latitude"]),
            "longitude": get_value(row, ["Longitude"]),

            "report_sheet": source_sheet,

            "is_battery": is_battery,
            "battery_confidence": confidence,
            "battery_class": battery_class,
            "signal_score": score,
            "signal_flags": ";".join(flags),
        })

    return pd.DataFrame(out)
