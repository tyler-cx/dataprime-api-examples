import json
import os
import requests
from datetime import datetime, timedelta, timezone
from helperFuncs import iso_utc

# Be sure to use the endpoint relevant to your org, and an API key with sufficient permissions.
DEFAULT_ENDPOINT = os.getenv("CORALOGIX_DATAPRIME_ENDPOINT", "https://api.us1.coralogix.com/api/v1/dataprime/query")
DEFAULT_API_KEY = os.getenv("CORALOGIX_API_KEY", "")

def run_query(query: str, endpoint: str = DEFAULT_ENDPOINT, api_key: str = DEFAULT_API_KEY, timeout: int = 60) -> requests.Response:

    if not api_key:
        raise ValueError("Missing CORALOGIX_API_KEY (env var) or api_key parameter.")

    # I have added a timeframe of one hour, feel free to change.
    now = datetime.now(timezone.utc)
    start = now - timedelta(hours=1)

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    payload = {
        "query": query, 
        "metadata": {
            # Use tier to notate frequent search vs archive
            "tier": "TIER_ARCHIVE",
            "syntax": "QUERY_SYNTAX_DATAPRIME",
            "startDate": iso_utc(start),
            "endDate": iso_utc(now),
            # I have put this here as an abitrary limit, large requests should be sent to the background query API
            "limit": 2000 
        }    
    }
    return requests.post(endpoint, headers=headers, json=payload, timeout=timeout)

