import requests
from pathlib import Path

def download(url: str, path: str):
    print(f"Downloading: {url}")

    r = requests.get(url, timeout=60)

    if r.status_code != 200:
        raise RuntimeError(f"Failed download: {r.status_code}")

    Path(path).parent.mkdir(parents=True, exist_ok=True)

    with open(path, "wb") as f:
        f.write(r.content)

    print("Saved:", path)
    return path
