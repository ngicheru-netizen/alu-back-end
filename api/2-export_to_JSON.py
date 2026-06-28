#!/usr/bin/python3
"""Gather data from a REST API about an
employee's TODO list and turn data to JSON"""

import json
import requests
import sys

if __name__ == "__main__":
    employee_ID = sys.argv[1]
    base = f"https://jsonplaceholder.typicode.com/users/{employee_ID}"
    user_url = base
    todos_url = f"{base}/todos"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()
    TOTAL_NUMBER_OF_TASKS = len(todos)
    EMPLOYEE_NAME = user["name"]

    DONE_TASKS = []
    for todo in todos:
        if todo["completed"]:
            DONE_TASKS.append(todo)

    NUMBER_OF_DONE_TASKS = len(DONE_TASKS)

    EMPLOYEE_USERNAME = user["username"]
    tasks = []

    for todo in todos:
        tasks.append(
            {
                "USER_ID": employee_ID,
                "task": todo["title"],
                "completed": todo["completed"],
                "USERNAME": EMPLOYEE_USERNAME,
                "TASK_TITLE": todo["title"],
            }
        )
    data = {employee_ID: tasks}

    with open(f"{employee_ID}.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
