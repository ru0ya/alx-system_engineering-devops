#!/usr/bin/python3
"""gets employee TODO list progress"""

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

    with open("{}.csv".format(employeeId, newline=""), 'w') as f:
        for task in tasks:
            f.write('"{}", "{}", "{}", "{}"\n'
                    .format(employeeId, username, task.get('completed'),
                            task.get('title')))
