#!/usr/bin/python3
"""
This script gathers data from an API for a given employee ID and exports the TODO list progress to a CSV file.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    api_url = "https://jsonplaceholder.typicode.com"

    user_info = requests.get(f"{api_url}/users/{employee_id}").json()
    todos = requests.get(f"{api_url}/todos?userId={employee_id}").json()

    employee_name = user_info.get("username")

    with open(f"{employee_id}.csv", mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([employee_id, employee_name, todo["completed"], todo["title"]])
