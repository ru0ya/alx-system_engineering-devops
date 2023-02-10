#!/usr/bin/python3
"""exports employee data in json format"""

import json
import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    site_url = "https://jsonplaceholder.typicode.com/users"
    url = site_url + "/" + employeeId

    response = requests.get(url)
    username = response.json().get('username')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    dictionary = {employeeId: []}
    for task in tasks:
        dictionary[employeeId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })

    with open("{}.json".format(employeeId), 'w') as f:
        json.dump(dictionary, f)
