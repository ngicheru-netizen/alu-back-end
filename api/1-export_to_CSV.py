#!/usr/bin/python3
"""Gather data from a REST API about an
employee's TODO list and turn data to CSV"""

import csv
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

    data_list = []

    EMPLOYEE_USERNAME = user["username"]

    for todo in todos:
        data_list.append(
            {
                "USER_ID": employee_ID,
                "USERNAME": EMPLOYEE_USERNAME,
                "TASK_COMPLETED_STATUS": todo["completed"],
                "TASK_TITLE": todo["title"],
            }
        )
    fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    with open(f"{employee_ID}.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writerows(data_list)
