from dataprimeQuery import run_query
from helperFuncs import print_ndjson

query = r"""
source logs
| filter $d.message != null
| extract $d.message into $d.http using regexp(e=/status=(?<status>\d{3}).*duration_ms=(?<duration_ms>\d+)/)
| choose $m.timestamp, $d.serviceName, $d.http.status, $d.http.duration_ms, $d.message
| limit 50
""".strip()

resp = run_query(query)
print_ndjson(resp)