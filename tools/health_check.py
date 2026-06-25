from pathlib import Path
import importlib
import sys

REQUIRED_FILES = [
    ".gitignore",
    "README.md",
    "USAGE.md",
    "requirements.txt",
    "run_pipeline.py",
    "src/eia_resolver.py",
    "src/downloader.py",
    "src/loader.py",
    "src/transformer_v45.py",
    "docs/SOURCE_BOUNDARY.md",
    "docs/METHODOLOGY.md",
    "docs/VALIDATION.md",
    "outputs/README.md",
    "outputs/active_operating_by_state.csv",
    "outputs/planned_pipeline_by_state.csv",
    "outputs/strict_all_statuses_by_status.csv",
    "reports/README.md",
    "reports/VALIDATION_SUMMARY.md",
    "reports/DATA_DICTIONARY.md",
    "reports/PUBLIC_RESULTS_BOUNDARY.md",
]

PUBLIC_TEXT_FILES = [
    "README.md",
    "USAGE.md",
    "docs/SOURCE_BOUNDARY.md",
    "docs/METHODOLOGY.md",
    "docs/VALIDATION.md",
    "outputs/README.md",
    "reports/README.md",
    "reports/VALIDATION_SUMMARY.md",
    "reports/DATA_DICTIONARY.md",
    "reports/PUBLIC_RESULTS_BOUNDARY.md",
]

PRIVATE_TERMS = [
    "portfolio",
    "recruiter",
    "career",
    "GPT",
]

REQUIRED_IMPORTS = [
    "pandas",
    "openpyxl",
    "requests",
    "bs4",
    "src.eia_resolver",
    "src.downloader",
    "src.loader",
    "src.transformer_v45",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def check_required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not Path(path).exists()]
    if missing:
        fail("Missing required files: " + ", ".join(missing))
    print("PASS: required file check")


def check_private_terms() -> None:
    for file_path in PUBLIC_TEXT_FILES:
        text = Path(file_path).read_text(encoding="utf-8", errors="ignore")
        lower = text.lower()
        for term in PRIVATE_TERMS:
            if term.lower() in lower:
                fail(f"Private/internal term found in {file_path}: {term}")
    print("PASS: private term scan")


def check_imports() -> None:
    for module_name in REQUIRED_IMPORTS:
        importlib.import_module(module_name)
    print("PASS: import check")


def main() -> None:
    print("Repository health check")
    check_required_files()
    check_private_terms()
    check_imports()
    print("PASS: repository health check completed")


if __name__ == "__main__":
    main()
