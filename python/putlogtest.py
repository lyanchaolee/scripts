#!/usr/bin/env python

import httplib, urllib

conn = httplib.HTTPConnection("localhost:8000")
params = urllib.urlencode({'@logtype': 'test', '@logdetail': 'test'})
conn.request("GET", "/worklog/putlog/", params)
res = conn.getresponse()

print res.read()