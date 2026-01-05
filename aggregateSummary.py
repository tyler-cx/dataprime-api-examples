from dataprimeQuery import run_query
from helperFuncs import print_ndjson

# This uses aggregate to compute stats over the full dataset (not grouped)
query = """
source spans
| aggregate
    count() as total_spans
""".strip()

resp = run_query(query)
print_ndjson(resp)