from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
VISUALS_DIR = PROJECT_ROOT / "visuals"
VISUAL_NOTE_PATH = PROJECT_ROOT / "docs" / "VISUAL_NOTE.md"

ACTIVE_PATH = OUTPUTS_DIR / "active_operating_by_state.csv"
PLANNED_PATH = OUTPUTS_DIR / "planned_pipeline_by_state.csv"
STATUS_PATH = OUTPUTS_DIR / "strict_all_statuses_by_status.csv"


def _read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Missing input file: {path}")
    df = pd.read_csv(path)
    if df.empty:
        raise RuntimeError(f"Input CSV is empty: {path}")
    return df


def _validate_columns(df: pd.DataFrame, required: list[str], label: str) -> None:
    missing = [column for column in required if column not in df.columns]
    if missing:
        raise RuntimeError(f"{label} is missing required columns: {missing}")


def _assert_required_limitations(text: str) -> None:
    required_phrases = [
        "strict EIA-860M",
        "not final market-total",
        "not forecasts",
        "not grid reliability",
        "not grid stress",
        "not policy",
        "not investment",
        "not operational",
        "not recommendations",
        "not infrastructure adequacy",
    ]
    for phrase in required_phrases:
        if phrase not in text:
            raise RuntimeError(f"Missing required limitation phrase: {phrase}")


def _assert_no_private_leakage(text: str) -> None:
    forbidden_terms = [
        "C:\\Users\\",
        "C:/Users/",
        "Supervisor",
        "Codex",
        "GPT",
        "gate",
        "governance",
        "internal validation",
        "portfolio",
        "recruiter",
        "career",
    ]
    lower = text.lower()
    for term in forbidden_terms:
        if term.lower() in lower:
            raise RuntimeError(f"Forbidden private/workflow term found: {term}")


def _plot_state_capacity(df: pd.DataFrame, output_path: Path, title: str, caption: str) -> None:
    _validate_columns(
        df,
        ["state", "generator_rows", "unique_plants", "capacity_mw", "energy_capacity_mwh", "missing_generator_id"],
        title,
    )

    plot_df = df.copy()
    plot_df["capacity_mw"] = pd.to_numeric(plot_df["capacity_mw"], errors="coerce")
    plot_df = plot_df.dropna(subset=["capacity_mw"])
    plot_df = plot_df.sort_values("capacity_mw", ascending=True)

    if plot_df.empty:
        raise RuntimeError(f"No numeric capacity_mw values available for {title}")

    height = max(7, 0.23 * len(plot_df) + 2.5)
    fig, ax = plt.subplots(figsize=(11, height))

    ax.barh(plot_df["state"], plot_df["capacity_mw"])
    ax.set_title(title)
    ax.set_xlabel("Capacity MW")
    ax.set_ylabel("State")
    ax.grid(axis="x", linewidth=0.4, alpha=0.35)

    fig.text(0.5, 0.01, caption, ha="center", fontsize=9)
    fig.tight_layout(rect=[0, 0.05, 1, 0.96])
    fig.savefig(output_path, dpi=180, bbox_inches="tight")
    plt.close(fig)


def _plot_status_breakdown(df: pd.DataFrame, output_path: Path) -> None:
    _validate_columns(
        df,
        ["status", "generator_rows", "unique_plants", "capacity_mw", "energy_capacity_mwh", "missing_generator_id"],
        "status breakdown",
    )

    plot_df = df.copy()
    plot_df["capacity_mw"] = pd.to_numeric(plot_df["capacity_mw"], errors="coerce")
    plot_df = plot_df.dropna(subset=["capacity_mw"])

    status_order = ["Operating", "Planned", "Other", "Retired"]
    plot_df["status_order"] = plot_df["status"].map(
        {status: index for index, status in enumerate(status_order)}
    )
    plot_df = plot_df.sort_values(["status_order", "status"])

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(plot_df["status"], plot_df["capacity_mw"])
    ax.set_title("Strict battery records by source-reported status")
    ax.set_xlabel("Source-reported status")
    ax.set_ylabel("Capacity MW")
    ax.grid(axis="y", linewidth=0.4, alpha=0.35)

    fig.text(
        0.5,
        0.01,
        "Strict EIA-860M battery classifier records grouped by source-reported status; categories should not be combined into final deployment totals.",
        ha="center",
        fontsize=9,
    )
    fig.tight_layout(rect=[0, 0.08, 1, 0.95])
    fig.savefig(output_path, dpi=180, bbox_inches="tight")
    plt.close(fig)


def _write_visual_note() -> None:
    text = """# Visual Note

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
"""
    _assert_required_limitations(text)
    _assert_no_private_leakage(text)
    VISUAL_NOTE_PATH.write_text(text, encoding="utf-8")


def main() -> None:
    VISUALS_DIR.mkdir(exist_ok=True)

    active = _read_csv(ACTIVE_PATH)
    planned = _read_csv(PLANNED_PATH)
    statuses = _read_csv(STATUS_PATH)

    _plot_state_capacity(
        active,
        VISUALS_DIR / "active_operating_by_state.png",
        "Operating strict battery records by state",
        "State-level operating records classified by the strict EIA-860M battery rule; not a final market-total or deployment estimate.",
    )

    _plot_state_capacity(
        planned,
        VISUALS_DIR / "planned_pipeline_by_state.png",
        "Planned strict battery records by state",
        "State-level planned records classified by the strict EIA-860M battery rule; not a forecast or buildout prediction.",
    )

    _plot_status_breakdown(statuses, VISUALS_DIR / "status_breakdown.png")
    _write_visual_note()

    print("visual_outputs_created=3")
    print("visual_note_created=1")


if __name__ == "__main__":
    main()
