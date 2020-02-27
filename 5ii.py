import requests
url = 'http://172.17.50.43/algenius'
r = requests.get(url)
print(r.text)
print("Status Code:","\n************")
print("\t*",r.status_code)