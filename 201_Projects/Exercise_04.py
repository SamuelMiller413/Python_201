'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''
import requests
from pprint import pprint
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "id" : 556,
    "first_name": "Exorcise(b)",
    "last_name": "_03(b)",
    "email": "getemgone@church.net(b)"
}

response = requests.put(base_url, json=body)
response = requests.get(base_url)
content = response.json()
pprint(content['data'][-1])