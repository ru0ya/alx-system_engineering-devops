#!/usr/bin/python3
"""gets employee TODO list progress"""

import requests
import sys
import csv


if __name__ == '__main__':
    employeeId = sys.argv[1]
    site_url = "https://jsonplaceholder.typicode.com/users"
    url = site_url + "/" + employeeId

    response = requests.get(url)
    emp_names = response.json().get('name')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()
    completed = 0
    completed_tasks = []

    for task1 in tasks:
        if task1.get('completed'):
            completed_tasks.append(task1)
            completed += 1


    with open("{}", mode="w") as f:

    for task1 in completed_tasks:
        print("\t {}".format(task1.get('title')))
