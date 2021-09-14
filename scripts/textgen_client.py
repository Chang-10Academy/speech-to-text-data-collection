import http.client, json
conn = http.client.HTTPConnection("localhost:8000")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.read().decode('utf-8'))
