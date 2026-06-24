import requests
from bs4 import BeautifulSoup
from functools import lru_cache

BASE_URL = "https://www.eia.gov/electricity/data/eia860m/"
HEADERS = {"User-Agent": "Mozilla/5.0"}


@lru_cache(maxsize=1)
def fetch_index():
    r = requests.get(BASE_URL, headers=HEADERS, timeout=30)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    links = []

    for a in soup.find_all("a", href=True):
        href = a["href"]

        if "generator" in href and href.endswith(".xlsx"):
            if href.startswith("http"):
                links.append(href)
            else:
                links.append("https://www.eia.gov" + href)

    return sorted(set(links))


def select_latest():
    links = fetch_index()

    if not links:
        raise RuntimeError("No EIA links found")

    # prefer recent years first
    recent = [l for l in links if any(y in l for y in ["2026", "2025", "2024", "2023"])]

    pool = recent if recent else links

    priority_months = [
        "december",
        "november",
        "october",
        "september",
        "august"
    ]

    for m in priority_months:
        for l in pool:
            if m in l.lower():
                return l

    return pool[-1]
