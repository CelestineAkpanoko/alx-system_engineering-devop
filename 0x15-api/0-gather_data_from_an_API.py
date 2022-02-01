#!/usr/bin/python3

""" Use a specific REST API to retrieve employees todo list
"""

import requests
import sys


API_URL = 'https://jsonplaceholder.typicode.com'
'''The API's URL.'''


if __name__ == '__main__':
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
        employee = requests.get('{}/users/{}'.format(API_URL, id)).json()
        todos = requests.get('{}/todos'.format(API_URL)).json()
        total_todos = list(filter(lambda x: x.get('userId') == id, todos))
        todos_completed = list(filter(lambda x: x.get('completed'), todos))
        print(
            'Employee {} is done with tasks({}/{}):'.format(
                employee.get('name'),
                len(todos_completed),
                len(total_todos)
            )
        )
        for todos_com in todos_completed:
            print('\t {}'.format(todos_completed.get('title')))
