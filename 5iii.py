import requests
url = 'http://172.17.50.43/algenius'
r = requests.get(url)
print(r.text)
print("Status Code:","\n************")
print("\t*",r.status_code)
h = requests.head(url)
print("Header:","\n************")
for line in h.headers:
    print("\t",line,":",h.headers[line])
url1="http://httpbin.org/headers"
fake_header = {
    "User-Agent":"Mobile"
}
rh = requests.get(url1,headers=fake_header)
print(rh.text)