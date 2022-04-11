import os
import requests
import json


env_var = os.environ
print(env_var['EMAIL_CHANDRA'])
print("----------")

EMAIL_CHANDRA = os.environ('EMAIL_CHANDRA')
API_CHANDRA = os.environ('API_CHANDRA')

# EMAIL_CHANDRA = '$ {{ secrets.EMAIL_CHANDRA }}'
# API_CHANDRA = '$ {{ secrets.API_CHANDRA }}'

url = "https://chandratech.atlassian.net/rest/api/3/issue/Ap-17"
# token = 'EqijvLWIwETIVbQXEgBFEA26'
headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

r = requests.get(url, headers=headers, auth=(EMAIL_CHANDRA, API_CHANDRA))

#print(r.text)
#print(type(r))


print(json.dumps(json.loads(r.text), sort_keys=True, indent=4, separators=(",", ": ")))
