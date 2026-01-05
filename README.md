# Coralogix DataPrime API Examples (Python)

A small set of Python examples showing how to query Coralogix data using the DataPrime HTTP API:

- basic queries
- filtering + field selection
- aggregations (`aggregate`, `groupby`)
- sorting / top-N
- parsing & enrichment (`extract` + regexp)

## Prerequisites

- Python 3.9+
- `requests`

Install deps:

```bash
pip install -r requirements.txt
```

## Notes

- The functionality for running the query resides in the dataprimeQuery.py file. I also have a few helper functions that are for parsing JSON and dates.
