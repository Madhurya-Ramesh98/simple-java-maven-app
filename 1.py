
import requests
import json

url = "https://chandratech.atlassian.net/rest/api/3/issue/Ap-17"
token = 'EqijvLWIwETIVbQXEgBFEA26'
headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

r = requests.get(url, headers=headers, auth=('surisetty.chandrakiran@gmail.com', token))

#print(r.text)
#print(type(r))


print(json.dumps(json.loads(r.text), sort_keys=True, indent=4, separators=(",", ": ")))
