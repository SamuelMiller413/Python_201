'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''
import requests
from pprint import pprint
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(base_url)
content = response.json()
# body = {
#     "first_name": "Samuel",#add first name inside quotes
#     "last_name": "Miller",#add last name inside quotes
#     "email": "samuelmillerwriting@gmail.com"#add email inside quotes
# }
body = {
    "first_name": "Exorcise",
    "last_name": "_03",
    "email": "getemgone@church.net"
}
post_response = requests.post(base_url, json=body)
response = requests.get(base_url)
print(response)
content = response.json()
pprint(content['data'][-1])
