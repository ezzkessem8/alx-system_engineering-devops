#!/usr/bin/python3
"""
This script gathers data from an API and exports the TODO list progress of all employees to a JSON file.
"""

import json
import requests

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com"

    users = requests.get(f"{api_url}/users").json()
    all_todos = requests.get(f"{api_url}/todos").json()

    data = {}
    for user in users:
        user_id = user["id"]
        username = user["username"]
        tasks = [{"username": username, "task": todo["title"], "completed": todo["completed"]} 
                 for todo in all_todos if todo["userId"] == user_id]
        data[str(user_id)] = tasks

    with open("todo_all_employees.json", mode='w') as file:
        json.dump(data, file)
