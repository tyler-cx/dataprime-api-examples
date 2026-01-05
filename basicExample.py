from dataprimeQuery import run_query
from helperFuncs import print_ndjson

"""
Any valid Dataprime query should work.
Source is generally logs or spans, but their are potential other datasets such as "system" datasets for diagnostics.
Each query will expect at a minimun a source, and usually at least one keyword.
Keywords are as follows

[filter,f,where,block,b,create,c,add,a,move,m,remove,r,replace,redact,choose,select,convert,conv,extract,e,limit,orderby,sortby,order by,sort by,find,text,wildfind,wildtext,lucene,groupby,gb,multigroupby,aggregate,agg,distinct,count,top,bottom,countby,enrich,join,union,explode,dedupeby,stitch]

"""
query = "source logs | limit 10"

resp = run_query(query)
print_ndjson(resp)
