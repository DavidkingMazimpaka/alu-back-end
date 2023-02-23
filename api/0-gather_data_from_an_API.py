#!/usr/bin/python3
""" 
This script retrieves a to-do list for a specific user from a RESTful API and 
prints out the tasks that the user has completed.
"""

import json
import requests
import sys

# Define a usage function to print a usage message and exit
def usage():
    print("Usage: {} <user_id>".format(sys.argv[0]))
    sys.exit(1)

if __name__ == "__main__":
    # Check if a user ID was provided as a command-line argument
    if len(sys.argv) != 2:
        usage()

    # Retrieve the user data and to-do list from the API
    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    
    try:
        user_res = requests.get(user_url)
        user_res.raise_for_status() # Raise an error if the request failed
        user = user_res.json()
        
        todo_res = requests.get(todo_url)
        todo_res.raise_for_status() # Raise an error if the request failed
        todos = todo_res.json()
        
    except (requests.exceptions.RequestException, ValueError) as e:
        print("Error: {}".format(e))
        sys.exit(1)
        
    # Filter the completed tasks
    done = [t for t in todos if t['completed']]
    
    # Print the results
    print('Employee {} is done with tasks ({}/{}):'.format(
        user['name'], len(done), len(todos)))
    
    for t in done:
        print("\t" + t["title"])
