#!/usr/bin/python3

"""
Export to CSV.
"""

import csv
import json
import requests
import sys


def main():
    # Get user ID from command-line arguments.
    user_id = sys.argv[1]

    # Fetch user data from API.
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_response = requests.get(user_url)
    user = json.loads(user_response.text)

    # Fetch user's to-do list from API.
    todo_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    todo_response = requests.get(todo_url)
    todos = json.loads(todo_response.text)

    # Prepare CSV data.
    csv_data = [
        [
            str(todo["userId"]),
            user["username"],
            str(todo["completed"]),
            todo["title"]
        ]
        for todo in todos
    ]

    # Write CSV file.
    filename = f"{user['id']}.csv"
    with open(filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(csv_data)


if __name__ == "__main__":
    main()
