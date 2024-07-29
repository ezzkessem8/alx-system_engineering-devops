#!/usr/bin/python3
"""
This script gathers data from an API for a given employee ID and exports the TODO list progress to a JSON file.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    api_url = "https://jsonplaceholder.typicode.com"

    user_info = requests.get(f"{api_url}/users/{employee_id}").json()
    todos = requests.get(f"{api_url}/todos?userId={employee_id}").json()

    employee_name = user_info.get("username")

    tasks = [{"task": todo["title"], "completed": todo["completed"], "username": employee_name} for todo in todos]

    with open(f"{employee_id}.json", mode='w') as file:
        json.dump({str(employee_id): tasks}, file)
