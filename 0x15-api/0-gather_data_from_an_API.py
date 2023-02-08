#!/usr/bin/python3
"""Python script that using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""


import requests


def get_employee_todo_list(employee_id):
    """fetches employee ID and returns information
    about his/her TODO list progress"""
    url = (f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    response = requests.get(url)
    todo_list = response.json()
    completed_tasks = [task for task in todo_list if task["completed"]]
    name_url = (f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    name_response = requests.get(name_url)
    name = name_response.json()["name"]

    print(f"Employee {name} is done with tasks
          ({len(completed_tasks)}/{len(todo_list)}): ")
    for task in completed_tasks:
        print(f"\t {task['title']}")


employee_id = 1
get_employee_todo_list(employee_id)
