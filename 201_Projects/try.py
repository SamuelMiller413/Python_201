import requests
import json
from pprint import pprint

from requests.api import request

# url = "http://demo.codingnomads.co:8080/tasks_api/users"
# selection = input(
#     "Please select from the following options (enter the number of the action you would like to take) \n 1) create a new account \n 2) View all your tasks \n 3) View your completed tasks \n 4) View only your incomplete tasks \n 5) Create a new task \n 6) Update an existing task \n 7) Delete a task \n"
# )
# if selection == "1":
#     print("We will create a new account for you ")
#     firstName = input("Type your First Name ")
#     lastName = input("Type your Last Name ")
#     email = input("Type in your email ")
#     NewUser = {"first_name": firstName, "last_name": lastName, "email": email}
#     x = requests.post(url, json=NewUser)

# elif selection == "2":
#     userid = input("Please type your userid to show all your tasks ")
#     response = requests.get(url + "/" + userid + "/" + "tasks?complete=-1")
#     output = response.json()
#     outputData = output["data"]

#     for item in outputData:
#         print(item)
#         if item["userId"] == userid:
#             print(item)
#         # else:
#         #     print("Your ID doesn't exist")

# elif selection == "3":
#     userid = input("Please type your userid to show all your completed tasks ")
#     response = requests.get(url + "/" + userid + "/" + "tasks?complete=true")
#     output = response.json()
#     outputData = output["data"]

#     for item in outputData:
#         print(item)
#         if item["userId"] == userid:
#             print(item)

# elif selection == "4":
#     userid = input("Please type your userid to show all your incompleted tasks ")
#     response = requests.get(url + "/" + userid + "/" + "tasks?complete=false")
#     output = response.json()
#     outputData = output["data"]

#     for item in outputData:
#         print(item)
#         if item["userId"] == userid:
#             print(item)

# elif selection == "5":
#     print("We will create a new task for you ")
#     description = input("Type your task description ")
#     taskName = input("Type your Name ")
#     taskuserid = input("Type a task user ID ")
#     NewUser = {"description": description, "name": taskName, "userId": taskuserid}
#     taskurl = "http://demo.codingnomads.co:8080/tasks_api/tasks"
#     x = requests.post(taskurl, json=NewUser)
#     print(x.status_code)

# elif selection == "6":
#     print("We will update a task for you ")
#     taskurl = "http://demo.codingnomads.co:8080/tasks_api/tasks"
#     description = input("Type your task description ")
#     taskName = input("Type your Name ")
#     taskuserid = input("Type a task user ID ")
#     NewUser = {"description": description, "name": taskName, "userId": taskuserid}
#     x = requests.post(taskurl, json=NewUser)
#     print(x.status_code)

# elif selection == "7":
#     idDelete = input("Please type the ID for the task you want to delete ")
#     taskurl = "http://demo.codingnomads.co:8080/tasks_api/tasks"
#     response = requests.delete(taskurl + "/" + idDelete)
#     print(response.status_code)

user_url = "http://demo.codingnomads.co:8080/tasks_api/users"
task_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"

params = {"id": 219, "name":"Ferris Buehler"}
body = {
    "id": 219,
    "userId": 5,
    "name": "Ferris Buehler",
    "description": "Pretend to be sick all day.",
    "completed": "true"
    }

# response = requests.get(task_url['data'][body])
# j_print = response.json()
# pprint(j_print)
print("\n\n")
# j_list = list(j_print['data'])
# pprint(j_list[-1])
# putting = requests.put(task_url, )

body = {
    "id": 219,
    "userId": 5,
    "name": "Ferris Buehler",
    "description": "Pretend to be sick all day.",
    "completed": "false"
    }
# put_req = requests.put(task_url, json=body)
# patch_request = requests.patch(task_url, json=body)

new = requests.get(f"{task_url}/219")
pprint(new.json())