#!/usr/bin/python3
"""Gather data from a REST API about an employee's TODO list."""

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

    print(
        "Employee",
        EMPLOYEE_NAME,
        "is done with tasks",
        f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}): ",
    )

    for todo in DONE_TASKS:
        print(f"\t {todo['title']}")
