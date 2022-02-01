#!/usr/bin/python3

""" Use a specific REST API to retrieve employees todo list
"""

import requests
import sys

if __name__ == "__main__":
    api_url = 'https://jsonplaceholder.typicode.com/'
    emp_id = sys.argv[1]
    employee = requests.get(api_url + 'user/{}'.format(emp_id)).json()
    todos = requests.get(api_url + 'todos', params={'userId': emp_id}).json()

    completed_task = [todo.get('title') for todo in todos if todo.get('completed') is True]
    print('Employee {} is done with tasks({}/{}):'.format(
        employee.get('name'), len(completed_task), len(todos)))
    [print('\t {}'.format(c)) for c in completed_task]
