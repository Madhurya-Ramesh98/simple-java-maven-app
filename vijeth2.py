import requests
import json
import os

EMAIL = os.environ['EMAIL']
JIRA_API = os.environ['JIRA_API']


url = 'https://vijeths.atlassian.net/rest/api/3/search?jql=project = "SM"'

headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

r = requests.get(url, headers=headers, auth=(EMAIL, JIRA_API))

#print(r.text)
#print(type(r))


print(r.json())
