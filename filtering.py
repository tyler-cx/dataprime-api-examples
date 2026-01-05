from dataprimeQuery import run_query
from helperFuncs import print_ndjson

"""
It is advisable to use filter first to narrow results for faster responses.
It is also commonplace to chain multiple filters together.
Choose allows you to return only the data that you need.
Orderby + limit provide "latest N" style views. 

*** The keys in this query (e.g. $d.k8s.namespace) may not exist in your environment, feel free to modify as you see fit.
"""
query = """
source logs
| filter $d.k8s.namespace == 'prod'
| filter $m.severity == ERROR
| choose $m.timestamp, $d.k8s.namespace, $d.serviceName, $d.message
| orderby $m.timestamp desc
| limit 20
""".strip()

resp = run_query(query)
print_ndjson(resp)