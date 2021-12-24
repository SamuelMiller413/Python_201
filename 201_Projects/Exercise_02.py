'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''

import requests
from pprint import pprint
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(base_url)
content = response.json()
# data = response.json()
# pprint(data['data'][0]['first_name'])
# pprint(data)


email_list = []
for i in range(len(base_url)):
    email_list.append(content['data'][i]['email'])
print(email_list)
# print(content['data'][0]['email'])