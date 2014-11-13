import httplib


conn = httplib.HTTPConnection('test.gewala.net')
conn.request("GET", "/openapi2/router/rest?appkey=xiaomitv&format=xml&method=com.gewara.partner.movie.opiSeatList&sign=C8E4C7F641817C53B323F0995E92D896&signmethod=MD5&timestamp=2014-08-26%2009:11:44&v=1.0&mpid=36087373")
r = conn.getresponse()
print r.status, r.reason


content = r.read()
print content
conn.close()
