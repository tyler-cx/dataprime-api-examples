from dataprimeQuery import run_query
from helperFuncs import print_ndjson

# Group-by rollup (avg/max/count per dimension)
query = """
source spans
| groupby $l.subsystemName
    avg(duration) as avg_duration,
    max(duration) as max_duration,
    count() as span_count
| orderby span_count desc
| limit 50
""".strip()

resp = run_query(query)
print_ndjson(resp)