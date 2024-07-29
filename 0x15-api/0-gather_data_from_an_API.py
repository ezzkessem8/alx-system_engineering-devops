#!/usr/bin/python3
"""
This script gathers data from an API for a given employee ID and displays the TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    api_url = "https://jsonplaceholder.typicode.com"

    user_info = requests.get(f"{api_url}/users/{employee_id}").json()
    todos = requests.get(f"{api_url}/todos?userId={employee_id}").json()

    employee_name = user_info.get("name")
    completed_tasks = [todo["title"] for todo in todos if todo["completed"]]
    total_tasks = len(todos)

    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")
