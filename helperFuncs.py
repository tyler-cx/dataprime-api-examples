import json
import requests
from typing import Any, Dict, Iterator
from datetime import datetime, timezone

def iter_ndjson(response_text: str) -> Iterator[Dict[str, Any]]:
    """
    Parses newline-delimited JSON (NDJSON). Skips empty lines.
    """
    for line in response_text.splitlines():
        line = line.strip()
        if not line:
            continue
        yield json.loads(line)

def print_ndjson(response: requests.Response) -> None:
    if response.status_code != 200:
        print(f"Request failed: HTTP {response.status_code}")
        print(response.text)
        return
    try:
        for obj in iter_ndjson(response.text):
            print(json.dumps(obj, indent=2))
    except json.JSONDecodeError:
        print("Response is not valid NDJSON/JSON:")
        print(response.text)

def iso_utc(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")

