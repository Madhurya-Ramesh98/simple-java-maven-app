import requests

import json

issueType=[]

response = requests.get('https://vijeths.atlassian.net/rest/api/3/issue/createmeta?projectKeys=PP&expand=projects.issuetypes.fields',auth=('vijeth565@gmail.com','6pmJmZTxKpLjePpnUx8j7DF3'))

print("---------------------------------")



for data in response.json()['projects']:

    for d in (data['issuetypes']):

        issueType.append(d)

print(issueType)
