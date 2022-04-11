import requests
import os
import json
EMAIL = os.environ['EMAIL']
JIRA_API = os.environ['JIRA_API']




issueType=[]

response = requests.get('https://vijeths.atlassian.net/rest/api/3/issue/createmeta?projectKeys=PP&expand=projects.issuetypes.fields',auth=(EMAIL,JIRA_API))
print(response.json())
# print("---------------------")



# for data in response.json()['projects']:

#     for d in (data['issuetypes']):

#         issueType.append(d)

# print(issueType)

print("---------------------")
