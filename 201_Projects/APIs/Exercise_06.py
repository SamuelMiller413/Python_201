'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.


'''
import requests
from pprint import pprint

user_url = "http://demo.codingnomads.co:8080/tasks_api/users"
task_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"
menu = '''
    Please select from the following options (enter the number of the action you'd like to take):
    1) Create a new account 
    2) View all your tasks
    3) View your completed tasks
    4) View only your incomplete tasks
    5) Create a new task 
    6) Update an existing task 
    7) Delete a task 
                -or- any letter key to quit
'''

def prompt(sentence):
    space = "\n -> " 
    return input(f"\n{sentence}{space}")
def check(response):
    if response.lower() == "s":
            pass
    else:
        return response
def post_user(first_name, last_name, email):
    new_user = {
    "first_name": first_name,
    "last_name": last_name,
    "email": email
    }
    x = requests.post(user_url, json=new_user)
    return print(f"The account belonging to {first_name} {last_name} has been added.")
def get_tasks(userId):
    response = requests.get(f"{user_url}/{userId}/tasks")
    tasks = response.json()
    task_list = []
    for item in tasks['data']:
        task_list.append(item)
    for i in range(len(task_list)):
        print(f"{i}.")
        pprint(task_list[i])
    # tasks = tasks['data']
    # return print(tasks)
def get_completions(userId):
    response = requests.get(f"{user_url}/{userId}/tasks?complete=true")
    tasks = response.json()
    iterable = tasks['data']
    print("\nTasks Completed:\n")
    for i in range(len(iterable)):
        print(f"\n  Task:   {iterable[i]['name']}\n  Description:    {iterable[i]['description']}\n  Completed: {iterable[i]['completed']}\n")
def get_incompletes(userId):
    response = requests.get(f"{user_url}/{userId}/tasks?complete=false")
    tasks = response.json()
    iterable = tasks['data']
    print("\nIncomplete Tasks:\n")
    for i in range(len(iterable)):
        print(f"\n  Task:   {iterable[i]['name']}\n  Description:    {iterable[i]['description']}\n  Completed: {iterable[i]['completed']}\n")
def post_task(userId, name, description):
    new_task = {
    "userId": userId,
    "name": name,
    "description": description
    }
    response = requests.post(task_url, json=new_task)
    print(f"{name} has been added to your list of tasks.")
def put(id, userId, name, description, completed):
    updates = {
        "id": int(id),
        "userId": int(userId),
        "name": name,
        "description": description,
        "completed": completed 
    }
    new = requests.put("http://demo.codingnomads.co:8080/tasks_api/tasks", json=updates)
    new = requests.get(f"{task_url}/{id}")
    print(f"\nUpdated Version:\n")
    pprint(new.json())
    print("\n")
def delete(task):
    chop = f"{task_url}/{task['id']}" 
    deletion = requests.delete(chop)
    return print("Deleted.")

prompting = True
while prompting:
    try:
        item = int(prompt(menu))
        if item == 1:
            first_name = prompt(f"Alright. What is your first name?")
            last_name = prompt(f"What is your last name, {first_name}?")
            email = prompt(f"What is your email?")
            post_user(first_name, last_name, email)        
        elif item == 2:
            userId = prompt("What is your userId?")
            get_tasks(userId)
        elif item == 3:
            # view completed tasks 
            userId = prompt("What is your userId?")
            get_completions(userId)
        elif item == 4:
            userId = prompt("What is your userId?")
            get_incompletes(userId)
        elif item == 5:
            userId = prompt("What is your userId?")
            name_task = prompt("What is the name of the task?")
            description = prompt(f"Yikes, {name_task}! Good luck with that one...\nWould you describe it for the record?")
            post_task(userId,name_task,description)
        elif item == 6:
            userId = int(prompt("What is your userId?"))
            old = get_tasks(userId)
            
            which_up = int(prompt(f"Which task would you like to update?"))
            
            current_task = old[which_up]

            up_name = prompt(f"Enter new name.\nIt's currently: {current_task['name']}\n                      -or- (s) for skip")
            if up_name == "s":
                up_name = current_task["name"]
            else:
                up_name = up_name
            up_descr = prompt(f"Enter new description.\nIt's currently: {current_task['description']}\n                      -or- (s) for skip")
            if up_descr == "s":
                up_descr = current_task["description"]
            else:
                up_descr = up_descr
            up_status = prompt(f"Enter new status.\nIt's currently: {current_task['completed']}\n                      -or- (s) for skip")        
            if up_status == "s":
                up_status = current_task["completed"]
            else:
                up_status = up_status
            id = current_task['id']
            updates = {
                "id" : int(id),
                "userId": int(userId),
                "name": up_name,
                "description": up_descr,
                "completed": up_status
                }
            put(id,userId,up_name,up_descr,up_status)
        elif item == 7:
            userId = int(prompt("What is your userId?"))
            old = get_tasks(userId)
            # old = get_tasks(userId)
            
            which_up = int(prompt(f"Which task would you like to delete?"))
            
            current_task = old[which_up]
            delete(current_task)
    except ValueError:
        print("\nGoodbye!\n")
        prompting = False
    



