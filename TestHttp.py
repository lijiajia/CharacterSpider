import httplib


conn = httplib.HTTPConnection('tool.httpcn.com')
conn.request("GET", "/Html/KangXi/BuShou/1_1.html")
r = conn.getresponse()
print r.status, r.reason


content = r.read()
print content
conn.close()
