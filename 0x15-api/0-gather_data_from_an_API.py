#!/usr/bin/python3
"""
Script that uses REST API to return emplyee's todo list progress
using employee ID
"""
import requests
from sys import argv


if __name__ == '__main__':
    try:
        id = int(argv[1])
    except ValueError:
        exit()

    def to_do_list(id):
        api_url = "https://jsonplaceholder.typicode.com"
        user_url = f"{api_url}/users/{id}"
        to_do_url = f"{user_url}/todos"

        user_repsonse = requests.get(user_url).json()
        to_do_response = requests.get(to_do_url).json()
        name = user_repsonse.get("name")
        # total tasks
        total = len(to_do_response)
        # completed tasks
        comp = sum(elem['completed'] is True for elem in to_do_response)
        # formatting output
        print(f"Employee {name} is done with tasks({comp}/{total}):")
        # printing incdividual remaining tasks
        for tasks in to_do_response:
            if tasks.get('completed') is True:
                print(f"\t{tasks.get('title')}")
    to_do_list(id)
