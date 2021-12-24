'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''
import requests
from pprint import pprint
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

# body = {
#     "id" : 556,
#     "first_name": "Exorcise(b)",
#     "last_name": "_03(b)",
#     "email": "getemgone@church.net(b)"
# }

response = requests.delete(base_url + "/556")
response = requests.get(base_url)
content = response.json()
pprint(content['data'][-1])