from dataprimeQuery import run_query
from helperFuncs import print_ndjson

query = """
source logs
| filter $m.severity == ERROR
| groupby resource.attributes['k8s.container.name'] aggregate count() as error_count
| orderby error_count desc
""".strip()

resp = run_query(query)
print_ndjson(resp)