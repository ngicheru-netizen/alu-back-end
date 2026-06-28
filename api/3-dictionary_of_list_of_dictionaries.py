#!/usr/bin/python3
"""Gather data from a REST API about all of
an employee's TODO list and turn data to JSON"""

import json
import requests
import sys

if __name__ == "__main__":
    base = f"https://jsonplaceholder.typicode.com"
    all_users = requests.get(f"{base}/users/").json()
    all_todos = requests.get(f"{base}/todos/").json()

    usernames = {}
    for user in all_users:
        usernames[user["id"]] = user["username"]

    data = {}
    for todo in all_todos:
        uid = str(todo["userId"])
        if uid not in data:
            data[uid] = []
        data[uid].append(
            {
                "username": usernames[todo["userId"]],
                "task": todo["title"],
                "completed": todo["completed"],
            }
        )

    with open(f"todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
